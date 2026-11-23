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

**Data as of 2026-11-23** · 623 verified cells across 19 provider-buckets

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
| Workflow engine (graph/DAG, durable, resumable) | 📄 Documented<br>graph (DAG + cyclic), swarm, workflow-in-code | 📄 Documented | 📄 Documented<br>Workflow Runtime | 🟡 Preview<br>GoalPipeline, TeamPipeline, SOP engine (ordered, verified, resumable steps) |
| Local dev loop (no cloud creds, hot reload, debug UI) | 📄 Documented<br>strands CLI | 📄 Documented | 📄 Documented | 📄 Documented |
| Long-running agents (max session duration, async/background) | 📄 Documented<br>Strands harness (background tasks) | 📄 Documented<br>background responses (continuation tokens), background agents (experimental), Durable Extension | 📄 Documented | 📄 Documented |
| Multi-tenant serving with tenant/session isolation | 📄 Documented<br>tenant-scoping primitives; serving isolation delegated to AgentCore Runtime | 📄 Documented<br>app-enforced (guidance and hooks only, no built-in tenant model) | · | 📄 Documented |
| Agent-to-agent (A2A) protocol support | 📄 Documented | 📄 Documented<br>client (A2AAgent), server (A2A hosting for .NET, Python, Go) | 📄 Documented | 📄 Documented<br>client (A2AAgent) + server example |

### Model access

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Model routing / fallback / cost-tiering | 📄 Documented<br>ModelRouter | 🟡 Preview<br>.NET only, experimental (RoutePersistingRoutingChatClient) | 🟡 Preview | 📄 Documented<br>per-reply routing (ModelRouterMiddleware), fallback model (ModelConfig) |
| Can the SDK talk to a rival cloud's models? | 📄 Documented | 📄 Documented<br>Microsoft Foundry, Azure OpenAI, OpenAI, +5 | 📄 Documented | 📄 Documented<br>OpenAI, Anthropic, Gemini, +7 |
| OpenAI-compatible endpoint | 📄 Documented<br>client only (consumes OpenAI-compatible endpoints) | 📄 Documented<br>consume any OpenAI-compatible endpoint, expose agents as Chat Completions / Responses | 📄 Documented | 📄 Documented<br>client only (consumes OpenAI-compatible endpoints) |

### Tools & context

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Function/tool calling; parallel tool calls | 📄 Documented<br>parallel by default | 📄 Documented<br>function tools; parallel (Python concurrent by default, .NET opt-in) | 📄 Documented | 📄 Documented<br>JSON-Schema tools, sequential and concurrent tool calls |
| MCP client support | 📄 Documented | 📄 Documented<br>MCPToolDefinition / hostedtool.MCPServer | 📄 Documented | 📄 Documented |
| Built-in tool library shipped with the SDK | 📄 Documented<br>Vended tools (strands.vended_tools) | 📄 Documented<br>code interpreter, file search, web search, +11 | 📄 Documented | 📄 Documented<br>Bash, PowerShell, Read, +9 |
| Uploadable skill packs (reusable capability bundles) | 📄 Documented<br>AgentSkills plugin | 📄 Documented<br>SKILL.md directories (file, code, class and MCP sources) | 📄 Documented | 📄 Documented |
| OpenAPI -> tool import | 📄 Documented<br>AgentCore Gateway OpenAPI targets (consumed via Strands' MCP client) | 📄 Documented<br>Foundry OpenAPI tool (via Foundry Toolbox in Agent Framework) | 📄 Documented | 📄 Documented<br>Alibaba Cloud AI 网关 HTTP-to-MCP (consumed via AgentScope's MCP client) |
| Code interpreter / sandbox | 📄 Documented<br>Docker, SSH, custom Sandbox | 📄 Documented<br>provider-hosted Code Interpreter (OpenAI Responses / Foundry), CodeAct backends (Hyperlight, Monty, Local .NET) | 📄 Documented | 📄 Documented<br>local, Docker, Apple Container, +5 |

### Memory & state

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Short-term session/thread memory | 📄 Documented<br>bring-your-own storage (managed option via AgentCore Memory) | 📄 Documented<br>bring-your-own or service-managed (AgentSession) | 📄 Documented | 📄 Documented<br>bring-your-own (AgentState serialised to Redis or SQL storage) |
| Checkpointer interface + pluggable backends | 📄 Documented<br>LocalFileStorage, S3Storage, InMemoryStorage, +1 | 📄 Documented<br>InMemory, File, Azure Cosmos DB (workflow checkpoints); Redis, +2 | 📄 Documented | 📄 Documented<br>RedisStorage, AsyncSQLAlchemyStorage (SQLite, PostgreSQL, MySQL), custom StorageBase |
| Checkpointing and resume-after-failure | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| Human-in-the-loop (interrupt/resume, approval gates) | 📄 Documented<br>HumanInTheLoop intervention + Interrupts | 📄 Documented | 📄 Documented | 📄 Documented |
| Callback/hook points for custom policy | 📄 Documented | 📄 Documented<br>agent run middleware, function-calling middleware, chat-client middleware, +1 | 📄 Documented | 📄 Documented |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | Alibaba |
|---|---|---|---|---|
| OpenTelemetry / GenAI semconv; span-level tool-call traces | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Can the SDK emit to any OTel backend, or vendor-locked? | 📄 Documented<br>any OTLP backend | 📄 Documented<br>any OTel backend (OTLP, Azure Monitor, console, Aspire Dashboard) | 📄 Documented<br>any-otel-backend | 📄 Documented<br>any OTLP backend |
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
| Launch-stage evidence trail (where the vendor does/doesn't state GA) | 📄 Documented | 📄 Documented<br>1.0 (.NET and Python) since 2026-04-03; Go in public preview | ✅ GA | ✅ GA<br>AgentScope (Java SDK carries the stated GA) |

---

## Bucket B — Managed agentic platform (*assemble*)

> Who runs it in prod?

Products compared: **AWS**: Amazon Bedrock AgentCore · **Azure**: Microsoft Foundry Agent Service · **GCP**: Gemini Enterprise Agent Platform · **BytePlus**: BytePlus ModelArk · **Alibaba**: Alibaba Cloud Model Studio

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code-first vs low-code builder | 📄 Documented<br>AgentCore Harness (configuration) and AgentCore Runtime (code) | 📄 Documented<br>both | 📄 Documented<br>Agent Studio (low-code) + Agent Development Kit (code-first) | 📄 Documented<br>BytePlus AgentKit Studio + AgentKit CLI; ModelArk Managed Agents | 📄 Documented<br>both |
| Multi-agent patterns | 📄 Documented<br>AgentCore (Runtime code-defined agents; Harness subagent tool) | 📄 Documented<br>A2A tool (Foundry Agent Service) + Foundry workflows (preview, retiring) | 📄 Documented<br>Agent Development Kit (ADK) + A2A on Agent Runtime | 📄 Documented<br>orchestrator / sub-agent delegation (coordinator), persistent multi-level sub-agent threads (multiagent_20261001) | 📄 Documented<br>Agent orchestration applications |
| Workflow engine (graph/DAG, durable, resumable) | 📄 Documented<br>AWS Step Functions (AgentCore harness integration); Amazon Bedrock Flows | 🟡 Preview<br>Foundry workflows (preview; retiring 2026-12-01) -> Agent Framework workflows on hosted agents | 📄 Documented<br>ADK workflows (graph-based, resumable) + Agent Studio flow builder | 📄 Documented<br>BytePlus AgentKit Studio (VeADK workflow agents) | 📄 Documented<br>Flow Agent — 工作流应用 |
| Managed agent runtime | ✅ GA<br>AgentCore Runtime | ✅ GA<br>Agent Runtime | ✅ GA<br>Agent Runtime | ✅ GA<br>BytePlus AgentKit Runtime | 📄 Documented<br>百炼 Managed Agents |
| Managed agent harness (pre-assembled, opt-in agent loop you configure) | ✅ GA<br>AgentCore Harness | 🟡 Preview<br>Microsoft Copilot harness | 🟡 Preview<br>Managed Agents API (Antigravity harness) | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>Alibaba Cloud AgentCore — 托管 Harness (separate product from Model Studio) |
| Managed real-time voice agents | 📄 Documented<br>AgentCore Runtime bidirectional streaming (+ Amazon Nova 2 Sonic) | ✅ GA<br>Voice-based prompt agents (via Voice Live) | 📄 Documented<br>Gemini Live API (+ Agent Runtime bidirectional streaming) | 📄 Documented<br>BytePlus RTC Conversational AI | 📄 Documented<br>通义多模态交互开发套件 (multimodal-dialog applications) |
| Managed agent loop (define + invoke an agent in one API call) | ✅ GA<br>AgentCore Harness | ✅ GA<br>Prompt agents (Foundry) | 🟡 Preview<br>Managed Agents API | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>百炼 Flow Agent — 智能体应用 (Agent 2.0) |
| Session lifecycle API (start, manage, event stream) | 📄 Documented<br>AgentCore Runtime sessions (+ Amazon Bedrock Managed Agents, powered by OpenAI, preview) | 📄 Documented<br>Hosted agents (Foundry Agent Service) | ✅ GA<br>Agent Platform Sessions | 📄 Documented | 📄 Documented<br>百炼 Managed Agents |
| Long-running agents (max session duration, async/background) | 📄 Documented | 📄 Documented<br>Background Responses + Hosted Agents | 📄 Documented | 📄 Documented | 📄 Documented<br>百炼 Managed Agents |
| Multi-tenant serving with tenant/session isolation | 📄 Documented<br>AgentCore Runtime (+ AgentCore Memory namespaces) | 📄 Documented<br>Hosted agents (per-session sandboxes + durable state store) | 📄 Documented<br>Sessions + Memory Bank IAM Conditions | 📄 Documented | 📄 Documented<br>AgentRun (Sandbox / AgentRuntime) + Alibaba Cloud AgentCore |
| Framework agnosticism | 📄 Documented<br>CrewAI, LangGraph, LlamaIndex, +4 | 📄 Documented<br>Microsoft Agent Framework, LangGraph, LangChain / Deep Agents, +4 | 📄 Documented<br>ADK, LangGraph, LangChain, +5 | 📄 Documented<br>BytePlus AgentKit Runtime | 📄 Documented<br>AgentRun + Alibaba Cloud AgentCore (高代码 Agent) |
| Agent-to-agent (A2A) protocol support | ✅ GA<br>AgentCore Runtime | ✅ GA | 🟡 Preview<br>Agent Runtime + Agent Registry | 📄 Documented<br>BytePlus AgentKit A2A Center | 📄 Documented<br>AI 网关 (+ Nacos AI Registry) |
| Can agents you build be published INTO the vendor's packaged product? | 📄 Documented<br>AWS Agent Registry -> Amazon Quick | 📄 Documented | 📄 Documented<br>Gemini Enterprise (register ADK agents from Agent Runtime) | 📄 Documented<br>BytePlus AgentKit -> ArkClaw Enterprise Application Center | 📄 Documented<br>Alibaba Cloud AgentCore — 账号集成 (DingTalk / WeChat / Feishu channels) |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| First-party frontier models | 📄 Documented<br>Amazon Nova (on Amazon Bedrock) | 📄 Documented<br>Foundry Models sold by Azure (Azure OpenAI + Microsoft models) | 📄 Documented<br>Gemini models on Agent Platform | 📄 Documented<br>Dola Seed 2.1 Turbo, Seed 2.0 Pro, Seed 2.0 Lite, +2 | 📄 Documented<br>qwen4-max, qwen3.7-plus, qwen3.8-flash |
| Third-party model catalog | 📄 Documented | 📄 Documented | 📄 Documented<br>Model Garden (partner and open models as MaaS) | 📄 Documented<br>DeepSeek, Z.ai (GLM), Deemos (Hyper3D), +1 | 📄 Documented<br>DeepSeek, GLM, Kimi, +1 |
| BYO / open-weight hosting; provisioned throughput | ✅ GA<br>Amazon Bedrock Custom Model Import + Provisioned Throughput | ✅ GA<br>Fireworks on Foundry, Foundry managed compute, provisioned throughput | 📄 Documented<br>Model Garden self-deployed models + Provisioned Throughput | 🟠 Limited<br>BytePlus ModelArk Model Unit + custom model upload | 📄 Documented<br>Model Studio 模型导入 + 专属部署 / DTU; AgentRun FunModel |
| Fine-tuning, distillation, prompt caching | ✅ GA<br>Amazon Bedrock model customization and prompt caching | 📄 Documented<br>Training in Microsoft Foundry (Managed Training, Programmed Training) + prompt caching | ✅ GA<br>Gemini tuning (SFT, preference, RLFT) + context caching | 📄 Documented<br>BytePlus ModelArk model fine-tuning + context cache | 📄 Documented<br>Model Studio 模型调优 + 上下文缓存 |
| Model routing / fallback / cost-tiering | 📄 Documented<br>Amazon Bedrock intelligent prompt routing + AgentCore Gateway model fallback | ✅ GA<br>Model router (Foundry Models) | 📄 Documented<br>Consumption options (Provisioned Throughput spillover, Priority / Flex / Deferred tiers) | 📄 Documented<br>BytePlus AgentKit Gateway (model service / model groups) | 📄 Documented<br>Model Studio 智能路由 + AI 网关 + AgentRun 模型治理 |
| OpenAI-compatible endpoint | 📄 Documented<br>Amazon Bedrock (bedrock-runtime and bedrock-mantle endpoints) | 📄 Documented<br>Responses API | 📄 Documented<br>OpenAI compatibility (Chat Completions / Responses) | 📄 Documented | 📄 Documented |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Function/tool calling; parallel tool calls | 📄 Documented<br>Amazon Bedrock (Responses, Chat Completions, Converse, InvokeModel) | 📄 Documented<br>Function calling (Foundry Agent Service; parallel calls via Foundry Models) | 📄 Documented<br>Gemini function calling (+ Managed Agents service-side tools) | 📄 Documented | 📄 Documented |
| Managed MCP server hosting | 📄 Documented<br>AgentCore Gateway | 📄 Documented | 📄 Documented<br>Agent Gateway | 📄 Documented<br>BytePlus AgentKit Gateway (MCP services) | 📄 Documented |
| Managed MCP registry / catalog | ✅ GA<br>AWS Agent Registry | 📄 Documented<br>Toolbox | ✅ GA<br>Agent Registry | 📄 Documented<br>BytePlus AgentKit Gateway (MCP toolsets) and A2A Center | 📄 Documented<br>百炼 MCP 广场 (official + third-party MCP catalog) |
| Managed skills registry / catalog | ✅ GA<br>AWS Agent Registry | 🟡 Preview<br>Foundry Skills (versioned Skills API) | 📄 Documented<br>Agent Registry (standalone skills) + Skill Registry (preview) | 📄 Documented<br>BytePlus AgentKit Skill (formerly Skills Center) | 📄 Documented<br>Alibaba Cloud AgentCore — Skill 管理 + Skill 广场 (plus the Agent Catalog) |
| Agent gateway / policy enforcement point for agent traffic | ✅ GA<br>AgentCore Gateway | 📄 Documented<br>AI gateway in Azure API Management (plus the newer Azure AI Gateway) | ✅ GA<br>Agent Gateway | 📄 Documented<br>BytePlus AgentKit Gateway | 📄 Documented<br>AI 网关 (Cloud-native API Gateway — AI Gateway) |
| Uploadable skill packs (reusable capability bundles) | ✅ GA<br>AgentCore Harness (Skills) | 🟡 Preview<br>Foundry Skills (versioned Skills API) | 🟡 Preview<br>Skill Registry (+ skills injected by the Managed Agents harness) | 📄 Documented | 📄 Documented<br>百炼 Skill (Skill 管理) |
| OpenAPI -> tool import | 📄 Documented<br>AgentCore Gateway (OpenAPI targets) | 📄 Documented<br>OpenAPI tool (Foundry Agent Service) | 📄 Documented<br>ADK OpenAPIToolset | 📄 Documented<br>BytePlus AgentKit Gateway (HTTP to MCP) | 📄 Documented<br>AI 网关 (HTTP-to-MCP) + 百炼 custom MCP import |
| Code interpreter / sandbox | ✅ GA<br>AgentCore Code Interpreter | 📄 Documented | 🟡 Preview<br>Code Execution (Sandbox) | 📄 Documented | 📄 Documented<br>百炼 Sandbox — Code Interpreter Sandbox |
| Managed browser / computer use | ✅ GA<br>AgentCore Browser | ✅ GA<br>Browser automation tool (Foundry Agent Service) | ✅ GA<br>Agent Platform Computer Use (Sandbox) | 📄 Documented<br>BytePlus AgentKit (AIO Sandbox template) | 📄 Documented<br>百炼 Sandbox — Browser Use Sandbox |
| Built-in web search tool | ✅ GA<br>AgentCore Web Search (Web Search API and Web Search Tool connector) | 📄 Documented | ✅ GA<br>Grounding with Google Search (+ Web Grounding for Enterprise) | 📄 Documented | 📄 Documented<br>Model Studio 联网搜索 (web_search tool) |
| Agent payments / microtransactions | ✅ GA<br>AgentCore Payments | · | ·<br>Agent Payments Protocol (AP2) — open protocol, no managed service | · | · |
| Managed knowledge base / RAG | ✅ GA<br>Amazon Bedrock Managed Knowledge Base (AgentCore Gateway connector) | 📄 Documented<br>file search, Foundry IQ, SharePoint, +2 | 📄 Documented<br>RAG Engine | 📄 Documented<br>BytePlus Knowledge base (Knowledge Engine) | 📄 Documented |
| Structured data / text-to-SQL over warehouses | 📄 Documented<br>Amazon Bedrock Knowledge Bases (structured data stores) | ✅ GA<br>Microsoft Fabric data agent (reached via the Fabric IQ tool, preview) | ✅ GA<br>Conversational Analytics API (BigQuery / Looker data agents) | · | 📄 Documented<br>Quick BI (智能小Q) — sibling product; AgentCore 智能问数 scenario |
| First-party AI-service tools callable as tools | 📄 Documented<br>AgentCore Gateway built-in connectors (+ Harness built-in tools) | 📄 Documented<br>Foundry Tools (Azure Speech, Language, Translator) + Agent Service built-in tools | 📄 Documented<br>Gemini built-in tools + Google Cloud remote MCP servers | 📄 Documented<br>ModelArk Managed Agents built-in tools + BytePlus Info Quest MCP | 📄 Documented<br>Model Studio built-in tools + official MCP services + ParseX |

### Memory & state

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Short-term session/thread memory | 📄 Documented<br>AgentCore Memory | 📄 Documented | ✅ GA<br>Sessions | 📄 Documented<br>BytePlus AgentKit Sessions | 📄 Documented<br>百炼 Flow Agent apps (session_id) + Managed Agents sessions |
| Long-term memory (semantic, episodic, preference) | ✅ GA<br>AgentCore Memory | 🟡 Preview | ✅ GA<br>Agent Platform Memory Bank | 📄 Documented<br>BytePlus AgentKit Memory | 📄 Documented<br>百炼 Memory (记忆库) + Managed Agents Memory Store |
| Per-end-user namespacing; TTL, deletion, export | 📄 Documented<br>AgentCore Memory | 🟡 Preview<br>Memory (Foundry Agent Service) | 📄 Documented<br>Agent Platform Memory Bank | 📄 Documented<br>Persistent memory | 📄 Documented<br>百炼 Memory (记忆库) |
| Checkpointing and resume-after-failure | 📄 Documented<br>AgentCore Runtime session storage (preview) and capacity provider volumes | 📄 Documented<br>Hosted agents (resilient execution + durable state store) | 📄 Documented<br>Sandbox snapshots + ADK Resume + Sessions | 📄 Documented | 📄 Documented<br>百炼 Managed Agents (+ AgentCore Runtime) |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Agent workload identity | ✅ GA<br>AgentCore Identity | 📄 Documented | ✅ GA<br>Agent Identity | 🟡 Preview<br>BytePlus AgentKit Identity (agent identity / WorkloadIdentity) | 📄 Documented |
| Delegated end-user auth (OAuth token vault, 3LO, on-behalf-of) | 📄 Documented<br>AgentCore Identity | 📄 Documented | 📄 Documented<br>Agent Identity auth manager | 📄 Documented | 📄 Documented<br>Agent Identity (智能体身份) |
| Least-privilege scoping of tool access; per-tool policy | ✅ GA<br>Policy in AgentCore | 📄 Documented<br>Agent identity (Microsoft Entra Agent ID) + MCP allowed_tools + Foundry tool governance policies | ✅ GA<br>Agent Gateway IAM Unified Access Policies (+ semantic governance) | 📄 Documented | 📄 Documented<br>AI 网关 (per-tool auth) + Agent Identity (RAM policies) |
| Guardrails | 📄 Documented | 📄 Documented | 📄 Documented<br>Safety Filters + Model Armor + Sensitive Data Protection | 📄 Documented<br>ModelArk Content filter | 📄 Documented<br>AI Guardrails + AI Gateway |
| Human-in-the-loop (interrupt/resume, approval gates) | 📄 Documented<br>AgentCore Harness inline functions + Gateway MCP elicitation | 📄 Documented<br>MCP tool approvals (Foundry Agent Service) | 📄 Documented<br>ADK Tool Confirmation + Computer use safety confirmations | 📄 Documented | 📄 Documented<br>百炼 Managed Agents (tool approval) + Alibaba Cloud AgentCore |
| Audit trail of every tool invocation | 📄 Documented<br>AgentCore Gateway + AWS CloudTrail (+ AgentCore Observability) | 📄 Documented<br>Microsoft Entra Agent ID logs + Foundry tracing (Application Insights) | 📄 Documented<br>Agent Gateway access logs + Cloud Audit Logs | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>Alibaba Cloud AgentCore + Agent Identity / ActionTrail + AgentLoop |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| OpenTelemetry / GenAI semconv; span-level tool-call traces | ✅ GA<br>AgentCore Observability | ✅ GA | ✅ GA<br>Agent Observability | 📄 Documented<br>BytePlus AgentKit Observability (APMPlus) | 📄 Documented<br>百炼 Evolution — 应用观测 |
| Token & cost attribution per agent / tenant / session | 📄 Documented<br>Amazon Bedrock cost attribution (+ AgentCore resource tags) | 🟡 Preview<br>Foundry cost management (Monitor > Cost, cost controls) | 📄 Documented<br>Custom metadata labels + inference request metadata logs | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>AgentRun + AI 网关 + AgentCore |
| Native APM tie-in | 📄 Documented<br>Amazon CloudWatch | 📄 Documented<br>Application Insights | ✅ GA<br>Agent Observability (Cloud Monitoring, Cloud Trace, Cloud Logging) | 📄 Documented<br>BytePlus AgentKit Observability (APMPlus, TLS) | 📄 Documented<br>AgentRun observability (ARMS / Prometheus) + AgentCore (CloudMonitor 2.0) + AgentLoop |
| Evaluation service | ✅ GA<br>AgentCore Evaluations | 📄 Documented | ✅ GA<br>Agent Evaluation (Evaluation Service) | 📄 Documented<br>BytePlus AgentKit Evaluation | 📄 Documented<br>百炼 Evolution — 应用评测 |
| Versioning, aliases, canary, rollback | 📄 Documented<br>AgentCore Runtime and Harness versions/endpoints (+ Optimization A/B testing) | 📄 Documented | 🟡 Preview<br>Agent Runtime revisions and traffic splitting | 📄 Documented<br>BytePlus AgentKit Runtime | 📄 Documented<br>AgentRun AgentRuntime + AI 网关 (canary) + AgentLoop assets |
| IaC coverage and CI/CD story | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented<br>BytePlus AgentKit CLI | 📄 Documented<br>Terraform alicloud provider (AgentLoop, AI Gateway, PAI, FC) + 百炼 Managed Agents CLI |
| Private networking | ✅ GA | 📄 Documented | 📄 Documented | 📄 Documented<br>BytePlus AgentKit Runtime | 📄 Documented<br>Model Studio PrivateLink + AgentRun / AgentCore |
| Automated agent optimization | ✅ GA<br>AgentCore Optimization | 🟡 Preview<br>agent optimizer | 📄 Documented<br>ADK adk optimize (GEPA) + Prompt Optimizer | 📄 Documented<br>BytePlus AgentKit Studio (auto-evaluation, Harness Sidecar) | 📄 Documented<br>百炼 Evolution — 应用优化 + AgentLoop |
| Managed end-user feedback collection | · | · | 📄 Documented<br>Feedback service | · | · |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Pricing axes | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Which primitives bill separately | 📄 Documented | 📄 Documented<br>Foundry Agent Service pricing | 📄 Documented | 📄 Documented<br>ModelArk Managed Agents | 📄 Documented<br>Alibaba Cloud AgentCore + 百炼 Agent services |
| Free tier, commitment/savings plans, marketplace procurement | 📄 Documented<br>AgentCore pricing (+ Bedrock Provisioned Throughput, AWS Marketplace) | 📄 Documented<br>Microsoft Agent prepurchase plan, PTU reservations, Azure Marketplace | 📄 Documented | 📄 Documented<br>BytePlus AgentKit | 📄 Documented |
| Support tier & SLA on the agent runtime specifically | 📄 Documented<br>99.9% | · | · | · | 📄 Documented<br>Alibaba Cloud AgentCore (Agent 运行时) — separate product from Model Studio |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Region availability OF THE AGENT RUNTIME | 📄 Documented | ✅ GA | 📄 Documented | 📄 Documented<br>Johor (ap-southeast-1), Dublin (eu-west-1) | 📄 Documented<br>Singapore, US (Virginia), China (Beijing), +3 |
| Per-tool regional availability (does every tool work in every region?) | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Hard service limits (files, messages, tools, versions) | 📄 Documented | 📄 Documented | 📄 Documented<br>Agent Runtime | 📄 Documented<br>BytePlus AgentKit | 📄 Documented |
| Launch-stage evidence trail (where the vendor does/doesn't state GA) | ✅ GA<br>Amazon Bedrock AgentCore | ✅ GA<br>Foundry Agent Service | ✅ GA<br>Gemini Enterprise Agent Platform (Agent Runtime, formerly Vertex AI Agent Engine) | ✅ GA<br>BytePlus AgentKit | 🟡 Preview |
| Data residency, in-region processing, cross-region inference behavior | 📄 Documented<br>AgentCore cross-region inference (Memory, Policy, Evaluations) + Bedrock CRIS | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Training-on-customer-data policy, retention, abuse-monitoring opt-out | 📄 Documented<br>Amazon Bedrock (model inference); AgentCore has no service-wide statement | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Certifications | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented<br>ISO 9001, ISO 20000, ISO 22301, +10 | 📄 Documented<br>SOC 2 |
| Gov / sovereign cloud availability | 📄 Documented<br>AgentCore in AWS GovCloud (US-West) and AWS China Regions | 📄 Documented<br>US Gov Virginia, US Gov Arizona | 📄 Documented<br>Google Distributed Cloud air-gapped (Gemini on GDC) + Assured Workloads | · | 📄 Documented<br>Apsara Stack (飞天企业版) private / sovereign cloud — sibling product |

---

## Bucket C — Out-of-box AI capability (*buy*)

> Can I buy instead of build?

Products compared: **AWS**: Amazon Q Business · **Azure**: Microsoft Copilot · **GCP**: Gemini Enterprise · **BytePlus**: BytePlus ArkClaw Enterprise · **Alibaba**: Alibaba Cloud Model Studio Flow Agent

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Code-first vs low-code builder | 📄 Documented<br>low-code / no-code | 📄 Documented<br>both | 📄 Documented<br>both | 📄 Documented | 📄 Documented<br>both |
| Packaged assistant — is it purchasable, and what does it cover? | ❌ No<br>Amazon Q Business | 📄 Documented | 📄 Documented | 📄 Documented<br>BytePlus ArkClaw Enterprise | 📄 Documented |
| Can the packaged product invoke agents you built yourself? | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Model access

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Is the underlying model choosable, or fixed and opaque? | 📄 Documented<br>AWS Quick | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Tools & context

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Built-in web search tool | 📄 Documented<br>AWS Quick | 📄 Documented<br>Bing web grounding (admin- and user-toggleable) | 📄 Documented | 📄 Documented<br>BytePlus ArkClaw Enterprise | 📄 Documented<br>Quark Search official plugin (quark_search); model built-in web search in workflows |
| First-party AI-service tools callable as tools | 📄 Documented<br>AWS Quick | 📄 Documented<br>web search (Bing), image generation, speech translation (Teams Interpreter agent) | 📄 Documented | 📄 Documented<br>BytePlus ArkClaw Enterprise | 📄 Documented<br>Python code interpreter, calculator, image generation, +5 |
| Prebuilt SaaS/enterprise connectors | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 🟡 Preview<br>百炼 Connector |
| Enterprise index freshness (real-time vs batch crawl) | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented<br>VikingDB Knowledge Engine | 📄 Documented |

### Memory & state

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Conversation history, personalization, retention controls | 📄 Documented<br>30-day retention; user delete; personalization on by default | 📄 Documented<br>activity history + memory (memory in preview); Purview retention for chats | 📄 Documented | 📄 Documented | 📄 Documented |

### Trust — identity, guardrails, human-in-the-loop

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Guardrails | 📄 Documented | 📄 Documented | 📄 Documented<br>Model Armor | 📄 Documented | 📄 Documented<br>AI Guardrails |
| Audit trail of every tool invocation | 📄 Documented | 📄 Documented<br>Microsoft Purview Audit | 📄 Documented | 📄 Documented | 📄 Documented<br>QwenWork (Enterprise Premium admin console) |
| Permission-aware retrieval (ACL trimming at query time) | 📄 Documented | 📄 Documented | 📄 Documented | · | · |
| DLP, tenant isolation, admin controls | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Operate — observability, eval, deployment

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Managed end-user feedback collection | 📄 Documented | 📄 Documented<br>built-in thumbs up/down, admin-reviewable | 📄 Documented | 📄 Documented<br>BytePlus ArkClaw Enterprise | 📄 Documented<br>QwenWork |
| Admin & adoption analytics, answer-feedback loop | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |

### Commercial (OSS health for bucket A)

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Per-seat cost, minimum seats, annual commitment | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented |
| Bundling with licenses you already own | 📄 Documented<br>AWS Quick | 📄 Documented | 📄 Documented | 📄 Documented<br>BytePlus ArkClaw | ❌ No |
| Add-on vs included; per-connector or per-index surcharges | 📄 Documented | 📄 Documented<br>Microsoft Copilot (Copilot Credits usage-based billing) | 📄 Documented | 📄 Documented | 📄 Documented |

### Sovereignty & reach

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| Launch-stage evidence trail (where the vendor does/doesn't state GA) | ✅ GA<br>Amazon Q Business | ✅ GA<br>GA 2023-11-01 (as "Copilot for Microsoft 365"); newer features in Frontier / preview | ✅ GA<br>Gemini Enterprise | 📄 Documented<br>BytePlus ArkClaw Enterprise | 📄 Documented |
| Training-on-customer-data policy, retention, abuse-monitoring opt-out | 📄 Documented | 📄 Documented | 📄 Documented | 📄 Documented<br>BytePlus ModelArk | 📄 Documented |
| Certifications | 📄 Documented<br>HIPAA, SOC 1, SOC 2, +3 | 📄 Documented<br>GDPR, ISO 27001, ISO 27018, +2 | 📄 Documented<br>HIPAA, FedRAMP, ISO 27001, +8 | 📄 Documented<br>BytePlus cloud platform (platform-level certifications) | 📄 Documented<br>Alibaba Cloud Model Studio |
| Gov / sovereign cloud availability | 📄 Documented<br>AWS Quick | 📄 Documented<br>Microsoft Copilot for U.S. government (GCC, GCC High, DoD) | 📄 Documented<br>Assured Workloads | ·<br>BytePlus ArkClaw Enterprise | ·<br>Alibaba Cloud Model Studio Flow Agent |
| Where the enterprise index physically lives | 📄 Documented<br>us-east-1, us-west-2, eu-west-1, +1 | 📄 Documented | 📄 Documented<br>global, us, eu, +6 | 📄 Documented<br>VikingDB Knowledge Engine | 📄 Documented |

---

## Bucket D — AI coding tools (*code*)

> Which AI coding tool fits my dev team?

Products compared: **AWS**: Kiro · **Azure**: GitHub Copilot · **GCP**: Google Antigravity · **BytePlus**: TRAE · **Alibaba**: Qoder CN series

### Build & orchestrate

| Capability | AWS | Azure | GCP | BytePlus | Alibaba |
|---|---|---|---|---|---|
| IDE integration (VS Code, JetBrains, Vim/Neovim, other) | 📄 Documented<br>Kiro IDE, Kiro for VS Code, CLI, +3 | 📄 Documented<br>VS Code, Visual Studio, JetBrains, +3 | ✅ GA<br>VS Code, Visual Studio, JetBrains, +4 | 📄 Documented<br>TRAE IDE (TraeCode), TraeCode Plugin (VS Code, JetBrains) | 📄 Documented<br>Qoder CN IDE, JetBrains, CLI, +4 |
| CLI / terminal agent mode | 📄 Documented<br>Kiro CLI | 📄 Documented | 📄 Documented<br>Antigravity CLI (agy) | ⚪ OSS<br>Trae Agent (bytedance/trae-agent, open source) | 📄 Documented<br>Qoder CN CLI |
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
| Launch-stage evidence trail (where the vendor does/doesn't state GA) | ✅ GA | ✅ GA<br>GitHub Copilot | ✅ GA<br>Google Antigravity | 📄 Documented | 📄 Documented |

---

## Research coverage

Three different things, deliberately kept apart — collapsing them into one number
is what produced this project's first fairness bug:

- **Sourced** — we read the authoritative page and cited it.
- **Verified** — the cell carries a fact (any status except `unknown`).
- **Stage stated** — the *vendor* stated a launch stage (`ga`/`preview`/`limited`).

| Provider | Bucket | Cells | Sourced | Verified | Stage stated |
|---|---|---|---|---|---|
| Alibaba | A | 32 | 32 (100%) | 31 (97%) | 2 (6%) |
| Alibaba | B | 64 | 64 (100%) | 62 (97%) | 1 (2%) |
| Alibaba | C | 23 | 23 (100%) | 21 (91%) | 1 (4%) |
| Alibaba | D | 12 | 12 (100%) | 12 (100%) | 0 (0%) |
| AWS | A | 32 | 32 (100%) | 32 (100%) | 0 (0%) |
| AWS | B | 64 | 63 (98%) | 63 (98%) | 23 (36%) |
| AWS | C | 23 | 23 (100%) | 23 (100%) | 1 (4%) |
| AWS | D | 12 | 12 (100%) | 12 (100%) | 2 (17%) |
| Azure | A | 32 | 32 (100%) | 32 (100%) | 1 (3%) |
| Azure | B | 64 | 64 (100%) | 61 (95%) | 19 (30%) |
| Azure | C | 23 | 23 (100%) | 23 (100%) | 1 (4%) |
| Azure | D | 12 | 12 (100%) | 12 (100%) | 3 (25%) |
| BytePlus | B | 64 | 64 (100%) | 59 (92%) | 4 (6%) |
| BytePlus | C | 23 | 23 (100%) | 21 (91%) | 0 (0%) |
| BytePlus | D | 12 | 12 (100%) | 12 (100%) | 0 (0%) |
| GCP | A | 32 | 32 (100%) | 31 (97%) | 2 (6%) |
| GCP | B | 64 | 64 (100%) | 62 (97%) | 22 (34%) |
| GCP | C | 23 | 23 (100%) | 23 (100%) | 1 (4%) |
| GCP | D | 12 | 12 (100%) | 12 (100%) | 3 (25%) |

**Stage stated is near-zero everywhere** — vendors document capabilities without
saying whether they are GA. That is a finding about the industry's disclosure, and
it must be reported symmetrically: earlier revisions of this data inferred GA from
silence for AWS and Azure while recording `unknown` for Google on identical
evidence, which flattered two providers and penalised a third.

Gaps are deliberate and visible. A `·` is a research TODO, not a vendor verdict.

