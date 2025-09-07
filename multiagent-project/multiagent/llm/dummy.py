from __future__ import annotations

from .base import LLM


class DummyLLM(LLM):
    def generate(self, prompt: str) -> str:
        return f"[DUMMY RESPONSE]\n{prompt[:200]}..."

