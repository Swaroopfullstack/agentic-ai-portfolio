# Showcase the work with evidence

## Four-minute demo recording

1. **0:00–0:25** Show the architecture and labeled runtime mode. Say whether the recording uses actual hosted inference or offline routing fixtures.
2. **0:25–1:10** Upload Iris, inspect its profile, ask for a chart, train the classifier comparison and explain CV versus the held-out test.
3. **1:10–1:50** Ask a NIST PDF question, show the exact page/chunk evidence, compare a second retrieval strategy and ask an unsupported question.
4. **1:50–2:20** Remember a preference, continue a session, then demonstrate that Bob cannot see Alice's private uploaded evidence.
5. **2:20–3:00** Submit an export, switch to a reviewer, approve it and download the real artifact. Show that rejection creates no artifact.
6. **3:00–3:30** Run MCP discovery/PDF loading and show the A2A agent card/message result.
7. **3:30–4:00** Show tests, fixture-specific evaluation and one limitation you would address for a larger deployment.

Use screenshots of actual runs. Never add client names, real users, invented traffic, uptime, savings or employment history to a portfolio demonstration.

## Suggested LinkedIn post

> I built InsightForge, a multi-agent data-analysis assistant using LangGraph, LangChain, FastAPI and Streamlit.
>
> A supervisor routes requests to Data, RAG, ML, Tools and Memory specialists. Users can upload CSVs/PDFs, compare tabular ML models, inspect cited document evidence and retain session history/preferences.
>
> I also built focused companion projects for advanced retrieval, persisted human review, parallel research, MCP/A2A interoperability, Google ADK workflows and LangChain foundations.
>
> Gemini is the configurable default through init_chat_model; provider/model, sampling settings and retrieval counts are centralized. Public fixtures include NIST AI RMF, Iris and diabetes, with provenance.
>
> Engineering work includes owner isolation, reviewer authorization, idempotent exports, persisted checkpoints, bounded training, provider failure controls, and integration tests. My repository distinguishes verified local behavior from live-provider and deployment checks.
>
> Repository: ADD_YOUR_GITHUB_LINK
> Demo: ADD_YOUR_RECORDING_LINK
>
> #AgenticAI #LangGraph #LangChain #FastAPI #Python #MachineLearning

Replace the placeholders only after publishing your repository/video. If the demo runs offline, state that plainly in the post or recording. Add real test counts and metrics from the release's validation report instead of copying numbers that may go stale.

## Resume / project bullets

- Designed a LangGraph supervisor routing validated requests to Data, RAG, ML, Tools and Memory specialists, with trusted runtime identity and persistent session state.
- Built a document Q&A pipeline using LangChain, Chroma and configurable Hugging Face embeddings, with page provenance, hybrid/MMR retrieval and citation validation.
- Implemented bounded automatic target/problem inference and sklearn model comparison with training-only cross-validation, a baseline and separate held-out winner evaluation.
- Added SQLite-backed conversation/preferences, checkpointed human review and a role-authorized idempotent export transaction tested across restart.
- Developed a Streamlit interface and authenticated FastAPI service with typed validation, rate/concurrency controls and reproducible uv configuration; implemented real MCP and A2A interoperability examples.

Describe these as **portfolio/project experience** unless they were actually part of your employment. The tabular models are trained and evaluated locally; this suite does not claim a deployed model-serving endpoint. Production readiness depends on the deployment checks documented in the repository.

## Interview questions to prepare

Why a supervisor instead of a single tool-calling agent? How are private documents filtered? Why is a model's route not authority? What can go wrong with random train/test splits? How do review transactions survive graph replay? Why are generation top-k and retrieval k different? What changes for multiple replicas? Which tests run without credentials, and which checks need real services?
