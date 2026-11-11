# Portfolio implementation and validation plan

Status: the seven project entrypoints, shared implementation, public fixtures, learning guides, concept matrix and local validation are delivered. See [validated scope](reports/VALIDATION.md) for executed checks and the external release work that remains. This file records the original implementation contract.

## Deliverables

1. **InsightForge:** LangGraph supervisor → Data/RAG/ML/Tools/Memory specialists; Streamlit CSV/document upload, charts, owned sessions and persisted preferences.
2. **EvidenceDesk:** document Q&A with Chroma, optional real Hugging Face embeddings, hybrid/MMR/multi-query/parent/extractive-compression/self-query retrieval and evidence evaluation.
3. **ReviewOps:** checkpointed human approval, authorized decisions, idempotent exports, audit records and FastAPI contracts.
4. **ResearchSwarm:** Send fan-out, reducer aggregation, analysis/write/review subgraphs, bounded revision and explicit unsuccessful exhaustion.
5. **ProtocolBridge:** real MCP stdio/HTTP tools over an allowlisted public PDF/CSV catalog; a small versioned A2A service/client and discovery exercise.
6. **TripWise ADK:** actual optional Google ADK agents with state, callbacks, sequential/parallel/loop composition, deterministic tools and A2A export.
7. **Foundation Studio:** prompts, LCEL branches/parallel operations, structured results, streaming and a Gradio conversation interface.

Use a uv-managed monorepo: reusable infrastructure lives in `src/portfolio`, each project has its own launch files, README, demo flow and architecture. Do not copy user course credentials, databases or notebooks into this repository. Live LLMs are configured through one `init_chat_model` factory; Gemini is the configured default. Demo responses and lexical embeddings must remain visibly labeled.

## Production contracts

- Derive identity from configured bearer credentials; never accept tenant/user authority from the model.
- Persist datasets, sessions/preferences, document provenance, checkpoints, approvals and idempotency records; restrict storage paths to server-created IDs.
- Validate upload type/size/rows/columns and generated operation schemas; never run arbitrary generated Python/SQL/shell.
- Train models in a bounded subprocess; fit preprocessing only on training folds; compare cross-validation scores and evaluate the selected model on a reserved test set.
- Bound model calls, retries, retrieval context, concurrency, request rate and file downloads. Scope caches and all queries by identity and version.
- Keep application failures distinguishable from successful outcomes, redact logs and expose real readiness checks.
- Supply a single-instance durable-volume deployment contract plus an explicitly separate PostgreSQL checkpoint option. Scaling requires shared business/object stores and a distributed job/admission backend; do not claim that a local SQLite image is horizontally scalable.

## Validation strategy before implementation

Use focused unit tests for settings/provider options, preprocessing and safe operations; temporary real SQLite/Chroma stores for ownership, restart and retrieval integration; FastAPI TestClient for authenticated request flows, denied decisions and idempotency; actual MCP stdio transport calls; deterministic LangGraph tests for routing/fan-out/checkpoints/interrupts. Use the real public CSV/PDF fixtures for demonstrations and provenance.

Run both regression and classification model comparisons. Exercise Streamlit through AppTest and a running browser when tooling permits. Run actual local Hugging Face embeddings if the model can be downloaded; record any download/service limitation. Construct provider adapters without making billable inference requests; live inference needs separately supplied keys. Container builds and hosted CI/cloud releases require the corresponding runtime; record whether they actually ran.

The final topic matrix must map the existing notes' objectives to implementation, a reproducible exercise, or an explicitly optional external integration. A documentation link alone does not mean the external integration ran. LinkedIn copy must accurately state the tested scope and avoid invented deployment, traffic or accuracy metrics.
