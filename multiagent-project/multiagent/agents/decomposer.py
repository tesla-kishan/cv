from __future__ import annotations

from typing import Any, Dict, List

from ..types import Agent, BlackboardState


class Decomposer(Agent):
    def __init__(self):
        super().__init__(name="Decomposer")

    def step(self, state: BlackboardState) -> BlackboardState:
        if state.tasks:
            return state
        tasks: List[str] = [
            "extract constraints",
            "enumerate route candidates",
            "collect context: fares, delays, weather",
            "synthesize itinerary",
            "critique and finalize",
        ]
        state.tasks = tasks
        return state

