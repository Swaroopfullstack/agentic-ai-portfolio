# Remaining course concepts: explicit practice and integration exercises

The suite implements the requested multi-agent analysis product and seven complementary workflows. The full notes also contain alternative frameworks, external services and specific support/travel/banking policies. Those are not silently counted as delivered product features. Use this guide with the per-objective [matrix](CONCEPT_COVERAGE.md). An exercise means additional work is required before claiming that feature in a portfolio.

## A. Provider SDKs, structured strategies and model limits

Trace the actual adapter's raw AIMessage and usage metadata in a controlled live run. Compare direct Google GenAI/OpenAI SDK calls with the LangChain boundary. Keep a token/cost experiment separate from model training: these apps perform inference against hosted language models, while the ML agent trains tabular sklearn models locally.

Practice `ToolStrategy` versus `ProviderStrategy` using a provider/model you have verified supports the feature. Assert `structured_response` separately from conversational messages. Test malformed JSON, missing fields, invalid bounds and a schema-valid false answer. For Azure, add explicit resource endpoint/deployment/API-version settings and a deployment-specific test; changing only a generic model string is insufficient.

## B. Tool execution, SQL and error observations

The [labs](../src/portfolio/labs.py) run actual ToolNode execution and emit a matching observation ID. Extend this with two independent calls and one dependent call; verify observations are attached to the right proposals. Add `wrap_tool_call` that returns a ToolMessage with the original ID on a known recoverable failure. Avoid converting an authorization denial into a successful observation.

The SQL lab uses an owned snapshot plus SQLite's authorizer and progress limits. A natural-language SQL product also needs schema inspection, query checking, allowlisted schemas/views, per-user data filtering enforced independently of generated SQL, least-privilege credentials and bounded rows/time. Do not expose the business database through a general administrator SQL toolkit. Parameterize values; table/column identifiers need allowlists.

Weather/Tavily/search adapters require credentials or verified public endpoints. Add typed input, request timeout, safe URL handling, bounded output and source attribution. Treat retrieved pages as untrusted content. Filesystem/glob/grep tools require a fixed allowed root with resolved-path checks. Shell execution needs a separate sandbox and explicit policy; the main assistant deliberately has no general shell/Python execution tool.

## C. Memory compaction and guardrails

Compare buffer, fixed window, token trim, generated summary and hybrid recent-history/summary strategies on the same conversation. The labs demonstrate trim; InsightForge bounds message state and stores durable preferences. Add real SummarizationMiddleware or a conditional graph summary node, preserve tool-call/result pairing, and test a detail that can be lost in compression. Checkpoint persistence does not create semantic long-term knowledge automatically.

Try redact/mask/hash/block policies for input, model output and tool observations. The implemented regex redaction is heuristic and narrow. Create false-positive and false-negative examples. A keyword banking screen is not transaction authorization. Enforce account ownership, amount limits, sufficient funds and idempotency at the transactional tool boundary.

## D. Gmail OAuth and sensitive actions

Create your own cloud project, enable Gmail API, configure consent/scopes and a desktop OAuth client. Store refresh/access tokens privately and request the smallest scopes. First implement a read-only message query. Sending requires binding a human-reviewed immutable recipient/subject/body to the actual outgoing API call, an outbox/delivery record, duplicate protection and failure recovery. A model saying “sent” is not delivery evidence. This repository performs no Gmail operations and stores no OAuth tokens.

ReviewOps teaches the permission/transaction/replay pattern with a concrete local export. Add edit/reject/request-information variants with argument revalidation and versioned fingerprints before adapting it to email, refunds or cancellation.

## E. Graph inspection, replay and dynamic workflows

Run the labs' state history, historical branch, sequential interrupts, tools/custom streams and Mermaid output. Add typed input/output/private graph channels, then demonstrate why hidden output fields do not protect a trace. Compare `updates`, `values`, model `messages` chunks and custom progress: token display cannot stand in for tool completion or review approval.

Implement a fraud-check child graph on a versioned synthetic transaction dataset: tag frequency/value/reason/timing checks, bound each score, explicitly define weights and join before aggregation. The original course contains distinct three-check and four-check variants; do not merge contradictory rules without choosing a canonical specification. Compare a child graph node versus a tool-invoked child and test state mapping independently.

## F. Support application business rules

The course support capstones include customer/admin identity, orders, joins/seeds, cancellation, return eligibility, policy versions, pending approval, nested fraud and notifications. These are a distinct product from a data-analysis assistant. Reuse the suite's identity, persisted review and subgraph patterns, but first write canonical rules and seed expectations. Test unauthorized access, stale decisions, duplicate execution, approved/rejected outcomes and restart recovery. A refund row is not proof that money moved; a notification row is not proof that email arrived.

## G. ADK scopes, declarative agents and MCP

The TripWise project runs actual callbacks/workflows/counters and durable sessions. Extend state experiments with session keys, `user:` preferences, `app:` shared state and invocation-only `temp:` keys. Verify scope with two users, two sessions and a process restart. Compare AgentTool return-to-caller with explicit agent transfer. Declare input/output schemas and verify they actually gate input/output; defining an unused model changes no runtime behavior.

Build an ADK YAML agent and a prime-checking imported function. Then add an MCPToolset with explicit stdio/HTTP connection parameters, a tool-name allowlist and scoped cleanup. Do not assume the manually implemented LangChain MCP adapter also validates ADK's MCPToolset integration. The latter requires its own integration test. Compare newer ADK Workflow composition with the course's deprecated Sequential/Parallel/Loop classes on the locked SDK.

## H. Enterprise TripWise extensions

Employee/trip/approval/booking/expense/notification records, date validation, canonical destination/vendor/per-diem policies, four-stage planning, policy specialists, manager budget decisions, artifact versions and expense arithmetic are course-specific business features. Define their ownership and policy versions before building them. Keep annual and per-trip budget meanings separate. Unsupported cities must fail explicitly; educational quote fixtures cannot be described as live flight/hotel availability.

Use ReviewOps as the review transaction pattern, then implement separate booking/notification adapters, immutable operation IDs and reconciliation for external outcomes. Add a genuine manager/admin panel with role checks. A2A adapters cannot guarantee inventory consistency across independent booking services; require reservation/expiry/version rules at the service boundary. Local artifacts/session data need durable storage and matching trip IDs before restart claims.

## I. A2A task operations and remote registries

ProtocolBridge executes actual card discovery and SDK messages with durable tasks. Extend it with a cooperative long-running executor, cancellation, status/artifact event sequencing, reconnect/retry and task recovery. An SDK EventQueue is an event transport, not a persistent work scheduler. Map authenticated principals to private task ownership before exposing nonpublic data. Test RemoteA2aAgent as a separate proxy integration rather than assuming the direct SDK client covers it. Allowlist remote HTTPS origins and validate discovered endpoints before sending secrets.

## J. Reliability, tracing, evaluation and deployment

Exercise breaker closed/open/half-open transitions and one-probe behavior, timeout/retry composition, exact TTL cache invalidation and authorization-separated keys. Add in-flight deduplication and semantic caching only after measuring their effects; the supplied cache is exact. Reserve full-context/input/output budgets, reconcile actual provider usage separately and use current prices when producing dollar reports.

For judge-based evaluations, use expert labels, calibration slices, unsupported/no-answer cases, bounded scores and failure modes. A judge's numeric score is not a factual guarantee. Add hosted trace export only with safe metadata/redaction and access controls. Validate containers, Render or another host's PORT/persistent disk semantics, CI promotion, rollback and restore in your deployment. The repository contains runnable local evidence and Docker/CI definitions; external infrastructure checks are explicitly separate release work.

## How to close an extension

Write a concrete feature requirement; implement it behind a bounded, authenticated interface; add a meaningful success/failure/restart test; run it against the relevant actual service in a controlled environment; record versions, results and limits; then update that matrix row. A renamed README or an installed package alone does not close an integration objective.
