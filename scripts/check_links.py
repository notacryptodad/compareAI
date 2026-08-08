# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml", "httpx"]
# ///
"""Check that every `source:` URL in data/ still resolves.

A vendor moving or deleting a doc page is a strong signal that the cell needs
re-verification — it is how renames get caught early.

Run:  uv run scripts/check_links.py
"""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

import httpx
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def main() -> int:
    urls: dict[str, list[str]] = defaultdict(list)

    for fpath in sorted(DATA.rglob("*.yaml")):
        if fpath.name == "taxonomy.yaml":
            continue
        doc = yaml.safe_load(fpath.read_text(encoding="utf-8")) or {}
        rel = fpath.relative_to(DATA)
        for key in ("repo", "docs"):
            if url := doc.get(key):
                urls[url].append(f"{rel}:{key}")
        for rid, cell in (doc.get("capabilities") or {}).items():
            if url := (cell or {}).get("source"):
                urls[url].append(f"{rel}:{rid}")

    print(f"Checking {len(urls)} distinct URL(s)\n")

    failures: list[tuple[str, str, list[str]]] = []
    redirects: list[tuple[str, str, list[str]]] = []

    headers = {"User-Agent": "compareAI-linkcheck/0.1 (+https://github.com/)"}
    with httpx.Client(follow_redirects=False, timeout=20, headers=headers) as client:
        for url, cells in sorted(urls.items()):
            try:
                r = client.head(url)
                if r.status_code >= 400 or r.status_code == 405:
                    r = client.get(url)
            except httpx.HTTPError as exc:
                failures.append((url, f"{type(exc).__name__}: {exc}", cells))
                print(f"  ERR  {url}")
                continue

            if r.status_code in (301, 302, 307, 308):
                loc = r.headers.get("location", "?")
                redirects.append((url, loc, cells))
                print(f"  {r.status_code}  {url}\n       -> {loc}")
            elif r.status_code >= 400:
                failures.append((url, f"HTTP {r.status_code}", cells))
                print(f"  {r.status_code}  {url}")
            else:
                print(f"  {r.status_code}  {url}")

    if redirects:
        print(f"\n{len(redirects)} redirect(s) — update the source URL, and check whether")
        print("the product was renamed (that is a changelog entry, not just a link fix):")
        for url, loc, cells in redirects:
            print(f"  ! {url}\n    -> {loc}\n    cells: {', '.join(cells[:4])}"
                  + (f" +{len(cells) - 4} more" if len(cells) > 4 else ""))

    if failures:
        print(f"\n{len(failures)} FAILURE(s) — these cells must be re-verified:")
        for url, why, cells in failures:
            print(f"  x {url} ({why})\n    cells: {', '.join(cells[:4])}"
                  + (f" +{len(cells) - 4} more" if len(cells) > 4 else ""))
        return 1

    print("\nOK — all source URLs resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
