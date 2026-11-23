# Changelog

> [!WARNING]
> **Generated file — do not edit.** Run `uv run scripts/changelog.py`.

`change` = the vendor shipped something. `research` = our coverage caught up.
Distinguishing these keeps the feed from crying wolf every time we fill a gap.

## 2026-11-23

415 update(s) — 104 vendor change(s), 311 research update(s).

| Provider | Bucket | Capability | Change | Tag |
|---|---|---|---|---|
| AWS | A | Agent-to-agent (A2A) protocol support | `status`: — → documented | `research` |
| AWS | A | Uploadable skill packs (reusable capability bundles) | `status`: — → documented; `product`: — → AgentSkills plugin | `research` |
| AWS | A | Built-in tool library shipped with the SDK | `product`: strands-agents-tools → Vended tools (strands.vended_tools) | `change` |
| AWS | A | Checkpointing and resume-after-failure | `status`: — → documented | `research` |
| AWS | A | Checkpointer interface + pluggable backends | `status`: — → documented; `value`: — → LocalFileStorage, S3Storage, InMemoryStorage, custom Storage; community Valkey; AgentCore Memory | `research` |
| AWS | A | Code interpreter / sandbox | `status`: — → documented; `value`: — → Docker, SSH, custom Sandbox | `research` |
| AWS | A | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → documented | `research` |
| AWS | A | Local dev loop (no cloud creds, hot reload, debug UI) | `product`: strandly → strands CLI | `change` |
| AWS | A | Long-running agents (max session duration, async/background) | `status`: — → documented; `product`: — → Strands harness (background tasks) | `research` |
| AWS | A | Model routing / fallback / cost-tiering | `status`: — → documented; `product`: — → ModelRouter; `value`: — → ordered fallback, classifier routing, custom strategy | `research` |
| AWS | A | Multi-agent patterns | `value`: — → agents-as-tools, graph, swarm, workflow, a2a | `change` |
| AWS | A | Multi-tenant serving with tenant/session isolation | `status`: — → documented; `value`: — → tenant-scoping primitives; serving isolation delegated to AgentCore Runtime | `research` |
| AWS | A | OpenAI-compatible endpoint | `status`: — → documented; `value`: — → client only (consumes OpenAI-compatible endpoints) | `research` |
| AWS | A | OpenAPI -> tool import | `status`: — → documented; `product`: — → AgentCore Gateway OpenAPI targets (consumed via Strands' MCP client) | `research` |
| AWS | A | Community signal (contributors, issue response, production adopters) | `value`: {"commits": 2338, "forks": 1000, "open_issues": 449, "open_prs": 194, "stars": 6800} → {"commits": 3414, "contributors": 378, "forks": 1600, "open_issues": 780, "open_prs": 565, "stars": 9300} | `change` |
| AWS | A | Can the SDK emit to any OTel backend, or vendor-locked? | `status`: — → documented; `value`: — → any OTLP backend | `research` |
| AWS | A | Does the SDK phone home telemetry by default, and can you disable it? | `status`: none → documented | `change` |
| AWS | A | Short-term session/thread memory | `status`: — → documented; `value`: — → bring-your-own storage (managed option via AgentCore Memory) | `research` |
| AWS | A | Function/tool calling; parallel tool calls | `status`: — → documented; `value`: — → parallel by default | `research` |
| AWS | A | Workflow engine (graph/DAG, durable, resumable) | `status`: — → documented; `value`: — → graph (DAG + cyclic), swarm, workflow-in-code | `research` |
| AWS | B | Agent-to-agent (A2A) protocol support | `status`: — → ga; `product`: — → AgentCore Runtime | `research` |
| AWS | B | Agent gateway / policy enforcement point for agent traffic | `status`: — → ga; `product`: — → AgentCore Gateway | `research` |
| AWS | B | Automated agent optimization | `status`: preview → ga | `change` |
| AWS | B | Agent payments / microtransactions | `status`: preview → ga | `change` |
| AWS | B | Uploadable skill packs (reusable capability bundles) | `status`: — → ga; `product`: — → AgentCore Harness (Skills) | `research` |
| AWS | B | Agent workload identity | `status`: documented → ga | `change` |
| AWS | B | First-party AI-service tools callable as tools | `status`: — → documented; `product`: — → AgentCore Gateway built-in connectors (+ Harness built-in tools) | `research` |
| AWS | B | Code-first vs low-code builder | `status`: — → documented; `product`: — → AgentCore Harness (configuration) and AgentCore Runtime (code) | `research` |
| AWS | B | Managed browser / computer use | `status`: documented → ga | `change` |
| AWS | B | BYO / open-weight hosting; provisioned throughput | `status`: — → ga; `product`: — → Amazon Bedrock Custom Model Import + Provisioned Throughput | `research` |
| AWS | B | Certifications | `value`: {"certified": ["HIPAA eligible", "FedRAMP (Class C)", "SOC 2", "ISO 27001:2022", "ISO 27017:2015", "ISO 27018:2019", "ISO 27701:2019", "ISO 22301:2019", "ISO 20000-1:2018", "ISO 9001:2015", "CSA STAR"], "self_assessed_pending_audit": ["BIO", "C5", "CISPE", "CPSTIC", "ENS High", "FINMA", "GNS", "GSMA", "HITRUST", "IRAP", "ISMAP", "MTCS", "OSPAR", "PCI", "Pinakes", "PiTuKri"]} → {"certified": ["HIPAA eligible", "FedRAMP (Class C and Class D)", "SOC 2", "ISO 27001:2022", "ISO 27017:2015", "ISO 27018:2019", "ISO 27701:2019", "ISO 22301:2019", "ISO 20000-1:2018", "ISO 9001:2015", "CSA STAR"], "self_assessed_pending_audit": ["BIO", "C5", "CISPE", "CPSTIC", "ENS High", "FINMA", "GNS", "GSMA", "HITRUST", "IRAP", "ISMAP", "MTCS", "OSPAR", "PCI", "Pinakes", "PiTuKri"]} | `change` |
| AWS | B | Checkpointing and resume-after-failure | `status`: — → documented; `product`: — → AgentCore Runtime session storage (preview) and capacity provider volumes | `research` |
| AWS | B | Code interpreter / sandbox | `status`: documented → ga | `change` |
| AWS | B | Token & cost attribution per agent / tenant / session | `status`: — → documented; `product`: — → Amazon Bedrock cost attribution (+ AgentCore resource tags) | `research` |
| AWS | B | Data residency, in-region processing, cross-region inference behavior | `status`: — → documented; `product`: — → AgentCore cross-region inference (Memory, Policy, Evaluations) + Bedrock CRIS | `research` |
| AWS | B | Can agents you build be published INTO the vendor's packaged product? | `status`: — → documented; `product`: — → AWS Agent Registry -> Amazon Quick | `research` |
| AWS | B | Managed end-user feedback collection | `status`: — → unknown | `research` |
| AWS | B | First-party frontier models | `status`: — → documented; `product`: — → Amazon Nova (on Amazon Bedrock); `value`: — → Nova 2 Lite, Nova 2 Sonic, Nova 2.5 Sonic, Nova Micro, Nova Lite, Nova Pro, Nova Multimodal Embeddings, Nova Reel | `research` |
| AWS | B | Free tier, commitment/savings plans, marketplace procurement | `status`: — → documented; `product`: — → AgentCore pricing (+ Bedrock Provisioned Throughput, AWS Marketplace) | `research` |
| AWS | B | Human-in-the-loop (interrupt/resume, approval gates) | `status`: — → documented; `product`: — → AgentCore Harness inline functions + Gateway MCP elicitation | `research` |
| AWS | B | Managed knowledge base / RAG | `status`: none → ga; `product`: — → Amazon Bedrock Managed Knowledge Base (AgentCore Gateway connector) | `change` |
| AWS | B | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → ga; `product`: — → Amazon Bedrock AgentCore | `research` |
| AWS | B | Long-term memory (semantic, episodic, preference) | `status`: documented → ga | `change` |
| AWS | B | Managed agent harness (pre-assembled, opt-in agent loop you configure) | `status`: — → ga; `product`: — → AgentCore Harness | `research` |
| AWS | B | Managed MCP registry / catalog | `status`: preview → ga; `product`: AgentCore Registry / AWS Agent Registry → AWS Agent Registry | `change` |
| AWS | B | Per-end-user namespacing; TTL, deletion, export | `status`: — → documented; `product`: — → AgentCore Memory | `research` |
| AWS | B | Model routing / fallback / cost-tiering | `status`: — → documented; `product`: — → Amazon Bedrock intelligent prompt routing + AgentCore Gateway model fallback | `research` |
| AWS | B | Multi-agent patterns | `status`: — → documented; `product`: — → AgentCore (Runtime code-defined agents; Harness subagent tool) | `research` |
| AWS | B | Multi-tenant serving with tenant/session isolation | `status`: — → documented; `product`: — → AgentCore Runtime (+ AgentCore Memory namespaces) | `research` |
| AWS | B | OpenAI-compatible endpoint | `status`: — → documented; `product`: — → Amazon Bedrock (bedrock-runtime and bedrock-mantle endpoints) | `research` |
| AWS | B | OpenAPI -> tool import | `status`: — → documented; `product`: — → AgentCore Gateway (OpenAPI targets) | `research` |
| AWS | B | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: documented → ga | `change` |
| AWS | B | Pricing axes | `value`: {"applies_to": ["Runtime", "Browser Tool", "Code Interpreter"], "per_gb_hour": 0.00945, "per_vcpu_hour": 0.0895} → {"applies_to": ["Runtime microVMs v1", "Browser Tool", "Code Interpreter"], "per_gb_hour": 0.00945, "per_vcpu_hour": 0.0895, "runtime_v2_per_gb_hour": 0.0169, "runtime_v2_per_vcpu_hour": 0.1276} | `change` |
| AWS | B | Region availability OF THE AGENT RUNTIME | `value`: {"evaluations": 16, "harness_memory_optimization": 15, "payments": 4, "policy": 19, "registry": 5, "runtime_gateway_identity_builtin_tools_observability": 20} → {"harness_memory": 16, "optimization": 21, "payments": 12, "policy_evaluations": 22, "region_table_columns": 24, "registry": 10, "runtime_instances": 15, "runtime_microvms_gateway_identity_builtin_tools_observability": 24, "web_answer": 1, "web_search_api": 6, "web_search_tool": 7} | `change` |
| AWS | B | Hard service limits (files, messages, tools, versions) | `status`: — → documented | `research` |
| AWS | B | Session lifecycle API (start, manage, event stream) | `status`: — → documented; `product`: — → AgentCore Runtime sessions (+ Amazon Bedrock Managed Agents, powered by OpenAI, preview) | `research` |
| AWS | B | Managed skills registry / catalog | `status`: — → ga; `product`: — → AWS Agent Registry | `research` |
| AWS | B | Gov / sovereign cloud availability | `status`: — → documented; `product`: — → AgentCore in AWS GovCloud (US-West) and AWS China Regions | `research` |
| AWS | B | Structured data / text-to-SQL over warehouses | `status`: — → documented; `product`: — → Amazon Bedrock Knowledge Bases (structured data stores) | `research` |
| AWS | B | Audit trail of every tool invocation | `status`: — → documented; `product`: — → AgentCore Gateway + AWS CloudTrail (+ AgentCore Observability) | `research` |
| AWS | B | Function/tool calling; parallel tool calls | `status`: — → documented; `product`: — → Amazon Bedrock (Responses, Chat Completions, Converse, InvokeModel) | `research` |
| AWS | B | Per-tool regional availability (does every tool work in every region?) | `status`: — → documented; `value`: — → {"builtin_tools_browser_code_interpreter": 24, "custom_model_import": 4, "gateway": 24, "web_answer": 1, "web_search_api": 6, "web_search_tool": 7} | `research` |
| AWS | B | Training-on-customer-data policy, retention, abuse-monitoring opt-out | `product`: — → Amazon Bedrock (model inference); AgentCore has no service-wide statement | `change` |
| AWS | B | Fine-tuning, distillation, prompt caching | `status`: — → ga; `product`: — → Amazon Bedrock model customization and prompt caching | `research` |
| AWS | B | Versioning, aliases, canary, rollback | `status`: — → documented; `product`: — → AgentCore Runtime and Harness versions/endpoints (+ Optimization A/B testing) | `research` |
| AWS | B | Managed real-time voice agents | `status`: — → documented; `product`: — → AgentCore Runtime bidirectional streaming (+ Amazon Nova 2 Sonic) | `research` |
| AWS | B | Built-in web search tool | `status`: — → ga; `product`: — → AgentCore Web Search (Web Search API and Web Search Tool connector) | `research` |
| AWS | B | Workflow engine (graph/DAG, durable, resumable) | `status`: — → documented; `product`: — → AWS Step Functions (AgentCore harness integration); Amazon Bedrock Flows | `research` |
| AWS | C | Add-on vs included; per-connector or per-index surcharges | `status`: — → documented | `research` |
| AWS | C | First-party AI-service tools callable as tools | `status`: — → documented; `product`: — → AWS Quick; `value`: — → Amazon Bedrock, Amazon Textract, Amazon Comprehend, Amazon Comprehend Medical | `research` |
| AWS | C | Code-first vs low-code builder | `status`: — → documented; `value`: — → low-code / no-code | `research` |
| AWS | C | Certifications | `status`: — → documented; `value`: — → HIPAA, SOC 1, SOC 2, SOC 3, PCI, ISO 42001 | `research` |
| AWS | C | Conversation history, personalization, retention controls | `status`: — → documented; `value`: — → 30-day retention; user delete; personalization on by default | `research` |
| AWS | C | Managed end-user feedback collection | `status`: — → documented | `research` |
| AWS | C | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → ga; `product`: — → Amazon Q Business | `research` |
| AWS | C | Bundling with licenses you already own | `status`: none → documented; `product`: — → AWS Quick | `change` |
| AWS | C | Is the underlying model choosable, or fixed and opaque? | `status`: none → documented; `product`: — → AWS Quick; `value`: — → mode tiers (Fast / Balanced / Smart) plus thinking effort; underlying model not named | `change` |
| AWS | C | Gov / sovereign cloud availability | `status`: — → documented; `product`: — → AWS Quick; `value`: — → AWS GovCloud (US-West) with agentic features; GovCloud (US-East) and China (Beijing) without | `research` |
| AWS | C | Audit trail of every tool invocation | `status`: — → documented | `research` |
| AWS | C | Built-in web search tool | `status`: — → documented; `product`: — → AWS Quick | `research` |
| AWS | D | Agentic coding (multi-file edits, task execution, tool use) | `status`: preview → ga | `change` |
| AWS | D | CLI / terminal agent mode | `product`: — → Kiro CLI | `change` |
| AWS | D | AI code review (PR review, inline suggestions) | `status`: unknown → documented | `research` |
| AWS | D | Free tier or usage-based option | `status`: preview → documented; `value`: — → 50 credits/month | `change` |
| AWS | D | Per-seat pricing (individual / business / enterprise tiers) | `status`: preview → documented; `value`: — → {"addon_credit": 0.04, "power": 200, "pro": 20, "pro_max": 100, "pro_plus": 40, "team_seat": 20} | `change` |
| AWS | D | IDE integration (VS Code, JetBrains, Vim/Neovim, other) | `value`: Kiro IDE, CLI, Web → Kiro IDE, Kiro for VS Code, CLI, Web, Mobile, Kiro Crew | `change` |
| AWS | D | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: preview → ga | `change` |
| AWS | D | Model choice in coding tool | `value`: Anthropic Claude, open-weight models → Auto router, OpenAI GPT-5.6, Anthropic Claude, xAI Grok, open-weight models | `change` |
| Alibaba | A | Agent-to-agent (A2A) protocol support | `status`: — → documented; `value`: — → client (A2AAgent) + server example | `research` |
| Alibaba | A | Uploadable skill packs (reusable capability bundles) | `status`: — → documented | `research` |
| Alibaba | A | Built-in tool library shipped with the SDK | `status`: — → documented; `value`: — → Bash, PowerShell, Read, Write, Edit, Glob, Grep, TaskCreate, TaskGet, TaskList, TaskUpdate, AskUser | `research` |
| Alibaba | A | Checkpointing and resume-after-failure | `status`: — → documented | `research` |
| Alibaba | A | Checkpointer interface + pluggable backends | `status`: — → documented; `value`: — → RedisStorage, AsyncSQLAlchemyStorage (SQLite, PostgreSQL, MySQL), custom StorageBase | `research` |
| Alibaba | A | Can the SDK talk to a rival cloud's models? | `value`: OpenAI, Anthropic, Gemini, DashScope, DeepSeek, Moonshot, xAI, Ollama → OpenAI, Anthropic, Gemini, DashScope, DeepSeek, Moonshot, Volcengine, xAI, Ollama, MiniMax | `change` |
| Alibaba | A | In-repo eval harness runnable in your own CI | `product`: — → OpenJudge (agentscope-ai/OpenJudge) | `change` |
| Alibaba | A | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → ga; `product`: — → AgentScope (Java SDK carries the stated GA); `value`: — → Python 2.0.x no GA statement (PyPI "4 - Beta"); agentscope-java "v2.0.0 GA" (2026-07) | `research` |
| Alibaba | A | Model routing / fallback / cost-tiering | `status`: — → documented; `value`: — → per-reply routing (ModelRouterMiddleware), fallback model (ModelConfig) | `research` |
| Alibaba | A | Multi-agent patterns | `value`: leader-worker, task planning → leader-worker, task planning, pipeline | `change` |
| Alibaba | A | OpenAI-compatible endpoint | `status`: — → documented; `value`: — → client only (consumes OpenAI-compatible endpoints) | `research` |
| Alibaba | A | OpenAPI -> tool import | `status`: — → documented; `product`: — → Alibaba Cloud AI 网关 HTTP-to-MCP (consumed via AgentScope's MCP client) | `research` |
| Alibaba | A | Community signal (contributors, issue response, production adopters) | `value`: {"stars": 28700} → {"stars": 36485} | `change` |
| Alibaba | A | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: none → documented | `change` |
| Alibaba | A | Can the SDK emit to any OTel backend, or vendor-locked? | `status`: — → documented; `value`: — → any OTLP backend | `research` |
| Alibaba | A | Languages supported | `value`: python → python, java, typescript | `change` |
| Alibaba | A | Does the SDK phone home telemetry by default, and can you disable it? | `status`: none → unknown | `research` |
| Alibaba | A | Short-term session/thread memory | `status`: — → documented; `value`: — → bring-your-own (AgentState serialised to Redis or SQL storage) | `research` |
| Alibaba | A | Function/tool calling; parallel tool calls | `status`: — → documented; `value`: — → JSON-Schema tools, sequential and concurrent tool calls | `research` |
| Alibaba | A | Workflow engine (graph/DAG, durable, resumable) | `status`: — → preview; `value`: — → GoalPipeline, TeamPipeline, SOP engine (ordered, verified, resumable steps) | `research` |
| Alibaba | B | Agent-to-agent (A2A) protocol support | `status`: — → documented; `product`: — → AI 网关 (+ Nacos AI Registry) | `research` |
| Alibaba | B | Agent gateway / policy enforcement point for agent traffic | `status`: — → documented; `product`: — → AI 网关 (Cloud-native API Gateway — AI Gateway) | `research` |
| Alibaba | B | Automated agent optimization | `status`: — → documented; `product`: — → 百炼 Evolution — 应用优化 + AgentLoop | `research` |
| Alibaba | B | Agent payments / microtransactions | `status`: — → unknown | `research` |
| Alibaba | B | Uploadable skill packs (reusable capability bundles) | `status`: — → documented; `product`: — → 百炼 Skill (Skill 管理) | `research` |
| Alibaba | B | First-party AI-service tools callable as tools | `status`: — → documented; `product`: — → Model Studio built-in tools + official MCP services + ParseX | `research` |
| Alibaba | B | Native APM tie-in | `status`: — → documented; `product`: — → AgentRun observability (ARMS / Prometheus) + AgentCore (CloudMonitor 2.0) + AgentLoop | `research` |
| Alibaba | B | Managed browser / computer use | `status`: none → documented; `product`: — → 百炼 Sandbox — Browser Use Sandbox | `change` |
| Alibaba | B | BYO / open-weight hosting; provisioned throughput | `status`: — → documented; `product`: — → Model Studio 模型导入 + 专属部署 / DTU; AgentRun FunModel | `research` |
| Alibaba | B | Checkpointing and resume-after-failure | `status`: — → documented; `product`: — → 百炼 Managed Agents (+ AgentCore Runtime) | `research` |
| Alibaba | B | Code interpreter / sandbox | `product`: — → 百炼 Sandbox — Code Interpreter Sandbox | `change` |
| Alibaba | B | Token & cost attribution per agent / tenant / session | `status`: — → documented; `product`: — → AgentRun + AI 网关 + AgentCore | `research` |
| Alibaba | B | Data residency, in-region processing, cross-region inference behavior | `status`: — → documented | `research` |
| Alibaba | B | Delegated end-user auth (OAuth token vault, 3LO, on-behalf-of) | `status`: — → documented; `product`: — → Agent Identity (智能体身份) | `research` |
| Alibaba | B | Can agents you build be published INTO the vendor's packaged product? | `status`: — → documented; `product`: — → Alibaba Cloud AgentCore — 账号集成 (DingTalk / WeChat / Feishu channels) | `research` |
| Alibaba | B | Evaluation service | `product`: — → 百炼 Evolution — 应用评测 | `change` |
| Alibaba | B | Managed end-user feedback collection | `status`: — → unknown | `research` |
| Alibaba | B | First-party frontier models | `value`: Qwen-Max, Qwen-Plus, Qwen-Flash → qwen4-max, qwen3.7-plus, qwen3.8-flash | `change` |
| Alibaba | B | Framework agnosticism | `status`: — → documented; `product`: — → AgentRun + Alibaba Cloud AgentCore (高代码 Agent) | `research` |
| Alibaba | B | Free tier, commitment/savings plans, marketplace procurement | `status`: — → documented | `research` |
| Alibaba | B | Human-in-the-loop (interrupt/resume, approval gates) | `status`: — → documented; `product`: — → 百炼 Managed Agents (tool approval) + Alibaba Cloud AgentCore | `research` |
| Alibaba | B | IaC coverage and CI/CD story | `status`: — → documented; `product`: — → Terraform alicloud provider (AgentLoop, AI Gateway, PAI, FC) + 百炼 Managed Agents CLI | `research` |
| Alibaba | B | Long-running agents (max session duration, async/background) | `status`: — → documented; `product`: — → 百炼 Managed Agents | `research` |
| Alibaba | B | Long-term memory (semantic, episodic, preference) | `status`: none → documented; `product`: — → 百炼 Memory (记忆库) + Managed Agents Memory Store | `change` |
| Alibaba | B | Managed agent harness (pre-assembled, opt-in agent loop you configure) | `status`: — → documented; `product`: — → Alibaba Cloud AgentCore — 托管 Harness (separate product from Model Studio) | `research` |
| Alibaba | B | Managed agent loop (define + invoke an agent in one API call) | `product`: 百炼 visual agent builder (Agent 1.0) → 百炼 Flow Agent — 智能体应用 (Agent 2.0) | `change` |
| Alibaba | B | Managed agent runtime | `product`: 百炼 / Bailian application platform (Agent 1.0) → 百炼 Managed Agents | `change` |
| Alibaba | B | Managed MCP registry / catalog | `status`: — → documented; `product`: — → 百炼 MCP 广场 (official + third-party MCP catalog) | `research` |
| Alibaba | B | Per-end-user namespacing; TTL, deletion, export | `status`: — → documented; `product`: — → 百炼 Memory (记忆库) | `research` |
| Alibaba | B | Model routing / fallback / cost-tiering | `status`: — → documented; `product`: — → Model Studio 智能路由 + AI 网关 + AgentRun 模型治理 | `research` |
| Alibaba | B | Multi-tenant serving with tenant/session isolation | `status`: — → documented; `product`: — → AgentRun (Sandbox / AgentRuntime) + Alibaba Cloud AgentCore | `research` |
| Alibaba | B | OpenAPI -> tool import | `status`: — → documented; `product`: — → AI 网关 (HTTP-to-MCP) + 百炼 custom MCP import | `research` |
| Alibaba | B | OpenTelemetry / GenAI semconv; span-level tool-call traces | `product`: — → 百炼 Evolution — 应用观测 | `change` |
| Alibaba | B | Private networking | `status`: — → documented; `product`: — → Model Studio PrivateLink + AgentRun / AgentCore | `research` |
| Alibaba | B | Support tier & SLA on the agent runtime specifically | `product`: — → Alibaba Cloud AgentCore (Agent 运行时) — separate product from Model Studio; `value`: 99.9% → — | `change` |
| Alibaba | B | Which primitives bill separately | `status`: — → documented; `product`: — → Alibaba Cloud AgentCore + 百炼 Agent services | `research` |
| Alibaba | B | Hard service limits (files, messages, tools, versions) | `status`: — → documented | `research` |
| Alibaba | B | Session lifecycle API (start, manage, event stream) | `status`: — → documented; `product`: — → 百炼 Managed Agents | `research` |
| Alibaba | B | Short-term session/thread memory | `status`: — → documented; `product`: — → 百炼 Flow Agent apps (session_id) + Managed Agents sessions | `research` |
| Alibaba | B | Managed skills registry / catalog | `status`: — → documented; `product`: — → Alibaba Cloud AgentCore — Skill 管理 + Skill 广场 (plus the Agent Catalog) | `research` |
| Alibaba | B | Gov / sovereign cloud availability | `status`: — → documented; `product`: — → Apsara Stack (飞天企业版) private / sovereign cloud — sibling product | `research` |
| Alibaba | B | Structured data / text-to-SQL over warehouses | `status`: — → documented; `product`: — → Quick BI (智能小Q) — sibling product; AgentCore 智能问数 scenario | `research` |
| Alibaba | B | Third-party model catalog | `value`: DeepSeek, Kimi, GLM → DeepSeek, GLM, Kimi, MiniMax | `change` |
| Alibaba | B | Audit trail of every tool invocation | `status`: — → documented; `product`: — → Alibaba Cloud AgentCore + Agent Identity / ActionTrail + AgentLoop | `research` |
| Alibaba | B | Function/tool calling; parallel tool calls | `status`: — → documented | `research` |
| Alibaba | B | Least-privilege scoping of tool access; per-tool policy | `status`: — → documented; `product`: — → AI 网关 (per-tool auth) + Agent Identity (RAM policies) | `research` |
| Alibaba | B | Per-tool regional availability (does every tool work in every region?) | `status`: — → documented | `research` |
| Alibaba | B | Fine-tuning, distillation, prompt caching | `status`: — → documented; `product`: — → Model Studio 模型调优 + 上下文缓存 | `research` |
| Alibaba | B | Versioning, aliases, canary, rollback | `status`: — → documented; `product`: — → AgentRun AgentRuntime + AI 网关 (canary) + AgentLoop assets | `research` |
| Alibaba | B | Managed real-time voice agents | `status`: — → documented; `product`: — → 通义多模态交互开发套件 (multimodal-dialog applications) | `research` |
| Alibaba | B | Built-in web search tool | `status`: — → documented; `product`: — → Model Studio 联网搜索 (web_search tool) | `research` |
| Alibaba | B | Workflow engine (graph/DAG, durable, resumable) | `product`: — → Flow Agent — 工作流应用 | `change` |
| Alibaba | C | Add-on vs included; per-connector or per-index surcharges | `status`: — → documented | `research` |
| Alibaba | C | First-party AI-service tools callable as tools | `status`: — → documented; `value`: — → Python code interpreter, calculator, image generation, Quark search, QR code, GitHub search, official MCP (text-to-image, text-to-video, speech synthesis), document/image/audio/video parsing nodes | `research` |
| Alibaba | C | Certifications | `status`: — → documented; `product`: — → Alibaba Cloud Model Studio; `value`: — → SOC 2 | `research` |
| Alibaba | C | Conversation history, personalization, retention controls | `status`: — → documented | `research` |
| Alibaba | C | Managed end-user feedback collection | `status`: — → documented; `product`: — → QwenWork | `research` |
| Alibaba | C | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → documented | `research` |
| Alibaba | C | Permission-aware retrieval (ACL trimming at query time) | `status`: none → unknown | `research` |
| Alibaba | C | Prebuilt SaaS/enterprise connectors | `status`: documented → preview; `product`: — → 百炼 Connector | `change` |
| Alibaba | C | Per-seat cost, minimum seats, annual commitment | `value`: {"max": "USD 200/seat/month", "pro": "USD 100/seat/month", "standard": "USD 30/seat/month"} → {"advanced": "USD 75/seat/month", "premium": "USD 180/seat/month", "standard": "USD 20/seat/month"} | `change` |
| Alibaba | C | Gov / sovereign cloud availability | `status`: — → unknown; `product`: — → Alibaba Cloud Model Studio Flow Agent | `research` |
| Alibaba | C | Audit trail of every tool invocation | `status`: — → documented; `product`: — → QwenWork (Enterprise Premium admin console) | `research` |
| Alibaba | C | Built-in web search tool | `status`: — → documented; `value`: — → Quark Search official plugin (quark_search); model built-in web search in workflows | `research` |
| Alibaba | D | CLI / terminal agent mode | `product`: — → Qoder CN CLI | `change` |
| Alibaba | D | Per-seat pricing (individual / business / enterprise tiers) | `value`: {"enterprise": "\u00a5149/seat/month", "free": "\u00a50", "pro": "\u00a559/month", "pro_plus": "\u00a5169/month", "teams": "\u00a599/seat/month", "vpc": "\u00a5199/seat/month"} → {"advanced": "\u00a5169/month", "enterprise_dedicated": "\u00a5199/seat/month", "enterprise_standard": "\u00a5149/seat/month", "flagship": "\u00a5559/month", "free": "\u00a50", "pro": "\u00a559/month", "teams": "\u00a599/seat/month"} | `change` |
| Alibaba | D | IDE integration (VS Code, JetBrains, Vim/Neovim, other) | `value`: Qoder CN IDE, JetBrains, VS Code, CLI, Mobile, QoderWork → Qoder CN IDE, JetBrains, CLI, Mobile, Agent SDK, Cloud Agents, QoderWake | `change` |
| Azure | A | Agent-to-agent (A2A) protocol support | `status`: — → documented; `value`: — → client (A2AAgent), server (A2A hosting for .NET, Python, Go) | `research` |
| Azure | A | Uploadable skill packs (reusable capability bundles) | `status`: — → documented; `value`: — → SKILL.md directories (file, code, class and MCP sources) | `research` |
| Azure | A | Built-in tool library shipped with the SDK | `status`: — → documented; `value`: — → code interpreter, file search, web search, hosted MCP, local MCP, Foundry Toolbox, shell, image generation, computer use, Bing grounding, SharePoint, Fabric, browser automation, A2A tool | `research` |
| Azure | A | Checkpointer interface + pluggable backends | `status`: — → documented; `value`: — → InMemory, File, Azure Cosmos DB (workflow checkpoints); Redis, Cosmos DB, Valkey (chat history) | `research` |
| Azure | A | Code interpreter / sandbox | `status`: — → documented; `value`: — → provider-hosted Code Interpreter (OpenAI Responses / Foundry), CodeAct backends (Hyperlight, Monty, Local .NET) | `research` |
| Azure | A | Can the SDK talk to a rival cloud's models? | `value`: Microsoft Foundry, Azure OpenAI, OpenAI, GitHub Copilot SDK → Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic, Amazon Bedrock, Google Gemini / Vertex AI, Ollama, Mistral | `change` |
| Azure | A | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → documented; `value`: — → 1.0 (.NET and Python) since 2026-04-03; Go in public preview | `research` |
| Azure | A | Long-running agents (max session duration, async/background) | `status`: — → documented; `value`: — → background responses (continuation tokens), background agents (experimental), Durable Extension | `research` |
| Azure | A | Model routing / fallback / cost-tiering | `status`: — → preview; `value`: — → .NET only, experimental (RoutePersistingRoutingChatClient) | `research` |
| Azure | A | Multi-agent patterns | `value`: sequential, concurrent, handoff, group collaboration → sequential, concurrent, handoff, group chat, magentic | `change` |
| Azure | A | Multi-tenant serving with tenant/session isolation | `status`: — → documented; `value`: — → app-enforced (guidance and hooks only, no built-in tenant model) | `research` |
| Azure | A | OpenAI-compatible endpoint | `status`: — → documented; `value`: — → consume any OpenAI-compatible endpoint, expose agents as Chat Completions / Responses | `research` |
| Azure | A | OpenAPI -> tool import | `status`: — → documented; `product`: — → Foundry OpenAPI tool (via Foundry Toolbox in Agent Framework) | `research` |
| Azure | A | Community signal (contributors, issue response, production adopters) | `value`: {"commits": 2719, "forks": 2100, "open_issues": 525, "stars": 12600} → {"nuget_total_downloads": 13800000} | `change` |
| Azure | A | Callback/hook points for custom policy | `status`: — → documented; `value`: — → agent run middleware, function-calling middleware, chat-client middleware, Agent Hooks (Python, experimental) | `research` |
| Azure | A | Can the SDK emit to any OTel backend, or vendor-locked? | `status`: — → documented; `value`: — → any OTel backend (OTLP, Azure Monitor, console, Aspire Dashboard) | `research` |
| Azure | A | Languages supported | `value`: python, csharp → python, csharp, go | `change` |
| Azure | A | Does the SDK phone home telemetry by default, and can you disable it? | `status`: none → documented | `change` |
| Azure | A | Short-term session/thread memory | `status`: — → documented; `value`: — → bring-your-own or service-managed (AgentSession) | `research` |
| Azure | A | Function/tool calling; parallel tool calls | `status`: — → documented; `value`: — → function tools; parallel (Python concurrent by default, .NET opt-in) | `research` |
| Azure | B | Agent-to-agent (A2A) protocol support | `status`: preview → ga | `change` |
| Azure | B | Agent gateway / policy enforcement point for agent traffic | `status`: — → documented; `product`: — → AI gateway in Azure API Management (plus the newer Azure AI Gateway) | `research` |
| Azure | B | Automated agent optimization | `status`: documented → preview | `change` |
| Azure | B | Agent payments / microtransactions | `status`: — → unknown | `research` |
| Azure | B | Uploadable skill packs (reusable capability bundles) | `status`: — → preview; `product`: — → Foundry Skills (versioned Skills API) | `research` |
| Azure | B | First-party AI-service tools callable as tools | `status`: — → documented; `product`: — → Foundry Tools (Azure Speech, Language, Translator) + Agent Service built-in tools | `research` |
| Azure | B | Managed browser / computer use | `status`: — → ga; `product`: — → Browser automation tool (Foundry Agent Service) | `research` |
| Azure | B | BYO / open-weight hosting; provisioned throughput | `status`: — → ga; `product`: — → Fireworks on Foundry, Foundry managed compute, provisioned throughput | `research` |
| Azure | B | Checkpointing and resume-after-failure | `status`: — → documented; `product`: — → Hosted agents (resilient execution + durable state store) | `research` |
| Azure | B | Token & cost attribution per agent / tenant / session | `status`: — → preview; `product`: — → Foundry cost management (Monitor > Cost, cost controls) | `research` |
| Azure | B | Managed end-user feedback collection | `status`: — → unknown | `research` |
| Azure | B | First-party frontier models | `status`: — → documented; `product`: — → Foundry Models sold by Azure (Azure OpenAI + Microsoft models); `value`: — → Azure OpenAI GPT series (OpenAI-built, hosted and sold by Azure), MAI-Thinking-1 (preview), MAI-Image (preview), MAI-Voice / MAI-Transcribe (via Azure Speech), Phi, Microsoft-Decision-1.1 | `research` |
| Azure | B | Framework agnosticism | `value`: Microsoft Agent Framework, LangGraph, OpenAI Agents SDK, Anthropic Agent SDK, GitHub Copilot SDK, custom code → Microsoft Agent Framework, LangGraph, LangChain / Deep Agents, OpenAI Agents SDK, Anthropic Agent SDK, Copilot SDK, custom code | `change` |
| Azure | B | Free tier, commitment/savings plans, marketplace procurement | `status`: — → documented; `product`: — → Microsoft Agent prepurchase plan, PTU reservations, Azure Marketplace | `research` |
| Azure | B | Human-in-the-loop (interrupt/resume, approval gates) | `status`: — → documented; `product`: — → MCP tool approvals (Foundry Agent Service) | `research` |
| Azure | B | Managed knowledge base / RAG | `value`: file search, SharePoint, WorkIQ, Fabric IQ → file search, Foundry IQ, SharePoint, WorkIQ, Fabric IQ | `change` |
| Azure | B | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → ga; `product`: — → Foundry Agent Service | `research` |
| Azure | B | Managed agent harness (pre-assembled, opt-in agent loop you configure) | `status`: — → preview; `product`: — → Microsoft Copilot harness | `research` |
| Azure | B | Per-end-user namespacing; TTL, deletion, export | `status`: — → preview; `product`: — → Memory (Foundry Agent Service) | `research` |
| Azure | B | Model routing / fallback / cost-tiering | `status`: — → ga; `product`: — → Model router (Foundry Models) | `research` |
| Azure | B | Multi-agent patterns | `status`: — → documented; `product`: — → A2A tool (Foundry Agent Service) + Foundry workflows (preview, retiring); `value`: — → agent-as-tool delegation over A2A, sequential, group chat, human in the loop | `research` |
| Azure | B | Multi-tenant serving with tenant/session isolation | `status`: — → documented; `product`: — → Hosted agents (per-session sandboxes + durable state store) | `research` |
| Azure | B | OpenAPI -> tool import | `status`: — → documented; `product`: — → OpenAPI tool (Foundry Agent Service) | `research` |
| Azure | B | Region availability OF THE AGENT RUNTIME | `value`: {"agent_regions": 30, "class_a_private_ip": 22} → {"agent_regions": 30, "private_vnet_regions": 30} | `change` |
| Azure | B | Support tier & SLA on the agent runtime specifically | `status`: none → unknown | `research` |
| Azure | B | Which primitives bill separately | `status`: — → documented; `product`: — → Foundry Agent Service pricing | `research` |
| Azure | B | Session lifecycle API (start, manage, event stream) | `status`: — → documented; `product`: — → Hosted agents (Foundry Agent Service) | `research` |
| Azure | B | Managed skills registry / catalog | `status`: — → preview; `product`: — → Foundry Skills (versioned Skills API) | `research` |
| Azure | B | Structured data / text-to-SQL over warehouses | `status`: — → ga; `product`: — → Microsoft Fabric data agent (reached via the Fabric IQ tool, preview) | `research` |
| Azure | B | Audit trail of every tool invocation | `status`: — → documented; `product`: — → Microsoft Entra Agent ID logs + Foundry tracing (Application Insights) | `research` |
| Azure | B | Function/tool calling; parallel tool calls | `status`: — → documented; `product`: — → Function calling (Foundry Agent Service; parallel calls via Foundry Models) | `research` |
| Azure | B | Least-privilege scoping of tool access; per-tool policy | `status`: — → documented; `product`: — → Agent identity (Microsoft Entra Agent ID) + MCP allowed_tools + Foundry tool governance policies | `research` |
| Azure | B | Fine-tuning, distillation, prompt caching | `status`: — → documented; `product`: — → Training in Microsoft Foundry (Managed Training, Programmed Training) + prompt caching | `research` |
| Azure | B | Managed real-time voice agents | `status`: — → ga; `product`: — → Voice-based prompt agents (via Voice Live) | `research` |
| Azure | B | Built-in web search tool | `status`: preview → documented | `change` |
| Azure | B | Workflow engine (graph/DAG, durable, resumable) | `status`: — → preview; `product`: — → Foundry workflows (preview; retiring 2026-12-01) -> Agent Framework workflows on hosted agents | `research` |
| Azure | C | Add-on vs included; per-connector or per-index surcharges | `status`: — → documented; `product`: — → Microsoft Copilot (Copilot Credits usage-based billing) | `research` |
| Azure | C | First-party AI-service tools callable as tools | `status`: — → documented; `value`: — → web search (Bing), image generation, speech translation (Teams Interpreter agent) | `research` |
| Azure | C | Certifications | `status`: — → documented; `value`: — → GDPR, ISO 27001, ISO 27018, ISO 42001, HIPAA (BAA, configured implementations) | `research` |
| Azure | C | Conversation history, personalization, retention controls | `status`: — → documented; `value`: — → activity history + memory (memory in preview); Purview retention for chats | `research` |
| Azure | C | Managed end-user feedback collection | `status`: — → documented; `value`: — → built-in thumbs up/down, admin-reviewable | `research` |
| Azure | C | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → ga; `value`: — → GA 2023-11-01 (as "Copilot for Microsoft 365"); newer features in Frontier / preview | `research` |
| Azure | C | Is the underlying model choosable, or fixed and opaque? | `status`: none → documented | `change` |
| Azure | C | Gov / sovereign cloud availability | `status`: — → documented; `product`: — → Microsoft Copilot for U.S. government (GCC, GCC High, DoD); `value`: — → GCC, GCC High, DoD, EU Data Boundary | `research` |
| Azure | C | Audit trail of every tool invocation | `status`: — → documented; `product`: — → Microsoft Purview Audit | `research` |
| Azure | C | Built-in web search tool | `status`: — → documented; `value`: — → Bing web grounding (admin- and user-toggleable) | `research` |
| Azure | D | Agentic coding (multi-file edits, task execution, tool use) | `status`: documented → ga | `change` |
| Azure | D | Per-seat pricing (individual / business / enterprise tiers) | `value`: {"business": "$19/seat/month", "enterprise": "$39/seat/month", "free": "$0", "max": "$100/month", "pro": "$10/month", "pro_plus": "$39/month"} → {"business": "$19/seat/month", "copilot_access": "$0/user/month with GitHub Enterprise Cloud, else $10/user/month", "enterprise": "$39/seat/month", "free": "$0", "max": "$100/month", "pro": "$10/month", "pro_plus": "$39/month", "student": "$0"} | `change` |
| Azure | D | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: documented → ga; `product`: — → GitHub Copilot | `change` |
| Azure | D | MCP support in coding tool | `status`: documented → ga | `change` |
| Azure | D | Model choice in coding tool | `value`: GPT-5.4, GPT-5.3-Codex, GPT-5.5, GPT-5.6, Claude Opus 4.8, Claude Opus 5, Claude Sonnet 5, Claude Fable 5, Gemini 3.5 Flash, Gemini 3.1 Pro, Kimi K2.7 Code, Kimi K3 → GPT-5.3-Codex, GPT-5.4 nano, GPT-5.6 Luna, GPT-5.6 Sol, GPT-6 Astra, GPT-6 Luna, GPT-6 Sol, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6.2 Astra, GPT-6.2 Sol, Claude Fable 5, Claude Fable 5.1, Claude Fable 5.2, Claude Haiku 4.5, Claude Haiku 5.5, Claude Opus 4.8, Claude Opus 5.5, Claude Sonnet 4.6, Claude Sonnet 5, Claude Sonnet 5.5, Gemini 3.8 Flash, Gemini 4 Argon, Gemini 4 Carbon, Gemini 4 Hydrogen, Gemini 4 Neon, MAI-Code-1.1-Flash, MAI Code 2, MAI Code 2 Flash, Kimi K3, Grok 4.5, Grok 4.6, Grok 4.7 | `change` |
| BytePlus | B | Agent-to-agent (A2A) protocol support | `status`: — → documented; `product`: — → BytePlus AgentKit A2A Center | `research` |
| BytePlus | B | Agent gateway / policy enforcement point for agent traffic | `status`: — → documented; `product`: — → BytePlus AgentKit Gateway | `research` |
| BytePlus | B | Automated agent optimization | `status`: — → documented; `product`: — → BytePlus AgentKit Studio (auto-evaluation, Harness Sidecar) | `research` |
| BytePlus | B | Agent payments / microtransactions | `status`: — → unknown | `research` |
| BytePlus | B | Agent workload identity | `status`: documented → preview; `product`: — → BytePlus AgentKit Identity (agent identity / WorkloadIdentity) | `change` |
| BytePlus | B | First-party AI-service tools callable as tools | `status`: — → documented; `product`: — → ModelArk Managed Agents built-in tools + BytePlus Info Quest MCP | `research` |
| BytePlus | B | Native APM tie-in | `status`: — → documented; `product`: — → BytePlus AgentKit Observability (APMPlus, TLS) | `research` |
| BytePlus | B | Code-first vs low-code builder | `status`: — → documented; `product`: — → BytePlus AgentKit Studio + AgentKit CLI; ModelArk Managed Agents; `value`: — → code-first (VeADK / AgentKit SDK / CLI), low-code (AgentKit Studio), config-first (ModelArk Managed Agents console and API) | `research` |
| BytePlus | B | Managed browser / computer use | `status`: none → documented; `product`: — → BytePlus AgentKit (AIO Sandbox template) | `change` |
| BytePlus | B | BYO / open-weight hosting; provisioned throughput | `status`: — → limited; `product`: — → BytePlus ModelArk Model Unit + custom model upload | `research` |
| BytePlus | B | Checkpointing and resume-after-failure | `status`: — → documented | `research` |
| BytePlus | B | Token & cost attribution per agent / tenant / session | `status`: — → documented; `product`: — → ModelArk Managed Agents | `research` |
| BytePlus | B | Data residency, in-region processing, cross-region inference behavior | `status`: — → documented | `research` |
| BytePlus | B | Can agents you build be published INTO the vendor's packaged product? | `status`: — → documented; `product`: — → BytePlus AgentKit -> ArkClaw Enterprise Application Center | `research` |
| BytePlus | B | Evaluation service | `status`: none → documented; `product`: — → BytePlus AgentKit Evaluation | `change` |
| BytePlus | B | Managed end-user feedback collection | `status`: — → unknown | `research` |
| BytePlus | B | First-party frontier models | `value`: Dola Seed 2.0, Seed 2.0 Pro, Seed 2.0 Lite, Seed 2.0 Mini, Dola Seed 2.1 Turbo → Dola Seed 2.1 Turbo, Seed 2.0 Pro, Seed 2.0 Lite, Seed 2.0 Mini, Seed 2.0 Code Preview | `change` |
| BytePlus | B | Framework agnosticism | `status`: — → documented; `product`: — → BytePlus AgentKit Runtime; `value`: — → VeADK, LangChain, LangGraph, Google ADK, Strands, Bedrock AgentCore (migration), Dify (Studio migration), other Python frameworks via AgentKit SDK decorators | `research` |
| BytePlus | B | Free tier, commitment/savings plans, marketplace procurement | `status`: — → documented; `product`: — → BytePlus AgentKit | `research` |
| BytePlus | B | Guardrails | `product`: — → ModelArk Content filter | `change` |
| BytePlus | B | Human-in-the-loop (interrupt/resume, approval gates) | `status`: — → documented | `research` |
| BytePlus | B | IaC coverage and CI/CD story | `status`: — → documented; `product`: — → BytePlus AgentKit CLI | `research` |
| BytePlus | B | Managed knowledge base / RAG | `product`: Knowledge base → BytePlus Knowledge base (Knowledge Engine) | `change` |
| BytePlus | B | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: documented → ga; `product`: — → BytePlus AgentKit | `change` |
| BytePlus | B | Long-term memory (semantic, episodic, preference) | `product`: Persistent memory → BytePlus AgentKit Memory | `change` |
| BytePlus | B | Managed agent harness (pre-assembled, opt-in agent loop you configure) | `status`: — → documented; `product`: — → ModelArk Managed Agents | `research` |
| BytePlus | B | Managed agent runtime | `status`: documented → ga; `product`: ModelArk Managed Agents → BytePlus AgentKit Runtime | `change` |
| BytePlus | B | Managed MCP registry / catalog | `status`: — → documented; `product`: — → BytePlus AgentKit Gateway (MCP toolsets) and A2A Center | `research` |
| BytePlus | B | Managed MCP server hosting | `product`: — → BytePlus AgentKit Gateway (MCP services) | `change` |
| BytePlus | B | Per-end-user namespacing; TTL, deletion, export | `status`: — → documented; `product`: — → Persistent memory | `research` |
| BytePlus | B | Model routing / fallback / cost-tiering | `status`: — → documented; `product`: — → BytePlus AgentKit Gateway (model service / model groups) | `research` |
| BytePlus | B | Multi-agent patterns | `value`: orchestrator / sub-agent delegation → orchestrator / sub-agent delegation (coordinator), persistent multi-level sub-agent threads (multiagent_20261001) | `change` |
| BytePlus | B | Multi-tenant serving with tenant/session isolation | `status`: — → documented | `research` |
| BytePlus | B | OpenAI-compatible endpoint | `status`: — → documented | `research` |
| BytePlus | B | OpenAPI -> tool import | `status`: — → documented; `product`: — → BytePlus AgentKit Gateway (HTTP to MCP) | `research` |
| BytePlus | B | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: none → documented; `product`: — → BytePlus AgentKit Observability (APMPlus) | `change` |
| BytePlus | B | Private networking | `product`: — → BytePlus AgentKit Runtime | `change` |
| BytePlus | B | Support tier & SLA on the agent runtime specifically | `status`: none → unknown | `research` |
| BytePlus | B | Which primitives bill separately | `status`: — → documented; `product`: — → ModelArk Managed Agents | `research` |
| BytePlus | B | Hard service limits (files, messages, tools, versions) | `status`: — → documented; `product`: — → BytePlus AgentKit | `research` |
| BytePlus | B | Short-term session/thread memory | `status`: — → documented; `product`: — → BytePlus AgentKit Sessions | `research` |
| BytePlus | B | Managed skills registry / catalog | `status`: — → documented; `product`: — → BytePlus AgentKit Skill (formerly Skills Center) | `research` |
| BytePlus | B | Gov / sovereign cloud availability | `status`: — → unknown | `research` |
| BytePlus | B | Structured data / text-to-SQL over warehouses | `status`: — → unknown | `research` |
| BytePlus | B | Third-party model catalog | `status`: — → documented; `value`: — → DeepSeek, Z.ai (GLM), Deemos (Hyper3D), Hitem3D | `research` |
| BytePlus | B | Audit trail of every tool invocation | `status`: — → documented; `product`: — → ModelArk Managed Agents | `research` |
| BytePlus | B | Per-tool regional availability (does every tool work in every region?) | `status`: — → documented; `value`: — → {"agentkit": 1, "batch_inference": 1, "chat_and_image_generation_api": 2, "managed_agents": 1, "online_inference": 2, "responses_and_messages_api": 1, "tuning_and_dataset": 1} | `research` |
| BytePlus | B | Fine-tuning, distillation, prompt caching | `status`: — → documented; `product`: — → BytePlus ModelArk model fine-tuning + context cache | `research` |
| BytePlus | B | Versioning, aliases, canary, rollback | `status`: — → documented; `product`: — → BytePlus AgentKit Runtime | `research` |
| BytePlus | B | Managed real-time voice agents | `status`: — → documented; `product`: — → BytePlus RTC Conversational AI | `research` |
| BytePlus | B | Built-in web search tool | `status`: — → documented | `research` |
| BytePlus | B | Workflow engine (graph/DAG, durable, resumable) | `status`: — → documented; `product`: — → BytePlus AgentKit Studio (VeADK workflow agents) | `research` |
| BytePlus | C | Add-on vs included; per-connector or per-index surcharges | `status`: — → documented | `research` |
| BytePlus | C | Admin & adoption analytics, answer-feedback loop | `status`: — → documented | `research` |
| BytePlus | C | First-party AI-service tools callable as tools | `status`: — → documented; `product`: — → BytePlus ArkClaw Enterprise; `value`: — → web search (Searchinfinity), image model (Seedream via Agent Plan), video model (Seedance via Agent Plan), file upload and analysis, semantic file search | `research` |
| BytePlus | C | Code-first vs low-code builder | `status`: — → documented | `research` |
| BytePlus | C | Certifications | `status`: — → documented; `product`: — → BytePlus cloud platform (platform-level certifications) | `research` |
| BytePlus | C | Conversation history, personalization, retention controls | `status`: — → documented | `research` |
| BytePlus | C | DLP, tenant isolation, admin controls | `status`: — → documented | `research` |
| BytePlus | C | Managed end-user feedback collection | `status`: — → documented; `product`: — → BytePlus ArkClaw Enterprise | `research` |
| BytePlus | C | Guardrails | `status`: — → documented | `research` |
| BytePlus | C | Enterprise index freshness (real-time vs batch crawl) | `status`: — → documented; `product`: — → VikingDB Knowledge Engine | `research` |
| BytePlus | C | Where the enterprise index physically lives | `status`: — → documented; `product`: — → VikingDB Knowledge Engine | `research` |
| BytePlus | C | Can the packaged product invoke agents you built yourself? | `status`: — → documented | `research` |
| BytePlus | C | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → documented; `product`: — → BytePlus ArkClaw Enterprise | `research` |
| BytePlus | C | Bundling with licenses you already own | `status`: — → documented; `product`: — → BytePlus ArkClaw | `research` |
| BytePlus | C | Is the underlying model choosable, or fixed and opaque? | `status`: — → documented | `research` |
| BytePlus | C | Packaged assistant — is it purchasable, and what does it cover? | `status`: — → documented; `product`: — → BytePlus ArkClaw Enterprise | `research` |
| BytePlus | C | Permission-aware retrieval (ACL trimming at query time) | `status`: — → unknown | `research` |
| BytePlus | C | Prebuilt SaaS/enterprise connectors | `status`: — → documented | `research` |
| BytePlus | C | Per-seat cost, minimum seats, annual commitment | `status`: — → documented | `research` |
| BytePlus | C | Gov / sovereign cloud availability | `status`: — → unknown; `product`: — → BytePlus ArkClaw Enterprise | `research` |
| BytePlus | C | Audit trail of every tool invocation | `status`: — → documented | `research` |
| BytePlus | C | Training-on-customer-data policy, retention, abuse-monitoring opt-out | `status`: — → documented; `product`: — → BytePlus ModelArk | `research` |
| BytePlus | C | Built-in web search tool | `status`: — → documented; `product`: — → BytePlus ArkClaw Enterprise | `research` |
| BytePlus | D | CLI / terminal agent mode | `status`: unknown → oss; `product`: — → Trae Agent (bytedance/trae-agent, open source) | `research` |
| BytePlus | D | Code snippet retention & training policy | `status`: unknown → documented | `research` |
| BytePlus | D | AI code review (PR review, inline suggestions) | `status`: unknown → documented | `research` |
| BytePlus | D | Per-seat pricing (individual / business / enterprise tiers) | `value`: {"free": "$0", "pro": "$10/month"} → {"free": "$0", "pro": "$20/month", "pro_plus": "$60/month", "ultra": "$200/month"} | `change` |
| BytePlus | D | IDE integration (VS Code, JetBrains, Vim/Neovim, other) | `value`: TraeCode IDE → TRAE IDE (TraeCode), TraeCode Plugin (VS Code, JetBrains) | `change` |
| BytePlus | D | MCP support in coding tool | `status`: unknown → documented | `research` |
| BytePlus | D | Model choice in coding tool | `value`: GPT-5.4, Seed-2.1-Turbo, MiniMax-M3, Kimi-K2.5, Gemini-3 series → Seed-2.1-Turbo, GPT-6.x / GPT-5.x series, GLM-5.2, DeepSeek-V4.x, Kimi-K3 / K2.7-Code / K2.5, Gemini-3.1-Pro-Preview, MiniMax-M3, Grok-4.x (U.S. only) | `change` |
| GCP | A | Agent-to-agent (A2A) protocol support | `status`: — → documented | `research` |
| GCP | A | Uploadable skill packs (reusable capability bundles) | `status`: — → documented | `research` |
| GCP | A | Built-in tool library shipped with the SDK | `status`: — → documented | `research` |
| GCP | A | Checkpointing and resume-after-failure | `status`: — → documented | `research` |
| GCP | A | Checkpointer interface + pluggable backends | `status`: — → documented | `research` |
| GCP | A | Code interpreter / sandbox | `status`: — → documented | `research` |
| GCP | A | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → ga | `research` |
| GCP | A | Long-running agents (max session duration, async/background) | `status`: — → documented | `research` |
| GCP | A | Model routing / fallback / cost-tiering | `status`: — → preview | `research` |
| GCP | A | Multi-tenant serving with tenant/session isolation | `status`: — → unknown | `research` |
| GCP | A | OpenAI-compatible endpoint | `status`: — → documented | `research` |
| GCP | A | Community signal (contributors, issue response, production adopters) | `value`: {"stars": 21000} → {"stars": 22300} | `change` |
| GCP | A | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: — → documented | `research` |
| GCP | A | Callback/hook points for custom policy | `status`: — → documented | `research` |
| GCP | A | Can the SDK emit to any OTel backend, or vendor-locked? | `status`: — → documented; `value`: — → any-otel-backend | `research` |
| GCP | A | Does the SDK phone home telemetry by default, and can you disable it? | `status`: none → documented | `change` |
| GCP | A | Short-term session/thread memory | `status`: — → documented | `research` |
| GCP | A | Function/tool calling; parallel tool calls | `status`: — → documented | `research` |
| GCP | B | Agent-to-agent (A2A) protocol support | `status`: — → preview; `product`: — → Agent Runtime + Agent Registry | `research` |
| GCP | B | Agent gateway / policy enforcement point for agent traffic | `status`: — → ga; `product`: — → Agent Gateway | `research` |
| GCP | B | Automated agent optimization | `status`: — → documented; `product`: — → ADK adk optimize (GEPA) + Prompt Optimizer | `research` |
| GCP | B | Agent payments / microtransactions | `status`: — → unknown; `product`: — → Agent Payments Protocol (AP2) — open protocol, no managed service | `research` |
| GCP | B | Uploadable skill packs (reusable capability bundles) | `status`: — → preview; `product`: — → Skill Registry (+ skills injected by the Managed Agents harness) | `research` |
| GCP | B | Agent workload identity | `status`: documented → ga; `product`: — → Agent Identity | `change` |
| GCP | B | First-party AI-service tools callable as tools | `status`: — → documented; `product`: — → Gemini built-in tools + Google Cloud remote MCP servers | `research` |
| GCP | B | Native APM tie-in | `status`: — → ga; `product`: — → Agent Observability (Cloud Monitoring, Cloud Trace, Cloud Logging) | `research` |
| GCP | B | Code-first vs low-code builder | `status`: — → documented; `product`: — → Agent Studio (low-code) + Agent Development Kit (code-first); `value`: — → code-first, low-code | `research` |
| GCP | B | Managed browser / computer use | `status`: documented → ga; `product`: Computer Use (Sandbox) → Agent Platform Computer Use (Sandbox) | `change` |
| GCP | B | BYO / open-weight hosting; provisioned throughput | `status`: — → documented; `product`: — → Model Garden self-deployed models + Provisioned Throughput | `research` |
| GCP | B | Checkpointing and resume-after-failure | `status`: — → documented; `product`: — → Sandbox snapshots + ADK Resume + Sessions | `research` |
| GCP | B | Token & cost attribution per agent / tenant / session | `status`: — → documented; `product`: — → Custom metadata labels + inference request metadata logs | `research` |
| GCP | B | Delegated end-user auth (OAuth token vault, 3LO, on-behalf-of) | `product`: — → Agent Identity auth manager | `change` |
| GCP | B | Can agents you build be published INTO the vendor's packaged product? | `status`: — → documented; `product`: — → Gemini Enterprise (register ADK agents from Agent Runtime) | `research` |
| GCP | B | Evaluation service | `status`: documented → ga; `product`: Evaluation Service → Agent Evaluation (Evaluation Service) | `change` |
| GCP | B | First-party frontier models | `status`: — → documented; `product`: — → Gemini models on Agent Platform; `value`: — → Gemini 4 Neon, Gemini 4 Hydrogen, Gemini 4 Carbon, Gemini 4 Argon, Gemini 3.8 Flash, Gemini 3.8 Live, Gemma, Veo, Lyria | `research` |
| GCP | B | Framework agnosticism | `value`: ADK, LangGraph, LangChain, LlamaIndex, AG2, A2A, custom → ADK, LangGraph, LangChain, LlamaIndex, AG2, CrewAI, A2A, custom | `change` |
| GCP | B | Free tier, commitment/savings plans, marketplace procurement | `status`: — → documented | `research` |
| GCP | B | Guardrails | `product`: Safety Filters + Model Armor + DLP → Safety Filters + Model Armor + Sensitive Data Protection | `change` |
| GCP | B | Human-in-the-loop (interrupt/resume, approval gates) | `status`: — → documented; `product`: — → ADK Tool Confirmation + Computer use safety confirmations | `research` |
| GCP | B | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → ga; `product`: — → Gemini Enterprise Agent Platform (Agent Runtime, formerly Vertex AI Agent Engine) | `research` |
| GCP | B | Long-term memory (semantic, episodic, preference) | `product`: Memory Bank → Agent Platform Memory Bank | `change` |
| GCP | B | Managed agent harness (pre-assembled, opt-in agent loop you configure) | `status`: — → preview; `product`: — → Managed Agents API (Antigravity harness) | `research` |
| GCP | B | Managed MCP registry / catalog | `status`: documented → ga; `product`: Skill Registry → Agent Registry | `change` |
| GCP | B | Per-end-user namespacing; TTL, deletion, export | `status`: — → documented; `product`: — → Agent Platform Memory Bank | `research` |
| GCP | B | Model routing / fallback / cost-tiering | `status`: — → documented; `product`: — → Consumption options (Provisioned Throughput spillover, Priority / Flex / Deferred tiers) | `research` |
| GCP | B | Multi-agent patterns | `status`: — → documented; `product`: — → Agent Development Kit (ADK) + A2A on Agent Runtime; `value`: — → sub-agent delegation, sequential, parallel, loop, graph workflows, A2A | `research` |
| GCP | B | Multi-tenant serving with tenant/session isolation | `status`: — → documented; `product`: — → Sessions + Memory Bank IAM Conditions | `research` |
| GCP | B | OpenAI-compatible endpoint | `status`: — → documented; `product`: — → OpenAI compatibility (Chat Completions / Responses) | `research` |
| GCP | B | OpenAPI -> tool import | `status`: — → documented; `product`: — → ADK OpenAPIToolset | `research` |
| GCP | B | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: documented → ga; `product`: — → Agent Observability | `change` |
| GCP | B | Region availability OF THE AGENT RUNTIME | `status`: limited → documented; `value`: {"in_country_allowlist": ["ca", "in", "asia-northeast1 (JP)", "sg", "europe-west2 (UK)"], "multi_regions": ["global", "us", "eu"]} → {"multi_regions": ["us", "eu"], "region_list": ["us-east1", "us-east4", "us-west1", "us-central1", "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-west6", "europe-west8", "europe-southwest1", "asia-east1", "asia-east2", "asia-northeast1", "asia-northeast3", "asia-south1", "asia-southeast1", "asia-southeast2", "australia-southeast2", "me-west1", "northamerica-northeast1", "northamerica-northeast2", "southamerica-east1"], "regions": 23} | `change` |
| GCP | B | Support tier & SLA on the agent runtime specifically | `status`: documented → unknown; `value`: 99.5% (online inference), 99.9% (Agent Search API) → — | `research` |
| GCP | B | Which primitives bill separately | `status`: — → documented | `research` |
| GCP | B | Hard service limits (files, messages, tools, versions) | `status`: — → documented; `product`: — → Agent Runtime | `research` |
| GCP | B | Session lifecycle API (start, manage, event stream) | `status`: — → ga; `product`: — → Agent Platform Sessions | `research` |
| GCP | B | Managed skills registry / catalog | `status`: — → documented; `product`: — → Agent Registry (standalone skills) + Skill Registry (preview) | `research` |
| GCP | B | Gov / sovereign cloud availability | `status`: — → documented; `product`: — → Google Distributed Cloud air-gapped (Gemini on GDC) + Assured Workloads | `research` |
| GCP | B | Structured data / text-to-SQL over warehouses | `status`: — → ga; `product`: — → Conversational Analytics API (BigQuery / Looker data agents) | `research` |
| GCP | B | Third-party model catalog | `status`: — → documented; `product`: — → Model Garden (partner and open models as MaaS); `value`: — → Anthropic Claude, OpenAI GPT, xAI Grok, Meta Muse, Mistral, AI21 Jamba, DeepSeek, Llama, GLM, gpt-oss, Gemma | `research` |
| GCP | B | Audit trail of every tool invocation | `status`: — → documented; `product`: — → Agent Gateway access logs + Cloud Audit Logs | `research` |
| GCP | B | Function/tool calling; parallel tool calls | `status`: — → documented; `product`: — → Gemini function calling (+ Managed Agents service-side tools) | `research` |
| GCP | B | Least-privilege scoping of tool access; per-tool policy | `status`: — → ga; `product`: — → Agent Gateway IAM Unified Access Policies (+ semantic governance) | `research` |
| GCP | B | Per-tool regional availability (does every tool work in every region?) | `status`: — → documented | `research` |
| GCP | B | Fine-tuning, distillation, prompt caching | `status`: — → ga; `product`: — → Gemini tuning (SFT, preference, RLFT) + context caching | `research` |
| GCP | B | Versioning, aliases, canary, rollback | `status`: — → preview; `product`: — → Agent Runtime revisions and traffic splitting | `research` |
| GCP | B | Managed real-time voice agents | `status`: — → documented; `product`: — → Gemini Live API (+ Agent Runtime bidirectional streaming) | `research` |
| GCP | B | Built-in web search tool | `status`: — → ga; `product`: — → Grounding with Google Search (+ Web Grounding for Enterprise) | `research` |
| GCP | B | Workflow engine (graph/DAG, durable, resumable) | `status`: — → documented; `product`: — → ADK workflows (graph-based, resumable) + Agent Studio flow builder | `research` |
| GCP | C | Add-on vs included; per-connector or per-index surcharges | `status`: — → documented | `research` |
| GCP | C | First-party AI-service tools callable as tools | `status`: — → documented | `research` |
| GCP | C | Certifications | `status`: — → documented; `value`: — → HIPAA, FedRAMP, ISO 27001, ISO 27017, ISO 27018, ISO 27701, SOC 1, SOC 2, SOC 3, PCI DSS, BSI C5:2020 | `research` |
| GCP | C | Conversation history, personalization, retention controls | `status`: — → documented | `research` |
| GCP | C | Managed end-user feedback collection | `status`: — → documented | `research` |
| GCP | C | Where the enterprise index physically lives | `value`: global, us, eu, ca, in, asia-northeast1, sg, europe-west2 → global, us, eu, br, ca, in, asia-northeast1, sg, europe-west2 | `change` |
| GCP | C | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: — → ga; `product`: — → Gemini Enterprise | `research` |
| GCP | C | Per-seat cost, minimum seats, annual commitment | `value`: {"business": "USD 21/seat/month", "plus": "USD 30+/seat/month (annual)", "standard": "USD 30/seat/month (annual)"} → {"business": "USD 21/seat/month", "plus": "USD 30+/seat/month", "standard": "USD 30/seat/month (starting)"} | `change` |
| GCP | C | Gov / sovereign cloud availability | `status`: — → documented; `product`: — → Assured Workloads | `research` |
| GCP | C | Audit trail of every tool invocation | `status`: — → documented | `research` |
| GCP | C | Built-in web search tool | `status`: — → documented | `research` |
| GCP | D | Agentic coding (multi-file edits, task execution, tool use) | `status`: documented → ga | `change` |
| GCP | D | CLI / terminal agent mode | `product`: — → Antigravity CLI (agy) | `change` |
| GCP | D | AI code review (PR review, inline suggestions) | `product`: — → Gemini Code Assist on GitHub | `change` |
| GCP | D | Codebase indexing / repo-wide context | `product`: — → Gemini Code Assist Enterprise — code customization (legacy) | `change` |
| GCP | D | Per-seat pricing (individual / business / enterprise tiers) | `value`: {"enterprise_annual": "$45/seat/month", "enterprise_monthly": "$54/seat/month", "free": "$0", "standard_annual": "$19/seat/month", "standard_monthly": "$22.80/seat/month"} → {"free": "$0/month", "gemini_enterprise_payg": "$0 seat fee, consumption-based", "gemini_enterprise_standard_plus": "from $30/seat/month", "google_ai_pro": "consumer subscription (price not on this page)", "google_ai_ultra": "consumer subscription (price not on this page)"} | `change` |
| GCP | D | IDE integration (VS Code, JetBrains, Vim/Neovim, other) | `status`: documented → ga; `value`: VS Code, JetBrains, Android Studio, Cloud Shell Editor, Cloud Workstations → VS Code, Visual Studio, JetBrains, Android Studio, Zed, Xcode, Eclipse | `change` |
| GCP | D | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: documented → ga; `product`: — → Google Antigravity | `change` |
| GCP | D | Model choice in coding tool | `value`: Gemini 2.5 Pro, Gemini 2.5 Flash → Gemini 4 Neon, Gemini 4 Carbon, Gemini 4 Argon, Gemini 4 Hydrogen, Orchestrator, Gemini 3.8 Flash, Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.1 Pro, Claude Sonnet 5.5, Claude Opus 5.5 | `change` |
