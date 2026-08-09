# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Validate CompareAI data files against taxonomy.yaml.

Run:  uv run scripts/validate.py
      uv run scripts/validate.py --stale-days 90
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

BUCKET_FILES = {"a": "a-sdk.yaml", "b": "b-platform.yaml", "c": "c-outofbox.yaml", "d": "d-devtools.yaml"}
NEEDS_SOURCE = {"ga", "documented", "preview", "limited", "partner", "oss", "none"}

# A launch-stage claim requires the vendor to SAY the stage. `documented` exists for the
# common case where the docs describe a capability without any stage label.
# Enforced because ~40 cells were once marked `ga` purely from the absence of a preview
# label — for AWS and Azure but not Google, which biased the whole grid.
STAGE_CLAIMS = {"ga", "preview", "limited"}
STAGE_EVIDENCE = (
    "generally available", "general availability", " ga ", "ga)", "ga\"", "(ga",
    "preview", "beta", "allowlist", "private preview", "single-region", "single region",
    "limited", "experimental", "live",
)


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stale-days", type=int, default=90,
                    help="warn when verified_on is older than this")
    ap.add_argument("--expire-days", type=int, default=180,
                    help="error when verified_on is older than this")
    ap.add_argument("--today", default=None,
                    help="override today's date (YYYY-MM-DD) for reproducible runs")
    args = ap.parse_args()

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    tax = load(DATA / "taxonomy.yaml")
    statuses = set(tax["status_enum"])
    providers = set(tax["providers"])
    buckets = set(tax["buckets"])

    # row id -> set of buckets it is allowed in
    allowed: dict[str, set[str]] = {}
    for dim in tax["dimensions"].values():
        for row_id, row in (dim.get("rows") or {}).items():
            allowed.setdefault(row_id, set()).update(row["buckets"])

    errors: list[str] = []
    warnings: list[str] = []
    counts = {s: 0 for s in statuses}
    unsourced_rows: list[str] = []
    total = 0

    for provider in sorted(providers):
        pdir = DATA / provider
        if not pdir.is_dir():
            warnings.append(f"{provider}: no data directory yet")
            continue
        for bucket, fname in BUCKET_FILES.items():
            fpath = pdir / fname
            if not fpath.exists():
                warnings.append(f"{provider}/{fname}: not written yet")
                continue
            doc = load(fpath)
            where = f"{provider}/{fname}"

            if doc.get("provider") != provider:
                errors.append(f"{where}: provider field is {doc.get('provider')!r}, expected {provider!r}")
            if doc.get("bucket") != bucket:
                errors.append(f"{where}: bucket field is {doc.get('bucket')!r}, expected {bucket!r}")

            for row_id, cell in (doc.get("capabilities") or {}).items():
                total += 1
                loc = f"{where}:{row_id}"

                if row_id not in allowed:
                    warnings.append(f"{loc}: row id not in taxonomy (candidate new row?)")
                elif bucket not in allowed[row_id]:
                    errors.append(
                        f"{loc}: row declared for buckets {sorted(allowed[row_id])}, "
                        f"not {bucket!r}"
                    )

                status = cell.get("status")
                if status not in statuses:
                    errors.append(f"{loc}: invalid status {status!r}")
                    continue
                counts[status] += 1

                src, ver = cell.get("source"), cell.get("verified_on")

                if status in STAGE_CLAIMS:
                    blob = f"{cell.get('notes', '')} {cell.get('product', '')}".lower()
                    if not any(k in blob for k in STAGE_EVIDENCE):
                        errors.append(
                            f"{loc}: status {status!r} is a LAUNCH-STAGE claim but notes "
                            f"cite no vendor stage wording. Use `documented` unless the "
                            f"vendor states the stage."
                        )

                if status in NEEDS_SOURCE:
                    if not src:
                        errors.append(f"{loc}: status {status!r} requires a source URL")
                        unsourced_rows.append(loc)
                    if not ver:
                        errors.append(f"{loc}: status {status!r} requires verified_on")
                elif status == "unknown" and src and not cell.get("notes"):
                    # `unknown` WITH a source is legitimate: it means "we read the
                    # authoritative page and it did not state a status". That is a
                    # finding. Only flag it when there is no note explaining why.
                    warnings.append(
                        f"{loc}: status unknown with a source but no notes — "
                        f"explain what the source failed to state"
                    )

                if ver:
                    vdate = ver if isinstance(ver, dt.date) else dt.date.fromisoformat(str(ver))
                    age = (today - vdate).days
                    if age < 0:
                        errors.append(f"{loc}: verified_on {vdate} is in the future")
                    elif age > args.expire_days:
                        errors.append(
                            f"{loc}: verified_on {vdate} is {age}d old "
                            f"(>{args.expire_days}) — must revert to unknown or re-verify"
                        )
                    elif age > args.stale_days:
                        warnings.append(f"{loc}: verified_on {vdate} is {age}d old — stale")

    print(f"CompareAI validate — {total} cells across {len(providers)} providers "
          f"(as of {today})\n")
    print("Status distribution:")
    for s, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        if n:
            pct = 100 * n / total if total else 0
            print(f"  {s:<9} {n:>4}  {pct:5.1f}%")

    known = total - counts.get("unknown", 0)
    print(f"\nCoverage: {known}/{total} cells researched "
          f"({100 * known / total if total else 0:.1f}%)")

    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  ! {w}")
    if errors:
        print(f"\n{len(errors)} ERROR(s):")
        for e in errors:
            print(f"  x {e}")
        return 1

    print("\nOK — no errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
