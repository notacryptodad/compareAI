# CompareAI — project instructions

Comparison of agentic AI offerings across AWS, Azure, GCP, BytePlus, Alibaba Cloud.
Data-first: YAML in `data/` is the source of truth; `COMPARISON.md` is generated.

## Dev server

The site lives in `dist/` (built by `uv run scripts/build_data.py`). Always serve from
`dist/`, never the project root:

```bash
python3 -m http.server -d dist        # or: npx serve dist
```


## Data & verification rules (load-bearing — CI enforces them)

- Run before committing: `uv run scripts/validate.py`, `uv run scripts/check_quotes.py`,
  `uv run scripts/build_table.py`, `uv run scripts/check_links.py`.
- Anything in double quotes in a `notes:` field must be **verbatim** from the cited page;
  paraphrase without quote marks and tag `(Paraphrase.)`. `check_quotes.py` blocks CI on a
  mismatch — and it caught real **source drift** (AgentScope's README was reworded between
  08-04 and 08-07). A quote failure often means the vendor changed the page, not that you
  typo'd; re-verify and re-stamp `verified_on`.
- `ga`/`preview`/`limited` require the **vendor to state the stage**; otherwise use
  `documented`. `validate.py` rejects a stage claim whose notes cite no stage wording.
- **A cell scores the PROVIDER, not only the bucket file's headline product.** A capability
  often lives in a sibling product family — models in Bedrock / Foundry Models / Vertex AI
  rather than AgentCore / Foundry Agent Service / Agent Platform; voice in Nova Sonic; a
  separate agent platform such as BytePlus AgentKit. Before recording `unknown` or `none`,
  search the vendor's other product families, and when the evidence comes from one, set the
  cell's `product:` to that product. Scoping only to the headline product is how whole
  dimensions (Model access) went unresearched for AWS/Azure/GCP.
- Second-page quotes: when a note quotes a page other than `source`, write that page's
  **full URL** in the note — `check_quotes.py` checks quotes against it; a page named only
  by title can't be verified and is reported as an unmatched cross-page quote.
- `js-rendered docs` (docs.byteplus.com, aliyun agent sub-pages, volcengine) serve only a
  nav shell to HTTP fetches — use **Playwright + headless Chrome locally** to read bodies
  (`uv run --with playwright python …`, `channel="chrome"`). `check_quotes.py` reports
  these as UNVERIFIABLE, a deliberately weaker guarantee (see the BytePlus file header).

## Python

Use `uv` (per global instructions): `uv run scripts/x.py`, `uv add`, never `pip`/`python3`.
That includes throwaway one-liners and heredocs: `uv run python -I - <<'EOF'`.

## Subagent briefs

Research and fact-check subagents don't inherit these rules — put them in every brief:
`uv run` only (never `python3`/`python`/`pip`); never `rm` (move unwanted files to
`~/Documents/trashllm`); no state-changing git; edit only the files assigned to that agent.
