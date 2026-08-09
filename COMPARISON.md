# CompareAI — Comparison Tables

> [!WARNING]
> **Generated file — do not edit.** Run `uv run scripts/build_table.py`.
> Every non-`·` cell is backed by a first-party source URL and a verification
> date in `data/`. `·` means **not yet researched** — never "not offered".

**📄 Documented is not GA.** It means the capability is verified on a first-party
page that states no launch stage, or the row is a plain fact (license, languages)
where launch stage does not apply. ✅ GA appears only where the vendor says
"generally available". As of 2026-08-04 **no vendor page in this set does** —
which is itself the finding, and why every provider reads `documented` rather than
AWS/Azure reading GA while Google reads blank.

**Data as of 2026-08-09** · 242 verified cells across 14 provider-buckets

Legend: `ga` ✅ GA · `documented` 📄 Documented · `preview` 🟡 Preview · `limited` 🟠 Limited · `partner` 🔵 Partner · `oss` ⚪ OSS · `none` ❌ No · `unknown` ·

---

## Bucket A — Agent SDK / Dev Kit (*build*)

> How do I *write* an agent?

Products compared: **AWS**: Strands Agents · **Azure**: Microsoft Agent Framework · **GCP**: Agent Development Kit (ADK) · **Alibaba**: AgentScope

### Build & orchestrate

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Languages supported | 📄 Documented<br>python, typescript | 📄 Documented<br>python, csharp | 📄 Documented<br>python, typescript, go, +2 | 📄 Documented<br>python |
| Code-first vs low-code builder | 📄 Documented<br>code-first | 📄 Documented<br>code-first | 📄 Documented<br>code-first | 📄 Documented<br>code-first |
| Multi-agent patterns | 📄 Documented | 📄 Documented<br>sequential, concurrent, handoff, +1 | 📄 Documented<br>Task API | 📄 Documented<br>leader-worker, task planning |
| Workflow engine (graph/DAG, durable, resumable) | · | 📄 Documented | 📄 Documented<br>Workflow Runtime | · |
| Local dev loop (no cloud creds, hot reload, debug UI) | 📄 Documented<br>strandly | 📄 Documented | 📄 Documented | 📄 Documented |
| Long-running agents (max session duration, async/background) | · | · | · | 📄 Documented |
| Multi-tenant serving with tenant/session isolation | · | · | · | 📄 Documented |

### Model access

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Can the SDK talk to a rival cloud's models? | 📄 Documented | 📄 Documented<br>Microsoft Foundry, Azure OpenAI, OpenAI, +1 | 📄 Documented | 📄 Documented<br>OpenAI, Anthropic, Gemini, +5 |

### Tools & context

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| MCP client support | 📄 Documented | · | 📄 Documented | 📄 Documented |
| Built-in tool library shipped with the SDK | 📄 Documented<br>strands-agents-tools | · | · | · |
| OpenAPI -> tool import | · | · | 📄 Documented | · |
| Code interpreter / sandbox | · | · | · | 📄 Documented<br>local, Docker, Apple Container, +5 |

### Memory & state

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Checkpointing and resume-after-failure | · | 📄 Documented | · | · |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Human-in-the-loop (interrupt/resume, approval gates) | · | 📄 Documented | 📄 Documented | 📄 Documented |
| Callback/hook points for custom policy | 📄 Documented | · | · | 📄 Documented |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| OpenTelemetry / GenAI semconv; span-level tool-call traces | · | 📄 Documented | · | ❌ No |
| In-repo eval harness runnable in your own CI | 📄 Documented<br>strands-agents/evals | 📄 Documented | 📄 Documented | · |

### Commercial (OSS health for bucket A)

*Pricing is meaningless for a library. Bucket A is scored on OSS project health instead — the thing that actually determines whether you can depend on it.*

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| License | 📄 Documented<br>Apache-2.0 | 📄 Documented<br>MIT | 📄 Documented<br>Apache-2.0 | 📄 Documented<br>Apache-2.0 |
| Governance (single-vendor vs foundation; external maintainers?) | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor |
| Release cadence, breaking-change history, deprecation policy | · | 📄 Documented | 📄 Documented | 📄 Documented |
| Does the SDK force you onto that vendor's runtime? | ❌ No | ❌ No | ❌ No | ❌ No |
| Community signal (contributors, issue response, production adopters) | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Sovereignty & reach

*Not applicable — a library runs wherever you run it. One row only: default telemetry.*

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Does the SDK phone home telemetry by default, and can you disable it? | · | · | · | ❌ No |

---

## Bucket B — Managed agentic platform (*assemble*)

> Who runs it in prod?

Products compared: **AWS**: Amazon Bedrock AgentCore · **Azure**: Microsoft Foundry Agent Service · **GCP**: Gemini Enterprise Agent Platform · **BytePlus**: BytePlus ModelArk · **Alibaba**: Alibaba Cloud Model Studio

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code-first vs low-code builder | · | 📄 Documented<br>both | · | · | 📄 Documented<br>both |
| Multi-agent patterns | · | · | · | 📄 Documented<br>orchestrator / sub-agent delegation | · |
| Workflow engine (graph/DAG, durable, resumable) | · | · | · | · | 📄 Documented |
| Managed agent runtime | ✅ GA<br>AgentCore Runtime | ✅ GA<br>Agent Runtime | ✅ GA<br>Agent Runtime | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>百炼 / Bailian application platform (Agent 1.0) |
| Managed agent loop (define + invoke an agent in one API call) | ✅ GA<br>AgentCore Harness | ✅ GA<br>Prompt agents (Foundry) | · | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>百炼 visual agent builder (Agent 1.0) |
| Session lifecycle API (start, manage, event stream) | · | · | · | 📄 Documented | · |
| Long-running agents (max session duration, async/background) | 📄 Documented | · | 📄 Documented | 📄 Documented | · |
| Framework agnosticism | 📄 Documented<br>CrewAI, LangGraph, LlamaIndex, +4 | 📄 Documented<br>Microsoft Agent Framework, LangGraph, OpenAI Agents SDK, +3 | 📄 Documented<br>ADK, LangGraph, LangChain, +4 | · | · |
| Agent-to-agent (A2A) protocol support | · | 🟡 Preview | · | · | · |
| Can agents you build be published INTO the vendor's packaged product? | · | 📄 Documented | · | · | · |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| First-party frontier models | · | · | · | 📄 Documented<br>Dola Seed 2.0, Seed 2.0 Pro, Seed 2.0 Lite, +2 | 📄 Documented<br>Qwen-Max, Qwen-Plus, Qwen-Flash |
| Third-party model catalog | 📄 Documented | 📄 Documented | · | · | 📄 Documented<br>DeepSeek, Kimi, GLM |
| OpenAI-compatible endpoint | · | 📄 Documented<br>Responses API | · | · | 📄 Documented |
| Coding-agent plan / third-party coding-tool integration | · | · | · | · | 📄 Documented |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Function/tool calling; parallel tool calls | · | · | · | 📄 Documented | · |
| Managed MCP server hosting | 📄 Documented<br>AgentCore Gateway | 📄 Documented | 📄 Documented<br>Agent Gateway | 📄 Documented | 📄 Documented |
| Managed MCP registry / catalog | 🟡 Preview<br>AgentCore Registry / AWS Agent Registry | 📄 Documented<br>Toolbox | 📄 Documented<br>Skill Registry | · | · |
| Uploadable skill packs (reusable capability bundles) | · | · | · | 📄 Documented | · |
| Code interpreter / sandbox | 📄 Documented<br>AgentCore Code Interpreter | 📄 Documented | 🟡 Preview<br>Code Execution (Sandbox) | 📄 Documented | 📄 Documented |
| Managed browser / computer use | 📄 Documented<br>AgentCore Browser | · | 📄 Documented<br>Computer Use (Sandbox) | ❌ No | · |
| Built-in web search tool | · | 🟡 Preview | · | · | · |
| Agent payments / microtransactions | 🟡 Preview<br>AgentCore Payments | · | · | · | · |
| Managed knowledge base / RAG | ❌ No | 📄 Documented<br>file search, SharePoint, WorkIQ, +1 | 📄 Documented<br>RAG Engine | 📄 Documented<br>Knowledge base | 📄 Documented |

### Memory & state

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Short-term session/thread memory | 📄 Documented<br>AgentCore Memory | 📄 Documented | ✅ GA<br>Sessions | · | · |
| Long-term memory (semantic, episodic, preference) | 📄 Documented<br>AgentCore Memory | 🟡 Preview | ✅ GA<br>Memory Bank | 📄 Documented<br>Persistent memory | · |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Agent workload identity | 📄 Documented<br>AgentCore Identity | 📄 Documented | 📄 Documented | 📄 Documented | · |
| Delegated end-user auth (OAuth token vault, 3LO, on-behalf-of) | 📄 Documented<br>AgentCore Identity | 📄 Documented | 📄 Documented | 📄 Documented | · |
| Least-privilege scoping of tool access; per-tool policy | ✅ GA<br>Policy in AgentCore | · | · | 📄 Documented | · |
| Guardrails | 📄 Documented | 📄 Documented | · | 📄 Documented | · |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| OpenTelemetry / GenAI semconv; span-level tool-call traces | 📄 Documented<br>AgentCore Observability | ✅ GA | 📄 Documented | ❌ No | 📄 Documented |
| Native APM tie-in | 📄 Documented<br>Amazon CloudWatch | 📄 Documented<br>Application Insights | · | · | · |
| Evaluation service | ✅ GA<br>AgentCore Evaluations | 📄 Documented | 📄 Documented<br>Evaluation Service | ❌ No | 📄 Documented |
| Versioning, aliases, canary, rollback | · | 📄 Documented | · | · | · |
| IaC coverage and CI/CD story | 📄 Documented | 📄 Documented | 📄 Documented | · | · |
| Private networking | ✅ GA | 📄 Documented | 📄 Documented | 📄 Documented | · |
| Automated agent optimization | 🟡 Preview<br>AgentCore Optimization | 📄 Documented<br>agent optimizer | · | · | · |
| Managed end-user feedback collection | · | · | 📄 Documented<br>Feedback service | · | · |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Pricing axes | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Which primitives bill separately | 📄 Documented | · | · | · | · |
| Support tier & SLA on the agent runtime specifically | · | · | · | · | · |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Region availability OF THE AGENT RUNTIME | 📄 Documented | ✅ GA | 🟠 Limited | 📄 Documented<br>Johor (ap-southeast-1), Dublin (eu-west-1) | 📄 Documented<br>Singapore, US (Virginia), China (Beijing), +3 |
| Per-tool regional availability (does every tool work in every region?) | · | 📄 Documented | · | · | · |
| Hard service limits (files, messages, tools, versions) | · | 📄 Documented | · | · | · |
| Launch-stage evidence trail (where the vendor does/doesn't state GA) | · | · | · | · | · |
| Data residency, in-region processing, cross-region inference behavior | · | 📄 Documented | 📄 Documented | · | · |
| Training-on-customer-data policy, retention, abuse-monitoring opt-out | 📄 Documented | · | 📄 Documented | 📄 Documented | 📄 Documented |
| Certifications | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented<br>ISO 9001, ISO 20000, ISO 22301, +10 | · |
| Gov / sovereign cloud availability | · | 📄 Documented<br>US Gov Virginia, US Gov Arizona | · | · | · |

---

## Bucket C — Out-of-box AI capability (*buy*)

> Can I buy instead of build?

Products compared: **AWS**: Amazon Q Business · **Azure**: Microsoft 365 Copilot · **GCP**: Gemini Enterprise · **BytePlus**: None · **Alibaba**: 百炼 / Bailian visual application builder

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code-first vs low-code builder | · | 📄 Documented<br>both | 📄 Documented<br>both | · | 📄 Documented<br>both |
| Packaged assistant — is it purchasable, and what does it cover? | ❌ No<br>Amazon Q Business | 📄 Documented | 📄 Documented | · | 📄 Documented |
| Can the packaged product invoke agents you built yourself? | 📄 Documented | 📄 Documented | 📄 Documented | · | 📄 Documented |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Is the underlying model choosable, or fixed and opaque? | ❌ No | ❌ No | · | · | 📄 Documented |
| Coding-agent plan / third-party coding-tool integration | ❌ No | · | · | · | 📄 Documented |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Prebuilt SaaS/enterprise connectors | 📄 Documented | 📄 Documented | 📄 Documented | · | 📄 Documented |
| Enterprise index freshness (real-time vs batch crawl) | 📄 Documented | 📄 Documented | · | · | 📄 Documented |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Guardrails | 📄 Documented | 📄 Documented | · | · | · |
| Permission-aware retrieval (ACL trimming at query time) | 📄 Documented | 📄 Documented | 📄 Documented | · | · |
| DLP, tenant isolation, admin controls | 📄 Documented | 📄 Documented | · | · | · |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Admin & adoption analytics, answer-feedback loop | · | 📄 Documented | · | · | 📄 Documented |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Per-seat cost, minimum seats, annual commitment | 📄 Documented | 📄 Documented | · | · | · |
| Bundling with licenses you already own | ❌ No | 📄 Documented | 📄 Documented | · | · |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Training-on-customer-data policy, retention, abuse-monitoring opt-out | 📄 Documented | 📄 Documented | 📄 Documented | · | 📄 Documented |
| Where the enterprise index physically lives | 📄 Documented<br>us-east-1, us-west-2, eu-west-1, +1 | 📄 Documented | · | · | 📄 Documented |

---

## Research coverage

Three different things, deliberately kept apart — collapsing them into one number
is what produced this project's first fairness bug:

- **Sourced** — we read the authoritative page and cited it.
- **Verified** — the cell carries a fact (any status except `unknown`).
- **Stage stated** — the *vendor* stated a launch stage (`ga`/`preview`/`limited`).

| Provider | Bucket | Cells | Sourced | Verified | Stage stated |
|---|---|---|---|---|---|
| Alibaba | A | 19 | 18 (95%) | 18 (95%) | 0 (0%) |
| Alibaba | B | 24 | 19 (79%) | 16 (67%) | 0 (0%) |
| Alibaba | C | 15 | 12 (80%) | 10 (67%) | 0 (0%) |
| AWS | A | 17 | 15 (88%) | 13 (76%) | 0 (0%) |
| AWS | B | 29 | 29 (100%) | 28 (97%) | 8 (28%) |
| AWS | C | 14 | 13 (93%) | 13 (93%) | 0 (0%) |
| Azure | A | 17 | 16 (94%) | 15 (88%) | 0 (0%) |
| Azure | B | 35 | 34 (97%) | 32 (91%) | 7 (20%) |
| Azure | C | 15 | 15 (100%) | 14 (93%) | 0 (0%) |
| BytePlus | B | 26 | 25 (96%) | 24 (92%) | 0 (0%) |
| BytePlus | C | 0 | — | — | — |
| GCP | A | 16 | 15 (94%) | 15 (94%) | 0 (0%) |
| GCP | B | 25 | 23 (92%) | 22 (88%) | 5 (20%) |
| GCP | C | 15 | 8 (53%) | 7 (47%) | 0 (0%) |

**Stage stated is near-zero everywhere** — vendors document capabilities without
saying whether they are GA. That is a finding about the industry's disclosure, and
it must be reported symmetrically: earlier revisions of this data inferred GA from
silence for AWS and Azure while recording `unknown` for Google on identical
evidence, which flattered two providers and penalised a third.

Gaps are deliberate and visible. A `·` is a research TODO, not a vendor verdict.

