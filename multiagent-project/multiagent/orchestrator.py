from __future__ import annotations

from typing import List

from .agents import Decomposer, Planner, Researcher, Synthesizer, Critic
from .blackboard import BlackboardOrchestrator
from .types import BlackboardState, UserGoal


def build_default_orchestrator() -> BlackboardOrchestrator:
    agents = [
        Decomposer(),
        Planner(),
        Researcher(),
        Synthesizer(),
        Critic(),
    ]
    return BlackboardOrchestrator(agents=agents, max_rounds=6)


def run_pipeline(origin: str, destination: str, when: str, budget_inr: float | None) -> BlackboardState:
    goal = UserGoal(origin=origin, destination=destination, when=when, budget_inr=budget_inr)
    state = BlackboardState(goal=goal)
    orchestrator = build_default_orchestrator()
    final_state = orchestrator.run(state)
    return final_state

