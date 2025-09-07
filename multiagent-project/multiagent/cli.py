from __future__ import annotations

import json
from typing import Optional

import typer

from .orchestrator import run_pipeline

app = typer.Typer(add_completion=False, help="AI Multi-Agent Urban Mobility Assistant")


@app.command()
def run(
    origin: str = typer.Option(..., help="Start location"),
    destination: str = typer.Option(..., help="End location"),
    when: str = typer.Option(..., help="When to travel"),
    budget: Optional[float] = typer.Option(None, help="Budget in INR"),
    llm: str = typer.Option("dummy", help="LLM backend (dummy/ollama/openai) ignored in mock"),
    model: Optional[str] = typer.Option(None, help="Model name for selected LLM backend"),
):
    state = run_pipeline(origin=origin, destination=destination, when=when, budget_inr=budget)
    typer.echo(json.dumps({
        "plan": state.plan,
        "evidence": state.evidence,
        "critiques": state.critiques,
        "done": state.done,
    }, indent=2, ensure_ascii=False))


def main():
    app()


if __name__ == "__main__":
    main()

