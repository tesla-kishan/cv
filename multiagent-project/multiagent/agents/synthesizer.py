from __future__ import annotations

from ..types import Agent, BlackboardState


class Synthesizer(Agent):
    def __init__(self):
        super().__init__(name="Synthesizer")

    def step(self, state: BlackboardState) -> BlackboardState:
        if not state.plan:
            return state
        if state.done:
            return state
        fares = state.evidence.get("fares", {})
        total_cost = fares.get("metro", 0) + fares.get("auto", 0)
        itinerary = (
            f"Itinerary: {state.plan}\n"
            f"Estimated cost: ₹{total_cost}. Weather: {state.evidence.get('weather', {}).get('condition', 'n/a')}"
        )
        state.plan = itinerary
        return state

