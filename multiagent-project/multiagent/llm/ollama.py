from __future__ import annotations

import json
import subprocess
from typing import Optional

from .base import LLM


class OllamaLLM(LLM):
    def __init__(self, model: str = "mistral:7b-instruct", timeout: int = 60):
        self.model = model
        self.timeout = timeout

    def generate(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                [
                    "ollama",
                    "run",
                    self.model,
                    prompt,
                ],
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )
            if result.returncode != 0:
                return f"[OLLAMA ERROR] {result.stderr.strip()}"
            return result.stdout.strip()
        except FileNotFoundError:
            return "[OLLAMA NOT INSTALLED]"
        except subprocess.TimeoutExpired:
            return "[OLLAMA TIMEOUT]"

