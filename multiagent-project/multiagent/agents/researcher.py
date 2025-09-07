from __future__ import annotations

from ..types import Agent, BlackboardState


class Researcher(Agent):
    def __init__(self):
        super().__init__(name="Researcher")

    def step(self, state: BlackboardState) -> BlackboardState:
        # Mock signals; in a real system query APIs
        if "fares" not in state.evidence:
            state.evidence["fares"] = {"metro": 40, "auto": 120}
        if "delays" not in state.evidence:
            state.evidence["delays"] = {"metro": "minor", "auto": "traffic moderate"}
        if "weather" not in state.evidence:
            state.evidence["weather"] = {"condition": "clear", "temp_c": 30}
        return state

