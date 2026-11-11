"""Map both supplied notes audits without claiming unimplemented integrations work."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUP_ROUTES = {
    "Environment": "07-foundation-studio", "Direct model": "07-foundation-studio",
    "Streamlit": "01-insightforge", "LangChain models": "07-foundation-studio",
    "Structured agent": "07-foundation-studio", "Tools, ReAct": "01-insightforge",
    "LangChain middleware": "03-reviewops", "Memory growth": "01-insightforge",
    "Retrieval": "02-evidencedesk", "Agent streaming": "07-foundation-studio",
    "Gmail": "03-reviewops", "MCP protocol": "05-protocolbridge",
    "LangGraph fundamentals": "04-researchswarm", "LangGraph summaries": "03-reviewops",
    "Parallel graphs": "04-researchswarm", "Supervisors": "01-insightforge",
    "LangChain support": "03-reviewops", "LangGraph support": "04-researchswarm",
    "ADK first": "06-tripwise-adk", "ADK state": "06-tripwise-adk",
    "ADK delegation": "06-tripwise-adk", "ADK YAML": "05-protocolbridge",
    "TripWise:": "06-tripwise-adk",
    "FastAPI material": "01-insightforge",  # gitleaks:allow -- Known public project-folder label.
    "Foundations": "07-foundation-studio", "Prompts": "07-foundation-studio",
    "Tools, middleware": "03-reviewops", "MCP and graph": "04-researchswarm",
    "Agent teams": "04-researchswarm", "ADK and remote": "05-protocolbridge",
    "API, tests": "01-insightforge", "Reliable": "01-insightforge", "Deployment": "01-insightforge",
}

# Source-level evidence; matching is conservative. Unmatched objectives retain an
# explicit practice status, even if an application demonstrates part of the idea.
EVIDENCE = [
    (("environment variables", "typed settings", "virtual environment", "uv init"), "src/portfolio/config.py"),
    (("init_chat_model", "temperature, and generation", "system, user, and assistant", "stateless calls"), "src/portfolio/models.py"),
    (("gradio chat", "gradio message"), "src/portfolio/gradio_app.py"),
    (("script reruns", "ui history versus", "conversation identities", "chat_input"), "src/portfolio/ui.py"),
    (("runnablelambda", "runnable branching", "passthrough assignment", "optional history placeholders", "prompttemplate versus"), "src/portfolio/labs.py"),
    (("temperature, top-k", "cosine calculation", "embedding vector dimensions"), "src/portfolio/labs.py"),
    (("toolmessage", "toolnode", "custom progress", "state snapshot", "message ids", "superstep visibility"), "src/portfolio/labs.py"),
    (("two sequential form questions", "historical branch", "snapshot values/next"), "src/portfolio/labs.py"),
    (("pydanticoutputparser", "turn an unstructured", "optional fields, constrained"), "src/portfolio/foundations.py"),
    (("humanintheloopmiddleware", "model wrappers", "model logging plus hitl", "human review through langchain"), "src/portfolio/foundations.py"),
    (("pdf loading", "recursive chunk", "chroma index", "semantic embeddings", "similarity search", "grounded prompting", "multi-query expansion", "contextual compression", "child-vector hits", "self-query structured", "trusted metadata filters", "conversational research", "rag ingestion"), "src/portfolio/retrieval.py"),
    (("supervisor structured", "trusted toolruntime", "main state, worker", "dataclass/dictionary", "trusted user identity"), "src/portfolio/insight.py"),
    (("short-term messages", "long-term store scope", "namespace/key/json", "business data, ui conversation", "physical durability"), "src/portfolio/storage.py"),
    (("persisted checkpoints, admin queue", "pending action rows", "interrupt payload", "avoid broad try/except", "replay from the node", "approval/rejection and actual effects"), "src/portfolio/review.py"),
    (("send creates", "independent fan-out", "parent and child state", "test a specialist", "independent branches", "bounded attempts", "generate/review/revise", "map/reduce dataflow"), "src/portfolio/research.py"),
    (("client session initialization", "fastmcp function", "resources, resource", "mcp discovery", "async construction, process/client", "noninteractive subprocess"), "src/portfolio/protocol.py"),
    (("agent service boundary", "agent cards, skills", "adk to_a2a", "client event types"), "src/portfolio/a2a_project.py"),
    (("root_agent export", "runner, sessionservice", "async event iteration", "baseagent _run_async_impl", "eventactions/state_delta", "instruction placeholders", "sequential/parallel/loop workflows", "parallelagent news", "loopagent response", "iteration counter event"), "src/portfolio/adk_project.py"),
    (("http service boundary", "get/post routes", "application credentials", "depends injection", "lifespan setup", "unauthorized request", "production request ordering", "rate limits, token quotas"), "src/portfolio/api.py"),
    (("closed/open/half-open", "exact ttl versus semantic caches"), "src/portfolio/reliability.py"),
    (("versioned datasets, named", "baselines and regression"), "src/portfolio/evaluation.py"),
    (("compatible container runtime", "ci-gated release"), "Dockerfile"),
]
EXTERNAL_TERMS = ("gmail", "oauth", "tavily", "azure deployment", "postgresql", "remotea2aagent", "mcpToolset", "litellm", "yaml", "render deployment")
BUSINESS_TERMS = ("fraud", "refund", "cancellation", "banking", "payment", "expense", "per diem", "approved vendors", "travel admin", "handbook's policy", "return/shipping", "source fragments", "contradictory seed", "three-check notebook", "four-check handout")


def classify(text):
    value = text.casefold()
    if any(word.casefold() in value for word in EXTERNAL_TERMS):
        return "External integration exercise", "docs/EXTENSION_LABS.md"
    if any(word in value for word in BUSINESS_TERMS):
        return "Course-domain extension", "docs/EXTENSION_LABS.md"
    for needles, path in EVIDENCE:
        if any(needle.casefold() in value for needle in needles):
            return "Implementation example", path
    return "Guided practice / partial pattern", "docs/EXTENSION_LABS.md"


def build(notes: Path):
    records = []
    for label, filename in (("original", "CONCEPT_COVERAGE.json"), ("supplemental", "SUPPLEMENTAL_CONCEPT_COVERAGE.json")):
        audit = json.loads((notes/filename).read_text(encoding="utf-8"))
        for group in audit["groups"]:
            project = next((slug for prefix, slug in GROUP_ROUTES.items() if group["title"].startswith(prefix)), "07-foundation-studio")
            for concept in group["concepts"]:
                status, evidence = classify(concept["concept"])
                if not (ROOT/evidence).is_file():
                    raise FileNotFoundError(evidence)
                records.append({"id": f"{label}-{len(records)+1:03}", "source_audit": filename,
                    "group": group["title"], "concept": concept["concept"], "notes_sections": concept.get("sections", []),
                    "project": project, "status": status, "example_or_exercise": evidence,
                    "completion_rule": "Explain this objective, run the linked example where implemented, and complete any remaining extension before claiming full feature coverage"})
    counts = dict(Counter(row["status"] for row in records))
    output = {"source": "Two user-supplied full-course notes audits", "objectives": len(records),
              "status_counts": counts, "interpretation": "Every objective is accounted for; this is not a claim that every course-specific application/integration is implemented", "items": records}
    (ROOT/"docs"/"concept-coverage.json").write_text(json.dumps(output, indent=2), encoding="utf-8")
    lines = ["# Course concept coverage — all original and supplemental objectives", "",
        f"The two supplied notes audits contain **{len(records)} objectives**. Every objective appears below in prerequisite-family order. Duplicated course files were already consolidated by those audits.", "",
        "**Accounted for does not mean fully implemented.** An implementation example demonstrates the named pattern; composite objectives can still include additional course variants. External integrations and course-domain workflows are explicitly exercises. Read the original notes for the full explanation; these projects provide runnable practice and honest feature boundaries.", "",
        "| Status | Objectives |", "|---|---:|", *[f"| {key} | {value} |" for key, value in counts.items()], "",
        "[Learning path](LEARNING_PATH.md) · [Extension exercises](EXTENSION_LABS.md) · [Machine-readable matrix](concept-coverage.json)", ""]
    last = None
    for row in records:
        family = (row["source_audit"], row["group"])
        if family != last:
            lines += [f"## {row['group']}", "", "| Objective / notes section | Project | Evidence / status |", "|---|---|---|"]
            last = family
        text = row["concept"].replace("|", "\\|")
        sections = ", ".join(row["notes_sections"])
        lines.append(f"| {text} ({sections}) | [{row['project']}](../projects/{row['project']}/README.md) | [{row['status']}](../{row['example_or_exercise']}) |")
        next_index = records.index(row)+1
        if next_index == len(records) or records[next_index]["group"] != row["group"]:
            lines.append("")
    (ROOT/"docs"/"CONCEPT_COVERAGE.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    return {"objectives": len(records), "status_counts": counts}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--notes", type=Path, default=ROOT.parent/"feb-2026-batch-labdocs"/"full-course-notes")
    print(json.dumps(build(parser.parse_args().notes), indent=2))
