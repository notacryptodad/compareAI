# CompareAI — project instructions

Comparison of agentic AI offerings across AWS, Azure, GCP, BytePlus, Alibaba Cloud.
Data-first: YAML in `data/` is the source of truth; `COMPARISON.md` is generated.

## Dev server

The site lives in `dist/` (built by `uv run scripts/build_data.py`). Always serve from
`dist/`, never the project root:

```bash
python3 -m http.server -d dist        # or: npx serve dist
```

## Network: this host has domain-access restrictions — use jump-claude for web fetching

**This machine cannot reliably reach every domain the research needs.** When a fetch or
fact-check has to hit external vendor sites, route it through the **jump-claude** skill,
which runs a Claude agent on a remote box with unrestricted egress:

```
~/.claude/skills/jump-claude/jump-claude.sh setup
~/.claude/skills/jump-claude/jump-claude.sh launch <session> --task-file <f> --workdir '~' --model opus --effort high
~/.claude/skills/jump-claude/jump-claude.sh status/tail/wait/result <session>
```

Scope the remote task tightly and demand verbatim quotes + source URLs back (the whole
project rests on traceable evidence — see `docs/CONTRIBUTING.md`).

**Know when the restriction actually bites — don't reflexively spin up the remote box.** As
of the 2026-08 research, plain local `curl`/WebFetch *did* reach `aws.amazon.com`,
`docs.cloud.google.com`, `help.aliyun.com`, `docs.volcengine.com` and `docs.byteplus.com`
(all HTTP 200). The restriction is **selective**, so:

1. Try locally first for a single known URL.
2. If it hangs, times out, or DNS-fails, that's the restriction — hand the task to
   jump-claude rather than fighting it.
3. Also use jump-claude when a different network *vantage point* is the actual need —
   e.g. confirming a page is globally reachable vs. blocked-here, or when a vendor's
   announcement feed / API is shaped differently by region.

The two things that genuinely required the remote box last time were **discovery routes**,
not raw reachability: the AWS What's New JSON search API
(`aws.amazon.com/api/dirs/items/search?item.directoryId=whats-new-v2&q=<term>`) and the
Google Vertex AI **release notes** (launch stages live there, still under the pre-rename
product name — not in the product docs).

### Collecting remote output back to local

`jump-claude.sh result <session>` returns the agent's final text. For files written outside
the project workdir, use `jump-claude.sh fetch <session> <path>` to pull them back.
Prefer `--workdir '~/compareAI'` for repo-relative output so `fetch` just works.

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
- `js-rendered docs` (docs.byteplus.com, aliyun agent sub-pages, volcengine) serve only a
  nav shell to HTTP fetches — use **Playwright + headless Chrome locally** to read bodies
  (`uv run --with playwright python …`, `channel="chrome"`). `check_quotes.py` reports
  these as UNVERIFIABLE, a deliberately weaker guarantee (see the BytePlus file header).

## Python

Use `uv` (per global instructions): `uv run scripts/x.py`, `uv add`, never `pip`/`python3`.
