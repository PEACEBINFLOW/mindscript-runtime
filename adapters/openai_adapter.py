# 4.2-openai_adapter.py
"""
OpenAI adapter (pseudo, no real HTTP in v0.1).
Wire real client later.
"""

from __future__ import annotations
import os
from typing import Optional

from 4_adapters.base_adapter import BaseAdapter  # adjust imports in real project


class OpenAIAdapter(BaseAdapter):
    def __init__(self, model_name: str, api_key_env: str = "OPENAI_API_KEY"):
        self.model_name = model_name
        self.api_key_env = api_key_env

    def generate(self, prompt: str, temperature: Optional[float] = None) -> str:
        api_key = os.getenv(self.api_key_env, "")
        _ = api_key  # placeholder so linter doesn't complain

        # TODO: Replace this with real OpenAI call.
        return f"[openai:{self.model_name}] (mock) → {prompt[:120]}..."
