---
name: refresh
description: >
  End-to-end content refresh for CompareAI data cells. Detects staleness and dead links,
  fetches current vendor pages, updates YAML cells, validates, and fact-checks.
  Use when: (1) user says "refresh" / "update the data" / "check for updates" / "更新",
  (2) a specific provider or cell needs re-verification, (3) a vendor shipped something new
  (conference, blog, release notes mention), (4) cells approach the 90/180-day thresholds,
  (5) user provides new information about a vendor (e.g. "AgentScope released 2.0").
  Covers the full loop: detect → scope → fetch → update → validate → fact-check.
---

# Refresh (CompareAI) — End-to-End Content Update

This skill refreshes the project's data cells against live vendor documentation. It
combines detection (what's stale), research (fetch current state), editing (update YAML),
and verification (validate + fact-check) into one guided workflow.

## Inputs

The user may provide:
- **A specific provider/bucket** — e.g. "refresh GCP bucket B", "update Alibaba SDK data"
- **A specific cell** — e.g. "update aws/b-platform:code_interpreter"
- **New information** — e.g. "AgentScope released 2.0 and is GA now"
- **Nothing specific** — meaning "find what's stale and refresh it"

Adapt scope accordingly. A targeted refresh skips the full staleness sweep.

---

## Phase 1: Detect (what needs refreshing)

### If the user gave a specific target, skip to Phase 2.

### If doing a general sweep:

```bash
uv run scripts/staleness.py
```

This reports: EXPIRED (>180d, hard failures), STALE (>90d), research gaps by bucket,
sourced-but-unknown cells (cheap to revisit), and days until the next expiry.

```bash
uv run scripts/check_links.py
```

301 redirects signal vendor renames. 404s signal the page is gone. Both mean: re-research.

**Produce a hit list** ranked by priority:
1. EXPIRED cells (CI will fail on these)
2. Cells whose source URL moved or 404'd
3. STALE cells (approaching expiry)
4. Sourced-but-unknown cells (cheap: re-read the same URL, see if more is now stated)
5. Pure research gaps (unknown + no source) in low-coverage buckets

---

## Phase 2: Scope and plan

Tell the user what you intend to refresh and roughly how many cells. Get confirmation
before fetching — fetching is the expensive/slow step.

For each cell to refresh, note:
- The current `source` URL (or where to look if `source: null`)
- Whether the page is JS-rendered (BytePlus/Volcengine/some Alibaba pages — needs Playwright)
- Whether this host can reach it (try locally first; fall back to jump-claude)

---

## Phase 3: Fetch current vendor pages

### Fetch strategy (auto-escalating):

The fetch pipeline tries each method in order and **automatically escalates** when the
previous method fails to return useful content. A page is considered unreadable if:
- Body text is < 5000 characters (JS-rendered shell / nav-only)
- Response is a redirect chain that ends in a login wall
- Content is clearly a SPA skeleton (repetitive nav links, no article prose)

**Step 1: Local fetch (WebFetch or curl)** — always try first:
- `aws.amazon.com`, `docs.aws.amazon.com` — usually reachable
- `docs.cloud.google.com` — usually reachable
- `learn.microsoft.com` — usually reachable
- `github.com` — always reachable
- `help.aliyun.com`, `docs.byteplus.com` — reachable but often JS-rendered (empty body)

**Step 2: Playwright auto-fallback** — if Step 1 returned < 5000 chars of body text,
immediately retry with headless Chrome. Do NOT ask the user or skip the page:

```bash
uv run --with playwright python -c "
import asyncio
from playwright.async_api import async_playwright
async def m():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(channel='chrome', headless=True)
        pg = await b.new_page()
        await pg.goto('URL', wait_until='networkidle')
        await pg.wait_for_timeout(5000)
        text = await pg.inner_text('body')
        print(text)
        await b.close()
asyncio.run(m())"
```

Key details for Playwright fallback:
- Use `wait_until='networkidle'` (not `domcontentloaded`) — JS SPAs need network to settle
- Wait 5000ms (not 3500) — BytePlus and Alibaba SPAs are slow to hydrate
- If the page requires scrolling to load content (infinite scroll / lazy sections), add:
  ```python
  await pg.evaluate('window.scrollTo(0, document.body.scrollHeight)')
  await pg.wait_for_timeout(2000)
  ```
- For pages behind a language selector (e.g. Alibaba CN/EN toggle), set locale:
  ```python
  ctx = await b.new_context(locale='zh-CN')  # or 'en-US'
  pg = await ctx.new_page()
  ```

**Known Playwright-required domains** (skip Step 1 for these — go straight to Playwright):
- `docs.byteplus.com` — always JS-rendered, never returns body via HTTP
- `docs.volcengine.com` — same SPA framework as BytePlus
- `help.aliyun.com/zh/model-studio/` sub-pages (NOT the overview, which is server-rendered)
- `docs.aws.amazon.com` sub-pages for Q Business (some are JS-rendered)

**Step 3: jump-claude (remote EC2)** — when BOTH local fetch AND Playwright fail, or for:
- AWS What's New JSON search API (discovery routes)
- Google Vertex AI release notes (launch stages under old product name)
- Any URL that DNS-fails or hangs locally (network restriction, not rendering)
- When a different network vantage point is needed

```bash
# Write a tight task file first
cat > /tmp/refresh-task.md << 'EOF'
Fetch these URLs and return: (1) exact verbatim quotes relevant to [cell],
(2) any GA/preview/limited stage language, (3) the page title and last-updated date.
URLs: [list]
EOF

~/.claude/skills/jump-claude/jump-claude.sh setup
~/.claude/skills/jump-claude/jump-claude.sh launch refresh-$(date +%s) \
  --task-file /tmp/refresh-task.md --workdir '~/compareAI' --model opus --effort high
~/.claude/skills/jump-claude/jump-claude.sh wait refresh-*
~/.claude/skills/jump-claude/jump-claude.sh result refresh-*
```

### Batch Playwright fetching

When multiple URLs need Playwright (e.g. all BytePlus pages, or all Alibaba sub-pages),
batch them in a single script to avoid repeated browser launches:

```bash
uv run --with playwright python -c "
import asyncio, json
from playwright.async_api import async_playwright

URLS = [
    'https://docs.byteplus.com/en/docs/ModelArk/Introduction',
    'https://docs.byteplus.com/en/docs/ModelArk/2553713',
    # ... add all URLs
]

async def fetch_all():
    results = {}
    async with async_playwright() as pw:
        b = await pw.chromium.launch(channel='chrome', headless=True)
        for url in URLS:
            pg = await b.new_page()
            try:
                await pg.goto(url, wait_until='networkidle', timeout=30000)
                await pg.wait_for_timeout(5000)
                text = await pg.inner_text('body')
                results[url] = text[:50000]  # cap to avoid OOM
            except Exception as e:
                results[url] = f'ERROR: {e}'
            finally:
                await pg.close()
        await b.close()
    for url, text in results.items():
        print(f'\\n===== {url} =====')
        print(text[:20000])

asyncio.run(fetch_all())"
```

### Quote verification with Playwright

When `check_quotes.py` reports quotes as UNVERIFIABLE (JS-rendered shell), re-verify them
using Playwright before treating them as failures:

```bash
uv run --with playwright python -c "
import asyncio
from playwright.async_api import async_playwright

URL = 'https://docs.byteplus.com/en/docs/ModelArk/Introduction'
QUOTES = [
    'exact quote to find',
    'another quote to verify',
]

async def verify():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(channel='chrome', headless=True)
        pg = await b.new_page()
        await pg.goto(URL, wait_until='networkidle')
        await pg.wait_for_timeout(5000)
        text = await pg.inner_text('body')
        for q in QUOTES:
            status = 'FOUND' if q in text else 'ABSENT'
            print(f'  {status}: {q[:80]}')
        await b.close()
asyncio.run(verify())"
```

### What to extract from each page:

For each fetched page, record:
1. **Verbatim quotes** — copy-paste relevant sentences (these go in `notes:` in double quotes)
2. **Launch stage language** — any mention of GA / preview / beta / experimental / allowlist
3. **Product name** — check for renames (compare against current `product:` and `aliases:`)
4. **Specific values** — region lists, language lists, pricing numbers, limits
5. **Absence** — if a fact you're looking for is NOT on the page, that is itself a finding

---

## Phase 4: Update YAML cells

For each cell with new information:

```yaml
  cell_id:
    product: <exact vendor name, update if renamed>
    status: <see status rules below>
    value: <structured data if applicable>
    notes: >
      "Verbatim quote from the page." Additional context in your own words.
      (Paraphrase: anything not copy-pasted.)
    source: <URL you actually read — update if it 301'd>
    verified_on: <today's date, YYYY-MM-DD>
    verified_by: "@notacryptodad"
```

### Status rules (load-bearing — get these right):

| Status | When to use |
|---|---|
| `ga` | The page **says** "generally available" / "GA" |
| `preview` | The page **says** "preview" / "beta" / "experimental" |
| `limited` | Private preview, allowlist, single-region, GA-with-gating |
| `documented` | Verified on the page, but **no stage stated** — or a plain fact (license, count) |
| `none` | The page affirmatively says it is not supported |
| `unknown` | Cannot confirm from available sources |

**Critical:** `ga`/`preview`/`limited` require the vendor to STATE the stage. "No preview
label" ≠ GA. Use `documented` for verified-but-unlabelled capabilities.

### If a product was renamed:
- Update `product:` to the new name
- Add the old name to `aliases:`
- Note the rename in the file-level `notes:`
- This is a changelog-worthy event (`change`, not `research`)

### If information was REMOVED from a page:
- Do NOT downgrade blindly — check if it moved to another page first
- If genuinely removed, note it and consider whether status should change

---

## Phase 5: Validate

Run the full validation suite:

```bash
uv run scripts/validate.py
uv run scripts/check_quotes.py
uv run scripts/build_table.py
```

Fix any failures:
- **validate.py errors** — taxonomy mismatch, missing source, stage claim without evidence
- **check_quotes.py failures** — a "verbatim" quote doesn't match the page. Fix options:
  - Re-check: did you copy it exactly? Whitespace, punctuation, Unicode?
  - If the page changed: update the quote to match current wording
  - If it was never verbatim: remove quotes and mark `(Paraphrase.)`
- **build_table.py** — just regenerates; commit the new `COMPARISON.md`

Also run link check if you updated any source URLs:
```bash
uv run scripts/check_links.py
```

---

## Phase 6: Fact-check (for non-trivial changes)

**Skip this step for:** simple re-stamps where content hasn't changed, adding `verified_on`
dates, fixing typos.

**Run this step for:** new cells, status changes, new quotes, renames.

Invoke the `fact-check-loop` skill:
- It spawns independent subagents that adversarially verify each change
- Catches: fabricated quotes, unjustified status claims, embellishment, asymmetry

---

## Phase 7: Finalize

1. **Regenerate outputs:**
   ```bash
   uv run scripts/build_table.py          # COMPARISON.md
   uv run scripts/build_data.py           # dist/ for the site
   ```

2. **Generate changelog entries** (if this is a meaningful update):
   ```bash
   uv run scripts/changelog.py --git HEAD --date $(date +%Y-%m-%d)
   ```
   Tag entries correctly:
   - `change` — the vendor actually shipped/renamed/removed something
   - `research` — our coverage caught up (unknown → documented)

3. **Report to user:**
   - How many cells were refreshed
   - Any status changes (before → after)
   - Any renames detected
   - Any cells that could NOT be refreshed (unreachable, JS-rendered without Playwright)
   - Remaining gaps, if relevant

---

## Handling specific scenarios

### "A vendor released version X / got GA"

1. Identify which cells are affected (often multiple across the provider's files)
2. Find the authoritative source (release notes, changelog, docs page)
3. Update all affected cells — status, version in notes, quotes from announcement
4. Check for NEW capabilities that v2/GA might have added (new taxonomy rows?)
5. Run validation + fact-check

### "Refresh everything" (full sweep)

1. Run Phase 1 fully
2. Group cells by source URL (many cells share one page — one fetch covers multiple cells)
3. Process by provider to maintain context
4. Budget: a full sweep across all 5 providers is large. Suggest doing one provider or one
   bucket per session unless the user insists on everything at once.

### Conference season (re:Invent, Ignite, Cloud Next, Apsara)

1. Check the vendor's "What's New" / release notes feed for agent-related announcements
2. For each announcement: does it affect an existing cell, or does it warrant a new one?
3. New capabilities may need new taxonomy rows — add to `taxonomy.yaml` first
4. A rename without new capability is still a change worth recording

---

## Symmetry check (do this LAST, every time)

Before finishing, ask: "Did I apply the same standard to all five providers?"

- If you upgraded one provider's status, check the same row for the other four
- If you found a policy statement for one, look for the equivalent page for others
- If you left a cell unknown for one provider, make sure you didn't mark it documented
  for another on identical evidence

The project's worst bug was exactly this asymmetry. It takes 60 seconds to check and
prevents the most damaging class of error.
