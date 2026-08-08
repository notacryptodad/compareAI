# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Assemble the static site into dist/: emit data.json, copy the viewer.

The VIEWER (site/index.html, site/app.js) is static and never regenerated — it reads
this data.json at runtime. This script is the ONLY thing that turns YAML into what the
browser sees, which keeps the validation gate meaningful: nothing reaches the site
without passing through here (and, in CI, through validate.py first).

Runs two ways, same code path:
  local:       uv run scripts/build_data.py           (uv installs pyyaml from the header)
  Cloudflare:  pip install pyyaml && python scripts/build_data.py

Output is deterministic (no wall-clock timestamp) so rebuilds don't churn the diff;
the freshness date shown to users is max(verified_on) across cells.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"
DIST = ROOT / "dist"
BUCKET_FILES = {"a": "a-sdk.yaml", "b": "b-platform.yaml", "c": "c-outofbox.yaml"}


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main() -> int:
    tax = load(DATA / "taxonomy.yaml")
    providers = tax["providers"]

    # Flatten the taxonomy into what the viewer needs: ordered dimensions, each with
    # ordered rows carrying their label / applicable buckets / hint / any reframe note.
    dimensions = []
    for dkey, dim in tax["dimensions"].items():
        rows = []
        for rid, row in (dim.get("rows") or {}).items():
            rows.append({
                "id": rid,
                "label": row["label"],
                "buckets": row["buckets"],
                "hint": row.get("hint"),
            })
        dimensions.append({
            "id": dkey,
            "name": dim["name"],
            "reframe": dim.get("reframe") or {},
            "rows": rows,
        })

    # Per provider, per bucket: the capability cells, plus the product/source header.
    data: dict[str, dict] = {}
    all_dates: list[str] = []
    for pkey in providers:
        data[pkey] = {}
        for bkey, fname in BUCKET_FILES.items():
            fpath = DATA / pkey / fname
            if not fpath.exists():
                continue
            doc = load(fpath)
            caps = {}
            for rid, cell in (doc.get("capabilities") or {}).items():
                if not cell:
                    continue
                caps[rid] = {
                    "status": cell.get("status", "unknown"),
                    "product": cell.get("product"),
                    "value": cell.get("value"),
                    "notes": cell.get("notes"),
                    "source": cell.get("source"),
                    "verified_on": str(cell["verified_on"]) if cell.get("verified_on") else None,
                    "verified_by": cell.get("verified_by"),
                }
                if cell.get("verified_on"):
                    all_dates.append(str(cell["verified_on"]))
            data[pkey][bkey] = {
                "product": doc.get("product"),
                "aliases": doc.get("aliases") or [],
                "notes": doc.get("notes"),
                "capabilities": caps,
            }

    payload = {
        "data_as_of": max(all_dates) if all_dates else None,
        "status_enum": tax["status_enum"],
        "providers": providers,
        "buckets": tax["buckets"],
        "dimensions": dimensions,
        "data": data,
    }

    if not SITE.exists():
        print(f"error: {SITE} not found — the static viewer is missing", file=sys.stderr)
        return 1

    DIST.mkdir(exist_ok=True)
    # Copy the static viewer verbatim.
    for name in ("index.html", "app.js"):
        src = SITE / name
        if not src.exists():
            print(f"error: {src} missing", file=sys.stderr)
            return 1
        shutil.copy2(src, DIST / name)

    (DIST / "data.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    n_cells = sum(len(b["capabilities"]) for p in data.values() for b in p.values())
    print(f"Wrote dist/ — data.json ({n_cells} cells, as of {payload['data_as_of']}) "
          f"+ index.html + app.js")
    return 0


if __name__ == "__main__":
    sys.exit(main())
