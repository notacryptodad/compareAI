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

**Data as of 2026-11-22** · 345 verified cells across 19 provider-buckets

Legend: `ga` ✅ GA · `documented` 📄 Documented · `preview` 🟡 Preview · `limited` 🟠 Limited · `partner` 🔵 Partner · `oss` ⚪ OSS · `none` ❌ No · `unknown` ·

---

## Bucket A — Agent SDK / Dev Kit (*build*)

> How do I *write* an agent?

Products compared: **AWS**: Strands Agents · **Azure**: Microsoft Agent Framework · **GCP**: Agent Development Kit (ADK) · **Alibaba**: AgentScope

### Build & orchestrate

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Languages supported | 📄 Documented<br>python, typescript | 📄 Documented<br>python, csharp, go | 📄 Documented<br>python, typescript, go, +2 | 📄 Documented<br>python |
| Code-first vs low-code builder | 📄 Documented<br>code-first | 📄 Documented<br>both | 📄 Documented<br>code-first | 📄 Documented<br>code-first |
| Multi-agent patterns | 📄 Documented | 📄 Documented | 📄 Documented<br>Multi-agent orchestration | 📄 Documented<br>leader-worker, task planning |
| Workflow engine (graph/DAG, durable, resumable) | · | 📄 Documented | 📄 Documented<br>Graph Workflows | · |
| Local dev loop (no cloud creds, hot reload, debug UI) | 📄 Documented<br>strands-cli | 📄 Documented | 📄 Documented<br>Agents CLI | 📄 Documented |
| Long-running agents (max session duration, async/background) | · | · | · | 📄 Documented |
| Multi-tenant serving with tenant/session isolation | · | · | · | 📄 Documented |

### Model access

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Can the SDK talk to a rival cloud's models? | 📄 Documented | 📄 Documented<br>Microsoft Foundry, Anthropic, Azure OpenAI, +2 | 📄 Documented | 📄 Documented<br>OpenAI, Anthropic, Gemini, +6 |

### Tools & context

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| MCP client support | 📄 Documented | 📄 Documented<br>MCPStdioTool / MCPStreamableHTTPTool | 📄 Documented | 📄 Documented |
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
| Human-in-the-loop (interrupt/resume, approval gates) | 📄 Documented<br>HumanInTheLoop intervention + Interrupts | 📄 Documented | 📄 Documented | 📄 Documented |
| Callback/hook points for custom policy | 📄 Documented | · | · | 📄 Documented |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| OpenTelemetry / GenAI semconv; span-level tool-call traces | 📄 Documented | 📄 Documented | · | · |
| In-repo eval harness runnable in your own CI | 📄 Documented<br>strands-agents/evals | · | 📄 Documented | · |

### Commercial (OSS health for bucket A)

*Pricing is meaningless for a library. Bucket A is scored on OSS project health instead — the thing that actually determines whether you can depend on it.*

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| License | 📄 Documented<br>Apache-2.0 | · | 📄 Documented<br>Apache-2.0 | 📄 Documented<br>Apache-2.0 |
| Governance (single-vendor vs foundation; external maintainers?) | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor |
| Release cadence, breaking-change history, deprecation policy | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Does the SDK force you onto that vendor's runtime? | ❌ No | ❌ No | ❌ No | ❌ No |
| Community signal (contributors, issue response, production adopters) | 📄 Documented | · | 📄 Documented | 📄 Documented |

### Sovereignty & reach

*Not applicable — a library runs wherever you run it. One row only: default telemetry.*

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Does the SDK phone home telemetry by default, and can you disable it? | · | · | 📄 Documented | · |

---

## Bucket B — Managed agentic platform (*assemble*)

> Who runs it in prod?

Products compared: **AWS**: Amazon Bedrock AgentCore · **Azure**: Microsoft Foundry Agent Service · **GCP**: Gemini Enterprise Agent Platform · **BytePlus**: BytePlus AgentKit · **Alibaba**: Alibaba Cloud Model Studio Managed Agents

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code-first vs low-code builder | · | 📄 Documented<br>both | · | · | 📄 Documented<br>no-code, low-code |
| Multi-agent patterns | · | · | · | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>Agent orchestration applications |
| Workflow engine (graph/DAG, durable, resumable) | · | · | · | · | 📄 Documented |
| Managed agent runtime | ✅ GA<br>AgentCore Runtime | ✅ GA<br>Agent Runtime | ✅ GA<br>Agent Runtime | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>Managed Agents |
| Managed agent loop (define + invoke an agent in one API call) | ✅ GA<br>AgentCore Harness | 📄 Documented<br>Prompt agents | 🟡 Preview<br>Managed Agents API | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>Managed Agents |
| Session lifecycle API (start, manage, event stream) | · | · | · | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented |
| Long-running agents (max session duration, async/background) | 📄 Documented | 📄 Documented<br>Hosted Agents and Responses API | 📄 Documented | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented |
| Multi-tenant serving with tenant/session isolation | · | · | · | 📄 Documented | · |
| Framework agnosticism | 📄 Documented<br>CrewAI, LangGraph, LlamaIndex, +4 | 📄 Documented<br>Microsoft Agent Framework, LangGraph, OpenAI Agents SDK, +3 | 📄 Documented<br>ADK, LangGraph, LangChain, +5 | 📄 Documented | · |
| Agent-to-agent (A2A) protocol support | · | ✅ GA | · | · | · |
| Can agents you build be published INTO the vendor's packaged product? | · | 📄 Documented | · | · | · |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| First-party frontier models | · | · | · | · | 📄 Documented<br>Qwen4-Max, Qwen3.7-Plus, Qwen3.8-Flash |
| Third-party model catalog | 📄 Documented | 📄 Documented | · | · | 📄 Documented<br>DeepSeek, Kimi, GLM, +1 |
| OpenAI-compatible endpoint | · | 📄 Documented<br>Responses API | · | · | 📄 Documented |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Function/tool calling; parallel tool calls | · | · | · | 📄 Documented<br>ModelArk Managed Agents | · |
| Managed MCP server hosting | 📄 Documented<br>AgentCore Gateway | 📄 Documented | 📄 Documented<br>Agent Gateway | · | · |
| Managed MCP registry / catalog | ✅ GA<br>AWS Agent Registry | 📄 Documented<br>Toolbox | 📄 Documented<br>Agent Registry | · | · |
| Uploadable skill packs (reusable capability bundles) | · | · | · | 📄 Documented<br>ModelArk Managed Agents | · |
| Code interpreter / sandbox | 📄 Documented<br>AgentCore Code Interpreter | 📄 Documented | 📄 Documented<br>Code Execution | 📄 Documented<br>ModelArk Managed Agents | · |
| Managed browser / computer use | 📄 Documented<br>AgentCore Browser | · | 📄 Documented<br>Agent Platform Computer Use | · | 📄 Documented<br>UI Agent |
| Built-in web search tool | ✅ GA<br>AgentCore Web Search API and Web Search tool | 📄 Documented | · | 📄 Documented<br>ModelArk Managed Agents | · |
| Agent payments / microtransactions | ✅ GA<br>AgentCore Payments | · | · | · | · |
| Managed knowledge base / RAG | · | 📄 Documented<br>file search, Foundry IQ, SharePoint, +2 | 📄 Documented<br>Agent Retrieval | · | 📄 Documented |

### Memory & state

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Short-term session/thread memory | 📄 Documented<br>AgentCore Memory | 📄 Documented | 📄 Documented<br>Sessions | · | · |
| Long-term memory (semantic, episodic, preference) | 📄 Documented<br>AgentCore Memory | 📄 Documented | 📄 Documented<br>Agent Platform Memory Bank | 📄 Documented<br>Persistent memory | · |
| Per-end-user namespacing; TTL, deletion, export | · | · | · | 📄 Documented | · |
| Checkpointing and resume-after-failure | · | · | · | 📄 Documented<br>ModelArk Managed Agents | · |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Agent workload identity | 📄 Documented<br>AgentCore Identity | 📄 Documented | 📄 Documented | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented |
| Delegated end-user auth (OAuth token vault, 3LO, on-behalf-of) | 📄 Documented<br>AgentCore Identity | 📄 Documented | 📄 Documented | · | · |
| Least-privilege scoping of tool access; per-tool policy | ✅ GA<br>Policy in AgentCore | · | · | 📄 Documented<br>ModelArk Managed Agents | · |
| Guardrails | 📄 Documented | 📄 Documented | 📄 Documented<br>Model Armor + Agent Gateway policies | 📄 Documented<br>BytePlus AgentKit | 📄 Documented<br>AI safety guardrails |
| Audit trail of every tool invocation | · | · | · | 📄 Documented<br>BytePlus AgentKit | · |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| OpenTelemetry / GenAI semconv; span-level tool-call traces | 📄 Documented<br>AgentCore Observability | ✅ GA | 📄 Documented | · | · |
| Token & cost attribution per agent / tenant / session | · | · | · | 📄 Documented<br>ModelArk Managed Agents | · |
| Native APM tie-in | 📄 Documented<br>Amazon CloudWatch | 📄 Documented<br>Application Insights | · | · | · |
| Evaluation service | ✅ GA<br>AgentCore Evaluations | 📄 Documented | ✅ GA<br>Agent Evaluation | 📄 Documented<br>BytePlus AgentKit | · |
| Versioning, aliases, canary, rollback | · | 📄 Documented | · | 📄 Documented<br>ModelArk Managed Agents | · |
| IaC coverage and CI/CD story | 📄 Documented | 📄 Documented | 📄 Documented | · | · |
| Private networking | ✅ GA | 📄 Documented | 📄 Documented | · | · |
| Automated agent optimization | 🟡 Preview<br>AgentCore Optimization | 🟡 Preview<br>Agent optimizer | · | · | · |
| Managed end-user feedback collection | · | · | 📄 Documented<br>Feedback service | · | · |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Pricing axes | 📄 Documented<br>per_second_compute, per_instance_hour, per_request, +2 | 📄 Documented | 📄 Documented | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented |
| Which primitives bill separately | 📄 Documented | · | · | 📄 Documented<br>ModelArk Managed Agents | · |
| Support tier & SLA on the agent runtime specifically | · | · | 📄 Documented | · | 📄 Documented<br>99.9% |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Region availability OF THE AGENT RUNTIME | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented<br>Johor (ap-southeast-1), Dublin (eu-west-1) | · |
| Per-tool regional availability (does every tool work in every region?) | · | 📄 Documented | · | · | · |
| Hard service limits (files, messages, tools, versions) | · | 📄 Documented | · | · | · |
| Launch-stage evidence trail (where the vendor does/doesn't state GA) | · | · | · | 🟡 Preview | 🟡 Preview |
| Data residency, in-region processing, cross-region inference behavior | · | 📄 Documented | 📄 Documented | · | · |
| Training-on-customer-data policy, retention, abuse-monitoring opt-out | · | 📄 Documented | 📄 Documented | · | 📄 Documented |
| Certifications | 📄 Documented | 📄 Documented | 📄 Documented | · | 📄 Documented<br>SOC 2 |
| Gov / sovereign cloud availability | · | 📄 Documented<br>US Gov Virginia, US Gov Arizona | · | · | · |

---

## Bucket C — Out-of-box AI capability (*buy*)

> Can I buy instead of build?

Products compared: **AWS**: Amazon Q Business · **Azure**: Microsoft 365 Copilot · **GCP**: Gemini Enterprise · **BytePlus**: BytePlus ArkClaw Enterprise · **Alibaba**: Alibaba Cloud Bailian Flow Agent

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code-first vs low-code builder | · | 📄 Documented<br>both | 📄 Documented<br>both | 📄 Documented | 📄 Documented<br>no-code, low-code |
| Packaged assistant — is it purchasable, and what does it cover? | ❌ No<br>Amazon Q Business | 📄 Documented | 📄 Documented | 📄 Documented<br>BytePlus ArkClaw Enterprise | 📄 Documented |
| Can the packaged product invoke agents you built yourself? | 📄 Documented | 📄 Documented | 📄 Documented | · | · |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Is the underlying model choosable, or fixed and opaque? | · | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Prebuilt SaaS/enterprise connectors | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | · |
| Enterprise index freshness (real-time vs batch crawl) | 📄 Documented | · | 📄 Documented | · | · |

### Memory & state

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Conversation history, personalization, retention controls | · | · | · | 📄 Documented | · |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Guardrails | 📄 Documented | 📄 Documented | 📄 Documented<br>Model Armor | 📄 Documented | 📄 Documented<br>AI safety guardrails |
| Audit trail of every tool invocation | · | · | · | 📄 Documented | · |
| Permission-aware retrieval (ACL trimming at query time) | 📄 Documented | 📄 Documented | 📄 Documented | · | · |
| DLP, tenant isolation, admin controls | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Admin & adoption analytics, answer-feedback loop | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Per-seat cost, minimum seats, annual commitment | 📄 Documented | 📄 Documented | · | · | 📄 Documented |
| Bundling with licenses you already own | · | 📄 Documented | 📄 Documented | · | ❌ No |
| Add-on vs included; per-connector or per-index surcharges | · | · | · | · | · |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Training-on-customer-data policy, retention, abuse-monitoring opt-out | 📄 Documented | 📄 Documented | 📄 Documented | · | 📄 Documented |
| Certifications | · | · | · | · | · |
| Where the enterprise index physically lives | 📄 Documented<br>us-east-1, us-west-2, eu-west-1, +1 | 📄 Documented | 📄 Documented<br>global, us, eu, +6 | · | 📄 Documented<br>China (Beijing) |

---

## Bucket D — AI coding tools (*code*)

> Which AI coding tool fits my dev team?

Products compared: **AWS**: Kiro · **Azure**: GitHub Copilot · **GCP**: Antigravity · **BytePlus**: TRAE · **Alibaba**: Qoder CN series

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| IDE integration (VS Code, JetBrains, Vim/Neovim, other) | 📄 Documented<br>Kiro IDE, VS Code, CLI, +3 | 📄 Documented<br>VS Code, Visual Studio, JetBrains, +3 | 📄 Documented<br>Antigravity IDEs, VS Code, JetBrains, +1 | 📄 Documented<br>TRAE IDE, plugin | 📄 Documented<br>Qoder CN IDE, JetBrains |
| CLI / terminal agent mode | 📄 Documented | 📄 Documented | 📄 Documented<br>Antigravity CLI, Gemini CLI | 📄 Documented | 📄 Documented |
| Agentic coding (multi-file edits, task execution, tool use) | ✅ GA | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Is the underlying model choosable, or fixed and opaque? | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Model choice in coding tool | 📄 Documented<br>OpenAI, Anthropic, open-weight models | 📄 Documented<br>GPT-5.3-Codex, GPT-5.4 nano, GPT-5.6 Luna, +3 | 📄 Documented<br>Gemini 3.x | 📄 Documented | 📄 Documented<br>GLM, DeepSeek, Kimi, +1 |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| MCP support in coding tool | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Codebase indexing / repo-wide context | 📄 Documented | 📄 Documented | · | 📄 Documented | 📄 Documented |
| AI code review (PR review, inline suggestions) | 📄 Documented | 📄 Documented | · | · | 📄 Documented |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code snippet retention & training policy | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | · |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Per-seat pricing (individual / business / enterprise tiers) | 📄 Documented | 📄 Documented | · | 📄 Documented | 📄 Documented |
| Free tier or usage-based option | 📄 Documented | 📄 Documented | · | 📄 Documented | 📄 Documented |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Launch-stage evidence trail (where the vendor does/doesn't state GA) | ✅ GA | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

---

## Research coverage

Three different things, deliberately kept apart — collapsing them into one number
is what produced this project's first fairness bug:

- **Sourced** — we read the authoritative page and cited it.
- **Verified** — the cell carries a fact (any status except `unknown`).
- **Stage stated** — the *vendor* stated a launch stage (`ga`/`preview`/`limited`).

| Provider | Bucket | Cells | Sourced | Verified | Stage stated |
|---|---|---|---|---|---|
| Alibaba | A | 19 | 19 (100%) | 16 (84%) | 0 (0%) |
| Alibaba | B | 24 | 24 (100%) | 19 (79%) | 1 (4%) |
| Alibaba | C | 14 | 14 (100%) | 10 (71%) | 0 (0%) |
| Alibaba | D | 12 | 12 (100%) | 11 (92%) | 0 (0%) |
| AWS | A | 17 | 17 (100%) | 16 (94%) | 0 (0%) |
| AWS | B | 30 | 30 (100%) | 27 (90%) | 9 (30%) |
| AWS | C | 13 | 13 (100%) | 11 (85%) | 0 (0%) |
| AWS | D | 12 | 12 (100%) | 12 (100%) | 2 (17%) |
| Azure | A | 17 | 15 (88%) | 13 (76%) | 0 (0%) |
| Azure | B | 35 | 35 (100%) | 34 (97%) | 4 (11%) |
| Azure | C | 14 | 14 (100%) | 13 (93%) | 0 (0%) |
| Azure | D | 12 | 12 (100%) | 12 (100%) | 0 (0%) |
| BytePlus | B | 33 | 33 (100%) | 25 (76%) | 1 (3%) |
| BytePlus | C | 16 | 16 (100%) | 9 (56%) | 0 (0%) |
| BytePlus | D | 12 | 12 (100%) | 11 (92%) | 0 (0%) |
| GCP | A | 16 | 16 (100%) | 16 (100%) | 0 (0%) |
| GCP | B | 25 | 25 (100%) | 25 (100%) | 3 (12%) |
| GCP | C | 14 | 14 (100%) | 13 (93%) | 0 (0%) |
| GCP | D | 12 | 12 (100%) | 8 (67%) | 0 (0%) |

**Stage stated is near-zero everywhere** — vendors document capabilities without
saying whether they are GA. That is a finding about the industry's disclosure, and
it must be reported symmetrically: earlier revisions of this data inferred GA from
silence for AWS and Azure while recording `unknown` for Google on identical
evidence, which flattered two providers and penalised a third.

Gaps are deliberate and visible. A `·` is a research TODO, not a vendor verdict.

