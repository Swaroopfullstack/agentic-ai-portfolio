# Learn, build, explain, then demonstrate

Follow this sequence. Run code before adding complexity; keep a screenshot/result and explain one failure case for every stage.

## 1. Python environment and provider boundaries

Read [configuration](CONFIGURATION.md), inspect [config.py](../src/portfolio/config.py) and [models.py](../src/portfolio/models.py), then run `uv run portfolio doctor`. Explain why `.env` is private, why a provider key differs from an application login, and why client configuration can succeed before any inference. Try an invalid generation top-k with OpenAI and an unallowlisted model through the API. Both must fail.

## 2. Foundation Studio

Run [Project 07](../projects/07-foundation-studio/README.md) first. Follow prompt variables → messages → runnable transforms → parser/schema → model stream. Compare a schema-valid answer with a factually supported answer. Run the middleware fixture twice, approving and rejecting; observe actual tool-effect counts, not just the final sentence.

## 3. Data and ML fundamentals

Run [InsightForge](../projects/01-insightforge/README.md) with the Iris CSV. Read the summary and missing values. Identify the feature columns and target before training. Train all classifiers, then use diabetes for regression. Explain why CV selects the model, why the held-out test does not select it, and why a high score on one educational dataset is not a business guarantee. Override the target and explain the implications.

## 4. Evidence-grounded answers

Run [EvidenceDesk](../projects/02-evidencedesk/README.md) with the NIST PDF. Inspect the PDF page, child text and parent page. Compare vector, MMR and hybrid results. Increase retrieval k separately from generation sampling k. Test an unrelated question. Switch from the offline lexical backend to real HF embeddings and re-index; compare the evidence, not only how fluent the answer sounds.

## 5. Stateful orchestration and trust

Trace [InsightForge's graph](../src/portfolio/insight.py). Explain trusted runtime context, partial updates, message reducers, thread IDs, SQLite checkpoints and preference namespaces. Create two sessions and two users. Verify that memory continuity is intentional while private uploaded evidence never crosses user boundaries.

## 6. Human review

Complete [ReviewOps](../projects/03-reviewops/README.md). Submit an export as Alice, restart the backend, approve as the reviewer, and return as Alice to download. Try to approve as an analyst, submit stale versions, and reuse an idempotency key with different content. Explain the transaction and why a resumed graph is not permission to execute a new action.

## 7. Parallel research teams

Run [ResearchSwarm](../projects/04-researchswarm/README.md). Identify planner, per-query Send input, accumulating findings, deduplication and parent/child contracts. Run once with relevant documents and once with none. An exhausted review loop must remain an explicit failure/insufficient-evidence outcome.

## 8. Protocol boundaries

Run [ProtocolBridge](../projects/05-protocolbridge/README.md): initialize, discover, read a resource, call tools, then adapt tools into an agent. Try an arbitrary path as a source ID. Start the HTTP service and verify that missing credentials are denied. Discover the A2A card and send a message through the real SDK. Explain why a card's advertised security metadata alone cannot enforce authorization, and why an event queue is not a durable job queue.

## 9. ADK orchestration

Run [TripWise](../projects/06-tripwise-adk/README.md). Follow counter event → parallel specialists → writer → critic loop. Resume the same durable session, observe the increment, and contrast this with the default lifetime of an in-memory service. Identify where a model callback runs and where the tool validates the actual operation. The estimate tool is a teaching fixture, never a flight search or a purchase.

## 10. API, Git, deployment and evidence

Practice [Git](GIT_WORKFLOW.md) and [deployment](DEPLOYMENT.md). Run tests, inspect fixture-specific [evaluation](../reports/public-evaluation.json), then record the [showcase demo](LINKEDIN_SHOWCASE.md). Keep feature claims aligned to executable evidence. Review the [complete concept matrix](CONCEPT_COVERAGE.md), including credential-dependent integrations and course-specific business rules that remain extensions.

## Independent completion criteria

You can explain a request from authentication to result without reading a script; modify one specialist; add a meaningful failure test; switch the provider using configuration; explain a retrieval miss; recover a pending approval after restart; and describe the single-instance storage limit. Completing tutorials is useful preparation, while senior-role readiness also requires owning real incidents, product decisions, costs, security and deployment tradeoffs.
