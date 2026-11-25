# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Diff two snapshots of data/ and emit changelog entries.

The What's New feed is DERIVED from versioned YAML, never hand-written.

Two modes:
  --git <rev>       diff data/ at <rev> against the working tree (needs a git repo)
  --against <dir>   diff data/ against a copy of data/ from another directory

Outputs CHANGELOG.md, updates.json, and updates.xml (RSS).

Entries are tagged so the feed doesn't cry wolf:
  change   — the vendor actually shipped something (preview -> ga, new product, ...)
  research — our coverage caught up (unknown -> anything). Not a vendor launch.

Run:  uv run scripts/changelog.py --git HEAD --date 2026-08-04
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
BUCKET_FILES = {"a": "a-sdk.yaml", "b": "b-platform.yaml", "c": "c-outofbox.yaml", "d": "d-devtools.yaml", "e": "e-models.yaml"}

# Fields whose change is worth an entry. Everything else (notes, verified_by) is noise.
TRACKED = ("status", "product", "value", "limits")

RANK = {"none": 0, "unknown": 0, "limited": 1, "partner": 1, "preview": 2, "oss": 3, "ga": 4}


def load_yaml(text: str) -> dict:
    return yaml.safe_load(text) or {}


def read_working(provider: str, bucket: str) -> dict | None:
    fpath = DATA / provider / BUCKET_FILES[bucket]
    if not fpath.exists():
        return None
    return load_yaml(fpath.read_text(encoding="utf-8"))


def read_git(rev: str, provider: str, bucket: str) -> dict | None:
    rel = f"data/{provider}/{BUCKET_FILES[bucket]}"
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"{rev}:{rel}"],
            capture_output=True, text=True, check=True,
        )
    except subprocess.CalledProcessError:
        return None  # file did not exist at that rev
    return load_yaml(out.stdout)


def read_dir(base: Path, provider: str, bucket: str) -> dict | None:
    fpath = base / provider / BUCKET_FILES[bucket]
    if not fpath.exists():
        return None
    return load_yaml(fpath.read_text(encoding="utf-8"))


def classify(old_cell: dict | None, new_cell: dict) -> str:
    """change = vendor shipped something; research = our coverage caught up."""
    old_status = (old_cell or {}).get("status", "unknown")
    new_status = new_cell.get("status", "unknown")
    if old_cell is None or old_status == "unknown":
        return "research"
    if new_status == "unknown":
        return "research"  # reverted to unknown (staleness expiry)
    return "change" if old_status != new_status else "change"


def describe(field: str, old, new) -> str:
    def fmt(v):
        if v is None:
            return "—"
        if isinstance(v, list):
            return ", ".join(str(x) for x in v)
        if isinstance(v, dict):
            return json.dumps(v, sort_keys=True)
        return str(v)

    return f"`{field}`: {fmt(old)} → {fmt(new)}"


def main() -> int:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--git", metavar="REV", help="git revision to diff against")
    src.add_argument("--against", metavar="DIR", type=Path,
                     help="directory holding a previous copy of data/")
    ap.add_argument("--date", required=True,
                    help="YYYY-MM-DD stamp for these entries (no clock access in scripts)")
    ap.add_argument("--site-url", default="https://example.invalid/compareai")
    args = ap.parse_args()

    tax = load_yaml((DATA / "taxonomy.yaml").read_text(encoding="utf-8"))
    providers = tax["providers"]

    labels: dict[str, str] = {}
    for dim in tax["dimensions"].values():
        for rid, row in (dim.get("rows") or {}).items():
            labels[rid] = row["label"]

    entries: list[dict] = []

    for provider in providers:
        for bucket in BUCKET_FILES:
            new_doc = read_working(provider, bucket)
            if new_doc is None:
                continue
            if args.git:
                old_doc = read_git(args.git, provider, bucket)
            else:
                old_doc = read_dir(args.against, provider, bucket)

            new_caps = new_doc.get("capabilities") or {}
            old_caps = (old_doc or {}).get("capabilities") or {}

            if old_doc is None:
                entries.append({
                    "date": args.date,
                    "provider": providers[provider]["short"],
                    "bucket": bucket.upper(),
                    "row": "—",
                    "label": f"New coverage: {new_doc.get('product', provider)}",
                    "detail": f"{len(new_caps)} cells added",
                    "tag": "research",
                })
                continue

            for rid, new_cell in new_caps.items():
                old_cell = old_caps.get(rid)
                diffs = [
                    describe(f, (old_cell or {}).get(f), new_cell.get(f))
                    for f in TRACKED
                    if (old_cell or {}).get(f) != new_cell.get(f)
                ]
                if not diffs:
                    continue
                entries.append({
                    "date": args.date,
                    "provider": providers[provider]["short"],
                    "bucket": bucket.upper(),
                    "row": rid,
                    "label": labels.get(rid, rid),
                    "detail": "; ".join(diffs),
                    "tag": classify(old_cell, new_cell),
                    "product": new_cell.get("product") or new_doc.get("product"),
                })

            for rid in set(old_caps) - set(new_caps):
                entries.append({
                    "date": args.date,
                    "provider": providers[provider]["short"],
                    "bucket": bucket.upper(),
                    "row": rid,
                    "label": labels.get(rid, rid),
                    "detail": "cell removed",
                    "tag": "research",
                })

    entries.sort(key=lambda e: (e["provider"], e["bucket"], e["row"]))

    n_change = sum(1 for e in entries if e["tag"] == "change")
    n_research = len(entries) - n_change

    # --- CHANGELOG.md ---
    md = [
        "# Changelog",
        "",
        "> [!WARNING]",
        "> **Generated file — do not edit.** Run `uv run scripts/changelog.py`.",
        "",
        "`change` = the vendor shipped something. `research` = our coverage caught up.",
        "Distinguishing these keeps the feed from crying wolf every time we fill a gap.",
        "",
        f"## {args.date}",
        "",
        f"{len(entries)} update(s) — {n_change} vendor change(s), {n_research} research update(s).",
        "",
    ]
    if entries:
        md += ["| Provider | Bucket | Capability | Change | Tag |", "|---|---|---|---|---|"]
        for e in entries:
            md.append(
                f"| {e['provider']} | {e['bucket']} | {e['label']} | "
                f"{e['detail']} | `{e['tag']}` |"
            )
        md.append("")
    else:
        md += ["No changes.", ""]

    (ROOT / "CHANGELOG.md").write_text("\n".join(md), encoding="utf-8")

    # --- updates.json ---
    (ROOT / "updates.json").write_text(
        json.dumps({"generated": args.date, "entries": entries}, indent=2) + "\n",
        encoding="utf-8",
    )

    # --- updates.xml (RSS) ---
    items = []
    for e in entries:
        title = f"{e['provider']} {e['bucket']}: {e['label']}"
        items.append(
            "    <item>\n"
            f"      <title>{escape(title)}</title>\n"
            f"      <description>{escape(e['detail'])} [{e['tag']}]</description>\n"
            f"      <guid isPermaLink=\"false\">{escape(e['date'] + ':' + e['provider'] + ':' + e['bucket'] + ':' + e['row'])}</guid>\n"
            "    </item>"
        )
    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0">\n'
        "  <channel>\n"
        "    <title>CompareAI — Agentic capability updates</title>\n"
        f"    <link>{escape(args.site_url)}</link>\n"
        "    <description>Changes to agentic AI offerings across AWS, Azure, GCP, "
        "BytePlus, and Alibaba Cloud.</description>\n"
        + "\n".join(items)
        + "\n  </channel>\n</rss>\n"
    )
    (ROOT / "updates.xml").write_text(rss, encoding="utf-8")

    print(f"{len(entries)} entries ({n_change} change, {n_research} research)")
    print("Wrote CHANGELOG.md, updates.json, updates.xml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
