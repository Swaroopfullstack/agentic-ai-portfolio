"""Export seven self-contained showcase repos from tracked, credential-scanned sources.

The shared package is vendored so no sibling checkout or private dependency is needed.
Destinations must be new directories; this script never deletes or replaces a repo.
"""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess


SOURCE = Path(__file__).resolve().parents[1]
OUTPUT = SOURCE.parent / "standalone-projects"
OWNER = "Swaroopfullstack"
PROJECTS = [
    ("01-insightforge", "InsightForge", "insightforge-multi-agent-analytics", "insight",
     "LangGraph supervisor with Data, RAG, ML, Tools and Memory agents; CSV/PDF analysis, model comparison and durable sessions.",
     "insight.py", "Supervisor → Data / RAG / ML / Tools / Memory"),
    ("02-evidencedesk", "EvidenceDesk", "evidencedesk-agentic-rag", "evidence",
     "Document Q&A with LangChain, Chroma, Hugging Face embeddings, seven retrieval strategies and inspectable page citations.",
     "retrieval.py", "PDF → Pages → Chunks → Embeddings → Chroma → Retrieval → Cited answer"),
    ("03-reviewops", "ReviewOps", "reviewops-human-in-the-loop", "review",
     "Durable LangGraph human review: authenticated reviewer decisions, version checks, audit history and idempotent report exports.",
     "review.py", "Proposal → Persisted interrupt → Reviewer → Approve or reject → Immutable export"),
    ("04-researchswarm", "ResearchSwarm", "researchswarm-langgraph-agents", "research",
     "Evidence-grounded research team using LangGraph Send fan-out, reducers and a bounded writer/critic subgraph.",
     "research.py", "Planner → Parallel researchers → Evidence reducer → Writer / critic → Bounded outcome"),
    ("05-protocolbridge", "ProtocolBridge", "protocolbridge-mcp-a2a", "mcp",
     "Real MCP tools/resources and A2A agent discovery over public CSV/PDF data, with stdio and authenticated HTTP transports.",
     "protocol.py", "MCP client → Catalog tools / resources → Public CSV and PDF; A2A client → Evidence agent"),
    ("06-tripwise-adk", "TripWise ADK", "tripwise-google-adk", "adk",
     "Google ADK travel workflow with parallel specialists, tools, callbacks, bounded review and durable SQLite sessions.",
     "adk_project.py", "Runner → Session state → Parallel specialists → Writer → Bounded review"),
    ("07-foundation-studio", "Foundation Studio", "foundation-studio-langchain", "foundation",
     "Runnable LangChain foundations: LCEL, prompts, structured output, streaming, middleware, tool review and checkpoint labs.",
     "foundations.py", "Prompt → Runnable composition → Structured result → Streaming / Reviewed tool"),
]


def write(root: Path, relative: str, content: str):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def export():
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=SOURCE).decode().split("\0")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=SOURCE, text=True).strip()
    common_roots = {"pyproject.toml", "uv.lock", ".gitignore", ".gitattributes", ".dockerignore",
                    ".env.example", ".env.gemini.example", ".env.production.example"}
    common_docs = {"CONFIGURATION.md", "DEPLOYMENT.md", "ENV_SETUP.md", "API_EXAMPLES.md", "GIT_WORKFLOW.md"}
    selected = [name for name in tracked if name and (name in common_roots
        or name.startswith(("src/portfolio/", "tests/", "assets/public/", ".github/workflows/", ".streamlit/"))
        or (name.startswith("docs/") and Path(name).name in common_docs))]
    manifests = []
    for folder, title, slug, command, description, module, flow in PROJECTS:
        root = OUTPUT / slug
        if root.exists():
            raise FileExistsError(f"Refusing to overwrite existing repository: {root}")
        root.mkdir(parents=True)
        for name in selected:
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / name, target)

        # Keep the exact dependency resolution; only the local editable package is renamed.
        for name in ("pyproject.toml", "uv.lock"):
            content = (root / name).read_text(encoding="utf-8")
            content = content.replace('name = "agentic-ai-portfolio"', f'name = "{slug}"')
            if name == "pyproject.toml":
                content = content.replace("Seven runnable AI engineering portfolio projects with shared, configurable infrastructure", description)
                content = content.replace('[project.scripts]\n', '[project.scripts]\n' + f'{slug} = "portfolio.cli:main"\n')
            write(root, name, content)

        ui = (root / "src/portfolio/ui.py").read_text(encoding="utf-8")
        original = 'PROJECTS = ["InsightForge", "EvidenceDesk", "ReviewOps", "ResearchSwarm", "ProtocolBridge", "TripWise ADK", "Foundation Studio"]'
        assert original in ui
        ui = ui.replace(original, f'PROJECTS = [{title!r}]')
        ui = ui.replace('def run(project="InsightForge"):', f'def run(project={title!r}):')
        ui = ui.replace('selected_project = st.sidebar.selectbox("Project", PROJECTS, index=PROJECTS.index(project))',
                        'selected_project = project\n    st.sidebar.caption(project)')
        ui = ui.replace('projects/06-tripwise-adk/agents', 'agents')
        write(root, "src/portfolio/ui.py", ui)
        api = (root / "src/portfolio/api.py").read_text(encoding="utf-8")
        write(root, "src/portfolio/api.py", api.replace('title="AI Engineering Portfolio API"', f'title="{title} API"'))
        write(root, "app.py", f'"""Launch the dedicated {title} interface."""\nfrom portfolio.ui import run\n\nrun({title!r})')
        write(root, "demo.py", f'"""Run the {title} workflow. Demo mode needs no API key."""\nfrom portfolio.cli import demo, emit\n\nif __name__ == "__main__":\n    emit(demo({command!r}))')
        if command == "adk":
            shutil.copytree(SOURCE / "projects" / folder / "agents", root / "agents", ignore=shutil.ignore_patterns("__pycache__"))
        if command == "mcp":
            shutil.copyfile(SOURCE / "projects" / folder / "server.py", root / "server.py")
        if command == "foundation":
            shutil.copyfile(SOURCE / "projects" / folder / "gradio_app.py", root / "gradio_app.py")

        guide = (SOURCE / "projects" / folder / "README.md").read_text(encoding="utf-8")
        guide = "# " + title + " walkthrough\n\n" + guide[guide.index("## What to demonstrate"):]
        guide = guide.replace("../../", "../").replace("projects/06-tripwise-adk/agents", "agents")
        guide = guide.replace("See the complete concept matrix for explicit extension status.",
                              "The original course coverage matrix is in the linked portfolio hub.")
        write(root, "docs/WALKTHROUGH.md", guide)
        for name in common_docs:
            content = (root / "docs" / name).read_text(encoding="utf-8")
            content = content.replace("projects/01-insightforge/app.py", "app.py")
            content = content.replace("projects/06-tripwise-adk/agents", "agents")
            content = content.replace("uv run portfolio demo insight", f"uv run portfolio demo {command}")
            write(root, "docs/" + name, content)

        tests = (root / "tests/test_labs_ui.py").read_text(encoding="utf-8")
        tests = tests.replace('ROOT/"projects/01-insightforge/app.py"', 'ROOT/"app.py"')
        start = tests.index('        assert app.title[0].value == "InsightForge"')
        end = tests.index('    finally:', start)
        dedicated = f'        assert app.title[0].value == {title!r}\n        assert not app.error\n        assert all(item.label != "Project" for item in app.sidebar.selectbox)\n'
        if command == "insight":
            dedicated += '        app.chat_input[0].set_value("calculate 12 * (3 + 4)").run(timeout=60)\n        assert not app.exception and not app.error\n        assert any("84" in item.value for item in app.markdown)\n'
        tests = tests[:start] + dedicated + tests[end:]
        write(root, "tests/test_labs_ui.py", tests)
        write(root, "tests/test_standalone.py", '''"""Assert the installed runtime and fixtures belong to this checkout."""
import json
from pathlib import Path

import portfolio
from portfolio.config import ROOT
from portfolio.public_data import public_file
from portfolio.ui import PROJECTS


def test_checkout_is_self_contained():
    manifest = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))
    assert Path(portfolio.__file__).resolve().is_relative_to(ROOT)
    assert PROJECTS == [manifest["title"]]
    assert (ROOT / "app.py").is_file() and (ROOT / "demo.py").is_file()
    assert not (ROOT / "projects").exists()
    assert public_file("nist_ai_rmf").is_relative_to(ROOT)
    assert public_file("uci_iris").is_file()
''')

        docker = (SOURCE / "Dockerfile").read_text(encoding="utf-8")
        docker = docker.replace("COPY projects ./projects", "COPY app.py demo.py ./")
        docker = docker.replace("COPY assets ./assets", "COPY assets ./assets\nCOPY .streamlit ./.streamlit")
        if command == "adk":
            docker = docker.replace("COPY app.py demo.py ./", "COPY app.py demo.py ./\nCOPY agents ./agents")
        write(root, "Dockerfile", docker)
        compose = (SOURCE / "compose.yaml").read_text(encoding="utf-8")
        write(root, "compose.yaml", compose.replace("projects/01-insightforge/app.py", "app.py"))
        ci = (root / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        ci = ci.replace("name: Verify portfolio", "name: Verify " + title)
        ci = ci.replace("ruff check src tests", "ruff check src tests app.py demo.py")
        write(root, ".github/workflows/ci.yml", ci)
        extras = " --extra adk --extra gradio"
        specific = {
            "mcp": "\n### Protocol servers\n\n```powershell\nuv run portfolio mcp --transport stdio\n# For HTTP and A2A, set your private MCP_HTTP_TOKEN (24+ random characters).\nuv run portfolio mcp --transport http\nuv run --extra adk portfolio a2a\n```\n\nThe [walkthrough](docs/WALKTHROUGH.md) includes the real client commands and authentication requirements.\n",
            "adk": "\n### ADK developer UI and durable CLI\n\n```powershell\nuv run --extra adk adk web agents --port 8011\nuv run --extra adk portfolio adk --question \"Plan three days in Lisbon\"\n# Copy the returned session ID to continue the same durable CLI session.\nuv run --extra adk portfolio adk --session YOUR_SESSION_ID --question \"Review the assumptions\"\n```\n",
            "foundation": "\n### Gradio and executable labs\n\n```powershell\nuv run --extra gradio python gradio_app.py\nuv run python -m portfolio.labs\n```\n",
        }.get(command, "")
        repo_url = f"https://github.com/{OWNER}/{slug}"
        readme = f'''# {title}

**{description}**

[![Tests]({repo_url}/actions/workflows/ci.yml/badge.svg)]({repo_url}/actions/workflows/ci.yml)
[![Secret scan]({repo_url}/actions/workflows/secrets.yml/badge.svg)]({repo_url}/actions/workflows/secrets.yml)

Python · uv · Gemini via LangChain `init_chat_model` · FastAPI · Streamlit · SQLite

## What this project demonstrates

{flow}

Explore the [step-by-step demonstration](docs/WALKTHROUGH.md) and the [main implementation](src/portfolio/{module}). This repository contains its own source code, public fixtures, dependency lock, API, dedicated UI, tests and container configuration. Clone this repository by itself to run it.

## Quick start

Use Python 3.11–3.13 and uv. Run from this repository root:

```powershell
git clone {repo_url}.git
cd {slug}
uv sync --frozen{extras}
Copy-Item .env.example .env
uv run --frozen python demo.py
```

For macOS/Linux, replace `Copy-Item .env.example .env` with `cp .env.example .env`.

The default demo needs no paid API key. Real graphs, persistence, loaders, retrieval, ML and tools execute locally; model routing/writing use labeled deterministic fixtures. Demo embeddings are a lexical hashing baseline. Enable live inference and semantic embeddings explicitly below.

## Open the dedicated application

Terminal 1:

```powershell
uv run uvicorn portfolio.api:app --host 127.0.0.1 --port 8000 --workers 1
```

Terminal 2:

```powershell
uv run streamlit run app.py --server.address 127.0.0.1 --server.port 8501
```

Open http://localhost:8501. This opens **{title}** directly. Local development identities: `demo-alice-key`, `demo-bob-key`, `demo-reviewer-key`. Public CSV/PDF samples, attribution and hashes are in [assets/public](assets/public). The API contract is at http://localhost:8000/docs. Each checkout uses its own runtime directory. To run several repositories at once, assign distinct API/UI ports and set each UI's `API_BASE_URL` accordingly.
{specific}
## Gemini, providers and retrieval controls

The [Gemini example](.env.gemini.example) and [setup guide](docs/ENV_SETUP.md) explain private configuration. Install semantic embedding support with `uv sync --frozen --extra embeddings --extra adk --extra gradio`, then edit your private `.env`:

```dotenv
RUN_MODE=live
LLM_PROVIDER=google_genai
LLM_MODEL=gemini-3.8-flash
GOOGLE_API_KEY=REPLACE_WITH_YOUR_PRIVATE_KEY
LLM_TEMPERATURE=1.0
LLM_TOP_P=
LLM_TOP_K=
LLM_MAX_TOKENS=1600
EMBEDDING_BACKEND=huggingface
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
RETRIEVAL_K=4
RETRIEVAL_FETCH_K=16
```

Use a model ID available to your account. Switch both provider and model for OpenAI or Anthropic, and provide that provider's private key. Supported sampling controls vary by provider; OpenAI top-k is rejected explicitly. Generation top-k and retrieval k control different operations. Restart after changing configuration and re-index documents after changing embeddings. [Configuration details](docs/CONFIGURATION.md).

## Test and deploy

```powershell
uv run ruff check src tests app.py demo.py
uv run pytest -q
docker compose up --build
```

CI runs the runtime regression suite plus a dedicated real-HTTP Streamlit check for this project. The deployment contract is **one API instance, one worker, durable local storage**. Authentication, tenant ownership, request limits, bounded workers and provider budgets are implemented. Live-provider evaluation, Docker execution, cloud deployment, load tests and restore drills require verification in your deployment environment. [Deployment guide](docs/DEPLOYMENT.md).

## Code map

| Path | Purpose |
|---|---|
| [app.py](app.py) | Dedicated {title} Streamlit entry point |
| [demo.py](demo.py) | Focused workflow demonstration |
| [src/portfolio/{module}](src/portfolio/{module}) | Main project implementation |
| [src/portfolio/models.py](src/portfolio/models.py) | Provider-neutral model factory and budgets |
| [src/portfolio/config.py](src/portfolio/config.py) | Typed configuration and trusted identity |
| [tests](tests) | Workflow and shared-runtime regression checks |
| [docs/WALKTHROUGH.md](docs/WALKTHROUGH.md) | Demo script, concepts and tradeoffs |

## Source and portfolio

Extracted from [AI Engineering Portfolio](https://github.com/{OWNER}/agentic-ai-portfolio) at `{revision[:12]}`. The common `portfolio` runtime is intentionally vendored in full to preserve tested authorization, storage, model and protocol behavior. Only this project's launchers are included; there is no dependency on another checkout. Shared runtime tests may exercise supporting capabilities used by other projects. This is a standalone showcase application, not a claim that seven unrelated codebases were built independently.

Public datasets/PDFs retain their [provenance](assets/public/PROVENANCE.json). See the [portfolio directory](https://github.com/{OWNER}/agentic-ai-portfolio#standalone-project-repositories) for the other projects.
'''
        write(root, "README.md", readme)
        write(root, "docs/ARCHITECTURE.md", f'''# {title} architecture

{flow}

The dedicated [Streamlit entry point](../app.py) calls the authenticated [FastAPI boundary](../src/portfolio/api.py). The [runtime](../src/portfolio/runtime.py) owns the SQLite store, checkpointer, Chroma lifecycle, provider client and concurrency controls. The main project implementation is [{module}](../src/portfolio/{module}).

The common runtime is vendored here. No package is fetched from the original portfolio repository. `uv.lock` resolves all external dependencies. Runtime data is owned by this checkout; private uploads and keys are ignored by Git.

HTTP caller identity comes from a server-trusted bearer mapping. Tenant/user constraints are added by application code, not accepted from model output. Structured model output still needs business validation. Pending human review, durable sessions, tool effects and graph state are separate concepts.

Read the [walkthrough](WALKTHROUGH.md), [configuration](CONFIGURATION.md), [API examples](API_EXAMPLES.md) and [deployment contract](DEPLOYMENT.md) for the applicable workflow and storage boundaries.
''')
        manifest = {"title": title, "repository": slug, "description": description, "demo": command,
                    "url": repo_url, "source_revision": revision, "source_project": folder,
                    "runtime": "vendored self-contained portfolio package"}
        write(root, "project.json", json.dumps(manifest, indent=2))
        manifests.append({**manifest, "local_path": str(root)})
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write(OUTPUT, "repositories.json", json.dumps(manifests, indent=2))
    return manifests


if __name__ == "__main__":
    print(json.dumps(export(), indent=2))
