# AI Engineering Portfolio — seven runnable projects

Build and explain an end-to-end agentic application, then isolate each advanced pattern in its own project. Gemini is the configured default through LangChain `init_chat_model`. OpenAI and Anthropic use the same factory. Python, uv, LangChain, LangGraph, FastAPI, Streamlit, Chroma, Hugging Face, scikit-learn, MCP, ADK and A2A are integrated here.

## Standalone project repositories

Each project now has a dedicated repository with its own source, README, focused demo, UI entry point, frozen dependencies, tests and Docker configuration. Open a project directly:

| Project | Dedicated repository | Main focus |
|---|---|---|
| InsightForge | [insightforge-multi-agent-analytics](https://github.com/Swaroopfullstack/insightforge-multi-agent-analytics) | Supervisor, data analysis, RAG, ML and memory |
| EvidenceDesk | [evidencedesk-agentic-rag](https://github.com/Swaroopfullstack/evidencedesk-agentic-rag) | Seven retrieval strategies and document citations |
| ReviewOps | [reviewops-human-in-the-loop](https://github.com/Swaroopfullstack/reviewops-human-in-the-loop) | Durable approval, authorization and idempotent exports |
| ResearchSwarm | [researchswarm-langgraph-agents](https://github.com/Swaroopfullstack/researchswarm-langgraph-agents) | Parallel researchers and bounded writer/critic review |
| ProtocolBridge | [protocolbridge-mcp-a2a](https://github.com/Swaroopfullstack/protocolbridge-mcp-a2a) | Actual MCP and A2A clients, tools and services |
| TripWise ADK | [tripwise-google-adk](https://github.com/Swaroopfullstack/tripwise-google-adk) | ADK workflows, tools, callbacks and durable sessions |
| Foundation Studio | [foundation-studio-langchain](https://github.com/Swaroopfullstack/foundation-studio-langchain) | LCEL, prompts, structured output, streaming and middleware |

The original repository remains the combined learning hub. The standalone repositories vendor the tested common runtime and can be cloned independently.

## Start here

Run these commands **from this repository root**, in PowerShell or a terminal with uv installed:

```powershell
uv sync --frozen --extra embeddings --extra adk --extra gradio
Copy-Item .env.example .env
uv run portfolio bootstrap
uv run portfolio doctor
uv run uvicorn portfolio.api:app --host 127.0.0.1 --port 8000 --workers 1
```

Open a second terminal in the same folder:

```powershell
uv run streamlit run projects/01-insightforge/app.py --server.address 127.0.0.1
```

Visit http://localhost:8501. Development credentials are `demo-alice-key`, `demo-bob-key`, and `demo-reviewer-key`. Upload `assets/public/iris.csv` and `assets/public/nist-ai-rmf-1.0.pdf`. Ask “Summarize the data”, “Train and compare models”, “What are Govern, Map, Measure and Manage?”, “remember language=English”, and “calculate 12*(3+4)”. Every project is also available in the sidebar.

**Default `RUN_MODE=demo` needs no paid API key.** SQLite, Chroma, PDF extraction, graph execution, tool execution, review transactions and ML training are real. Model routing/writing use labeled deterministic fixtures. Demo embeddings use an explicitly labeled lexical hashing baseline. The HF embedding backend and live inference are opt-in, with no silent substitution after a provider failure.

## The projects

| Project | What you build | Launch / learning guide |
|---|---|---|
| 01 InsightForge | Supervisor + Data, RAG, ML, Tools, Memory; CSV/PDF upload; model comparison; session UI | [Guide](projects/01-insightforge/README.md) |
| 02 EvidenceDesk | Hybrid BM25/vector retrieval, MMR, multi-query, compression, parent expansion, self-query | [Guide](projects/02-evidencedesk/README.md) |
| 03 ReviewOps | Persisted human interrupt, analyst/reviewer roles, version checks, transactional idempotent export | [Guide](projects/03-reviewops/README.md) |
| 04 ResearchSwarm | Send fan-out, reducer, evidence aggregation, writer/critic subgraph, bounded revisions | [Guide](projects/04-researchswarm/README.md) |
| 05 ProtocolBridge | Actual MCP tools/resources, stdio/HTTP transport, agent adapter, A2A discovery and tasks | [Guide](projects/05-protocolbridge/README.md) |
| 06 TripWise ADK | Real Runner, sessions, callbacks, tools, Sequential/Parallel/Loop agents and deterministic BaseAgent | [Guide](projects/06-tripwise-adk/README.md) |
| 07 Foundation Studio | Prompts, Pydantic, LCEL branches/parallel/assignment, Gradio streaming, LangChain middleware + HITL | [Guide](projects/07-foundation-studio/README.md) |

These share an install, API and configuration intentionally. They are separately runnable workflows, not seven independently deployed microservices.

## Use Gemini and real Hugging Face embeddings

Edit your private `.env`:

```dotenv
RUN_MODE=live
GOOGLE_API_KEY=your-key
LLM_PROVIDER=google_genai
LLM_MODEL=gemini-3.8-flash
LLM_TEMPERATURE=1.0
LLM_TOP_P=
LLM_TOP_K=
LLM_MAX_TOKENS=1600
EMBEDDING_BACKEND=huggingface
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

Restart the API. The first HF run downloads model weights; allow extra disk/time. Re-index your documents after switching embeddings: backend/model are part of the collection identity, so incompatible indexes are not mixed. A model ID must be available to your account. See [configuration](docs/CONFIGURATION.md) for provider switching, sampling, retrieval counts and allowlists. `LLM_TOP_K` and `RETRIEVAL_K` are different controls.

For a complete copy-and-fill example, follow [private .env setup](docs/ENV_SETUP.md): [offline template](.env.example), [Gemini template](.env.gemini.example), or [production template](.env.production.example). Templates contain placeholders only; put actual keys in your local `.env` or hosting secret store.

## Run without the UI

```powershell
uv run portfolio demo insight
uv run portfolio demo evidence
uv run portfolio demo review
uv run portfolio demo research
uv run portfolio demo mcp
uv run portfolio demo mcp-agent
uv run --extra adk portfolio demo adk
uv run portfolio demo foundation
uv run --extra gradio python -m portfolio.gradio_app
uv run portfolio evaluate
```

CLI demos run with local operator authority. The HTTP API authenticates all user data operations. See the interactive API contract at http://localhost:8000/docs while the backend is running.

## Verify and learn

```powershell
uv run pytest -q --junitxml=reports/test-results.xml
uv run ruff check src tests
uv run portfolio evaluate
```

- [Learning path](docs/LEARNING_PATH.md): practice in prerequisite order.
- [Architecture](docs/ARCHITECTURE.md): state, ownership, graph and service boundaries.
- [API examples](docs/API_EXAMPLES.md): authenticated uploads, requests and SSE progress.
- [Concept coverage](docs/CONCEPT_COVERAGE.md): every objective from the two course audits, with implementation or explicit extension status.
- [Deployment and operations](docs/DEPLOYMENT.md): storage contract, Docker, CI, secrets, backup and rollback.
- [Git workflow](docs/GIT_WORKFLOW.md): branch, commit, review and release practice.
- [Validation evidence](reports/VALIDATION.md): what was actually executed and what still needs external infrastructure.
- [Public evaluation](reports/public-evaluation.json): fixture-specific metrics with baselines and limitations.
- [LinkedIn showcase](docs/LINKEDIN_SHOWCASE.md): demo script and truthful project descriptions.

[Actual demo screenshot](reports/insightforge-demo.png): the running Streamlit application displaying a real Iris model comparison, with its offline model-routing mode labeled.

## Deployment scope

This is a production-oriented reference implementation with enforced controls: authenticated ownership, role checks, input limits, persisted checkpoints, single-decision exports, rate/concurrency limits, provider timeout/retry/circuit breaker, and testable no-answer paths. Its supported storage architecture is **one API instance, one worker, durable local storage**. A cloud deployment, load test, restore drill, provider capability check and live response evaluation must be completed for your actual environment before calling that deployment production ready. See the concrete [deployment contract](docs/DEPLOYMENT.md).

## Public data and upstream documentation

Public fixtures retain their [provenance manifest](assets/public/PROVENANCE.json). NIST AI RMF **1.0 (2023)** is a versioned teaching corpus. Iris is CC BY 4.0 with repository attribution. The diabetes CSV comes from scikit-learn's bundled dataset. No endorsement or medical inference is claimed.

Implementation references: [LangChain models](https://docs.langchain.com/oss/python/langchain/models), [Google integration](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai), [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk), [ADK](https://google.github.io/adk-docs/), [A2A Python SDK](https://github.com/a2aproject/a2a-python), [scikit-learn](https://scikit-learn.org/stable/).
