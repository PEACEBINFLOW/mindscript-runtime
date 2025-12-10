# 3.2-ast.py
"""
AST definitions for MindScript runtime.
Keeps things simple for v0.1.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class PromptChunk:
    """
    Represents the prompt that will be sent to the LLM
    for a given stage, after any transformation.
    """
    stage_name: str
    content: str


@dataclass
class ExecutionPlan:
    """
    Ordered set of PromptChunks for execution.
    """
    chunks: List[PromptChunk]
