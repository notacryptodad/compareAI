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

**Data as of 2026-11-23** · 357 verified cells across 19 provider-buckets

Legend: `ga` ✅ GA · `documented` 📄 Documented · `preview` 🟡 Preview · `limited` 🟠 Limited · `partner` 🔵 Partner · `oss` ⚪ OSS · `none` ❌ No · `unknown` ·

---

## Bucket A — Agent SDK / Dev Kit (*build*)

> How do I *write* an agent?

Products compared: **AWS**: Strands Agents · **Azure**: Microsoft Agent Framework · **GCP**: Agent Development Kit (ADK) · **Alibaba**: AgentScope

### Build & orchestrate

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Languages supported | 📄 Documented<br>python, typescript | 📄 Documented<br>python, csharp, go | 📄 Documented<br>python, typescript, go, +2 | 📄 Documented<br>python, java, typescript |
| Code-first vs low-code builder | 📄 Documented<br>code-first | 📄 Documented<br>code-first | 📄 Documented<br>code-first | 📄 Documented<br>code-first |
| Multi-agent patterns | 📄 Documented<br>agents-as-tools, graph, swarm, +2 | 📄 Documented<br>sequential, concurrent, handoff, +2 | 📄 Documented<br>Task API | 📄 Documented<br>leader-worker, task planning, pipeline |
| Workflow engine (graph/DAG, durable, resumable) | · | 📄 Documented | 📄 Documented<br>Workflow Runtime | · |
| Local dev loop (no cloud creds, hot reload, debug UI) | 📄 Documented<br>strands CLI | 📄 Documented | 📄 Documented | 📄 Documented |
| Long-running agents (max session duration, async/background) | · | · | · | 📄 Documented |
| Multi-tenant serving with tenant/session isolation | · | · | · | 📄 Documented |

### Model access

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Can the SDK talk to a rival cloud's models? | 📄 Documented | 📄 Documented<br>Microsoft Foundry, Azure OpenAI, OpenAI, +5 | 📄 Documented | 📄 Documented<br>OpenAI, Anthropic, Gemini, +7 |

### Tools & context

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| MCP client support | 📄 Documented | 📄 Documented<br>MCPToolDefinition / hostedtool.MCPServer | 📄 Documented | 📄 Documented |
| Built-in tool library shipped with the SDK | 📄 Documented<br>Vended tools (strands.vended_tools) | · | · | · |
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
| OpenTelemetry / GenAI semconv; span-level tool-call traces | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| In-repo eval harness runnable in your own CI | 📄 Documented<br>strands-agents/evals | 📄 Documented | 📄 Documented | 📄 Documented<br>OpenJudge (agentscope-ai/OpenJudge) |

### Commercial (OSS health for bucket A)

*Pricing is meaningless for a library. Bucket A is scored on OSS project health instead — the thing that actually determines whether you can depend on it.*

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| License | 📄 Documented<br>Apache-2.0 | 📄 Documented<br>MIT | 📄 Documented<br>Apache-2.0 | 📄 Documented<br>Apache-2.0 |
| Governance (single-vendor vs foundation; external maintainers?) | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor | 📄 Documented<br>single-vendor |
| Release cadence, breaking-change history, deprecation policy | 📄 Documented<br>multiple per week | 📄 Documented | 📄 Documented | 📄 Documented |
| Does the SDK force you onto that vendor's runtime? | ❌ No | ❌ No | ❌ No | ❌ No |
| Community signal (contributors, issue response, production adopters) | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Sovereignty & reach

*Not applicable — a library runs wherever you run it. One row only: default telemetry.*

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Does the SDK phone home telemetry by default, and can you disable it? | 📄 Documented | 📄 Documented | 📄 Documented | · |

---

## Bucket B — Managed agentic platform (*assemble*)

> Who runs it in prod?

Products compared: **AWS**: Amazon Bedrock AgentCore · **Azure**: Microsoft Foundry Agent Service · **GCP**: Gemini Enterprise Agent Platform · **BytePlus**: BytePlus ModelArk · **Alibaba**: Alibaba Cloud Model Studio

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code-first vs low-code builder | · | 📄 Documented<br>both | · | · | 📄 Documented<br>both |
| Multi-agent patterns | · | · | · | 📄 Documented<br>orchestrator / sub-agent delegation (coordinator), persistent multi-level sub-agent threads (multiagent_20261001) | 📄 Documented<br>Agent orchestration applications |
| Workflow engine (graph/DAG, durable, resumable) | · | · | · | · | 📄 Documented<br>Flow Agent — 工作流应用 |
| Managed agent runtime | ✅ GA<br>AgentCore Runtime | ✅ GA<br>Agent Runtime | ✅ GA<br>Agent Runtime | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>百炼 Managed Agents |
| Managed agent loop (define + invoke an agent in one API call) | ✅ GA<br>AgentCore Harness | ✅ GA<br>Prompt agents (Foundry) | 🟡 Preview<br>Managed Agents API | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>百炼 Flow Agent — 智能体应用 (Agent 2.0) |
| Session lifecycle API (start, manage, event stream) | · | · | · | 📄 Documented | 📄 Documented<br>百炼 Managed Agents |
| Long-running agents (max session duration, async/background) | 📄 Documented | 📄 Documented<br>Background Responses + Hosted Agents | 📄 Documented | 📄 Documented | 📄 Documented<br>百炼 Managed Agents |
| Multi-tenant serving with tenant/session isolation | · | · | · | 📄 Documented | · |
| Framework agnosticism | 📄 Documented<br>CrewAI, LangGraph, LlamaIndex, +4 | 📄 Documented<br>Microsoft Agent Framework, LangGraph, LangChain / Deep Agents, +4 | 📄 Documented<br>ADK, LangGraph, LangChain, +5 | 📄 Documented<br>BytePlus AgentKit | · |
| Agent-to-agent (A2A) protocol support | ✅ GA<br>AgentCore Runtime | ✅ GA | 🟡 Preview<br>Agent Runtime + Agent Registry | · | · |
| Can agents you build be published INTO the vendor's packaged product? | · | 📄 Documented | · | · | · |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| First-party frontier models | · | · | · | 📄 Documented<br>Dola Seed 2.1 Turbo, Seed 2.0 Pro, Seed 2.0 Lite, +2 | 📄 Documented<br>qwen4-max, qwen3.7-plus, qwen3.8-flash |
| Third-party model catalog | 📄 Documented | 📄 Documented | · | · | 📄 Documented<br>DeepSeek, GLM, Kimi, +1 |
| OpenAI-compatible endpoint | · | 📄 Documented<br>Responses API | · | · | 📄 Documented |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Function/tool calling; parallel tool calls | · | · | · | 📄 Documented | · |
| Managed MCP server hosting | 📄 Documented<br>AgentCore Gateway | 📄 Documented | 📄 Documented<br>Agent Gateway | 📄 Documented | 📄 Documented |
| Managed MCP registry / catalog | ✅ GA<br>AWS Agent Registry | 📄 Documented<br>Toolbox | ✅ GA<br>Agent Registry | · | · |
| Uploadable skill packs (reusable capability bundles) | · | · | · | 📄 Documented | · |
| Code interpreter / sandbox | ✅ GA<br>AgentCore Code Interpreter | 📄 Documented | 🟡 Preview<br>Code Execution (Sandbox) | 📄 Documented | 📄 Documented<br>百炼 Sandbox — Code Interpreter Sandbox |
| Managed browser / computer use | ✅ GA<br>AgentCore Browser | ✅ GA<br>Browser automation tool (Foundry Agent Service) | ✅ GA<br>Agent Platform Computer Use (Sandbox) | 📄 Documented | 📄 Documented<br>百炼 Sandbox — Browser Use Sandbox |
| Built-in web search tool | ✅ GA<br>AgentCore Web Search (Web Search API and Web Search Tool connector) | 📄 Documented | · | 📄 Documented | · |
| Agent payments / microtransactions | ✅ GA<br>AgentCore Payments | · | · | · | · |
| Managed knowledge base / RAG | ✅ GA<br>Amazon Bedrock Managed Knowledge Base (AgentCore Gateway connector) | 📄 Documented<br>file search, Foundry IQ, SharePoint, +2 | 📄 Documented<br>RAG Engine | 📄 Documented<br>BytePlus Knowledge base (Knowledge Engine) | 📄 Documented |

### Memory & state

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Short-term session/thread memory | 📄 Documented<br>AgentCore Memory | 📄 Documented | ✅ GA<br>Sessions | · | · |
| Long-term memory (semantic, episodic, preference) | ✅ GA<br>AgentCore Memory | 🟡 Preview | ✅ GA<br>Agent Platform Memory Bank | 📄 Documented<br>Persistent memory | 📄 Documented<br>百炼 Memory (记忆库) + Managed Agents Memory Store |
| Per-end-user namespacing; TTL, deletion, export | · | · | · | 📄 Documented<br>Persistent memory | · |
| Checkpointing and resume-after-failure | · | · | · | 📄 Documented | · |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Agent workload identity | ✅ GA<br>AgentCore Identity | 📄 Documented | ✅ GA<br>Agent Identity | 📄 Documented | 📄 Documented |
| Delegated end-user auth (OAuth token vault, 3LO, on-behalf-of) | 📄 Documented<br>AgentCore Identity | 📄 Documented | 📄 Documented<br>Agent Identity auth manager | 📄 Documented | · |
| Least-privilege scoping of tool access; per-tool policy | ✅ GA<br>Policy in AgentCore | · | · | 📄 Documented | · |
| Guardrails | 📄 Documented | 📄 Documented | 📄 Documented<br>Safety Filters + Model Armor + Sensitive Data Protection | 📄 Documented<br>ModelArk Content filter | 📄 Documented<br>AI Guardrails + AI Gateway |
| Human-in-the-loop (interrupt/resume, approval gates) | · | · | · | 📄 Documented | · |
| Audit trail of every tool invocation | · | · | · | 📄 Documented<br>ModelArk Managed Agents | · |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| OpenTelemetry / GenAI semconv; span-level tool-call traces | ✅ GA<br>AgentCore Observability | ✅ GA | ✅ GA<br>Agent Observability | · | 📄 Documented<br>百炼 Evolution — 应用观测 |
| Token & cost attribution per agent / tenant / session | · | · | · | 📄 Documented<br>ModelArk Managed Agents | · |
| Native APM tie-in | 📄 Documented<br>Amazon CloudWatch | 📄 Documented<br>Application Insights | · | · | · |
| Evaluation service | ✅ GA<br>AgentCore Evaluations | 📄 Documented | ✅ GA<br>Agent Evaluation (Evaluation Service) | 📄 Documented<br>BytePlus AgentKit | 📄 Documented<br>百炼 Evolution — 应用评测 |
| Versioning, aliases, canary, rollback | · | 📄 Documented | · | 📄 Documented<br>ModelArk Managed Agents | · |
| IaC coverage and CI/CD story | 📄 Documented | 📄 Documented | 📄 Documented | · | · |
| Private networking | ✅ GA | 📄 Documented | 📄 Documented | 📄 Documented | · |
| Automated agent optimization | ✅ GA<br>AgentCore Optimization | 🟡 Preview<br>agent optimizer | · | · | · |
| Managed end-user feedback collection | · | · | 📄 Documented<br>Feedback service | · | · |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Pricing axes | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Which primitives bill separately | 📄 Documented | · | · | 📄 Documented<br>ModelArk Managed Agents | · |
| Support tier & SLA on the agent runtime specifically | 📄 Documented<br>99.9% | · | · | · | · |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Region availability OF THE AGENT RUNTIME | 📄 Documented | ✅ GA | 📄 Documented | 📄 Documented<br>Johor (ap-southeast-1), Dublin (eu-west-1) | 📄 Documented<br>Singapore, US (Virginia), China (Beijing), +3 |
| Per-tool regional availability (does every tool work in every region?) | · | 📄 Documented | · | · | · |
| Hard service limits (files, messages, tools, versions) | · | 📄 Documented | · | · | · |
| Launch-stage evidence trail (where the vendor does/doesn't state GA) | · | · | · | 📄 Documented | 🟡 Preview |
| Data residency, in-region processing, cross-region inference behavior | · | 📄 Documented | 📄 Documented | 📄 Documented | · |
| Training-on-customer-data policy, retention, abuse-monitoring opt-out | · | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Certifications | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented<br>ISO 9001, ISO 20000, ISO 22301, +10 | 📄 Documented<br>SOC 2 |
| Gov / sovereign cloud availability | · | 📄 Documented<br>US Gov Virginia, US Gov Arizona | · | · | · |

---

## Bucket C — Out-of-box AI capability (*buy*)

> Can I buy instead of build?

Products compared: **AWS**: Amazon Q Business · **Azure**: Microsoft Copilot · **GCP**: Gemini Enterprise · **BytePlus**: BytePlus ArkClaw Enterprise · **Alibaba**: Alibaba Cloud Model Studio Flow Agent

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code-first vs low-code builder | · | 📄 Documented<br>both | 📄 Documented<br>both | 📄 Documented | 📄 Documented<br>both |
| Packaged assistant — is it purchasable, and what does it cover? | ❌ No<br>Amazon Q Business | 📄 Documented | 📄 Documented | 📄 Documented<br>BytePlus ArkClaw Enterprise | 📄 Documented |
| Can the packaged product invoke agents you built yourself? | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Is the underlying model choosable, or fixed and opaque? | · | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Prebuilt SaaS/enterprise connectors | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 🟡 Preview<br>百炼 Connector |
| Enterprise index freshness (real-time vs batch crawl) | 📄 Documented | 📄 Documented | 📄 Documented | · | 📄 Documented |

### Memory & state

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Conversation history, personalization, retention controls | · | · | · | 📄 Documented | · |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Guardrails | 📄 Documented | 📄 Documented | 📄 Documented<br>Model Armor | 📄 Documented | 📄 Documented<br>AI Guardrails |
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
| Per-seat cost, minimum seats, annual commitment | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Bundling with licenses you already own | · | 📄 Documented | 📄 Documented | · | ❌ No |
| Add-on vs included; per-connector or per-index surcharges | · | · | · | 📄 Documented | · |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Training-on-customer-data policy, retention, abuse-monitoring opt-out | 📄 Documented | 📄 Documented | 📄 Documented | · | 📄 Documented |
| Certifications | · | · | · | · | · |
| Where the enterprise index physically lives | 📄 Documented<br>us-east-1, us-west-2, eu-west-1, +1 | 📄 Documented | 📄 Documented<br>global, us, eu, +6 | · | 📄 Documented |

---

## Bucket D — AI coding tools (*code*)

> Which AI coding tool fits my dev team?

Products compared: **AWS**: Kiro · **Azure**: GitHub Copilot · **GCP**: Google Antigravity · **BytePlus**: TRAE · **Alibaba**: Qoder CN series

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| IDE integration (VS Code, JetBrains, Vim/Neovim, other) | 📄 Documented<br>Kiro IDE, Kiro for VS Code, CLI, +3 | 📄 Documented<br>VS Code, Visual Studio, JetBrains, +3 | ✅ GA<br>VS Code, Visual Studio, JetBrains, +4 | 📄 Documented<br>TRAE IDE (TraeCode), TraeCode Plugin (VS Code, JetBrains) | 📄 Documented<br>Qoder CN IDE, JetBrains, CLI, +4 |
| CLI / terminal agent mode | 📄 Documented<br>Kiro CLI | 📄 Documented | 📄 Documented<br>Antigravity CLI (agy) | · | 📄 Documented<br>Qoder CN CLI |
| Agentic coding (multi-file edits, task execution, tool use) | ✅ GA | ✅ GA | ✅ GA | 📄 Documented | 📄 Documented |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Is the underlying model choosable, or fixed and opaque? | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Model choice in coding tool | 📄 Documented<br>Auto router, OpenAI GPT-5.6, Anthropic Claude, +2 | 📄 Documented<br>GPT-5.3-Codex, GPT-5.4 nano, GPT-5.6 Luna, +30 | 📄 Documented<br>Gemini 4 Neon, Gemini 4 Carbon, Gemini 4 Argon, +8 | 📄 Documented<br>Seed-2.1-Turbo, GPT-6.x / GPT-5.x series, GLM-5.2, +5 | 📄 Documented<br>GLM, DeepSeek, Kimi, +1 |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| MCP support in coding tool | 📄 Documented | ✅ GA | 📄 Documented | 📄 Documented | 📄 Documented |
| Codebase indexing / repo-wide context | 📄 Documented | 📄 Documented | 📄 Documented<br>Gemini Code Assist Enterprise — code customization (legacy) | 📄 Documented | 📄 Documented |
| AI code review (PR review, inline suggestions) | 📄 Documented | 📄 Documented | 📄 Documented<br>Gemini Code Assist on GitHub | 📄 Documented | 📄 Documented |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code snippet retention & training policy | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Per-seat pricing (individual / business / enterprise tiers) | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Free tier or usage-based option | 📄 Documented<br>50 credits/month | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

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
| Alibaba | A | 19 | 19 (100%) | 18 (95%) | 0 (0%) |
| Alibaba | B | 25 | 25 (100%) | 24 (96%) | 1 (4%) |
| Alibaba | C | 14 | 14 (100%) | 13 (93%) | 1 (7%) |
| Alibaba | D | 12 | 12 (100%) | 12 (100%) | 0 (0%) |
| AWS | A | 17 | 17 (100%) | 17 (100%) | 0 (0%) |
| AWS | B | 31 | 31 (100%) | 30 (97%) | 16 (52%) |
| AWS | C | 13 | 13 (100%) | 11 (85%) | 0 (0%) |
| AWS | D | 12 | 12 (100%) | 12 (100%) | 2 (17%) |
| Azure | A | 17 | 17 (100%) | 17 (100%) | 0 (0%) |
| Azure | B | 36 | 36 (100%) | 35 (97%) | 8 (22%) |
| Azure | C | 14 | 14 (100%) | 14 (100%) | 0 (0%) |
| Azure | D | 12 | 12 (100%) | 12 (100%) | 2 (17%) |
| BytePlus | B | 37 | 37 (100%) | 35 (95%) | 0 (0%) |
| BytePlus | C | 17 | 17 (100%) | 12 (71%) | 0 (0%) |
| BytePlus | D | 12 | 12 (100%) | 11 (92%) | 0 (0%) |
| GCP | A | 17 | 17 (100%) | 17 (100%) | 0 (0%) |
| GCP | B | 26 | 26 (100%) | 25 (96%) | 11 (42%) |
| GCP | C | 14 | 14 (100%) | 14 (100%) | 0 (0%) |
| GCP | D | 12 | 12 (100%) | 12 (100%) | 2 (17%) |

**Stage stated is near-zero everywhere** — vendors document capabilities without
saying whether they are GA. That is a finding about the industry's disclosure, and
it must be reported symmetrically: earlier revisions of this data inferred GA from
silence for AWS and Azure while recording `unknown` for Google on identical
evidence, which flattered two providers and penalised a third.

Gaps are deliberate and visible. A `·` is a research TODO, not a vendor verdict.

