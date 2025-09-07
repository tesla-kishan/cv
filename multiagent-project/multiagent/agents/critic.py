from __future__ import annotations

from ..types import Agent, BlackboardState


class Critic(Agent):
    def __init__(self):
        super().__init__(name="Critic")

    def step(self, state: BlackboardState) -> BlackboardState:
        if not state.plan:
            return state
        budget = state.goal.budget_inr
        fares = state.evidence.get("fares", {})
        total_cost = fares.get("metro", 0) + fares.get("auto", 0)
        critique = None
        if budget is not None and total_cost > budget:
            critique = f"Cost ₹{total_cost} exceeds budget ₹{int(budget)}"
        elif state.evidence.get("delays", {}).get("metro") == "major":
            critique = "Metro delays major; consider rideshare or bus alternatives"

        if critique:
            state.critiques.append(critique)
        else:
            state.done = True
        return state

