# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Generate the comparison tables from data/ into COMPARISON.md.

Run:  uv run scripts/build_table.py
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "COMPARISON.md"

BUCKET_FILES = {"a": "a-sdk.yaml", "b": "b-platform.yaml", "c": "c-outofbox.yaml", "d": "d-devtools.yaml"}

BADGE = {
    "ga": "✅ GA",
    "documented": "📄 Documented",
    "preview": "🟡 Preview",
    "limited": "🟠 Limited",
    "partner": "🔵 Partner",
    "oss": "⚪ OSS",
    "none": "❌ No",
    "unknown": "·",
}


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def cell_text(cell: dict | None) -> str:
    if not cell:
        return "·"
    badge = BADGE.get(cell.get("status", "unknown"), "?")
    parts = [badge]
    if prod := cell.get("product"):
        parts.append(f"<br>{prod}")
    elif (val := cell.get("value")) is not None:
        if isinstance(val, list):
            shown = ", ".join(str(v) for v in val[:3])
            if len(val) > 3:
                shown += f", +{len(val) - 3}"
            parts.append(f"<br>{shown}")
        elif isinstance(val, dict):
            pass
        else:
            parts.append(f"<br>{val}")
    return "".join(parts)


def main() -> int:
    tax = load(DATA / "taxonomy.yaml")
    providers = tax["providers"]
    pkeys = list(providers)

    # Load every data file.
    docs: dict[tuple[str, str], dict] = {}
    for p in pkeys:
        for b, fname in BUCKET_FILES.items():
            fpath = DATA / p / fname
            if fpath.exists():
                docs[(p, b)] = load(fpath)

    lines: list[str] = []
    add = lines.append

    add("# CompareAI — Comparison Tables")
    add("")
    add("> [!WARNING]")
    add("> **Generated file — do not edit.** Run `uv run scripts/build_table.py`.")
    add("> Every non-`·` cell is backed by a first-party source URL and a verification")
    add("> date in `data/`. `·` means **not yet researched** — never \"not offered\".")
    add("")
    add("**📄 Documented is not GA.** It means the capability is verified on a first-party")
    add("page that states no launch stage, or the row is a plain fact (license, languages)")
    add("where launch stage does not apply. ✅ GA appears only where the vendor says")
    add("\"generally available\". As of 2026-08-04 **no vendor page in this set does** —")
    add("which is itself the finding, and why every provider reads `documented` rather than")
    add("AWS/Azure reading GA while Google reads blank.")
    add("")

    # Freshness banner.
    all_dates = [
        str(c["verified_on"])
        for d in docs.values()
        for c in (d.get("capabilities") or {}).values()
        if c.get("verified_on")
    ]
    if all_dates:
        add(f"**Data as of {max(all_dates)}** · "
            f"{len(all_dates)} verified cells across {len(docs)} provider-buckets")
        add("")

    add("Legend: " + " · ".join(f"`{k}` {v}" for k, v in BADGE.items()))
    add("")

    for bkey, bmeta in tax["buckets"].items():
        present = [p for p in pkeys if (p, bkey) in docs]
        if not present:
            continue

        add("---")
        add("")
        add(f"## Bucket {bkey.upper()} — {bmeta['name']} (*{bmeta['verb']}*)")
        add("")
        add(f"> {bmeta['question']}")
        add("")

        prods = []
        for p in present:
            prod = docs[(p, bkey)].get("product", "—")
            prods.append(f"**{providers[p]['short']}**: {prod}")
        add("Products compared: " + " · ".join(prods))
        add("")

        head = "| Capability | " + " | ".join(providers[p]["short"] for p in present) + " |"
        sep = "|---|" + "---|" * len(present)

        for dim in tax["dimensions"].values():
            rows = dim.get("rows") or {}
            # Rows relevant to this bucket that any provider has data for.
            relevant = [
                (rid, r) for rid, r in rows.items()
                if bkey in r["buckets"]
                and any((docs[(p, bkey)].get("capabilities") or {}).get(rid) for p in present)
            ]
            if not relevant:
                continue

            add(f"### {dim['name']}")
            if reframe := (dim.get("reframe") or {}).get(bkey):
                add("")
                add(f"*{reframe.strip()}*")
            add("")
            add(head)
            add(sep)
            for rid, row in relevant:
                cells = [
                    cell_text((docs[(p, bkey)].get("capabilities") or {}).get(rid))
                    for p in present
                ]
                add(f"| {row['label']} | " + " | ".join(cells) + " |")
            add("")

    # Coverage summary.
    add("---")
    add("")
    add("## Research coverage")
    add("")
    add("Three different things, deliberately kept apart — collapsing them into one number")
    add("is what produced this project's first fairness bug:")
    add("")
    add("- **Sourced** — we read the authoritative page and cited it.")
    add("- **Verified** — the cell carries a fact (any status except `unknown`).")
    add("- **Stage stated** — the *vendor* stated a launch stage (`ga`/`preview`/`limited`).")
    add("")
    add("| Provider | Bucket | Cells | Sourced | Verified | Stage stated |")
    add("|---|---|---|---|---|---|")
    STAGED = {"ga", "preview", "limited"}
    for (p, b), d in sorted(docs.items()):
        caps = d.get("capabilities") or {}
        n = len(caps)
        sourced = sum(1 for c in caps.values() if c.get("source"))
        verified = sum(1 for c in caps.values() if c.get("status") != "unknown")
        staged = sum(1 for c in caps.values() if c.get("status") in STAGED)

        def pct(x: int) -> str:
            return f"{x} ({100 * x / n:.0f}%)" if n else "—"

        add(f"| {providers[p]['short']} | {b.upper()} | {n} | {pct(sourced)} "
            f"| {pct(verified)} | {pct(staged)} |")
    add("")
    add("**Stage stated is near-zero everywhere** — vendors document capabilities without")
    add("saying whether they are GA. That is a finding about the industry's disclosure, and")
    add("it must be reported symmetrically: earlier revisions of this data inferred GA from")
    add("silence for AWS and Azure while recording `unknown` for Google on identical")
    add("evidence, which flattered two providers and penalised a third.")
    add("")
    add("Gaps are deliberate and visible. A `·` is a research TODO, not a vendor verdict.")
    add("")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} — {len(lines)} lines, {len(docs)} provider-buckets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
