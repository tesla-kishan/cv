AI Multi-Agent Project: Urban Mobility Assistant

Problem Statement

Urban travelers struggle to plan efficient, safe, and cost-effective multi-modal trips (walking, metro, ride-share) under constraints like delays, crowd levels, safety advisories, and weather. Centralized systems often provide static suggestions and cannot personalize plans or adapt in real time. We propose a multi-agent system that decomposes a user’s goal (e.g., “Get from A to B after 6 PM with minimal walking and within ₹200”) and coordinates specialized agents to research transit options, reason about safety and delays, and synthesize an actionable plan.

Why Multi-Agent

- Decomposition: A Decomposer agent converts high-level goals into subproblems (routes, timing, budget).
- Specialization: Research, Planning, and Safety agents each focus on a specific capability.
- Collaboration: A Critic challenges assumptions and ensures constraints are satisfied.
- Robustness: If one agent fails (e.g., data source down), others can propose alternatives.

Project Description

The application exposes a CLI that accepts a travel goal and context (origin, destination, time, budget). An Orchestrator coordinates these agents over a shared blackboard:

- Decomposer: Extracts constraints and tasks.
- Planner: Proposes route candidates and sequences steps.
- Researcher: Gathers live-like signals (mocked APIs) for fares, delays, weather.
- Synthesizer: Produces a consolidated itinerary with rationale.
- Critic: Audits plan for constraint violations or missing evidence.

Agents operate in rounds. Each round, agents read the blackboard, post updates, and vote on readiness. The orchestrator stops when the plan is consistent or a max round limit is reached.

Tools, Libraries, and Frameworks

- Python 3.10+
- Typer (CLI)
- Pydantic (data models)
- Requests / httpx (optional for live APIs; mocked here)
- Optional: Streamlit for demo UI
- No heavy framework dependency required; architecture can plug into LangChain, CrewAI, or AutoGen if desired.

LLM Selection

- Ideal: GPT-4o or Claude 3.5 Sonnet for strong reasoning.
- Free-tier option: Google Gemini via free tier or Hugging Face open models (e.g., Mistral 7B Instruct) through `ollama` or `text-generation-inference`.
- Rationale: Agents require structured reasoning and consistency across rounds; a stronger model improves decomposition and critique quality. The system includes a Dummy LLM for offline testing and an Ollama adapter for open-source local models.

Repository Structure

```
multiagent-project/
  ├─ multiagent/
  │  ├─ __init__.py
  │  ├─ cli.py
  │  ├─ orchestrator.py
  │  ├─ blackboard.py
  │  ├─ types.py
  │  ├─ agents/
  │  │  ├─ __init__.py
  │  │  ├─ decomposer.py
  │  │  ├─ planner.py
  │  │  ├─ researcher.py
  │  │  ├─ synthesizer.py
  │  │  └─ critic.py
  │  └─ llm/
  │     ├─ __init__.py
  │     ├─ base.py
  │     ├─ dummy.py
  │     ├─ ollama.py
  │     └─ openai_adapter.py
  ├─ requirements.txt
  ├─ .gitignore
  └─ README.md
```

Setup

1. Python 3.10+ recommended
2. Create a virtual environment
3. Install dependencies

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Running the CLI

```
python -m multiagent.cli run \
  --origin "Connaught Place" \
  --destination "Hauz Khas" \
  --when "today 6:30pm" \
  --budget 200 \
  --llm dummy
```

To use Ollama-backed local models:

```
python -m multiagent.cli run --llm ollama --model mistral:7b-instruct
```

Deployment Options

- Streamlit demo: `streamlit run app.py` (optional add-on)
- Hugging Face Spaces: push this repo and configure Space with Python runtime
- Vercel: package Streamlit or a FastAPI wrapper

Submission Checklist

- Problem statement and value of multi-agent approach
- Description of agents and interaction pattern
- Tools and frameworks listed
- LLM selection with free-tier option and justification
- Code included with README; optional deployment link if you add Streamlit

