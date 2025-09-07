from __future__ import annotations

from dataclasses import replace
from typing import List

from .types import BlackboardState, Agent


class BlackboardOrchestrator:
    def __init__(self, agents: List[Agent], max_rounds: int = 6):
        self.agents = agents
        self.max_rounds = max_rounds

    def run(self, initial_state: BlackboardState) -> BlackboardState:
        state = initial_state
        for _ in range(self.max_rounds):
            if state.done:
                break
            for agent in self.agents:
                state = agent.step(state)
                if state.done:
                    break
        return state

