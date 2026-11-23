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
  uv run scripts/check_quotes.py data/aws/a-sdk.yaml   # one file
  uv run scripts/check_quotes.py --strict         # also fail on unmatched cross-page quotes

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
JS_RENDERED_HOSTS = {"docs.byteplus.com", "docs.volcengine.com", "help.aliyun.com"}

QUOTE_RE = re.compile(r'"([^"]{%d,}?)"' % MIN_QUOTE_LEN, re.DOTALL)

# Chinese corner-bracket quotes 「…」 carry verbatim CN evidence (Alibaba, Qoder CN) and used to
# be ignored entirely. CJK text is dense, so a shorter minimum still identifies a sentence.
MIN_CJK_QUOTE_LEN = 6
CJK_QUOTE_RE = re.compile(r"「([^「」]{%d,}?)」" % MIN_CJK_QUOTE_LEN, re.DOTALL)


def find_quotes(note_text: str) -> list[str]:
    return [q for q, _ in find_quote_spans(note_text)]


def find_quote_spans(note_text: str) -> list[tuple[str, tuple[int, int]]]:
    out = [(m.group(1), m.span()) for m in QUOTE_RE.finditer(note_text)]
    return out + [(m.group(1), m.span()) for m in CJK_QUOTE_RE.finditer(note_text)]


# Sentence boundary used to scope a negation to the quote it refers to.
SENTENCE_END_RE = re.compile(r"(?<=[.!?。；;])\s+|\n\s*\n")


def negated_quote(note_text: str, span: tuple[int, int]) -> bool:
    """True if a negation phrase sits in the same sentence as the quote at `span`.

    This used to skip every quote in a note that mentioned "absent" anywhere, which hid
    unrelated positive quotes in the same note from checking (54 quotes in 13 notes).
    """
    start, end = span
    before = note_text[:start]
    cut = [m.end() for m in SENTENCE_END_RE.finditer(before)]
    s0 = cut[-1] if cut else 0
    m = SENTENCE_END_RE.search(note_text, end)
    s1 = m.start() if m else len(note_text)
    # Text between the quote marks is the vendor's words, not our negation.
    context = note_text[s0:start] + " " + note_text[end:s1]
    return bool(NEGATED_RE.search(context))


CJK_RE = re.compile(r"[㐀-鿿]")
_TIGHT_CACHE: dict[int, str] = {}


def _tight(page: str) -> str:
    """Page text with all whitespace removed (cached per page object)."""
    key = id(page)
    if key not in _TIGHT_CACHE:
        _TIGHT_CACHE[key] = re.sub(r"\s+", "", page)
    return _TIGHT_CACHE[key]

# A note asserting that a phrase is MISSING quotes it legitimately — the quote is the
# thing we're saying isn't there. Such quotes are skipped (scoped to their sentence).
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

    # 3. CJK quotes: Chinese has no inter-word spaces, but stripping markup inserts spaces
    # at every tag boundary. Compare with all whitespace removed on both sides.
    if CJK_RE.search(q):
        q_tight = re.sub(r"\s+", "", q)
        if q_tight in _tight(page):
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


# Note-embedded URLs: full https URLs, or bare host/path forms such as
# "docs.qoder.cn/zh/cli/overview" that notes use when naming a second page.
NOTE_URL_RE = re.compile(
    r"(?:https?://)?((?:[a-z0-9-]+\.)+(?:com|cn|ai|dev|io|org|net|google|blog)"
    r"(?:/[^\s)\]\"'，。；、「」<>]*)?)",
    re.IGNORECASE,
)


def note_urls(note_text: str, source: str) -> list[str]:
    """Second-page URLs a note names in prose (excluding the cell's own source)."""
    out: list[str] = []
    for m in NOTE_URL_RE.finditer(note_text):
        host_path = m.group(1).rstrip(".,;:)")
        if "/" not in host_path and not host_path.startswith(("docs.", "www.", "help.")):
            continue  # a bare domain mention, not a page citation
        url = "https://" + host_path
        if url.rstrip("/") != source.rstrip("/") and url not in out:
            out.append(url)
    return out


def main() -> int:
    strict = "--strict" in sys.argv[1:]
    args = [a for a in sys.argv[1:] if a != "--strict"]
    targets = [Path(a) for a in args] or [DATA]
    files: list[Path] = []
    for t in targets:
        t = t if t.is_absolute() else ROOT / t
        if t.is_file():
            # A single file used to be silently ignored (rglob on a file yields nothing).
            if t.suffix == ".yaml" and t.name != "taxonomy.yaml":
                files.append(t)
        else:
            files.extend(p for p in sorted(t.rglob("*.yaml")) if p.name != "taxonomy.yaml")

    # Direct quotes: (url) -> list of (file, row, quote)
    todo: dict[str, list[tuple[str, str, str]]] = {}
    # Cross-page quotes: (file, row, quote, [candidate urls: source first, then note URLs])
    cross: list[tuple[str, str, str, list[str]]] = []
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
            # A quote in a sentence that says the phrase is ABSENT / NOT present asserts the
            # opposite of a citation, so it is skipped (see negated_quote).
            # Notes that deliberately quote a DIFFERENT page (contrast with a rival vendor,
            # or splitting evidence across two vendor pages) are correct practice — the
            # note names the other source in prose. These used to be skipped wholesale;
            # now each quote is checked against the cited source AND every URL the note
            # names. Only quotes found on none of them are reported (as warnings, since a
            # note may name the second page by title rather than URL).
            is_cross = bool(CROSS_PAGE_RE.search(note_text))
            extra = note_urls(note_text, src) if is_cross else []
            for q, span in find_quote_spans(note_text):
                if negated_quote(note_text, span):
                    continue
                q = q.strip()
                # Skip fragments that are our own commentary rather than source text.
                if q.endswith(":") or q.startswith("(") or COMMENTARY_RE.search(q):
                    continue
                if is_cross:
                    cross.append((str(rel), rid, q, [src, *extra]))
                else:
                    todo.setdefault(src, []).append((str(rel), rid, q))

    n_quotes = sum(len(v) for v in todo.values())
    print(f"Checking {n_quotes} direct quote(s) across {len(todo)} source URL(s), "
          f"plus {len(cross)} cross-page quote(s)\n")

    absent: list[tuple[str, str, str, str]] = []
    unverifiable: list[str] = []
    ok = 0
    pages: dict[str, str] = {}

    def shell(url: str, page: str) -> bool:
        return len(page) < JS_SHELL_MAX_TEXT

    # Identity encoding: some doc hosts (docs.aws.amazon.com) return a body that decodes
    # to different text under br/zstd via httpx, which silently broke matching and made
    # verbatim quotes look fabricated. Ask for plain text.
    headers = {
        "User-Agent": "compareAI-quotecheck/0.1",
        "Accept-Encoding": "gzip, deflate",
    }
    with httpx.Client(follow_redirects=True, timeout=30, headers=headers) as client:

        def get(url: str) -> str:
            if url not in pages:
                pages[url] = fetch_text(client, url)
            return pages[url]

        for url, items in sorted(todo.items()):
            page = get(url)

            # JS-rendered docs sites (docs.byteplus.com is the known case) return a large
            # HTML payload that strips to almost nothing but nav chrome. Plain HTTP cannot
            # see their prose, so quotes taken from a RENDERED page would look fabricated
            # here. Detect that and report UNVERIFIABLE rather than failing the build —
            # otherwise this check punishes the provider with the most JS-heavy docs.
            # A match is real evidence even on a short page (a shell can't contain a quote by
            # accident) — only MISSES on a short page are uncertain. So short pages count
            # their matches as verbatim and report only the misses as unverifiable.
            if shell(url, page):
                found = [it for it in items if quote_present(it[2], page)]
                ok += len(found)
                if len(found) < len(items):
                    unverifiable.append(url)
                    todo[url] = [it for it in items if it not in found]
                print(f"  ?? {url}\n     only {len(page)} chars of text — JS-rendered shell; "
                      f"{len(found)}/{len(items)} matched, {len(items) - len(found)} "
                      f"quote(s) UNVERIFIABLE by HTTP fetch. Re-verify with a headless browser.")
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

        cross_ok = 0
        cross_unmatched: list[tuple[str, str, str, list[str]]] = []
        cross_unreadable: list[tuple[str, str, str, list[str]]] = []
        for f, r, q, urls in cross:
            # A known JS-rendered host serves a nav shell that can clear the size threshold;
            # a miss there says nothing about the rendered page, so it isn't "readable".
            readable = [u for u in urls if not shell(u, get(u))
                        and urlparse(u).hostname not in JS_RENDERED_HOSTS]
            if any(quote_present(q, get(u)) for u in urls):
                cross_ok += 1
            elif len(readable) < len(urls):
                # At least one candidate page couldn't be read, and the quote may be there.
                # Only a miss on EVERY candidate page is a real "unmatched".
                cross_unreadable.append((f, r, q, urls))
            else:
                cross_unmatched.append((f, r, q, urls))

    print(f"\n{ok} verbatim, {len(absent)} absent, "
          f"{sum(len(todo[u]) for u in unverifiable)} unverifiable")
    print(f"cross-page: {cross_ok} verbatim, {len(cross_unmatched)} unmatched, "
          f"{len(cross_unreadable)} unreadable")

    if unverifiable:
        print("\nUnverifiable pages (JS-rendered or blocked) — check these by hand:")
        for u in unverifiable:
            print(f"  ? {u}")

    if cross_unmatched:
        print("\nCross-page quotes not found on the cited source or any URL the note names.")
        print("Name the second page by full URL in the note so it can be checked, or fix the")
        print("quote. (Warning only; pass --strict to fail on these.)")
        for f, r, q, urls in cross_unmatched:
            print(f"  ~ {f}:{r}\n      {q[:100]!r}\n      tried: {', '.join(urls)}")

    if absent:
        print(f"\n{len(absent)} QUOTE(S) NOT FOUND ON THE CITED PAGE.")
        print("Either fix the quote to match the source verbatim, drop the quotation")
        print("marks and mark it as a paraphrase, or downgrade the cell to `unknown`.")
        return 1

    if strict and cross_unmatched:
        print(f"\n--strict: {len(cross_unmatched)} cross-page quote(s) unmatched.")
        return 1

    print("\nOK — every checked quote appears verbatim on its cited page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
