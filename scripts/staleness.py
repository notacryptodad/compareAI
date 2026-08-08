# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Report which cells are aging and where research should go next.

This does NOT fetch anything or change data — it reads verified_on dates and prints a
ranked staleness report. Pair with check_links.py (moved/dead URLs) and a research pass
(re-fetch + fact-check-loop) to actually refresh. See the `refresh` skill.

  uv run scripts/staleness.py                 # report as of today
  uv run scripts/staleness.py --today 2026-11-05
  uv run scripts/staleness.py --stale-days 90 --expire-days 180
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
BUCKET_FILES = {"a": "a-sdk.yaml", "b": "b-platform.yaml", "c": "c-outofbox.yaml"}


def load(p: Path) -> dict:
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--today", default=None)
    ap.add_argument("--stale-days", type=int, default=90)
    ap.add_argument("--expire-days", type=int, default=180)
    args = ap.parse_args()
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    tax = load(DATA / "taxonomy.yaml")
    providers = tax["providers"]

    verified = []          # (age_days, provider, bucket, rid, date)
    unknown_sourced = []   # unknown but with a source (a documented gap — re-fetchable)
    unknown_nosrc = 0      # pure research gaps
    total = 0
    by_bucket_verified = Counter()
    by_bucket_total = Counter()

    for pkey in providers:
        for bkey, fname in BUCKET_FILES.items():
            fpath = DATA / pkey / fname
            if not fpath.exists():
                continue
            for rid, cell in (load(fpath).get("capabilities") or {}).items():
                if not cell:
                    continue
                total += 1
                by_bucket_total[(pkey, bkey)] += 1
                st = cell.get("status", "unknown")
                ver = cell.get("verified_on")
                if st != "unknown":
                    by_bucket_verified[(pkey, bkey)] += 1
                if ver:
                    vdate = ver if isinstance(ver, dt.date) else dt.date.fromisoformat(str(ver))
                    verified.append(((today - vdate).days, pkey, bkey, rid, str(vdate)))
                elif st == "unknown":
                    unknown_nosrc += 1
                if st == "unknown" and cell.get("source"):
                    unknown_sourced.append((pkey, bkey, rid))

    verified.sort(reverse=True)
    stale = [v for v in verified if args.stale_days < v[0] <= args.expire_days]
    expired = [v for v in verified if v[0] > args.expire_days]

    print(f"CompareAI staleness — as of {today}\n")
    print(f"  {total} cells · {len(verified)} verified · {unknown_nosrc} pure research gaps "
          f"(unknown + no source)")
    print(f"  thresholds: warn >{args.stale_days}d, expire >{args.expire_days}d\n")

    if verified:
        oldest = verified[0]
        nextflip = args.expire_days - oldest[0]
        print(f"  oldest verified cell: {oldest[4]} ({oldest[0]}d) — "
              f"{oldest[1]}/{oldest[2]}:{oldest[3]}")
        if nextflip >= 0:
            print(f"  first cell hits the {args.expire_days}d expiry in ~{nextflip} days\n")
        else:
            print()

    def show(title, rows):
        print(f"{title}: {len(rows)}")
        for age, p, b, rid, d in rows[:25]:
            print(f"    {age:>4}d  {p}/{b}:{rid}  (verified {d})")
        if len(rows) > 25:
            print(f"    … +{len(rows) - 25} more")
        print()

    if expired:
        show("EXPIRED (must re-verify or revert to unknown — validate.py errors on these)", expired)
    else:
        print("EXPIRED: none\n")
    show("STALE (re-verify soon)", stale) if stale else print("STALE: none\n")

    # Where to point a research pass: buckets with the most unresearched cells.
    print("Research gaps by provider-bucket (lowest coverage first):")
    ranked = sorted(by_bucket_total,
                    key=lambda k: by_bucket_verified[k] / by_bucket_total[k])
    for k in ranked:
        v, t = by_bucket_verified[k], by_bucket_total[k]
        if v < t:
            print(f"    {k[0]}/{k[1]}: {v}/{t} verified  ({t - v} gaps)")
    print()

    if unknown_sourced:
        print(f"Sourced-but-unknown cells ({len(unknown_sourced)}) — a page was read but "
              f"stated no fact; low-cost to revisit:")
        for p, b, rid in unknown_sourced[:15]:
            print(f"    {p}/{b}:{rid}")
        if len(unknown_sourced) > 15:
            print(f"    … +{len(unknown_sourced) - 15} more")
        print()

    # Exit nonzero only when something has EXPIRED — lets the skill/CI treat that as actionable.
    return 1 if expired else 0


if __name__ == "__main__":
    sys.exit(main())
