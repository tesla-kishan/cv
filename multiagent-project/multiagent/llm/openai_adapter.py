from __future__ import annotations

import os
from typing import Optional

from .base import LLM


class OpenAILLM(LLM):
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model

    def generate(self, prompt: str) -> str:
        # Lazy import to avoid dependency if unused
        try:
            from openai import OpenAI  # type: ignore
        except Exception:
            return "[OPENAI SDK NOT INSTALLED]"

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "[OPENAI_API_KEY NOT SET]"
        client = OpenAI(api_key=api_key)
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            return f"[OPENAI ERROR] {e}"

