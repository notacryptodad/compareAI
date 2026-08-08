# CompareAI — Agentic Capability Comparison Across Clouds

A side-by-side comparison of **agentic AI offerings** from the major cloud providers, in the
spirit of [comparecloud.in](https://comparecloud.in/) — but built for a stack where the
services do *not* map 1:1.

**Providers in scope (v1):** AWS · Microsoft Azure · Google Cloud · BytePlus · Alibaba Cloud

> [!NOTE]
> **Status: alpha — all three buckets populated.** 254 cells defined, **~58% verified**
> against first-party sources as of **2026-08-04**; the rest are honestly marked `unknown`.
> 14 of 15 provider-buckets have data (BytePlus bucket C is empty and says why).
> See [`COMPARISON.md`](COMPARISON.md) for the generated tables and
> [research coverage](COMPARISON.md#research-coverage) per provider.
>
> **No cell claims GA.** Not one vendor page in this set says "generally available", so
> every verified capability reads `documented`. That is a finding about the industry's
> disclosure, not a gap in this data — see [Scoring](#deliberately-opinionated-scoring).

**Quick start**

```bash
uv run scripts/validate.py      # taxonomy conformance, bucket legality, staleness
uv run scripts/check_quotes.py  # every quote must appear verbatim on its cited page
uv run scripts/build_table.py   # regenerate COMPARISON.md from data/
uv run scripts/check_links.py   # source URLs still resolve (catches renames)
```

---

## Why this exists

Ask "which cloud has the better agent platform?" and you get an unanswerable question, because
each vendor slices the stack differently:

| Bucket | AWS | Azure | Google Cloud | BytePlus | Alibaba Cloud |
|---|---|---|---|---|---|
| **A.** Agent SDK / Dev Kit | Strands Agents | Microsoft Agent Framework | Agent Development Kit (ADK) | *not researched* | AgentScope † |
| **B.** Managed agentic platform | Amazon Bedrock AgentCore | Microsoft Foundry Agent Service | Gemini Enterprise Agent Platform | ModelArk Managed Agents | Model Studio |
| **C.** Out-of-box AI capability | Amazon Q Business ⚠ | Microsoft 365 Copilot | Gemini Enterprise | *unreachable docs* | 百炼 app builder ‡ |

*Verified 2026-08-04 against first-party docs.*
*† AgentScope's Alibaba affiliation is **confirmed** via PyPI package metadata — author
"SysML team of Alibaba Tongyi Lab" at an `alibaba-inc.com` address. Neither the GitHub org
(`agentscope-ai`) nor agentscope.io states it; the package registry settled it.*
*⚠ **Amazon Q Business is closed to new customers** — its own docs open with that notice
and redirect to "Amazon Quick". Not a purchasable option, whatever its feature list says.*
*‡ Alibaba offers a visual **builder** for business users rather than a packaged assistant.
Recorded in bucket C as the closest honest fit, not as a like-for-like M365 Copilot rival.*

**Names drift fast — three of the five bucket-B products were renamed recently:**

| Was | Is now |
|---|---|
| Azure AI Foundry Agent Service / Azure AI Agent Service | **Microsoft** Foundry Agent Service |
| Vertex AI Agent Engine / Reasoning Engine | Gemini Enterprise Agent Platform |
| Vertex AI Vector Search 1.0 | Agent Retrieval (Vector Search 2.0) |

This is why `aliases[]` exists in the data model, and why the changelog is a first-class
feature rather than an afterthought.

The columns aren't equivalent products, they're **different decompositions of the same
problem**. So this project compares *capabilities*, positioned on a bucket axis, rather than
mapping product names.

## The two axes

### Axis 1 — Bucket (prevents apples-to-oranges)

Three product buckets, matching the three ways you can actually acquire agentic capability.
Every provider appears in all three columns; the buckets are not mutually exclusive.

| Bucket | Verb | What lives here | Buyer question |
|---|---|---|---|
| **A.** Agent SDK / Dev Kit | *build* | Code-first libraries, orchestration primitives, local dev loop | "How do I *write* an agent?" |
| **B.** Managed agentic platform | *assemble* | Hosted runtime, memory, gateway, identity, sandboxes, eval | "Who runs it in prod?" |
| **C.** Out-of-box AI capability | *buy* | Packaged assistants, low-code builders, prebuilt connectors | "Can I buy instead of build?" |

Scope notes:
- GPU infra and raw model APIs are **out of scope** — not agentic, and comparecloud.in already
  covers infra. Model catalogs appear as dimension 2 instead.
- Coding agents (Kiro, GitHub Copilot, Gemini Code Assist, Qoder, Trae) are a **sub-segment of
  C**, not a fourth bucket.
- Prebuilt AI *APIs* (OCR, speech, translation) are not agentic alone — they appear in
  dimension 3 as "first-party AI-service tools the agent can call."
- "ADK" is avoided as a bucket name because it is also a Google product name.

### Axis 2 — Capability dimensions

Eight dimensions, but they do **not** apply uniformly across buckets. This is a sparse matrix,
not a 3×8 grid — each intersection has its own row set, and three dimensions are reframed.

●●● core · ●● secondary · ● thin · ⟳ reframed · ✕ dropped

| Dimension | A. SDK | B. Platform | C. Out-of-box |
|---|---|---|---|
| 1 Build & orchestrate | ●●● | ●● | ● |
| 2 Model access | ● *portability* | ●●● | ● *"can you BYO?"* |
| 3 Tools & context | ●●● | ●●● | ●●● *connectors* |
| 4 Memory & state | ●● | ●●● | ● |
| 5 Trust | ● *hooks only* | ●●● | ●●● *ACL-aware* |
| 6 Operate | ●● | ●●● | ●● *admin analytics* |
| 7 Commercial | ⟳ **OSS health** | ●●● *per-second* | ●●● *per-seat* |
| 8 Sovereignty | ✕ *runs where you run* | ●●● | ●●● *where the index lives* |

**The three reframes** — do not reuse the same rows here:
- **7 for bucket A** → OSS project health: license, governance, release cadence, breaking-change
  history, and whether the SDK forces you onto that vendor's runtime.
- **6 for bucket C** → admin/adoption analytics and answer-quality feedback, not OTel spans.
- **5 for bucket C** → permission-aware retrieval (does it surface documents the asking user
  cannot open?), DLP, tenant isolation.

Full leaf-level rows per dimension. Each leaf is one comparable row on the site; the
**(A/B/C)** tag marks which buckets that row applies to.

<details>
<summary><b>1. Build & orchestrate</b></summary>

- First-party SDK; languages supported (Python / TS / Java / .NET / Go) — **(A)**
- Code-first vs low-code/visual builder vs both — **(A/B/C)**
- Multi-agent patterns: supervisor, swarm, hierarchical, handoff — **(A)**
- Workflow engine: graph/DAG, durable & resumable execution, retries — **(A/B)**
- Local dev loop: run without cloud creds, hot reload, debug UI — **(A)**
- Long-running agents: max session/task duration, async & background tasks — **(B)**
- Framework agnosticism: can you deploy LangGraph / CrewAI / a *rival cloud's* SDK
  on their runtime? — **(B)**
- Can the packaged product invoke agents you built yourself? — **(C)**
</details>

<details>
<summary><b>2. Model access</b></summary>

- First-party frontier models (Nova / GPT via Azure / Gemini / Seed / Qwen) — **(B)**
- Third-party catalog (Anthropic, Meta, Mistral, DeepSeek, …) — **(B)**
- BYO / open-weight hosting; dedicated throughput & provisioned capacity — **(B)**
- Fine-tuning, distillation, prompt caching — **(B)**
- Model routing / fallback / cost-tiering — **(A/B)**
- Model-provider adapters — can the SDK talk to a *rival* cloud's models? — **(A)**
- OpenAI-compatible endpoint (portability signal) — **(A/B)**
- Is the underlying model choosable, or fixed and opaque? — **(C)**
</details>

<details>
<summary><b>3. Tools & context</b></summary>

- Function/tool calling; parallel tool calls — **(A/B)**
- **MCP support**: as client **(A)**, as managed server host **(B)**, managed registry **(B)**
- Bundled/built-in tool library shipped with the SDK — **(A)**
- OpenAPI → tool import — **(A/B)**
- Managed **code interpreter** (sandboxed, network policy, session persistence) — **(B)**
- Managed **browser / computer use** (headless browser, live view, recording) — **(B)**
- Knowledge / RAG: managed knowledge bases, supported vector stores, parsing,
  chunking, hybrid search, reranking, graph RAG — **(B)**
- Structured data / text-to-SQL over warehouses — **(B)**
- First-party AI-service tools the agent can call (OCR, speech, translation, search) — **(B/C)**
- Prebuilt SaaS/enterprise connectors: count, which systems, auth model — **(C)**
- Enterprise index freshness: real-time vs batch crawl — **(C)**
</details>

<details>
<summary><b>4. Memory & state</b></summary>

- Short-term session/thread memory: managed vs bring-your-own — **(A/B)**
- Checkpointer interface + pluggable backends (Redis / Postgres / DynamoDB / …) — **(A)**
- Long-term memory: semantic, episodic, user-preference; automatic extraction — **(B)**
- Memory namespacing per end-user; TTL, deletion, export (GDPR-relevant) — **(B)**
- Checkpointing and resume-after-failure — **(A/B)**
- Conversation history + personalization; admin retention controls — **(C)**
</details>

<details>
<summary><b>5. Trust: identity, guardrails, human-in-the-loop</b></summary>

- Agent workload identity — does the agent get its *own* principal, or reuse a
  service role? — **(B)**
- Delegated end-user auth: OAuth token vault, 3-legged flows, on-behalf-of — **(B)**
- Least-privilege scoping of tool access; per-tool policy — **(B)**
- Guardrails: content filters, PII detection/redaction, denied topics,
  **prompt-injection defense**, jailbreak detection, groundedness check — **(B/C)**
- Human-in-the-loop: interrupt/resume, approval gates before side-effecting tools — **(A/B)**
- Callback/hook points for custom policy — in bucket A this is *all* you get,
  you build the rest — **(A)**
- Audit trail of every tool invocation (who, what, when, on whose behalf) — **(B/C)**
- **Permission-aware retrieval** — does it surface documents the asking user cannot
  open? ACL trimming at query time — **(C)**
- DLP, tenant isolation, admin controls — **(C)**
</details>

<details>
<summary><b>6. Operate: observability, eval, deployment</b></summary>

- OpenTelemetry / GenAI semantic conventions; span-level tool-call traces — **(A/B)**
- SDK-level instrumentation: emit to *any* OTel backend, or vendor-locked? — **(A)**
- In-repo eval harness runnable in your own CI — **(A)**
- Token & cost attribution per agent / per tenant / per session — **(B)**
- Native APM tie-in (CloudWatch / Azure Monitor / Cloud Trace / ARMS) — **(B)**
- Evaluation service: trajectory eval, LLM-as-judge, dataset mgmt, CI gating, online — **(B)**
- Versioning, aliases, canary, rollback — **(B)**
- IaC coverage (Terraform / CDK / Bicep / ROS) and CI/CD story — **(B)**
- Private networking: VPC/VNet integration, PrivateLink equivalent, egress allowlist — **(B)**
- Admin & adoption analytics, answer-feedback loop — *not* OTel spans — **(C)**
</details>

<details>
<summary><b>7. Commercial — and OSS health for bucket A</b></summary>

**Bucket A → OSS project health** (reframed; pricing is meaningless for a library):
- License (Apache 2.0 / MIT / other) and whether it is genuinely open
- Governance: single-vendor vs foundation; external maintainers accepted?
- Release cadence, breaking-change history, deprecation policy
- **Does the SDK force you onto that vendor's runtime**, or deploy anywhere?
- Community signal: contributors, issue response time, production adopters

**Bucket B → consumption pricing:**
- Pricing axes: per-token, per-runtime-second, per-GB memory, per-tool-call
- Which primitives bill separately (a classic surprise: gateway + memory + sandbox)
- Free tier, commitment/savings plans, marketplace procurement
- Support tier & SLA on the **agent runtime** specifically, not just the model API

**Bucket C → seat pricing:**
- Per-seat cost, minimum seat counts, annual commitment
- **Bundling with licenses you already own** (the M365 E5 effect) — often decides the deal
- Add-on vs included; per-connector or per-index surcharges
</details>

<details>
<summary><b>8. Sovereignty & reach</b></summary>

Not applicable to bucket A — a library runs wherever you run it. One row only:
*does the SDK phone home telemetry by default, and can you disable it?* — **(A)**

- Region availability *of the agent runtime* — usually far narrower than the cloud
  itself; this is the single most under-disclosed fact in the space — **(B)**
- Data residency and in-region processing guarantees; cross-region inference behavior — **(B)**
- Training-on-customer-data policy, retention & abuse-monitoring opt-out — **(B/C)**
- Certifications: SOC 2, ISO 27001/42001, HIPAA, PCI, GDPR, China MLPS — **(B/C)**
- Gov / sovereign cloud availability — **(B/C)**
- Where the **enterprise index** physically lives, and residency for it — **(C)**
- Practical fit: BytePlus and Alibaba Cloud are strongest for CN/SEA — call that out rather
  than penalizing them for a US-centric region list
</details>

## Early findings (2026-08-04)

Things the first research pass surfaced that no vendor page states plainly. Each is
traceable to a `source` in `data/`.

**Region availability is per-service, not per-platform.** AgentCore's 13 services do *not*
share a region footprint: Runtime, Gateway, Identity, Built-in Tools and Observability
reach 20 regions (incl. GovCloud), but Registry reaches **5** and Payments **4**. Anyone
who reads "AgentCore is in 20 regions" and designs around Registry will be wrong. This
single fact justifies the project.

**"No preview label" ≠ GA.** Google's Agent Platform pages carry no GA, Preview, or
Experimental label on *any* service — so every GCP bucket-B cell here is `unknown` on
status, not `ga`. That looks like a gap; it *is* the finding.

**Data-use terms hide in overview pages.** AgentCore's overview states: "AgentCore may use
and store your content to improve your service experience or performance." Easy to miss,
and exactly what a compliance reviewer needs. No opt-out is described on that page.

**Compliance coverage is uneven inside one product.** On Google's own security matrix,
Agent evaluation and Example Store are the only services marked *No* for VPC Service
Controls, CMEK, and data residency at rest — while Runtime, Sessions, Memory Bank and Code
Execution are *Yes*.

**Azure is alone in bridging B → C.** Agents built in Foundry can be published into
Microsoft 365 Copilot and Teams via the Entra Agent Registry. That is a distribution
channel, not a feature — and no other provider documents an equivalent.

**Framework agnosticism is asymmetric.** AgentCore Runtime explicitly lists **Google ADK**
and the OpenAI Agents SDK among supported frameworks; Foundry hosts LangGraph, OpenAI and
**Anthropic** SDKs. Google's platform lists ADK, LangGraph, LangChain, LlamaIndex, AG2 —
but no rival cloud's SDK, and notably **not CrewAI**, which AWS does name.

**ADK ships 5 languages** (Python, TypeScript, Go, Java, Kotlin) — against 2 for Strands
and Microsoft Agent Framework, and 1 for AgentScope. ADK is also the only SDK publishing
an explicit release cadence ("roughly bi-weekly").

**A whole category appeared since early 2026:** automated agent optimization (AWS
AgentCore Optimization, Azure agent optimizer) and agent payments (AWS only, x402
protocol, preview). Both were added to the taxonomy *because* the research found them —
neither was in the original eight dimensions.

**Corrections the research forced on this README's own first draft:** BytePlus does have a
managed agent offering (documented Managed Agents with sessions, skills, tool permission
policies); Strands lives in a `harness-sdk` monorepo, not `sdk-python`; and three of five
bucket-B products have been renamed.

## The project's own first defect (and the tool that caught it)

Worth documenting, because it validates the whole design and is the trap any contributor
will hit.

The first research pass used a fetch tool that answers questions about a page **using an
LLM summariser**. Its paraphrases got recorded into `notes:` as if they were verbatim
quotes. `scripts/check_quotes.py` — which re-fetches every cited page and substring-matches
every quoted string — found **40 fabricated quotes**, two of which were propping up a wrong
`status`:

| Cell | Was | Now | Why |
|---|---|---|---|
| `aws/a-sdk.yaml:otel_traces` | `ga` | `unknown` | "OpenTelemetry"/"OTel" appear **nowhere** in the Strands README. OTel support was an inference. |
| `aws/a-sdk.yaml:human_in_the_loop` | `ga` | `unknown` | "human-in-the-loop" not present; hooks and steering handlers are not the same claim. |

All 154 remaining quotes now verify verbatim, and CI blocks on this check. Two lessons
baked into `docs/CONTRIBUTING.md`: **an LLM summary is never a quote**, and quote only from
the page you actually cite.

Debugging the checker also surfaced two false-positive classes worth knowing about — quotes
elided with `...`, and quotes from a *second* page of the same vendor. Both are legitimate;
the checker now handles the first and the data now attributes the second correctly.

## The second defect: an asymmetry that favoured AWS and Azure

An independent fact-check pass (fresh context, told to be adversarial) found something the
quote checker structurally could not: **status over-claiming**, distributed unevenly.

~40 AWS and Azure cells were marked `ga` purely because no preview label appeared on the
page — while GCP cells got `unknown` for **identical** evidence, with the note "Status
genuinely unlabelled on the page — do not infer GA." Same evidence, three different
verdicts, favouring two providers and penalising a third. Precisely the trap this README
told contributors to avoid, committed at scale in the README's own dataset.

The root cause was a design flaw, not carelessness: one enum was doing two jobs. "Is the
license Apache-2.0" has no launch stage, so `ga` got abused as "verified". The fix splits
them — `documented` for a verified fact with no stage, `ga`/`preview`/`limited` only when
the vendor states the stage — and `validate.py` now **rejects** a stage claim whose notes
cite no vendor stage wording. 84 cells were re-scored; GCP's 14 sourced-but-unlabelled
cells moved up from `unknown` to `documented` in the same pass, so the asymmetry closed
from both ends.

The same pass also caught a **fairness inversion in the opposite direction**: Alibaba's
"will never use your data for model training" statement was sitting in an unfilled cell
while AWS's "may use and store your content" clause was surfaced prominently — the most
favourable fact for a CN provider invisible, the least favourable for AWS highlighted. Both
are now recorded, each citing its own page.

Other real defects it caught: two internal contradictions (Registry called "narrowest" at
5 regions when Payments has 4; Runtime called "widest" when four other services tie it), a
false cross-repo superlative (MAF is *not* the most-starred SDK here — AgentScope ~28.5k
and ADK ~21k both exceed it), ~10 cells whose region facts were provable only on a page
they didn't cite, and three nav-title-only cells that violated the project's own rule
against inferring capability from sidebar links.

**Why this matters for the project's design:** an automated checker verifies quotes but
cannot judge whether a *status* is warranted, and it cannot see asymmetry across providers.
That needs an adversarial reader with fresh context. Both belong in the loop.

### Bonus artifact: the A×B portability grid

5 SDKs × 5 platforms = 25 cells answering one question: **can I run this SDK on that
runtime?** Strands on Vertex Agent Engine? Google ADK on AgentCore? AgentScope on Azure?

Nobody publishes this, it is the most decision-relevant fact for anyone worried about
lock-in, and it only exists because the taxonomy has both an A and a B column. Same
`status` enum, same sourcing rules.

## Deliberately opinionated scoring

Most comparison sites either dump raw feature checkmarks (useless) or hand out 1–5 star ratings
(unfalsifiable). This project uses a **status enum per cell** — cheap to verify, hard to fudge:

| Status | Meaning |
|---|---|
| `ga` | Vendor **explicitly states** generally available |
| `preview` | Vendor **explicitly states** public preview / beta |
| `limited` | Private preview, allowlist, or single-region |
| `documented` | Verified on a first-party page that states **no launch stage** — or a plain fact (license, languages, counts) where stage doesn't apply |
| `partner` | Only via a third party / marketplace, not first-party |
| `oss` | Open-source, self-managed by you |
| `none` | Affirmatively not offered — the vendor says no |
| `unknown` | Not researched |

The enum separates **launch stage** from **fact verified**, because conflating them
produced this project's worst bug (below). `documented` is not a synonym for GA, and the
validator rejects a `ga`/`preview`/`limited` claim whose notes cite no vendor stage wording.

Three traps, all hit on the first research pass:

- **Absence of a preview label is not GA.** As of 2026-08-04, "generally available" appears
  on **none** of the AWS, Azure, or Google agent-platform overview pages. So `ga` count in
  this dataset is currently **zero** — everything verified is `documented`.
- **Apply the rule symmetrically or not at all.** See below.
- **`none` needs a positive statement.** "I couldn't find it" is `unknown`. This is what
  keeps thin English docs from reading as missing features.

No composite "winner" score. Instead, ship **decision lenses**: opinionated views like
*"lowest-lock-in stack"*, *"strictest-compliance stack"*, *"cheapest long-running agents"*,
*"best for China + SEA"* that filter the same underlying data.

## Data model

Source of truth is YAML, one file per provider per bucket. The site is generated — never
hand-edit HTML tables.

A real excerpt from `data/aws/b-platform.yaml` — note that the third cell is `unknown`
*with* a source, which is a finding about AWS's disclosure, not a gap in ours:

```yaml
provider: aws
bucket: b            # a | b | c
capabilities:
  code_interpreter:
    product: AgentCore Code Interpreter
    status: ga
    notes: >
      "An isolated sandbox environment for agents to execute code."
      Languages: "Python, JavaScript and TypeScript".
    source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
    verified_on: 2026-08-04
    verified_by: "@notacryptodad"

  agent_payments:
    product: AgentCore Payments
    status: preview            # explicitly labelled "(preview)" in the region table
    notes: >
      Only 4 regions: N. Virginia, Oregon, Frankfurt, Sydney.
    source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html
    verified_on: 2026-08-04
    verified_by: "@notacryptodad"

  long_running_agents:
    status: unknown
    notes: >
      "extended runtime support for asynchronous agents" is claimed but NO maximum
      session/execution duration is stated on the overview page. Needs the quotas page.
    source: null
    verified_on: null
```

**Rules:**
1. `status: unknown` is always acceptable. A guess dressed as a fact is not.
2. Every non-`unknown` cell needs a `source` and a `verified_on`. Accepted source types
   differ per bucket — this is deliberate:
   | Bucket | Authoritative source |
   |---|---|
   | **A.** SDK | GitHub repo, release notes, API reference — *the repo is the source of truth* |
   | **B.** Platform | Service documentation + pricing page + region table |
   | **C.** Out-of-box | Licensing/plan guide + admin documentation |
   Never a blog post, launch keynote, or press release.
3. Cells older than **90 days** render with a staleness warning; older than 180 days flip
   back to `unknown` in CI.
4. Marketing names change constantly (Azure AI Agent Service → AI Foundry Agent Service;
   Reasoning Engine → Agent Engine; Agentspace → Gemini Enterprise). Track `aliases[]` so
   search still finds the old name.

## Staying current — the changelog is a feature, not a chore

A stale comparison table is worse than no table: it becomes confidently wrong. This space
rewrites itself every few weeks, so freshness machinery is **v1 scope, not a later nicety**.

### What's New / Updates section

Because the data is versioned YAML, the changelog is *derived*, not hand-written. Every merged
PR that changes a `status`, `product`, `limits`, or pricing field emits an entry.

- `CHANGELOG.md` — generated by diffing YAML across commits; grouped by month, then provider
- **What's New page** on the site, plus a compact "recent changes" strip on the home page
- Every entry is a **before → after** with the PR link and both `verified_on` dates:
  > **2026-08** · Google Cloud · B · `code_interpreter`: `preview` → `ga` ([#41](.))
  > **2026-08** · Alibaba Cloud · A · AgentScope `mcp_client`: `unknown` → `ga` ([#43](.))
- Machine-readable `updates.json` + an **RSS/Atom feed** — this is what makes the site sticky
  and gets it linked from elsewhere
- Distinguish **real product changes** from **our research catching up**
  (`unknown → x` is our gap closing, not a vendor launch). Tag entries `change` vs `research`
  so the feed does not cry wolf.

### Review cadence

| Cadence | Action |
|---|---|
| **Weekly** | CI dead-link check; flag cells whose source URL moved or 404s |
| **Monthly** | Sweep one bucket in rotation (A → B → C); re-stamp `verified_on` |
| **Quarterly** | Full re-verification pass; anything past 180 days auto-reverts to `unknown` |
| **Event-driven** | Vendor conference season (re:Invent, Ignite, Cloud Next, Apsara, Force) — expect a burst; open a tracking issue per event |

CI runs a scheduled job that lists the N stalest cells and opens/updates a single
"stale cells" issue, so the work queue maintains itself rather than depending on memory.

## Proposed repo layout

```
compareAI/
├── data/                    # YAML source of truth
│   ├── schema.json          # JSON Schema — CI-enforced
│   ├── taxonomy.yaml        # buckets + capability dimensions (the two axes)
│   ├── portability.yaml     # the A×B grid: which SDK runs on which runtime
│   └── aws/  azure/  gcp/  byteplus/  alibaba/
│       ├── a-sdk.yaml
│       ├── b-platform.yaml
│       └── c-outofbox.yaml
├── site/                    # static site generator (Astro or Next.js SSG)
├── scripts/
│   ├── validate.py          # schema + staleness + dead-link check
│   ├── changelog.py         # diff YAML across commits → CHANGELOG.md + updates.json + RSS
│   └── export.py            # emit CSV / JSON / Markdown for reuse
├── CHANGELOG.md             # generated — do not hand-edit
└── docs/CONTRIBUTING.md
```

## Site UX (borrowing from comparecloud.in, then diverging)

Keep: one dense searchable table, sticky provider column headers, instant fuzzy filter,
deep-linkable rows.

Add:
- **Provider picker** — compare 2 of 5 instead of always 5 (mobile-hostile otherwise)
- **Bucket tabs** — A / B / C. Mandatory, not cosmetic: row sets genuinely differ per bucket,
  so a single merged table would be mostly empty cells
- **Diff mode** — hide rows where all selected providers are identical
- **Cell drill-down** — click a cell for notes, limits, source link, last-verified date
- **"As of" banner** — global freshness date, visible without scrolling
- **What's New strip** — recent changes on the home page, full feed at `/updates`
- **Export** — CSV/JSON so people can paste into their own architecture docs

## Roadmap

**v1 — get one honest, self-updating table shipped**

- [x] Lock the taxonomy (`data/taxonomy.yaml`) — 8 dimensions, 191 cells across 3 buckets
- [x] CI validation — `validate.py` (taxonomy conformance, bucket legality, staleness,
      source requirements), `check_quotes.py` (**verbatim-quote enforcement**),
      `check_links.py` (dead links & redirects), all wired into GitHub Actions
- [x] `changelog.py` → `CHANGELOG.md` + `updates.json` + RSS, with `change` vs `research`
      tagging so the feed doesn't cry wolf
- [x] `build_table.py` → generated `COMPARISON.md`
- [x] First research pass on buckets **A** and **B** — AWS, Azure, GCP verified against
      first-party docs; BytePlus and Alibaba mapped
- [x] Alibaba Cloud: CN-language Bailian (百炼) docs researched — they document a full
      agent app builder (visual + high-code, workflows, RAG, MCP) that the EN page omits
- [x] BytePlus: ModelArk doc bodies retrieved via headless Chrome — regions (only 2!),
      three-part pricing formula, sandbox, MCP, skills, orchestrator/sub-agent all verified
- [x] AgentScope affiliation confirmed (PyPI metadata → Alibaba Tongyi Lab)
- [x] AWS pricing axes + separately-billed primitives filled from the pricing page, which
      also revealed two preview stages the docs pages never stated
- [x] Bucket **C** populated for AWS, Azure, GCP, Alibaba
- [ ] Close the remaining `unknown` cells with `source: null` (~108 of 254) — SLAs,
      certifications, training-data policies, and per-tool region tables
- [ ] BytePlus bucket C — needs a headless browser against the marketing site
- [ ] Fill `oss_community` for ADK and AgentScope so SDK comparisons stop being lopsided
- [ ] Static site MVP: search + provider picker + bucket tabs + What's New page

**v2+**

- [ ] A×B portability grid
- [ ] Decision lenses
- [ ] Pricing calculator for a reference workload (e.g. 10k sessions/mo, 8 tool calls each)
- [ ] Coding-agent sub-segment within C

**Explicitly deferred past v1:** non-cloud agent platforms (OpenAI AgentKit, Anthropic Claude
Agent SDK, LangGraph Platform, CrewAI). Many real decisions are "AgentCore vs. LangGraph
Platform" — but adding them breaks the cloud-vs-cloud framing and doubles the research surface
before the core five are even complete. Revisit once v1 is fully verified.

## Contributing

PRs adding or correcting a cell are the whole point. One capability per PR where possible.
A PR is mergeable when: schema validates, `source` matches the accepted source type for that
bucket (see [Data model](#data-model)), `verified_on` is today, and the claim is reproducible
from the linked page alone.

Corrections from provider employees are welcome — please disclose the affiliation in the PR.

## Non-goals

- No benchmarks or latency/quality measurements — different project, different rigor.
- No "best cloud" verdict.
- No GPU infra or raw model-API comparison — comparecloud.in covers the former.
- No non-cloud agent platforms in v1 (see [Roadmap](#roadmap)).
- No paid placement, ever.

## License

Content: CC BY 4.0 · Code: MIT *(to be confirmed)*
