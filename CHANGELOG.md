# Changelog

> [!WARNING]
> **Generated file — do not edit.** Run `uv run scripts/changelog.py`.

`change` = the vendor shipped something. `research` = our coverage caught up.
Distinguishing these keeps the feed from crying wolf every time we fill a gap.

## 2026-11-23

139 update(s) — 90 vendor change(s), 49 research update(s).

| Provider | Bucket | Capability | Change | Tag |
|---|---|---|---|---|
| AWS | A | Built-in tool library shipped with the SDK | `product`: strands-agents-tools → Vended tools (strands.vended_tools) | `change` |
| AWS | A | Local dev loop (no cloud creds, hot reload, debug UI) | `product`: strandly → strands CLI | `change` |
| AWS | A | Multi-agent patterns | `value`: — → agents-as-tools, graph, swarm, workflow, a2a | `change` |
| AWS | A | Community signal (contributors, issue response, production adopters) | `value`: {"commits": 2338, "forks": 1000, "open_issues": 449, "open_prs": 194, "stars": 6800} → {"commits": 3414, "contributors": 378, "forks": 1600, "open_issues": 780, "open_prs": 565, "stars": 9300} | `change` |
| AWS | A | Does the SDK phone home telemetry by default, and can you disable it? | `status`: none → documented | `change` |
| AWS | B | Agent-to-agent (A2A) protocol support | `status`: — → ga; `product`: — → AgentCore Runtime | `research` |
| AWS | B | Automated agent optimization | `status`: preview → ga | `change` |
| AWS | B | Agent payments / microtransactions | `status`: preview → ga | `change` |
| AWS | B | Agent workload identity | `status`: documented → ga | `change` |
| AWS | B | Managed browser / computer use | `status`: documented → ga | `change` |
| AWS | B | Certifications | `value`: {"certified": ["HIPAA eligible", "FedRAMP (Class C)", "SOC 2", "ISO 27001:2022", "ISO 27017:2015", "ISO 27018:2019", "ISO 27701:2019", "ISO 22301:2019", "ISO 20000-1:2018", "ISO 9001:2015", "CSA STAR"], "self_assessed_pending_audit": ["BIO", "C5", "CISPE", "CPSTIC", "ENS High", "FINMA", "GNS", "GSMA", "HITRUST", "IRAP", "ISMAP", "MTCS", "OSPAR", "PCI", "Pinakes", "PiTuKri"]} → {"certified": ["HIPAA eligible", "FedRAMP (Class C and Class D)", "SOC 2", "ISO 27001:2022", "ISO 27017:2015", "ISO 27018:2019", "ISO 27701:2019", "ISO 22301:2019", "ISO 20000-1:2018", "ISO 9001:2015", "CSA STAR"], "self_assessed_pending_audit": ["BIO", "C5", "CISPE", "CPSTIC", "ENS High", "FINMA", "GNS", "GSMA", "HITRUST", "IRAP", "ISMAP", "MTCS", "OSPAR", "PCI", "Pinakes", "PiTuKri"]} | `change` |
| AWS | B | Code interpreter / sandbox | `status`: documented → ga | `change` |
| AWS | B | Managed knowledge base / RAG | `status`: none → ga; `product`: — → Amazon Bedrock Managed Knowledge Base (AgentCore Gateway connector) | `change` |
| AWS | B | Long-term memory (semantic, episodic, preference) | `status`: documented → ga | `change` |
| AWS | B | Managed MCP registry / catalog | `status`: preview → ga; `product`: AgentCore Registry / AWS Agent Registry → AWS Agent Registry | `change` |
| AWS | B | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: documented → ga | `change` |
| AWS | B | Pricing axes | `value`: {"applies_to": ["Runtime", "Browser Tool", "Code Interpreter"], "per_gb_hour": 0.00945, "per_vcpu_hour": 0.0895} → {"applies_to": ["Runtime microVMs v1", "Browser Tool", "Code Interpreter"], "per_gb_hour": 0.00945, "per_vcpu_hour": 0.0895, "runtime_v2_per_gb_hour": 0.0169, "runtime_v2_per_vcpu_hour": 0.1276} | `change` |
| AWS | B | Region availability OF THE AGENT RUNTIME | `value`: {"evaluations": 16, "harness_memory_optimization": 15, "payments": 4, "policy": 19, "registry": 5, "runtime_gateway_identity_builtin_tools_observability": 20} → {"harness_memory": 16, "optimization": 21, "payments": 12, "policy_evaluations": 22, "region_table_columns": 24, "registry": 10, "runtime_instances": 15, "runtime_microvms_gateway_identity_builtin_tools_observability": 24, "web_answer": 1, "web_search_api": 6, "web_search_tool": 7} | `change` |
| AWS | B | Training-on-customer-data policy, retention, abuse-monitoring opt-out | `status`: documented → unknown | `research` |
| AWS | B | Built-in web search tool | `status`: — → ga; `product`: — → AgentCore Web Search (Web Search API and Web Search Tool connector) | `research` |
| AWS | C | Bundling with licenses you already own | `status`: none → unknown | `research` |
| AWS | C | Is the underlying model choosable, or fixed and opaque? | `status`: none → unknown | `research` |
| AWS | D | Agentic coding (multi-file edits, task execution, tool use) | `status`: preview → ga | `change` |
| AWS | D | CLI / terminal agent mode | `product`: — → Kiro CLI | `change` |
| AWS | D | AI code review (PR review, inline suggestions) | `status`: unknown → documented | `research` |
| AWS | D | Free tier or usage-based option | `status`: preview → documented; `value`: — → 50 credits/month | `change` |
| AWS | D | Per-seat pricing (individual / business / enterprise tiers) | `status`: preview → documented; `value`: — → {"addon_credit": 0.04, "power": 200, "pro": 20, "pro_max": 100, "pro_plus": 40, "team_seat": 20} | `change` |
| AWS | D | IDE integration (VS Code, JetBrains, Vim/Neovim, other) | `value`: Kiro IDE, CLI, Web → Kiro IDE, Kiro for VS Code, CLI, Web, Mobile, Kiro Crew | `change` |
| AWS | D | Launch-stage evidence trail (where the vendor does/doesn't state GA) | `status`: preview → ga | `change` |
| AWS | D | Model choice in coding tool | `value`: Anthropic Claude, open-weight models → Auto router, OpenAI GPT-5.6, Anthropic Claude, xAI Grok, open-weight models | `change` |
| Alibaba | A | Can the SDK talk to a rival cloud's models? | `value`: OpenAI, Anthropic, Gemini, DashScope, DeepSeek, Moonshot, xAI, Ollama → OpenAI, Anthropic, Gemini, DashScope, DeepSeek, Moonshot, Volcengine, xAI, Ollama, MiniMax | `change` |
| Alibaba | A | In-repo eval harness runnable in your own CI | `product`: — → OpenJudge (agentscope-ai/OpenJudge) | `change` |
| Alibaba | A | Multi-agent patterns | `value`: leader-worker, task planning → leader-worker, task planning, pipeline | `change` |
| Alibaba | A | Community signal (contributors, issue response, production adopters) | `value`: {"stars": 28700} → {"stars": 36485} | `change` |
| Alibaba | A | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: none → documented | `change` |
| Alibaba | A | Languages supported | `value`: python → python, java, typescript | `change` |
| Alibaba | A | Does the SDK phone home telemetry by default, and can you disable it? | `status`: none → unknown | `research` |
| Alibaba | B | Managed browser / computer use | `status`: none → documented; `product`: — → 百炼 Sandbox — Browser Use Sandbox | `change` |
| Alibaba | B | Code interpreter / sandbox | `product`: — → 百炼 Sandbox — Code Interpreter Sandbox | `change` |
| Alibaba | B | Evaluation service | `product`: — → 百炼 Evolution — 应用评测 | `change` |
| Alibaba | B | First-party frontier models | `value`: Qwen-Max, Qwen-Plus, Qwen-Flash → qwen4-max, qwen3.7-plus, qwen3.8-flash | `change` |
| Alibaba | B | Long-running agents (max session duration, async/background) | `status`: — → documented; `product`: — → 百炼 Managed Agents | `research` |
| Alibaba | B | Long-term memory (semantic, episodic, preference) | `status`: none → documented; `product`: — → 百炼 Memory (记忆库) + Managed Agents Memory Store | `change` |
| Alibaba | B | Managed agent loop (define + invoke an agent in one API call) | `product`: 百炼 visual agent builder (Agent 1.0) → 百炼 Flow Agent — 智能体应用 (Agent 2.0) | `change` |
| Alibaba | B | Managed agent runtime | `product`: 百炼 / Bailian application platform (Agent 1.0) → 百炼 Managed Agents | `change` |
| Alibaba | B | OpenTelemetry / GenAI semconv; span-level tool-call traces | `product`: — → 百炼 Evolution — 应用观测 | `change` |
| Alibaba | B | Support tier & SLA on the agent runtime specifically | `status`: documented → unknown; `value`: 99.9% → — | `research` |
| Alibaba | B | Session lifecycle API (start, manage, event stream) | `status`: — → documented; `product`: — → 百炼 Managed Agents | `research` |
| Alibaba | B | Third-party model catalog | `value`: DeepSeek, Kimi, GLM → DeepSeek, GLM, Kimi, MiniMax | `change` |
| Alibaba | B | Workflow engine (graph/DAG, durable, resumable) | `product`: — → Flow Agent — 工作流应用 | `change` |
| Alibaba | C | Permission-aware retrieval (ACL trimming at query time) | `status`: none → unknown | `research` |
| Alibaba | C | Prebuilt SaaS/enterprise connectors | `status`: documented → preview; `product`: — → 百炼 Connector | `change` |
| Alibaba | C | Per-seat cost, minimum seats, annual commitment | `value`: {"max": "USD 200/seat/month", "pro": "USD 100/seat/month", "standard": "USD 30/seat/month"} → {"advanced": "USD 75/seat/month", "premium": "USD 180/seat/month", "standard": "USD 20/seat/month"} | `change` |
| Alibaba | D | CLI / terminal agent mode | `product`: — → Qoder CN CLI | `change` |
| Alibaba | D | Per-seat pricing (individual / business / enterprise tiers) | `value`: {"enterprise": "\u00a5149/seat/month", "free": "\u00a50", "pro": "\u00a559/month", "pro_plus": "\u00a5169/month", "teams": "\u00a599/seat/month", "vpc": "\u00a5199/seat/month"} → {"advanced": "\u00a5169/month", "enterprise_dedicated": "\u00a5199/seat/month", "enterprise_standard": "\u00a5149/seat/month", "flagship": "\u00a5559/month", "free": "\u00a50", "pro": "\u00a559/month", "teams": "\u00a599/seat/month"} | `change` |
| Alibaba | D | IDE integration (VS Code, JetBrains, Vim/Neovim, other) | `value`: Qoder CN IDE, JetBrains, VS Code, CLI, Mobile, QoderWork → Qoder CN IDE, JetBrains, CLI, Mobile, Agent SDK, Cloud Agents, QoderWake | `change` |
| Azure | A | Can the SDK talk to a rival cloud's models? | `value`: Microsoft Foundry, Azure OpenAI, OpenAI, GitHub Copilot SDK → Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic, Amazon Bedrock, Google Gemini / Vertex AI, Ollama, Mistral | `change` |
| Azure | A | Multi-agent patterns | `value`: sequential, concurrent, handoff, group collaboration → sequential, concurrent, handoff, group chat, magentic | `change` |
| Azure | A | Languages supported | `value`: python, csharp → python, csharp, go | `change` |
| Azure | A | Does the SDK phone home telemetry by default, and can you disable it? | `status`: none → documented | `change` |
| Azure | B | Agent-to-agent (A2A) protocol support | `status`: preview → ga | `change` |
| Azure | B | Automated agent optimization | `status`: documented → preview | `change` |
| Azure | B | Managed browser / computer use | `status`: — → ga; `product`: — → Browser automation tool (Foundry Agent Service) | `research` |
| Azure | B | Framework agnosticism | `value`: Microsoft Agent Framework, LangGraph, OpenAI Agents SDK, Anthropic Agent SDK, GitHub Copilot SDK, custom code → Microsoft Agent Framework, LangGraph, LangChain / Deep Agents, OpenAI Agents SDK, Anthropic Agent SDK, Copilot SDK, custom code | `change` |
| Azure | B | Managed knowledge base / RAG | `value`: file search, SharePoint, WorkIQ, Fabric IQ → file search, Foundry IQ, SharePoint, WorkIQ, Fabric IQ | `change` |
| Azure | B | Region availability OF THE AGENT RUNTIME | `value`: {"agent_regions": 30, "class_a_private_ip": 22} → {"agent_regions": 30, "private_vnet_regions": 30} | `change` |
| Azure | B | Support tier & SLA on the agent runtime specifically | `status`: none → unknown | `research` |
| Azure | B | Built-in web search tool | `status`: preview → documented | `change` |
| Azure | C | Is the underlying model choosable, or fixed and opaque? | `status`: none → documented | `change` |
| Azure | D | Agentic coding (multi-file edits, task execution, tool use) | `status`: documented → ga | `change` |
| Azure | D | Per-seat pricing (individual / business / enterprise tiers) | `value`: {"business": "$19/seat/month", "enterprise": "$39/seat/month", "free": "$0", "max": "$100/month", "pro": "$10/month", "pro_plus": "$39/month"} → {"business": "$19/seat/month", "copilot_access": "$0/user/month with GitHub Enterprise Cloud, else $10/user/month", "enterprise": "$39/seat/month", "free": "$0", "max": "$100/month", "pro": "$10/month", "pro_plus": "$39/month", "student": "$0"} | `change` |
| Azure | D | MCP support in coding tool | `status`: documented → ga | `change` |
| Azure | D | Model choice in coding tool | `value`: GPT-5.4, GPT-5.3-Codex, GPT-5.5, GPT-5.6, Claude Opus 4.8, Claude Opus 5, Claude Sonnet 5, Claude Fable 5, Gemini 3.5 Flash, Gemini 3.1 Pro, Kimi K2.7 Code, Kimi K3 → GPT-5.3-Codex, GPT-5.4 nano, GPT-5.6 Luna, GPT-5.6 Sol, GPT-6 Astra, GPT-6 Luna, GPT-6 Sol, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6.2 Astra, GPT-6.2 Sol, Claude Fable 5, Claude Fable 5.1, Claude Fable 5.2, Claude Haiku 4.5, Claude Haiku 5.5, Claude Opus 4.8, Claude Opus 5.5, Claude Sonnet 4.6, Claude Sonnet 5, Claude Sonnet 5.5, Gemini 3.8 Flash, Gemini 4 Argon, Gemini 4 Carbon, Gemini 4 Hydrogen, Gemini 4 Neon, MAI-Code-1.1-Flash, MAI Code 2, MAI Code 2 Flash, Kimi K3, Grok 4.5, Grok 4.6, Grok 4.7 | `change` |
| BytePlus | B | Managed browser / computer use | `status`: none → documented | `change` |
| BytePlus | B | Checkpointing and resume-after-failure | `status`: — → documented | `research` |
| BytePlus | B | Token & cost attribution per agent / tenant / session | `status`: — → documented; `product`: — → ModelArk Managed Agents | `research` |
| BytePlus | B | Data residency, in-region processing, cross-region inference behavior | `status`: — → documented | `research` |
| BytePlus | B | Evaluation service | `status`: none → documented; `product`: — → BytePlus AgentKit | `change` |
| BytePlus | B | First-party frontier models | `value`: Dola Seed 2.0, Seed 2.0 Pro, Seed 2.0 Lite, Seed 2.0 Mini, Dola Seed 2.1 Turbo → Dola Seed 2.1 Turbo, Seed 2.0 Pro, Seed 2.0 Lite, Seed 2.0 Mini, Seed 2.0 Code Preview | `change` |
| BytePlus | B | Framework agnosticism | `status`: — → documented; `product`: — → BytePlus AgentKit | `research` |
| BytePlus | B | Guardrails | `product`: — → ModelArk Content filter | `change` |
| BytePlus | B | Human-in-the-loop (interrupt/resume, approval gates) | `status`: — → documented | `research` |
| BytePlus | B | Managed knowledge base / RAG | `product`: Knowledge base → BytePlus Knowledge base (Knowledge Engine) | `change` |
| BytePlus | B | Per-end-user namespacing; TTL, deletion, export | `status`: — → documented; `product`: — → Persistent memory | `research` |
| BytePlus | B | Multi-agent patterns | `value`: orchestrator / sub-agent delegation → orchestrator / sub-agent delegation (coordinator), persistent multi-level sub-agent threads (multiagent_20261001) | `change` |
| BytePlus | B | Multi-tenant serving with tenant/session isolation | `status`: — → documented | `research` |
| BytePlus | B | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: none → unknown | `research` |
| BytePlus | B | Support tier & SLA on the agent runtime specifically | `status`: none → unknown | `research` |
| BytePlus | B | Which primitives bill separately | `status`: — → documented; `product`: — → ModelArk Managed Agents | `research` |
| BytePlus | B | Audit trail of every tool invocation | `status`: — → documented; `product`: — → ModelArk Managed Agents | `research` |
| BytePlus | B | Versioning, aliases, canary, rollback | `status`: — → documented; `product`: — → ModelArk Managed Agents | `research` |
| BytePlus | B | Built-in web search tool | `status`: — → documented | `research` |
| BytePlus | C | Add-on vs included; per-connector or per-index surcharges | `status`: — → documented | `research` |
| BytePlus | C | Admin & adoption analytics, answer-feedback loop | `status`: — → documented | `research` |
| BytePlus | C | Code-first vs low-code builder | `status`: — → documented | `research` |
| BytePlus | C | Certifications | `status`: — → unknown | `research` |
| BytePlus | C | Conversation history, personalization, retention controls | `status`: — → documented | `research` |
| BytePlus | C | DLP, tenant isolation, admin controls | `status`: — → documented | `research` |
| BytePlus | C | Guardrails | `status`: — → documented | `research` |
| BytePlus | C | Enterprise index freshness (real-time vs batch crawl) | `status`: — → unknown | `research` |
| BytePlus | C | Can the packaged product invoke agents you built yourself? | `status`: — → documented | `research` |
| BytePlus | C | Bundling with licenses you already own | `status`: — → unknown | `research` |
| BytePlus | C | Is the underlying model choosable, or fixed and opaque? | `status`: — → documented | `research` |
| BytePlus | C | Packaged assistant — is it purchasable, and what does it cover? | `status`: — → documented; `product`: — → BytePlus ArkClaw Enterprise | `research` |
| BytePlus | C | Permission-aware retrieval (ACL trimming at query time) | `status`: — → unknown | `research` |
| BytePlus | C | Prebuilt SaaS/enterprise connectors | `status`: — → documented | `research` |
| BytePlus | C | Per-seat cost, minimum seats, annual commitment | `status`: — → documented | `research` |
| BytePlus | C | Audit trail of every tool invocation | `status`: — → documented | `research` |
| BytePlus | C | Training-on-customer-data policy, retention, abuse-monitoring opt-out | `status`: — → unknown | `research` |
| BytePlus | D | Code snippet retention & training policy | `status`: unknown → documented | `research` |
| BytePlus | D | AI code review (PR review, inline suggestions) | `status`: unknown → documented | `research` |
| BytePlus | D | Per-seat pricing (individual / business / enterprise tiers) | `value`: {"free": "$0", "pro": "$10/month"} → {"free": "$0", "pro": "$20/month", "pro_plus": "$60/month", "ultra": "$200/month"} | `change` |
| BytePlus | D | IDE integration (VS Code, JetBrains, Vim/Neovim, other) | `value`: TraeCode IDE → TRAE IDE (TraeCode), TraeCode Plugin (VS Code, JetBrains) | `change` |
| BytePlus | D | MCP support in coding tool | `status`: unknown → documented | `research` |
| BytePlus | D | Model choice in coding tool | `value`: GPT-5.4, Seed-2.1-Turbo, MiniMax-M3, Kimi-K2.5, Gemini-3 series → Seed-2.1-Turbo, GPT-6.x / GPT-5.x series, GLM-5.2, DeepSeek-V4.x, Kimi-K3 / K2.7-Code / K2.5, Gemini-3.1-Pro-Preview, MiniMax-M3, Grok-4.x (U.S. only) | `change` |
| GCP | A | Community signal (contributors, issue response, production adopters) | `value`: {"stars": 21000} → {"stars": 22300} | `change` |
| GCP | A | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: — → documented | `research` |
| GCP | A | Does the SDK phone home telemetry by default, and can you disable it? | `status`: none → documented | `change` |
| GCP | B | Agent-to-agent (A2A) protocol support | `status`: — → preview; `product`: — → Agent Runtime + Agent Registry | `research` |
| GCP | B | Agent workload identity | `status`: documented → ga; `product`: — → Agent Identity | `change` |
| GCP | B | Managed browser / computer use | `status`: documented → ga; `product`: Computer Use (Sandbox) → Agent Platform Computer Use (Sandbox) | `change` |
| GCP | B | Delegated end-user auth (OAuth token vault, 3LO, on-behalf-of) | `product`: — → Agent Identity auth manager | `change` |
| GCP | B | Evaluation service | `status`: documented → ga; `product`: Evaluation Service → Agent Evaluation (Evaluation Service) | `change` |
| GCP | B | Framework agnosticism | `value`: ADK, LangGraph, LangChain, LlamaIndex, AG2, A2A, custom → ADK, LangGraph, LangChain, LlamaIndex, AG2, CrewAI, A2A, custom | `change` |
| GCP | B | Guardrails | `product`: Safety Filters + Model Armor + DLP → Safety Filters + Model Armor + Sensitive Data Protection | `change` |
| GCP | B | Long-term memory (semantic, episodic, preference) | `product`: Memory Bank → Agent Platform Memory Bank | `change` |
| GCP | B | Managed MCP registry / catalog | `status`: documented → ga; `product`: Skill Registry → Agent Registry | `change` |
| GCP | B | OpenTelemetry / GenAI semconv; span-level tool-call traces | `status`: documented → ga; `product`: — → Agent Observability | `change` |
| GCP | B | Region availability OF THE AGENT RUNTIME | `status`: limited → documented; `value`: {"in_country_allowlist": ["ca", "in", "asia-northeast1 (JP)", "sg", "europe-west2 (UK)"], "multi_regions": ["global", "us", "eu"]} → {"multi_regions": ["us", "eu"], "region_list": ["us-east1", "us-east4", "us-west1", "us-central1", "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-west6", "europe-west8", "europe-southwest1", "asia-east1", "asia-east2", "asia-northeast1", "asia-northeast3", "asia-south1", "asia-southeast1", "asia-southeast2", "australia-southeast2", "me-west1", "northamerica-northeast1", "northamerica-northeast2", "southamerica-east1"], "regions": 23} | `change` |
| GCP | B | Support tier & SLA on the agent runtime specifically | `status`: documented → unknown; `value`: 99.5% (online inference), 99.9% (Agent Search API) → — | `research` |
| GCP | C | Where the enterprise index physically lives | `value`: global, us, eu, ca, in, asia-northeast1, sg, europe-west2 → global, us, eu, br, ca, in, asia-northeast1, sg, europe-west2 | `change` |
| GCP | C | Per-seat cost, minimum seats, annual commitment | `value`: {"business": "USD 21/seat/month", "plus": "USD 30+/seat/month (annual)", "standard": "USD 30/seat/month (annual)"} → {"business": "USD 21/seat/month", "plus": "USD 30+/seat/month", "standard": "USD 30/seat/month (starting)"} | `change` |
| GCP | D | Agentic coding (multi-file edits, task execution, tool use) | `status`: documented → ga | `change` |
| GCP | D | CLI / terminal agent mode | `product`: — → Antigravity CLI (agy) | `change` |
| GCP | D | AI code review (PR review, inline suggestions) | `product`: — → Gemini Code Assist on GitHub | `change` |
| GCP | D | Codebase indexing / repo-wide context | `product`: — → Gemini Code Assist Enterprise — code customization (legacy) | `change` |
| GCP | D | Per-seat pricing (individual / business / enterprise tiers) | `value`: {"enterprise_annual": "$45/seat/month", "enterprise_monthly": "$54/seat/month", "free": "$0", "standard_annual": "$19/seat/month", "standard_monthly": "$22.80/seat/month"} → {"free": "$0/month", "gemini_enterprise_payg": "$0 seat fee, consumption-based", "gemini_enterprise_standard_plus": "from $30/seat/month", "google_ai_pro": "consumer subscription (price not on this page)", "google_ai_ultra": "consumer subscription (price not on this page)"} | `change` |
| GCP | D | IDE integration (VS Code, JetBrains, Vim/Neovim, other) | `status`: documented → ga; `value`: VS Code, JetBrains, Android Studio, Cloud Shell Editor, Cloud Workstations → VS Code, Visual Studio, JetBrains, Android Studio, Zed, Xcode, Eclipse | `change` |
| GCP | D | Model choice in coding tool | `value`: Gemini 2.5 Pro, Gemini 2.5 Flash → Gemini 4 Neon, Gemini 4 Carbon, Gemini 4 Argon, Gemini 4 Hydrogen, Orchestrator, Gemini 3.8 Flash, Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.1 Pro, Claude Sonnet 5.5, Claude Opus 5.5 | `change` |
