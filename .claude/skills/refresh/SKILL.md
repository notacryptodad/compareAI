---
name: refresh
description: >
  Check the CompareAI dataset for rot and decide what to re-research. Runs the staleness
  report (cells past 90/180 days), the dead/moved-link check (URL 404s and 301 redirects
  that signal vendor renames), and validation, then produces a prioritized verdict: what is
  safe, what is stale, what has moved, and where a research pass should go next.
  Use when: (1) user asks "any updates?" / "is the data current?" / "refresh the data",
  (2) periodically (roughly monthly, or when cells approach the 90-day mark),
  (3) before shipping/deploying, (4) user mentions staleness, re-verification, or "更新".
  This skill DETECTS rot; it does not fetch vendor changes itself — acting on its verdict
  means a research pass (local or jump-claude) plus the fact-check-loop skill.
---

# Refresh (CompareAI)

There is no upstream feed to pull — vendors don't push doc changes to this repo. "Refresh"
means: (1) mechanically detect what has aged or where source URLs moved, then (2) decide
whether a human/agent research pass is warranted. This skill does (1) and gives you the
decision for (2). It never edits data.

## Steps

1. **Staleness report** — what's aging and where the gaps are:
   ```bash
   uv run scripts/staleness.py
   ```
   Lists EXPIRED (>180d — `validate.py` errors on these), STALE (>90d), the oldest cell and
   days until the next expiry, research gaps ranked by lowest-coverage bucket, and the
   "sourced-but-unknown" cells that are cheap to revisit. Exit 1 iff something has EXPIRED.

2. **Moved / dead sources** — a 301 or 404 is the strongest early signal of a vendor rename
   (this repo has already caught Azure and Google renames this way):
   ```bash
   uv run scripts/check_links.py
   ```
   Redirects → update the `source:` URL and check whether the PRODUCT was renamed (that's a
   changelog entry, not just a link fix). 404s → the cited page is gone; re-research the cell.

3. **Validate + verify** — confirm the current state is internally sound:
   ```bash
   uv run scripts/validate.py
   uv run scripts/check_quotes.py
   ```

4. **Produce the verdict.** Summarize for the user:
   - Freshness: oldest cell, days to next expiry, counts stale/expired.
   - Moved/dead URLs, each with the cell(s) affected and whether it smells like a rename.
   - Recommended research target: the lowest-coverage bucket(s) from step 1, and any
     EXPIRED cells (which are now hard failures and must be re-verified or reverted).
   - A clear "no action needed" if nothing is stale and all links resolve.

## Acting on the verdict (separate, deliberate step — do NOT do automatically)

If the verdict says re-research is warranted:

1. **Fetch current vendor pages.** Locally if reachable; via **jump-claude** if this host's
   domain restriction blocks them or a different network vantage point is needed (see
   `CLAUDE.md`). JS-rendered docs (BytePlus/Volcengine, Alibaba agent pages) need Playwright
   + headless Chrome.
2. **Edit the affected cells**, re-stamping `verified_on` to today for every cell you
   actually re-read against a live page.
3. **Run the `fact-check-loop` skill** to adversarially confirm the changes — verbatim
   quotes, justified statuses, no embellishment, symmetry.
4. **Regenerate + gate:**
   ```bash
   uv run scripts/build_table.py     # COMPARISON.md
   uv run scripts/build_data.py      # dist/ for the site
   uv run scripts/changelog.py --git HEAD --date <today>   # What's New entries from the diff
   ```
   The changelog step turns your edits into dated before→after entries, tagging real vendor
   `change`s vs `research` catch-up so the feed doesn't cry wolf.

## Cadence guidance

- **Monthly**, or when `staleness.py` shows cells nearing 90 days, run steps 1–4 (detection).
- **This conference season matters** — re:Invent, Ignite, Cloud Next, Apsara, ByteDance
  events produce bursts of change; run a research pass shortly after each.
- The dataset was verified 2026-08; the first 180-day expiries land ~2026-Q1/Feb-2027, and
  they all cluster (same `verified_on`), so plan one sweep rather than being surprised by a
  wall of `validate.py` errors on the same day.

## Why this is a skill, not a cron job

Detection is mechanical, but *acting* on it needs judgment (is a 301 a rename? did the vendor
actually ship, or did our coverage just catch up?) and the network/Playwright handling. A
scheduled job could run steps 1–2 unattended and open an issue, but the repo isn't on GitHub
yet and the valuable part — deciding and re-verifying — isn't automatable. Invoke on demand.
