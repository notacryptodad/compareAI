---
name: fact-check-loop
description: >
  Iterative fact-checking loop for CompareAI's data cells against their cited first-party
  source URLs. Spawns independent subagents in fresh contexts to eliminate confirmation
  bias. Each round verifies quotes are verbatim, statuses are justified by the source, and
  no claim is embellished; the main agent fixes findings, then a fresh subagent re-checks
  until zero issues remain.
  Use when: (1) verifying data/*.yaml against sources before a release, (2) after a research
  pass that added or changed cells, (3) user says "fact-check the data" / "check for
  fabricated quotes" / "事实核查" / "幻觉检测", (4) periodic re-verification when cells
  approach the 90/180-day staleness thresholds.
---

# Fact-Check Loop (CompareAI)

Project-tailored copy. The generic skill checks a document against a source; **this one
checks the `data/*.yaml` cells against the first-party pages they cite**, which is the
project's whole value proposition (see `docs/CONTRIBUTING.md`).

## What is being checked

The "document" is the set of YAML files under `data/`. Each capability cell carries
`status`, `notes` (with double-quoted verbatim excerpts), `source` (a URL), and
`verified_on`. The subagent verifies, per cell:

1. **Verbatim quotes** — every double-quoted string in `notes` appears **verbatim** on the
   cited `source` page. A fabricated or paraphrased-but-quoted string is the worst possible
   defect. (This is the machine-checkable part `scripts/check_quotes.py` also covers — the
   subagent catches what the script cannot: quotes on JS-rendered pages, and semantic drift.)
2. **Status justification** — `ga`/`preview`/`limited` require the vendor to STATE the stage
   on some cited page; absence of a preview label is NOT proof of GA (use `documented`).
   `none` requires a positive "not offered" statement.
3. **No embellishment** — no claim in `notes`/`value` beyond what the source supports; no
   capability inferred from a navigation-title alone.
4. **Right source** — quotes are attributed to the page actually cited, not a sibling page.
5. **Symmetry** — a rule applied to one provider is applied to all (the fairness gate).

## Before you start — network & rendering constraints (READ)

This Mac host has selective domain restrictions and many vendor docs are JS-rendered.
So the subagent's fetch may legitimately fail where the data is still correct:

- **Prefer running the checker subagent locally**, but if its fetches time out / DNS-fail,
  the authoritative path is the **jump-claude** skill (EC2, unrestricted egress). See
  `CLAUDE.md`. Hand the subagent the same "verbatim quotes + URLs only" contract.
- **JS-rendered docs** (docs.byteplus.com, aliyun agent sub-pages, volcengine) return only a
  nav shell to plain HTTP. The subagent MUST use Playwright + headless Chrome to read them
  (`uv run --with playwright python …`, `channel="chrome"`) — otherwise it will wrongly
  report BytePlus/Volcengine quotes as absent. Tell it this in the prompt.
- Cells whose header note says the quote was browser-verified carry a weaker automated
  guarantee; the subagent should re-confirm via Playwright, not fail them blindly.

## Workflow

Maintain a `fixes_log`: `{round, file, cell, issue, fix_applied}`.

For each round `N` (from 1):

**(a)** Spawn a FRESH fact-check subagent via the Agent tool, `model: "opus"`, fresh context
every round (never `SendMessage` a prior one — fresh context = independent judgment).

**(b)** Build its prompt from [references/subagent-prompt.md](references/subagent-prompt.md):
which files/cells to check (or "all"), the cumulative `fixes_log`, round number, output format.

**(c)** Parse the result: `ALL_PASS` → exit; otherwise a list of findings → (d).

**(d)** Fix each VALID finding in the YAML. Downgrade unsupported statuses, convert
non-verbatim quotes to marked paraphrases or fix them to match, correct attribution.
Re-stamp `verified_on` when you re-verify a cell. Append to `fixes_log`.

**(e)** Re-run the local gates after fixing:
`uv run scripts/validate.py && uv run scripts/check_quotes.py && uv run scripts/build_table.py`

**(f)** Increment `N`, repeat from (a). **Max 6 rounds** — if issues persist, report and stop.

## Report

```
## Fact-Check Complete

| Round | Issues Found | Issues Fixed |
|-------|-------------|-------------|
| 1     | ...         | ...         |
| N     | 0 (PASS)    | —           |

Total rounds: N | Total issues fixed: X
Scripts: validate ✓  check_quotes ✓  check_links ✓
```

## Key rules

1. **Fresh agent every round** — new `Agent` call, new context, no confirmation bias.
2. **Cumulative fixes log** — pass full history so each agent re-verifies prior fixes.
3. **Finding classes** (subagent classifies each):
   - **Fabricated quote** — quoted string not on the cited page. Highest severity, must fix.
   - **Unsupported status** — `ga`/`preview`/`none` without vendor wording. Must fix.
   - **Embellishment / nav-title inference** — claim beyond the source. Must fix.
   - **Mis-attribution** — quote from a different page than cited. Must fix (re-source).
   - **Asymmetry** — rule applied unevenly across providers. Must fix.
   - **Acceptable** — verified fact, correctly marked. Skip, don't count.
4. **Source coverage** — read the FULL cited page (JS-rendered → Playwright) before judging.
5. **`unknown` with a source + explanatory note is CORRECT**, not a defect — it records a gap
   in the vendor's disclosure. Only flag it if the note's own claims are wrong.
6. **The subagent identifies; the main agent fixes and judges validity.** Don't let the
   subagent edit YAML.

## Relationship to the scripts

`check_quotes.py` is the cheap, always-on machine gate (substring-matches quotes over HTTP).
This loop is the expensive, adversarial, semantic gate — it catches unsupported statuses,
asymmetry, embellishment, and JS-rendered quotes that the script marks UNVERIFIABLE. Run the
loop before a release or after a big research pass; the script runs on every commit/CI.
