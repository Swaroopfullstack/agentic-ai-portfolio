"""Create a portable source/public-data ZIP, excluding all credentials and runtime data."""
from datetime import date
import hashlib
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_DIRS = {"src", "tests", "projects", "docs", "assets", "scripts", ".github", ".streamlit"}
ALLOWED_ROOT = {"README.md", "pyproject.toml", "uv.lock", ".gitignore", ".env.example", "IMPLEMENTATION_PLAN.md",
                ".env.gemini.example", ".env.production.example", ".gitattributes", "Dockerfile", "compose.yaml", ".dockerignore"}
ALLOWED_REPORTS = {"VALIDATION.md", "public-evaluation.json", "embedding-validation.json", "test-results.xml", "clean-environment-tests.xml",
                   "embedding-tests.xml", "streaming-tests.xml", "insightforge-demo.png"}


def package():
    output = ROOT/"dist"/f"AI_Engineering_Portfolio_Gemini_uv_{date.today().isoformat()}.zip"
    output.parent.mkdir(exist_ok=True)
    selected = []
    for directory, children, names in os.walk(ROOT):
        base = Path(directory)
        children[:] = [name for name in children if name not in {"__pycache__", ".pytest_cache", ".ruff_cache"}]
        if base == ROOT:
            children[:] = [name for name in children if name in ALLOWED_DIRS | {"reports"}]
        for name in names:
            path = base/name
            relative = path.relative_to(ROOT)
            parts = relative.parts
            if path.suffix in {".pyc", ".sqlite", ".db", ".log"} or (name.startswith(".env") and not (len(parts) == 1 and name in ALLOWED_ROOT)):
                continue
            include = (len(parts) == 1 and parts[0] in ALLOWED_ROOT) or parts[0] in ALLOWED_DIRS
            include |= len(parts) == 2 and parts[0] == "reports" and parts[1] in ALLOWED_REPORTS
            if include:
                selected.append(path)
    with ZipFile(output, "w", ZIP_DEFLATED, compresslevel=6) as archive:
        for path in selected:
            archive.write(path, "agentic-ai-portfolio/" + path.relative_to(ROOT).as_posix())
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(".zip.sha256").write_text(f"{digest}  {output.name}\n", encoding="ascii")
    return {"path": str(output), "files": len(selected), "bytes": output.stat().st_size, "sha256": digest}


if __name__ == "__main__":
    import json
    print(json.dumps(package(), indent=2))
