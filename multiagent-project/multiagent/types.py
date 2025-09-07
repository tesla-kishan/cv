from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


@dataclass
class UserGoal:
    origin: str
    destination: str
    when: str
    budget_inr: Optional[float] = None
    preferences: Dict[str, Any] = field(default_factory=dict)


@dataclass
class BlackboardState:
    goal: UserGoal
    tasks: List[str] = field(default_factory=list)
    evidence: Dict[str, Any] = field(default_factory=dict)
    plan: Optional[str] = None
    critiques: List[str] = field(default_factory=list)
    done: bool = False


class Agent:
    name: str

    def __init__(self, name: str):
        self.name = name

    def step(self, state: BlackboardState) -> BlackboardState:
        raise NotImplementedError


class LLM:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError

