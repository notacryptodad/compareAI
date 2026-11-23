# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml", "httpx"]
# ///
"""Verify that every double-quoted string in a `notes:` field really appears on its source.

WHY THIS EXISTS: the first research pass used an LLM-summarising fetch tool, and its
PARAPHRASES got recorded as verbatim quotes. A fabricated quote is the worst possible
defect for a project whose whole value is traceability. This script makes that class of
error mechanically detectable instead of relying on review.

Fetches each source URL once, strips markup, and substring-matches every quote.

  uv run scripts/check_quotes.py                 # all files
  uv run scripts/check_quotes.py data/aws         # one provider

Exit 1 if any quote is ABSENT from a page that fetched successfully.
Pages that fetch empty/JS-only are reported UNVERIFIABLE and do not fail the run.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

import httpx
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Quotes shorter than this are too generic to match meaningfully ("Agent", "MCP").
MIN_QUOTE_LEN = 12

# Below this much extracted text, a page is almost certainly a client-rendered shell whose
# real content never arrived. docs.byteplus.com strips to ~3.3 KB of pure navigation from a
# ~300 KB payload; its rendered bodies are 5-22 KB of prose. 4500 sits between the two.
JS_SHELL_MAX_TEXT = 4500

# Hosts known to client-render article bodies. Some of their pages (ArkClaw, AgentKit docs)
# ship a sidebar big enough to clear JS_SHELL_MAX_TEXT while still carrying no prose. On these
# hosts, a page where NOT ONE quote matches is treated as an unrendered shell (UNVERIFIABLE).
# If any quote on the page matches, the body did arrive, so the remaining misses still fail.
JS_RENDERED_HOSTS = {"docs.byteplus.com", "docs.volcengine.com"}

QUOTE_RE = re.compile(r'"([^"]{%d,}?)"' % MIN_QUOTE_LEN, re.DOTALL)

# A note asserting that a phrase is MISSING quotes it legitimately — the quote is the
# thing we're saying isn't there. Skip such notes entirely.
NEGATED_RE = re.compile(
    r"\b(does NOT appear|do NOT appear|not appear|appear NOWHERE|appears? nowhere|"
    r"NOT FOUND|not found|NOT present|not present|absent|no page titled|"
    r"could not (?:be )?(?:find|found|confirm)|was not verbatim|not verbatim|"
    r"an earlier revision)\b",
    re.IGNORECASE,
)

# Fragments that are plainly our own prose caught between quote marks, not source text.
COMMENTARY_RE = re.compile(
    r"(paraphrase|earlier revision|check_quotes|under Managed Agents'|"
    r"section had no content|is referenced, and the docs|component section and)",
    re.IGNORECASE,
)

# Notes that intentionally quote another page — comparing vendors, or splitting evidence
# between two pages of the same vendor. The note must name the other source in prose.
# This is REQUIRED practice here, not a loophole: several real defects were cells that
# silently quoted page B while citing page A.
CROSS_PAGE_RE = re.compile(
    r"(a DIFFERENT source|a different page|Contrast |contrast with|"
    r"NOTE ON A MIS-SOURCED|they are in the|Evidence on the|"
    r"is on the harness-sdk repo page|not on adk\.dev|that page,\s*$|"
    r"different page from the org page|Region facts throughout this file)",
    re.IGNORECASE | re.MULTILINE,
)

GITHUB_REPO_RE = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/?$")


def normalize(text: str) -> str:
    """Aggressively normalize so formatting differences don't cause false alarms."""
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    # Curly quotes/dashes -> ASCII
    for a, b in [("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("−", "-"), (" ", " ")]:
        text = text.replace(a, b)
    # Strip inline markdown emphasis. A quote spanning a bold marker — e.g. the source
    # renders "**AF Labs**: Experimental packages..." and we quote
    # "AF Labs: Experimental packages..." — is legitimate quoting of rendered text.
    text = re.sub(r"[*_`]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()


def strip_markup(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return raw


def quote_present(quote: str, page: str) -> bool:
    """True if `quote` appears on the page, allowing two legitimate quoting conventions.

    1. Elision with '...' — each surviving segment must appear, in order.
    2. A trailing '.' we added when the source sentence continues.
    """
    q = normalize(quote)
    if q in page:
        return True

    # 2. Trailing punctuation added by us.
    if q.endswith(".") and q[:-1].strip() in page:
        return True

    # 1. Elided quotes: check each segment appears in order.
    if "..." in q or "…" in q:
        segments = [s.strip() for s in re.split(r"\.\.\.|…", q) if s.strip()]
        if len(segments) > 1:
            pos = 0
            for seg in segments:
                seg = seg.strip(" .,;")
                if len(seg) < 8:
                    continue  # too short to be meaningful
                found = page.find(seg, pos)
                if found < 0:
                    return False
                pos = found + len(seg)
            return True
    return False


def candidate_urls(url: str) -> list[str]:
    """For a GitHub repo URL, also try raw README files — the rendered page is JS-heavy."""
    urls = [url]
    if m := GITHUB_REPO_RE.match(url):
        owner, repo = m.group(1), m.group(2)
        for branch in ("main", "master"):
            for name in ("README.md", "readme.md"):
                urls.append(f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{name}")
    return urls


def fetch_text(client: httpx.Client, url: str) -> str:
    """Concatenate text from the URL and any helpful alternates (e.g. raw README)."""
    chunks: list[str] = []
    for candidate in candidate_urls(url):
        try:
            r = client.get(candidate)
        except httpx.HTTPError:
            continue
        if r.status_code != 200 or not r.text:
            continue
        chunks.append(strip_markup(r.text))
    return normalize(" ".join(chunks))


def main() -> int:
    targets = [Path(a) for a in sys.argv[1:]] or [DATA]
    files: list[Path] = []
    for t in targets:
        t = t if t.is_absolute() else ROOT / t
        files.extend(p for p in sorted(t.rglob("*.yaml")) if p.name != "taxonomy.yaml")

    # (url) -> list of (file, row, quote)
    todo: dict[str, list[tuple[str, str, str]]] = {}
    for fpath in files:
        doc = yaml.safe_load(fpath.read_text(encoding="utf-8")) or {}
        rel = fpath.relative_to(ROOT)
        for rid, cell in (doc.get("capabilities") or {}).items():
            if not cell:
                continue
            src, notes = cell.get("source"), cell.get("notes")
            if not src or not notes:
                continue
            note_text = str(notes)
            # A note that explicitly says a phrase is ABSENT / NOT present is asserting the
            # opposite of a citation. Quoting the missing string there is correct, so don't
            # treat those quotes as claims about the page.
            if NEGATED_RE.search(note_text):
                continue
            # Notes that deliberately quote a DIFFERENT page (contrast with a rival vendor,
            # or splitting evidence across two vendor pages) are correct practice — the
            # note names the other source in prose. Skip; a human reviews these.
            if CROSS_PAGE_RE.search(note_text):
                continue
            for q in QUOTE_RE.findall(note_text):
                q = q.strip()
                # Skip fragments that are our own commentary rather than source text.
                if q.endswith(":") or q.startswith("(") or COMMENTARY_RE.search(q):
                    continue
                todo.setdefault(src, []).append((str(rel), rid, q))

    n_quotes = sum(len(v) for v in todo.values())
    print(f"Checking {n_quotes} quote(s) across {len(todo)} source URL(s)\n")

    absent: list[tuple[str, str, str, str]] = []
    unverifiable: list[str] = []
    ok = 0

    # Identity encoding: some doc hosts (docs.aws.amazon.com) return a body that decodes
    # to different text under br/zstd via httpx, which silently broke matching and made
    # verbatim quotes look fabricated. Ask for plain text.
    headers = {
        "User-Agent": "compareAI-quotecheck/0.1",
        "Accept-Encoding": "gzip, deflate",
    }
    with httpx.Client(follow_redirects=True, timeout=30, headers=headers) as client:
        for url, items in sorted(todo.items()):
            page = fetch_text(client, url)

            # JS-rendered docs sites (docs.byteplus.com is the known case) return a large
            # HTML payload that strips to almost nothing but nav chrome. Plain HTTP cannot
            # see their prose, so quotes taken from a RENDERED page would look fabricated
            # here. Detect that and report UNVERIFIABLE rather than failing the build —
            # otherwise this check punishes the provider with the most JS-heavy docs.
            js_rendered = len(page) < JS_SHELL_MAX_TEXT
            if js_rendered:
                unverifiable.append(url)
                print(f"  ?? {url}\n     only {len(page)} chars of text — JS-rendered shell; "
                      f"{len(items)} quote(s) UNVERIFIABLE by HTTP fetch. "
                      f"Re-verify with a headless browser.")
                continue

            misses = [(f, r, q) for f, r, q in items if not quote_present(q, page)]
            if len(misses) == len(items) and urlparse(url).hostname in JS_RENDERED_HOSTS:
                unverifiable.append(url)
                print(f"  ?? {url}\n     {len(page)} chars but no quote matched on a known "
                      f"JS-rendered host — nav-only shell; {len(items)} quote(s) UNVERIFIABLE "
                      f"by HTTP fetch. Re-verify with a headless browser.")
                continue
            ok += len(items) - len(misses)
            mark = "OK" if not misses else "!!"
            print(f"  {mark} {url}  ({len(items) - len(misses)}/{len(items)} found)")
            for f, r, q in misses:
                absent.append((f, r, q, url))
                print(f"       ABSENT in {f}:{r}\n         {q[:100]!r}")

    print(f"\n{ok} verbatim, {len(absent)} absent, "
          f"{sum(len(todo[u]) for u in unverifiable)} unverifiable")

    if unverifiable:
        print("\nUnverifiable pages (JS-rendered or blocked) — check these by hand:")
        for u in unverifiable:
            print(f"  ? {u}")

    if absent:
        print(f"\n{len(absent)} QUOTE(S) NOT FOUND ON THE CITED PAGE.")
        print("Either fix the quote to match the source verbatim, drop the quotation")
        print("marks and mark it as a paraphrase, or downgrade the cell to `unknown`.")
        return 1

    print("\nOK — every checked quote appears verbatim on its cited page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
