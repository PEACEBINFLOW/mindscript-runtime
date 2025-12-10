# 4.4-local_stub_adapter.py
"""
Local stub adapter for testing.
Does not call any external API.
"""

from __future__ import annotations
from typing import Optional

from 4_adapters.base_adapter import BaseAdapter  # adjust imports in real project


class LocalStubAdapter(BaseAdapter):
    def __init__(self, model_name: str = "stub-model"):
        self.model_name = model_name

    def generate(self, prompt: str, temperature: Optional[float] = None) -> str:
        return f"[local:{self.model_name}] echo\n---\n{prompt}"
