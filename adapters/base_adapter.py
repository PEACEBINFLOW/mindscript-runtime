# 4.1-base_adapter.py
"""
Base adapter interface for LLM providers.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class BaseAdapter(ABC):
    @abstractmethod
    def generate(self, prompt: str, temperature: Optional[float] = None) -> str:
        ...
