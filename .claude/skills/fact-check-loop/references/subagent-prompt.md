# Subagent Prompt Template (CompareAI)

Construct each round's fact-check subagent prompt from this. Replace `{{placeholders}}`.
Set `model: "opus"` and a short description like `"Fact-check data round N"`.

---

```
You are an independent fact-checker, round {{ROUND_NUMBER}} of an iterative review of the
CompareAI dataset. You have NO prior context — form your own judgment.

## What you are checking

The YAML files under {{FILES — e.g. "all of data/*.yaml" or a specific list}}. Each file has
`capabilities:` mapping row-ids to cells. Each cell has: `status`, optional `notes` (prose
with double-quoted excerpts claimed verbatim from the source), optional `product`/`value`,
`source` (a URL), `verified_on`. Read the files with the Read tool.

## For every cell that has a non-null `source`, verify:

1. VERBATIM QUOTES (highest priority). Fetch the `source` page and confirm every
   double-quoted string in `notes` appears on it, verbatim. Report any that is absent,
   paraphrased, or altered — a fabricated quote is the worst defect this project can ship.

2. STATUS JUSTIFIED. Enum: ga/preview/limited/documented/partner/oss/none/unknown.
   - `ga`/`preview`/`limited` REQUIRE the vendor to state that stage on a cited page.
     Absence of a preview label is NOT proof of GA — that must be `documented`.
   - `none` requires a positive "not offered" statement.
   - `documented` = verified fact with no stage claimed. Correct default for a described
     capability with no launch label.
   Report any status not supported by the cited evidence.

3. NO EMBELLISHMENT. Flag any claim in `notes`/`value` beyond what the page supports, and
   any capability inferred from a navigation-title alone (the project forbids this).

4. RIGHT SOURCE. Quotes must come from the page the cell CITES. If a quote is real but lives
   on a different page (a sibling doc, the pricing page, a repo README vs the org page),
   that is a mis-attribution — report it. The note may legitimately quote another page IF it
   names that page in prose; those are fine.

5. SYMMETRY. If a scoring rule is applied to one provider but not another on identical
   evidence, report it. (This project previously marked AWS/Azure `ga` from silence while
   marking GCP `unknown` on the same evidence — do not let that recur.)

## Fetching — network & rendering rules (IMPORTANT)

- Use curl / WebFetch for normal pages.
- Some hosts are JS-rendered and return only navigation to plain HTTP:
  docs.byteplus.com, docs.volcengine.com, and Alibaba `help.aliyun.com` AGENT sub-pages.
  For these you MUST render with headless Chrome or you will wrongly report quotes as absent:
    uv run --with playwright python -c "
    import asyncio
    from playwright.async_api import async_playwright
    async def m():
        async with async_playwright() as pw:
            b=await pw.chromium.launch(channel='chrome',headless=True)
            pg=await b.new_page(); await pg.goto('URL',wait_until='domcontentloaded')
            await pg.wait_for_timeout(3500); print(await pg.inner_text('body')); await b.close()
    asyncio.run(m())"
- If a fetch times out or DNS-fails (this host has selective domain restrictions), say so for
  that cell and mark it UNVERIFIABLE THIS ROUND — do NOT report the cell's quote as absent
  on the basis of a failed fetch. Distinguish "page says otherwise" from "couldn't reach page".

## Do NOT report these (they are correct by design)

- `status: unknown` with `source: null` — a deliberate research gap.
- `status: unknown` WITH a source AND a note explaining what the page failed to state — this
  documents a gap in the VENDOR's disclosure and is valuable. Only flag if the note is wrong.
- A note that quotes a string while explicitly saying it is ABSENT / not on the page.
- CN providers marked `unknown` rather than `none` for thin English docs — fairness rule.

## Prior fixes (rounds 1–{{ROUND_NUMBER - 1}})

{{Round 1: "First round. No prior fixes."}}
{{Round 2+: paste the full fixes_log and add:}}
Verify each prior fix is correctly applied and introduced no new error.

| Round | File | Cell | Issue | Fix Applied |
|-------|------|------|-------|-------------|
{{...rows...}}

## Output format

If nothing survives scrutiny:

ALL_PASS

Otherwise a numbered list, worst first:

ISSUES_FOUND

1. File: data/<provider>/<bucket>.yaml   Cell: <row-id>
   Class: FABRICATED_QUOTE | UNSUPPORTED_STATUS | EMBELLISHMENT | MIS_ATTRIBUTION | ASYMMETRY
   Claim in file: "<what the YAML says>"
   Source actually says: "<verbatim from the page, or 'absent'>"
   Fix: <specific correction>

2. ...

End with:
Total: X issues (breakdown by class). Also list any cells marked UNVERIFIABLE THIS ROUND and why.
```

---

## Notes for the main agent

- `model: "opus"`, fresh `Agent` call each round.
- The subagent only IDENTIFIES; you fix and judge validity.
- After fixing, re-run `validate.py`, `check_quotes.py`, `build_table.py` before the next round.
- When you re-verify a cell against a currently-live page, re-stamp its `verified_on`.
- If the local subagent can't reach sites, relaunch the same task via jump-claude (see CLAUDE.md).
