# Contributing to CompareAI

The whole value of this project is that **every cell is traceable and falsifiable**. A PR
that adds a plausible-sounding claim without a source makes the project worse than empty.

## The one rule

> If you cannot point to a first-party page that states it, the status is `unknown`.

`unknown` is not a failure. A guess dressed as a fact is.

## Workflow

```bash
uv run scripts/validate.py      # must pass with 0 errors
uv run scripts/check_quotes.py  # must pass with 0 absent — CI blocks on this
uv run scripts/build_table.py   # regenerate COMPARISON.md — commit the result
uv run scripts/check_links.py   # optional locally; CI runs it weekly
```

## Quote discipline (read this before writing a `notes:` field)

**Anything inside double quotes must be copy-pasted from the source.** Not retyped, not
tidied, not reflowed — pasted. `check_quotes.py` fetches every cited page and substring-
matches every quote, and CI fails the build on a miss.

This rule exists because it was already violated at scale: the first research pass used a
tool that summarised pages with an LLM, and **40 of its paraphrases got recorded as
verbatim quotes**. Two cells had a `ga` status resting entirely on wording that was never
on the page — `otel_traces` for Strands cited OpenTelemetry support, but the strings
"OpenTelemetry" and "OTel" appear nowhere in that README. Both are now `unknown`.

Practical rules:

- **Paraphrasing is fine — just don't use quote marks.** Write it as your own sentence and
  add `(Paraphrase.)`. Reviewers can tell the difference; the checker can't guess.
- **Elision with `...` is allowed.** The checker verifies each segment in order.
- **Quote only from the page you cite.** If a fact comes from a second page, name that page
  in the note or give it its own cell. Two AWS pages caused several mismatches this way.
- **Saying a phrase is absent is a legitimate use of quote marks.** The checker skips notes
  containing "does NOT appear", "not found", "could not confirm", etc.
- **Never let an LLM summary become a quote.** If a fetch tool returns prose "quoting" a
  page, that prose is a summary until you verify it against the raw page.
- **JS-rendered docs are exempt from the automated check — and that is a weaker
  guarantee, not a free pass.** `docs.byteplus.com` serves ~300 KB of HTML that strips to
  ~3.3 KB of navigation; the prose only exists after JavaScript runs. `check_quotes.py`
  detects this (under 4,500 chars of extracted text) and reports UNVERIFIABLE instead of
  failing, because otherwise the provider with the most JS-heavy docs would be the one the
  tool punishes. If you add quotes from such a page, verify them yourself with a headless
  browser and say so in the cell's notes, because CI cannot do it for you:

  ```bash
  uv run --with playwright python -c "
  import asyncio
  from playwright.async_api import async_playwright
  async def m():
      async with async_playwright() as pw:
          b = await pw.chromium.launch(channel='chrome', headless=True)
          pg = await b.new_page()
          await pg.goto('URL', wait_until='domcontentloaded'); await pg.wait_for_timeout(3500)
          print(await pg.inner_text('body')); await b.close()
  asyncio.run(m())"
  ```

## Adding or correcting a cell

1. Find the row id in `data/taxonomy.yaml`. If none fits, add one there first — and note
   in your PR why an existing row didn't work. New rows are welcome; the taxonomy was
   already extended once by research (agent payments, agent optimization, managed agent
   loop all came from real findings).
2. Confirm the row's `buckets:` list includes the bucket you're editing. The validator
   enforces this — it caught three genuine taxonomy bugs on its first run.
3. Edit `data/<provider>/<a-sdk|b-platform|c-outofbox>.yaml`.
4. Fill in the cell:

```yaml
  code_interpreter:
    product: AgentCore Code Interpreter    # exact vendor name, no paraphrase
    status: documented                     # NOT `ga` — see status rules below
    value: [python, javascript, typescript]
    notes: >
      "An isolated sandbox environment for agents to execute code."
      Anything you inferred rather than read goes here, marked as inference.
    source: https://docs.aws.amazon.com/...  # the page you actually read
    verified_on: 2026-08-04                  # the date YOU read it
    verified_by: "@your-handle"
```

## Status rules

The enum tracks **two different things**. Keep them apart:

| Status | Use when |
|---|---|
| `ga` | The page **says** "generally available" |
| `preview` | The page **says** preview / beta / experimental |
| `limited` | Private preview, allowlist, or a single region |
| `documented` | Verified on the page, but it states **no launch stage** — or the row is a plain fact (license, languages, star count) where stage is meaningless |
| `partner` | Only through a third party or marketplace |
| `oss` | Open source, you self-manage it |
| `none` | The page affirmatively says it is not supported |
| `unknown` | Not researched |

`ga`/`preview`/`limited` are **launch-stage claims** and require the vendor to state the
stage — `validate.py` rejects them if your notes cite no stage wording. Everything else
verified is `documented`. As of 2026-08-04 the dataset has **zero** `ga` cells, because no
vendor page in it says "generally available".

**Four traps, all of which we have already hit:**

- **Absence of a preview label is not GA.** This one bit hard: ~40 AWS and Azure cells were
  marked `ga` from silence while GCP cells were marked `unknown` on *identical* evidence.
  Use `documented`.
- **Apply every rule symmetrically across providers, or the grid lies.** Before you submit,
  ask: "if the other four providers' docs said exactly this, would I score them the same?"
  A rule applied to one vendor and not another is worse than no rule.
- **A navigation link title is not evidence of a capability.** We violated this for three
  ADK cells and had to walk them back. The BytePlus file was sourced entirely from sidebar
  titles for three research passes and correctly held everything at `unknown` — until a
  headless browser reached the real bodies and lifted it to 42% verified. The lesson cuts
  both ways: don't infer from nav titles, *and* don't assume nav-only is the ceiling.
  Check whether the docs are a JS app before concluding a vendor discloses less.
- **`none` requires a positive statement.** "I didn't find it" is `unknown`. Only record
  `none` when the vendor says no.

**Watch for asymmetry in what you leave blank, too.** An unfilled cell is not neutral. We
once had Alibaba's "will never use your data for model training" sitting blank while AWS's
"may use and store your content" was surfaced — the favourable fact for one provider
invisible, the unfavourable one for another prominent. If you record a policy for one
vendor, check the same row for the others.

## `unknown` with a source is a legitimate, valuable cell

If you read the authoritative page and it failed to state something, record that:

```yaml
  runtime_regions:
    status: unknown
    notes: >
      NO region list on the overview or deploy page — only a pointer to data residency
      docs. Must find the dedicated locations page.
    source: https://...     # the page you read
    verified_on: 2026-08-04
```

This is one of the most useful things you can contribute: it documents a gap in the
*vendor's* disclosure. The validator requires a `notes` explaining what the page failed
to state, so these can't be confused with unresearched cells.

## Further reading

- **[GEO readiness of vendor docs](insights/geo-readiness.md)** — why JS-rendered docs
  make providers invisible to AI search tools (Perplexity, Google AI Overview) and what
  that means for this comparison's methodology and the vendors' discoverability.

## Accepted sources, per bucket

| Bucket | Authoritative source |
|---|---|
| **A** SDK | GitHub repo, release notes, API reference — the repo *is* the source of truth |
| **B** Platform | Service documentation, pricing page, region/quota table |
| **C** Out-of-box | Licensing/plan guide, admin documentation |

Never a blog post, launch keynote, press release, conference talk, or another comparison
site. If a vendor announced something but hasn't documented it, it isn't shippable here.

## Fairness rules

- **Do not penalize BytePlus or Alibaba Cloud for thin English docs.** Cite CN-language
  first-party docs when those are authoritative; note the language in `notes`. `unknown`
  means "we haven't researched it", never "they lack it".
- **Do not compare across buckets.** A model platform's six regions is not comparable to
  an agent runtime's twenty. If the products aren't the same kind of thing, say so in
  `notes` rather than letting the table imply a comparison.
- **Disclose affiliation.** Corrections from provider employees are very welcome — just
  say so in the PR. Domain expertise is an asset; undisclosed advocacy isn't.

## Scale claims to the evidence

Prefer "documented" over "supported", "not stated" over "not available". The `notes` field
exists so you can be precise about what you know versus what you inferred. Quote the
source verbatim where the exact wording matters — those quotes get spot-checked.

## PR checklist

- [ ] `uv run scripts/validate.py` passes with 0 errors
- [ ] `COMPARISON.md` regenerated and committed
- [ ] Every non-`unknown` cell has `source` + `verified_on` + `verified_by`
- [ ] `verified_on` is the date you actually read the page
- [ ] Quotes in `notes` are verbatim
- [ ] `ga`/`preview`/`limited` only where the vendor states the stage; else `documented`
- [ ] Symmetry check: would you score the other four providers the same on this evidence?
- [ ] No comparative/superlative claim sourced to a single vendor's page
- [ ] Affiliation disclosed, if any
