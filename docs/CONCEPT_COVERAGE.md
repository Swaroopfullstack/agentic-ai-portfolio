# Course concept coverage — all original and supplemental objectives

The two supplied notes audits contain **281 objectives**. Every objective appears below in prerequisite-family order. Duplicated course files were already consolidated by those audits.

**Accounted for does not mean fully implemented.** An implementation example demonstrates the named pattern; composite objectives can still include additional course variants. External integrations and course-domain workflows are explicitly exercises. Read the original notes for the full explanation; these projects provide runnable practice and honest feature boundaries.

| Status | Objectives |
|---|---:|
| Implementation example | 100 |
| Guided practice / partial pattern | 148 |
| External integration exercise | 12 |
| Course-domain extension | 21 |

[Learning path](LEARNING_PATH.md) · [Extension exercises](EXTENSION_LABS.md) · [Machine-readable matrix](concept-coverage.json)

## Environment, configuration, and package structure

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Project interpreter, virtual environment, imports, and dependency installation (2.1) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/config.py) |
| Environment variables, provider credentials, and configuration validation (2.2, 2.4) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/config.py) |
| Functions, dictionaries, type hints, Pydantic, generators, and async Python (2.3) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| load_dotenv precedence, uv init/add/sync, src packages, and editable installation (2.5) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/config.py) |
| Typed settings, SecretStr, lru_cache, and process-local configuration (25.13) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/config.py) |

## Direct model calls, conversation, and Gradio

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Construct a provider client and inspect a chat-completion response (3.1) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| System, user, and assistant roles and response content (3.2) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/models.py) |
| Tokens, temperature, and generation limits (3.3) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/models.py) |
| Stateless calls versus an explicitly supplied conversation message list (3.4) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/models.py) |
| Chat helper functions and a Gradio chat interface (3.5) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/gradio_app.py) |
| Convert Gradio message history into the provider request format (3.6) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/gradio_app.py) |

## Streamlit chat and financial-analysis UI

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Script reruns, session_state initialization, chat_input, and chat_message (4.1, 4.2) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/ui.py) |
| Run and stop the local UI server; invoke only for a new input (4.1, 4.2) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| UI history versus execution checkpoints versus business records (4.3) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/ui.py) |
| Replace Thinking text with st.empty; Boolean button results and disabled state (4.4) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Financial inputs, prompt construction, chain testing, and sidebar-driven analysis (5.5) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## LangChain models, prompts, parsers, and LCEL

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| ChatOpenAI, init_chat_model, message classes, and Azure deployment configuration (5.1) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| invoke, ainvoke, batch, and stream execution interfaces (5.2) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| ChatPromptTemplate variables and prompt-model-parser pipe composition (5.3) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| String parsing, JSON parsing, nested Pydantic validation, and malformed output (5.4) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| ChatAnthropic and provider-specific capabilities (5.6) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| PromptTemplate versus ChatPromptTemplate; partial variables and format instructions (5.6) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/labs.py) |
| PydanticOutputParser parses and validates the model's text (5.6) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/foundations.py) |
| RunnableLambda transforms and RunnableParallel named branches (5.7) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Provider-executed tools versus client-executed tool calls and content blocks (5.8) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Structured agent output

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Turn an unstructured answer into a typed application contract (6.1) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/foundations.py) |
| ToolStrategy versus ProviderStrategy and supported model capabilities (6.2) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| structured_response versus conversational messages (6.2) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Schema correctness versus factual correctness versus completed business actions (6.3) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Tools, ReAct, SQL, and short-term memory

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Reason/action/observation agent loop and tool descriptions (7.1, 7.3) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| bind_tools exposes schemas; runtime execution and ToolMessage supply observations (7.2) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/labs.py) |
| create_agent configuration and repeated tool selection (7.3) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Weather HTTP tools, filesystem read/write, and custom/prebuilt Tavily search (7.4) | [01-insightforge](../projects/01-insightforge/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Natural-language SQL: list tables, inspect schema, query, and interpret rows (7.5) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| SQL permissions and ownership checks at the actual data boundary (7.5, 18.9) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Explicit @tool args_schema with Pydantic argument validation (7.6) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| thread_id continuity and independent conversation identities (9.1) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/ui.py) |
| InMemorySaver, SQLite checkpoints, PostgreSQL checkpoints, and connection lifetime (9.2) | [01-insightforge](../projects/01-insightforge/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Short-term messages versus durable user knowledge (9.3) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/storage.py) |

## LangChain middleware and guardrails

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Middleware placement around the model/tool/agent lifecycle (8.1, 8.7) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Model wrappers, handler return values, and call logging (8.2) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/foundations.py) |
| Static model choice versus dynamic model routing (8.3) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Static prompts, dynamic prompts, trusted context, and role-aware instructions (8.4) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| wrap_tool_call errors and valid tool observations with matching call IDs (8.5) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| PII redact, mask, hash, and block strategies; input/output/tool-result targets (8.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Before/after hooks versus wrappers; sync versus async hooks (8.7) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Model failure, tool failure, retries, and tracing the correct execution call (8.8) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| HumanInTheLoopMiddleware composed with custom middleware (12.3, 12.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/foundations.py) |

## Memory growth and compression

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Conversation growth, token budget, cost, latency, and bounded context (9.4) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Trim messages while preserving valid message/tool-call relationships (9.4) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| SummarizationMiddleware triggers and recent-message retention (9.5) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Summary loss, missing detail, and memory-growth/trim/summary comparisons (9.5) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Retrieval and the employee-handbook corpus

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| RAG ingestion versus query-time retrieval and answer generation (10.1) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| PDF loading, Document text, page/source metadata, and provenance (10.2) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Recursive chunk splitting, overlap, and context boundaries (10.2) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Semantic embeddings and cosine similarity versus the offline lexical demonstration (10.3) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Chroma index creation, persistence, stale indexes, and embedding consistency (10.3) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Similarity search, score direction, top-k, MMR diversity, and batch retrieval (10.4) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Retrieval as an optional agent tool versus always-retrieve middleware (10.5) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Grounded prompting, missing evidence, citations, and explicit source return (10.6) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| The actual handbook's policy categories and its role as sample retrieval data (10.7) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |

## Agent streaming

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| updates for progress, messages for model chunks, and custom tool events (11.1) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Trace model proposal, tool start/result, and final answer (11.2) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Custom progress reporting with a stream writer (11.1, 11.2) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Separate token display from approval and actual tool execution (11.3) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Gmail, OAuth, and human review

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Cloud project, enabled Gmail API, consent screen, desktop OAuth client, and scopes (12.1) | [03-reviewops](../projects/03-reviewops/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| User consent, access token, refresh token, and private local credential storage (12.1) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Gmail toolkit and a query/response email workflow (12.1, 12.2) | [03-reviewops](../projects/03-reviewops/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Pause before sending or other sensitive tool execution (12.2, 12.3) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Approval/edit/reject decisions and allowed_decisions (12.3, 12.4) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Resume with Command on the same saved thread; validate edited arguments (12.4, 12.5) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Custom model logging plus HITL on a real agent in the offline scripted-model demo (12.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/foundations.py) |

## MCP protocol, clients, server tools, and Git workflow

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Host, client, server, reusable capabilities, and discovery before execution (13.1, 13.2) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Client session initialization, list_tools, call_tool, and structured tool responses (13.2) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/protocol.py) |
| FastMCP function registration and a minimal server (13.3) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/protocol.py) |
| Filesystem and database tools: listing, creation, schema inspection, and queries (13.3, 13.6) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Stdio process lifetime versus legacy SSE versus Streamable HTTP (13.4) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| MultiServerMCPClient, async tool loading, and adapter conversion for an agent (13.5) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Filesystem roots and read-only SQL enforced in code/permissions (13.6) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Local Git subprocess operations versus hosted GitHub repository/PR operations (13.7, 27.2) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Node/server launch, credentials, branch/edit/add/commit/push, and PR workflow (13.7) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Noninteractive subprocess execution, explicit working directories, and bounded access (13.7) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/protocol.py) |
| Incomplete middleware syntax and undefined client call in original source fragments (13.8) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Resources, resource templates, tool calls, and prompt capabilities (13.9) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/protocol.py) |
| MCP CLI installation, desktop registration, interpreter paths, and transport matching (13.10) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## LangGraph fundamentals and message state

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| StateGraph, typed state, nodes returning partial updates, START, END, and compile (14.1, 14.2) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Reducers versus replacement and concurrent writes to shared keys (14.3) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Annotated state and operator.add aggregation (14.3, 16.1) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| MessagesState/add_messages, message IDs, replacement, and RemoveMessage (14.4) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Input schema, output schema, and private node channels (14.5, 14.8) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Rebuild a model/tools loop with bind_tools, ToolNode, and conditional routing (14.6) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Stream updates versus values and inspect a state snapshot (14.7, 15.1) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Mermaid graph output, optional PNG renderer, and xray subgraph expansion (14.7) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Public output shape does not establish a security boundary for internal traces (14.8) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## LangGraph summaries, checkpoints, and interrupts

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Checkpoint snapshot, values, next tasks, and thread continuation (15.1) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Summary state, conditional summarize node, retaining recent messages, and removal (15.2) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| interrupt payload, pending execution, and Command(resume=...) (15.3) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/review.py) |
| Replay from the node beginning and side effects before an interrupt (15.4) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/review.py) |
| Avoid broad try/except swallowing interrupts (15.4) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/review.py) |
| Approve/reject routing, edit a draft, and request additional information (15.5) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Two sequential form questions and stable interrupt order (15.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/labs.py) |
| JSON-serializable payloads, typed resume values, and input validation (15.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Parallel graphs, dynamic Send, and fraud demonstrations

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Independent fan-out branches and a reducer for branch results (16.1) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/research.py) |
| Web/wiki research branches and a synthesis step (16.1, 16.2) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Explicit fan-in join and dependencies before aggregation (16.2) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Send creates data-dependent workers with per-worker input (16.3) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/research.py) |
| Generate topics, map joke generation, then choose a best joke through typed output (16.3) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| SQL-backed frequency, value, reason, and timing fraud checks (16.4) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Keep the three-check notebook and four-check handout variants distinct (16.4) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Tagged branch results, bounded scores, weighted aggregation, and risk thresholds (16.5) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Supervisors, specialists, and nested subgraphs

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Supervisor structured routing to specialized workers and FINISH (17.1) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/insight.py) |
| Agent-node factories, worker results, and conditional return to the supervisor (17.1) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Handoff limits and termination rules (17.2) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Parent and child state contracts and explicit input/output transformation (17.3) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/research.py) |
| Fraud child workflow inside a parent order/return workflow (17.3) | [01-insightforge](../projects/01-insightforge/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Command state updates and navigation versus ordinary edges (17.4) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Test a specialist/subgraph boundary before the full team (17.5) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/research.py) |

## LangChain support capstone: data, tools, approval, and UI

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Single main support agent and customer/admin journeys (18.1) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Package/module dependency order and incremental construction (18.2, 18.10) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Business tables, keys/joins, SQL seeds, and database initialization (18.3) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Login, trusted user identity, conversation ID, and tool runtime context (18.4) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/insight.py) |
| Policy chunks, persistent vector store, source metadata, and policy versions (18.5) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Cancellation eligibility, approval, database mutation, and notification trace (18.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Return/refund eligibility and the difference between database records and payment delivery (18.7) | [03-reviewops](../projects/03-reviewops/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Pending action rows, persisted checkpoints, admin queue, and resume identity (18.8) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/review.py) |
| Business data, UI conversation data, checkpoints, and Chroma schemas have different roles (18.3, 18.8) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/storage.py) |
| SQL toolkit limitations, simulated email claims, and stronger authorization/idempotency (18.9) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| README/dependency setup, logging middleware, Gmail options, and customer/admin practice (18.2, 18.9, 18.10) | [03-reviewops](../projects/03-reviewops/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Empty package markers and scaffold entry points add packaging context, not new agent behavior (2.5, 18.2) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## LangGraph support capstone: nested returns and fraud

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Supervisor, order, inventory, policy agents, and reusable notification utility (19.1) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Specification versus implementation, contradictory seed counts, and policy differences (19.2) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Main state, worker routing, message accumulation, and completion (19.3) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/insight.py) |
| Direct cancellation versus the previous capstone's approval-gated cancellation (19.4) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Return validation, pending record, human gate, approved/rejected finalization (19.5) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Nested Send fraud checks with 35/35/15/15 weights and explanations (19.6) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Child workflow as a tool versus child compiled graph as a node (19.7) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| SQLite business storage versus PostgreSQL checkpoints and dashboard resume (19.8) | [04-researchswarm](../projects/04-researchswarm/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Customer chat, admin queue, fraud score display, and test scenarios (19.8, 19.9) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Return/shipping/FAQ documents are distinct course policies, not universal business rules (19.2, 19.4) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |

## ADK first agent, Runner, schemas, and direct Gemini SDK

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| ADK package scaffold, root_agent export, model-backed Agent, and function tools (20.1, 20.2) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| Runner, SessionService, app/user/session identity, and types.Content (20.3) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| Async event iteration, final response, function calls, and function responses (20.4) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| CLI run, web UI, API server, and SSE execution (20.5) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Input/output schemas, output_key, include_contents, and LiteLLM model adapters (20.6) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Direct Gemini SDK request-response, streaming, and multi-turn chat (20.7) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Legacy google-generativeai examples versus current google-genai client syntax (20.7) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## ADK state, scopes, events, and guardrail callbacks

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| ToolContext state and remembered translation preferences (21.1) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Session, user:, app:, and invocation-only temp: state scopes (21.2) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Instruction placeholders, optional missing values, and output_key data flow (21.3) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| EventActions/state_delta, Runner processing, and session persistence (21.4) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| before_model_callback returning a response versus allowing the request (21.5) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Banking balance/history/transfer tools, intent screening, and audit state (21.6) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Validate transactions in the tool; keywords cannot guarantee safe money movement (21.6) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## ADK delegation and workflow design patterns

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Coordinator delegation to todo/reminder/motivation specialists (22.1) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Global demonstration state versus isolated session/user state (22.1) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Agent transfer versus AgentTool returning a result to its caller (22.2) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| SequentialAgent sales-data generation, analysis, and final report through output keys (22.3) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| LoopAgent response generation, quality critique, revision, and attempt limit (22.4) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| escalate termination, accepted output, and exhausted-loop fallback (22.5) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| ParallelAgent news/financial/sentiment research with distinct output keys and synthesis (22.6) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| Dispatcher, hierarchy, review/critique, and terminal-input human review (22.7, 22.8) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| BaseAgent _run_async_impl asynchronous generator for deterministic work (22.9) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| Iteration counter event deltas and simulated post-escalation ticket/email helpers (22.9) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Implementation example](../src/portfolio/adk_project.py) |

## ADK YAML configuration and MCP tools

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Declarative YAML agent model, instructions, imported tools, and specialist references (23.1) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Prime checker deterministic function and Python module import path (23.2) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| MCPToolset transport configuration and tool name filtering (23.3) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Async construction, process/client lifetime, and cleanup on completion (23.3) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/protocol.py) |

## TripWise: project setup and domain boundaries

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Root coordinator, four-stage planning, policy specialist, and expense pipeline (24.1) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Configuration, module roles, README setup, .env.example, and initialization (24.2) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Employee/trip/approval/booking/expense/notification schemas and durable business facts (24.3) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| In-memory session/artifact lifetime versus persistent SQLite (24.3) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Requirements collection, Pydantic date constraints, and actually enforcing declared schemas (24.4) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Parallel flight/hotel/transport/visa research and distinct result keys (24.5) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Mock booking data, unknown-city fallback, and live-provider evidence (24.5) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Itinerary quality loop, threshold, bounded iterations, and counter scope (24.6) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Budget comparison, pending manager review, and later status reads (24.7) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Manager authorization, stale decisions, and annual-versus-per-trip budget meaning (24.7) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Artifact save/load, name/version, and mismatched current_trip_id keys (24.8) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Default direct policy tools versus optional MCP factory (24.9) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Travel, per diem, approved vendors, expenses, and restricted-destination policy content (24.9) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Conflicting expense deadlines/category names and canonical business rules (24.9) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Expense collection, validation, arithmetic, report/item insertion, and artifact generation (24.10) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Simulated notification record versus actual delivery/reimbursement (24.10) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| A2A service adapters and optional flight/hotel/notification endpoints (24.11) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| MCP capability calls versus remote-agent tasks; explicit remote inputs (24.11) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Streamlit employee/manager flows, event logging, and shared local Runner (24.12) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Async runner lifecycle, asyncio.run boundary, and seven source scenarios (24.12) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Travel Admin Panel requirement is absent from supplied implementation (24.13) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Declared schemas, optional factories, and services must be wired to affect execution (24.13) | [06-tripwise-adk](../projects/06-tripwise-adk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## FastAPI material in the Word anthology

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| HTTP service boundary, client/server roles, app, and Uvicorn (25.1, 25.2) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/api.py) |
| GET/POST routes, path parameters, query parameters, and validation (25.2) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/api.py) |
| Pydantic request/response models and output filtering (25.3) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Application credentials separated from provider secrets (25.4) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/api.py) |
| Depends injection for identity, configuration, and services (25.5) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/api.py) |
| Async model/chain invocation and blocking-work boundaries (25.6) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| StreamingResponse, SSE event framing, and incremental client output (25.7) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| BackgroundTasks versus a durable external job queue (25.8) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| CORS, HTTPException, status codes, and error bodies (25.9) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Lifespan setup/cleanup for model, database, and runtime clients (25.10) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/api.py) |
| TestClient, lifespan-aware tests, and unauthorized request checks (25.11) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/api.py) |
| Dependency packaging, Docker, worker state, reverse proxy, and production boundaries (25.12, 33.1) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Typed environment-backed settings dependency and cached initialization (25.13) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Foundations and model boundaries

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Training, inference, token generation and the model/API/application distinction (1.3, 1.4) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Managed versus self-hosted models, open weights and private networking limits (2.6) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Notebook kernel/virtual environment identity, dependency reproducibility and debugging (2.5, 2.7) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/config.py) |
| Temperature, top-k and top-p with a normalized probability example (3.7) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Usage metadata, input/output costs and context-window limits (3.8, 31.9) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Resource caching versus session state; owned thread selection and rerun loops (4.5, 4.6) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Prompts, runnables and structured results

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Optional history placeholders, few-shot examples and prompt composition (5.9) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Sequential/parallel runnable contracts and passthrough assignment (5.7, 5.10) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Runnable branching, input/output schema inspection and debug boundaries (5.11) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/labs.py) |
| String/JSON/Pydantic parsing versus model-level and agent-level structured output (5.4, 5.6, 6.4) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Optional fields, constrained values and structure versus factual support (6.3, 6.4, 29.9) | [07-foundation-studio](../projects/07-foundation-studio/README.md) | [Implementation example](../src/portfolio/foundations.py) |

## Tools, middleware and memory

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Decorated tool objects, argument schemas, names and descriptions (7.6, 7.7) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Multiple tool proposals, observation IDs and dependent versus independent execution (7.8) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| SQL table/schema/query-check/query-execution roles and permission boundaries (7.9, 13.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Middleware nesting, immutable overrides and relevant-message routing (8.9) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Tool retry attempts, capped backoff, jitter and failure observations (8.10, 30.10) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Shell execution policy, working directory, actual exit status and runtime access (8.11) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Todo/planning and filesystem glob/grep tools versus execution evidence (8.12) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Checkpoint scope versus long-term store scope and physical durability (9.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/storage.py) |
| Namespace/key/JSON store operations and cross-user/tenant separation (9.7, 9.8) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/storage.py) |
| Trusted ToolRuntime context, dataclass/dictionary access and hidden runtime arguments (9.8) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/insight.py) |
| RunnableWithMessageHistory sessions versus graph threads/checkpoints (9.9) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Buffer/window/summary/hybrid strategies, token trimming and valid tool history (9.4, 9.5, 9.10) | [03-reviewops](../projects/03-reviewops/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Human review through LangChain middleware, approval/rejection and actual effects (12.3, 12.4, 12.6) | [03-reviewops](../projects/03-reviewops/README.md) | [Implementation example](../src/portfolio/foundations.py) |

## Retrieval from basic indexing to advanced strategies

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Retrieval versus fine-tuning versus authoritative factual tools (10.8) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Embedding vector dimensions, cosine calculation and non-probabilistic scores (10.3, 10.9) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Exact/approximate indexes, local/hosted embeddings, cache namespaces and persistence (10.10) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Lazy loaders, PDF/page provenance, recursive/markdown/code splitting (10.2, 10.11) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Similarity/distance/threshold semantics and correct MMR relevance/diversity direction (10.4, 10.12) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Trusted metadata filters, no-answer behavior and backend filter translation (10.12, 10.17) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Middleware retrieval versus an agent-selected retrieval tool (10.5) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Multi-query expansion, bounded work and stable document deduplication (10.13) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Contextual compression, hybrid BM25/dense search and weighted rank fusion (10.14) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Child-vector hits, parent-document expansion and consistent parent-store persistence (10.15) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Conversational research assistant, standalone follow-up queries and one evidence set (10.16) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |
| Self-query structured criteria combined with mandatory access filters (10.17) | [02-evidencedesk](../projects/02-evidencedesk/README.md) | [Implementation example](../src/portfolio/retrieval.py) |

## MCP and graph execution

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| MCP discovery, resources, transport/session initialization and cleanup (13.2, 13.4, 13.9, 13.11) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/protocol.py) |
| State schemas, reducer deltas, message identities and superstep visibility (14.3, 14.4, 14.9) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Conditional edges and exact validated routing instead of prose matching (14.10) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Snapshot values/next/config/metadata/parent/task/history inspection (15.7) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Replay versus a historical branch versus copying state into another thread (15.8) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/labs.py) |
| Static breakpoints versus dynamic interrupt/resume, preserving review decisions (15.9) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Generate/review/revise loops, bounded attempts and truthful exhaustion (15.10) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/research.py) |
| Generated-code execution boundaries and alignment of task/tests/acceptance (15.10, 32.5) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Independent branches, explicit joins and dynamically dispatched Send tasks (16.1, 16.2, 16.3) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/research.py) |
| Map/reduce dataflow versus actual concurrency and result provenance (16.6) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Implementation example](../src/portfolio/research.py) |

## Agent teams and project composition

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Supervisor routing, final deliverable selection and bounded handoffs (17.1, 17.2, 17.6) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Messages, structured shared state and blackboard communication (17.6) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Local specialist handoffs, departments, nested supervisors and subgraph contracts (17.3, 17.4, 17.7) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Multi-agent versus multi-model/multimodal; evaluate a simpler baseline (17.7, 17.8) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Research planning/search/analysis/writing/review with actual evidence rather than fixtures (17.8) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Original support project progression and distinct policy/workflow variants (18.1, 19.1) | [04-researchswarm](../projects/04-researchswarm/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## ADK and remote A2A

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Runner identity, event iteration, sessions and state scopes (20.3, 20.4, 21.2, 21.4) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Model callbacks versus tool-operation validation and the banking-screening failure (21.7) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Sequential/parallel/loop workflows, deterministic counters and business escalation (22.3, 22.4, 22.6, 22.9, 22.10) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/adk_project.py) |
| Declarative agents and MCP lifetime/filtering (23.1, 23.3) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Agent service boundary, A2A versus MCP and protocol version compatibility (23.4) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/a2a_project.py) |
| Agent cards, skills, modes, authentication metadata and discovery limits (23.5, 23.9) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/a2a_project.py) |
| Executor/handler/ASGI adapter and EventQueue versus durable job queues (23.6) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Message/context/task/thread identities and trusted principal mapping (23.7) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Task lifecycle, status/artifact events, cooperative cancellation and durability (23.8) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Course-domain extension](../docs/EXTENSION_LABS.md) |
| Client event types, secure registry lookup and transport failures (23.9) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [Implementation example](../src/portfolio/a2a_project.py) |
| ADK to_a2a server adapter, RemoteA2aAgent client proxy and inventory consistency (23.10) | [05-protocolbridge](../projects/05-protocolbridge/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |

## API, tests and evaluation

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Production request ordering, typed outcomes, lifecycle and blocking-call handling (28.7, 28.8, 28.10) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/api.py) |
| Rate limits, token quotas, concurrency, readiness and protected operational endpoints (28.11) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/api.py) |
| Scaffold settings/imports versus enforced identity, graph and memory behavior (28.12) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Unit/integration/live-provider/task/operational testing evidence (29.8) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Versioned datasets, named experiments, baselines and regression slices (29.7, 29.9) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/evaluation.py) |
| Judge calibration, bounded structured scores and evaluator edge cases (29.5, 29.9) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Reliable and measurable operation

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Closed/open/half-open breaker, consecutive failures and bounded probes (30.9) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/reliability.py) |
| Retry composition, deadlines, safe fallbacks and operation idempotency (30.10) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Nested traces, current setup, safe metadata and redaction before export (31.7) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Exact TTL versus semantic caches, scoped keys, invalidation and in-flight work (31.8) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../src/portfolio/reliability.py) |
| Full-context token budgets, output reservation, usage reconciliation and model routing cost (31.9) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |
| Regex/LLM guard false positives and negatives, PII boundaries and output-check limits (32.8) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

## Deployment and the learning path

| Objective / notes section | Project | Evidence / status |
|---|---|---|
| Managed Render deployment, PORT, secret injection and persistent state (33.10) | [01-insightforge](../projects/01-insightforge/README.md) | [External integration exercise](../docs/EXTENSION_LABS.md) |
| Compatible container runtime, image cache, non-root ownership and health semantics (33.11) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../Dockerfile) |
| CI-gated release verification and rollback (33.8, 33.9, 33.10) | [01-insightforge](../projects/01-insightforge/README.md) | [Implementation example](../Dockerfile) |
| One prerequisite order, canonical lab and independent completion evidence (34.8, 34.9, 34.10) | [01-insightforge](../projects/01-insightforge/README.md) | [Guided practice / partial pattern](../docs/EXTENSION_LABS.md) |

