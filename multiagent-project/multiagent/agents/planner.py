from __future__ import annotations

from ..types import Agent, BlackboardState


class Planner(Agent):
    def __init__(self):
        super().__init__(name="Planner")

    def step(self, state: BlackboardState) -> BlackboardState:
        if state.plan:
            return state
        if not state.tasks:
            return state
        # naive candidate plan using available evidence as it accumulates
        budget = state.goal.budget_inr
        budget_note = f" within ₹{int(budget)}" if budget is not None else ""
        plan_text = (
            f"Start at {state.goal.origin}. Take metro to an interchange, then last-mile auto to {state.goal.destination}. "
            f"Depart around {state.goal.when}{budget_note}."
        )
        state.plan = plan_text
        return state

