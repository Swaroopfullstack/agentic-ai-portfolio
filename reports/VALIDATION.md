# Validation evidence — 2026-11-11

## Executed environment

Windows, CPython 3.13.6, uv 0.13.5. The suite was installed from the frozen lockfile into a new `.venv-verify` with **system site packages disabled**. The clean install used the ADK and Gradio extras; actual Hugging Face validation used the embeddings extra in the primary environment. Python 3.11–3.13 are declared in the project range; the local run exercised 3.13. After publication, the hosted Ubuntu [verification workflow](https://github.com/Swaroopfullstack/agentic-ai-portfolio/actions/runs/43005050770) and [secret-scanning workflow](https://github.com/Swaroopfullstack/agentic-ai-portfolio/actions/runs/43005050464) both completed successfully.

Key tested versions: LangChain 1.4.10, LangGraph 1.2.20, Chroma 1.5.9, FastAPI 0.162.4, scikit-learn 1.9.1, MCP 1.30.0, Google ADK 2.14.0 and A2A SDK 1.3.0. The lockfile records all dependencies.

## Results

| Check | Actual result | Evidence |
|---|---|---|
| Entire suite in clean environment | **46 passed, 1 skipped**, 163.71 s | [JUnit](test-results.xml) |
| Optional real Hugging Face + Chroma integration | **1 passed**, 61.68 s | [JUnit](embedding-tests.xml), [model result](embedding-validation.json) |
| Focused SSE graph streaming after context fix | **1 passed**; also included in final full suite | [JUnit](streaming-tests.xml) |
| Ruff over source, tests, scripts and project launchers | All checks passed | `uv run ruff check src tests scripts projects` |
| Editor diagnostics | No errors found | Workspace Problems check |
| Hosted GitHub Actions | Verification and secret scanning both passed on initial publication | Workflow links above |
| Public data acquisition | NIST PDF + UCI Iris downloaded; diabetes exported from sklearn | [Provenance](../assets/public/PROVENANCE.json) |
| Real browser demo | Uploaded public fixtures, routed requests, retained preference, trained classifier comparison and rendered/download controls | [Actual screenshot](insightforge-demo.png) |

The one skip in the clean full run is the opt-in Hugging Face test: that clean installation intentionally omitted the large embeddings extra. It was run separately with cached real weights and passed. Taken together, the **47 distinct tests passed across the two environments**; the optional test is not reported as an executed pass in the clean-environment run.

The full suite command was:

```powershell
& '.venv-verify/Scripts/python.exe' -B -X utf8 -m pytest tests -q --junitxml=reports/test-results.xml
```

The explicit embedding run was:

```powershell
$env:HF_HUB_OFFLINE='1'
$env:RUN_EMBEDDING_TESTS='1'
& '.venv/Scripts/python.exe' -B -X utf8 -m pytest tests/test_embeddings.py -q --junitxml=reports/embedding-tests.xml
```

Weights were downloaded in an earlier successful actual-model run. The final test uses `embedding_local_only=true` to avoid Hub metadata lookups while validating real inference. Its 384-dimensional embedding query ranked `animals.txt` first for “An animal enjoys outdoor play”, with cosine similarity approximately 0.5953. This small example validates wiring, not broad semantic quality.

## What the tests actually exercise

- Real LangGraph supervisor routing and persisted state; safe calculation; data operations; durable preferences and owned history.
- Actual SQLite and Chroma ingestion, reopening, metadata/source provenance, tenant/user isolation, seven retrieval strategies, no-answer behavior and scoped caching.
- Both bounded ML child-process workflows, actual five-classifier/six-regressor comparison, baseline and held-out metric reporting, and timeout failure handling.
- HTTP authentication, forbidden roles, rejected authority fields, cross-owner denial, upload/profile/chat operations, review version/idempotency rules and restart recovery of a pending interrupt.
- Real LangChain middleware and native human-review pause/resume. Approval/rejection produce distinct actual effects.
- Real MCP stdio subprocess/session discovery, tools/resources, public PDF page parsing/search, invalid source rejection, agent schema adapter, and authenticated Streamable HTTP initialization. Host/origin protection remains enabled.
- Real ADK Runner/events/tools/parallel-writing-review workflows with labeled fixture inference and durable database sessions across runs.
- Real A2A card discovery and official SDK JSON-RPC messages against the ASGI service, authenticated access and completed task evidence. This is not a simulated HTTP-shaped dictionary exchange.
- Actual Uvicorn socket + Streamlit AppTest chat/project selection; Gradio interface/fixture streaming; actual LCEL batch/async execution, custom progress, ToolNode observation IDs, read-only SQL denial and sequential interrupt ordering.
- Actual Gemini/OpenAI/Anthropic SDK adapter construction with dummy credentials and no network inference; validation of incompatible provider settings and model/token reservation bounds.

## Public experiments

Run `uv run portfolio evaluate` to recreate [public-evaluation.json](public-evaluation.json). The recorded experiment used demo answer/routing fixtures and **hashing** retrieval embeddings, not hosted inference or HF semantic retrieval.

| Experiment | Recorded outcome |
|---|---|
| NIST PDF | 48 text pages, 164 chunks |
| Three retrieval smoke questions, k=4 | Expected-term recall 1.0 in each retrieved context |
| Iris classifier winner | Logistic Regression; held-out accuracy/F1 ≈ 0.9333 on 30 test rows |
| Diabetes regressor winner | Ridge; held-out R² ≈ 0.4541, MAE ≈ 42.812, RMSE ≈ 53.777 on 89 test rows |

Model selection uses three-fold cross-validation on training data. Dummy baselines and all candidate validation results are in the JSON. A fixed random seed enables reproduction. These are small educational experiments: expected-term recall is not expert relevance/faithfulness measurement, a random split does not resolve entity/time/semantic leakage, and the reported ML numbers are not product-performance promises.

## Defects found and corrected during validation

The public PDF exposed a Windows subprocess encoding problem; parsing now uses explicit UTF-8. Clean ADK setup exposed the SQLAlchemy asyncio extra requirement; it is declared and locked. Explicit Chroma client ownership/close fixed Windows file-lock cleanup. MCP HTTP tests use an allowed local Host rather than disabling DNS-rebinding checks. SSE iteration exposed ContextVar tokens crossing copied thread contexts; each advance now binds/resets context before yielding, and the focused and final full tests pass.

## Limits and remaining release checks

- **No hosted LLM inference was executed.** Actual model credentials, entitlement, tool-call behavior, structured-output behavior and sampling compatibility require a controlled live run for each enabled model. The app never silently falls back from live failure to demo.
- **No Docker build, cloud deployment, load test or backup/restore drill was executed.** Docker was unavailable locally. Hosted CI subsequently passed after GitHub publication. Use the [deployment contract](../docs/DEPLOYMENT.md) before a real release.
- The supported app shape is one API instance/worker with durable local storage. This is not horizontal scale or high availability certification.
- ADK emits six deprecation warnings for the course's SequentialAgent/ParallelAgent/LoopAgent patterns in the locked 2.14 SDK. Their actual workflows pass; migration to the newer Workflow API requires deliberate future work.
- Course-specific Gmail OAuth, enterprise support/refund/booking/expense workflows, RemoteA2aAgent proxy, ADK MCPToolset/YAML, PostgreSQL deployment and tracing exporters are explicitly marked exercises/extensions in the [281-objective matrix](../docs/CONCEPT_COVERAGE.md). Installed packages or documentation do not count as successful external integrations.

## Reproduction order

Follow [the root quickstart](../README.md), run the full tests, run the optional embeddings test after installing/warming that model, then run the public evaluation. For a live release, configure production credentials/settings and execute the environment-specific checks documented above. Keep each release's lockfile, test report and experiment data together.

## Publication and credential checks

Published [portfolio repository](https://github.com/Swaroopfullstack/agentic-ai-portfolio). The initial 99-file remote Git tree was fetched and compared with the local scanned tree: they matched exactly. Gitleaks 8.30.1 checked staged files and committed history with no credential findings. One reviewed false positive for a literal project-folder label has an explicit inline annotation in the course-map script. The hosted secret scan passed too.

Only blank/placeholder environment templates are tracked. Private environment files, runtime databases/uploads, virtual environments and key/token files are ignored. Machine hostnames were removed from public JUnit metadata. Actual passwords, provider keys and stored GitHub credentials were not changed by this publication. See [private environment setup](../docs/ENV_SETUP.md).
