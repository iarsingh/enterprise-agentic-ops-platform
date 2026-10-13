# Enterprise Agentic AI Operations Platform

## Overview

A capstone lab that models an agentic operations flow from a customer UI through authentication, a supervisor, specialist agents for RAG, data, cloud and SRE work, MCP tools, a human approval gate and an audit trail. Execution stays false: the agent run endpoint routes and records work but does not carry it out. A React front end, Docker Compose setup and a `/v1` ops API for workspaces, tenant isolation and job approval sit around the agent code.

- **Built with:** Python, FastAPI, React, TypeScript, MCP, pytest, Docker, GitHub Actions
- **Scope:** Laptop lab with no hosted model; cluster apply stays false until a human approves.

<!-- project-guide:start -->
## Project guide

[Project architecture](PROJECT_ARCHITECTURE.md) · [Interview questions and answers](INTERVIEW_QA.md)

Use the architecture document for the component diagram, implementation boundaries, and verification entry points. The interview guide includes source-backed answers and project walkthroughs.

### Implementation map

| Component | Responsibility |
| --- | --- |
| [`src/agentx/main.py`](src/agentx/main.py) | HTTP handlers: `GET /healthz`, `POST /agent/run` |
| [`src/agentx/ops.py`](src/agentx/ops.py) | HTTP handlers: `GET /readyz`, `POST /workspaces`, `GET /workspaces`, `POST /workspaces/{workspace_id}/jobs`, `GET /jobs/{job_id}` |
| [`src/agentx/agent.py`](src/agentx/agent.py) | Functions: `run` |
| [`requirements.txt`](requirements.txt) | Implementation or supporting configuration |
| [`web/src/App.tsx`](web/src/App.tsx) | User interface code/assets |
| [`Dockerfile`](Dockerfile) | Container build/service configuration |
| [`Makefile`](Makefile) | Implementation or supporting configuration |
| [`docker-compose.yml`](docker-compose.yml) | Container build/service configuration |
| [`tests/test_agent.py`](tests/test_agent.py) | Executable checks and regression examples |
| [`tests/test_ops.py`](tests/test_ops.py) | Executable checks and regression examples |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | GitHub Actions job definitions |
| [`README.md`](README.md) | Project explanations or operating notes |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Project explanations or operating notes |

### Local setup and verification

From the repository root (the commands follow the checked-in manifests):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

To serve the FastAPI application locally, install the server separately if it is not already available:

```bash
python -m pip install uvicorn
PYTHONPATH=src python -m uvicorn agentx.main:app --reload
```

<!-- project-guide:end -->

Phase 9 capstone

Skills: React, FastAPI, supervisor, RAG/data/cloud/SRE, MCP, approval, audit

Customer UI → auth → supervisor → agents → MCP → approval → execution(false) → audit.

```bash
pip install -r requirements.txt
pytest -q
```

Laptop proof. No hosted model. Cluster apply stays false until a human approves.

## Ops plane

Workspaces, tenant isolation, job approval, and audit live under `/v1`. Production apply is refused. See `docs/ARCHITECTURE.md`.

## Documentation checks

Project architecture, interview guides, and local source links are checked automatically on pushes and pull requests. Run the same check locally:

```bash
python3 .github/scripts/validate_project_docs.py
```

See [service improvements and local run instructions](docs/UPGRADES.md).
