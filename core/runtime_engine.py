# 3.3-runtime_engine.py
"""
Minimal runtime engine:
- take a MindScriptProgram
- turn it into an ExecutionPlan
- execute each stage using an adapter
"""

from __future__ import annotations
from typing import Dict, Any, List

from 3_core.parser import parse_mindscript  # adjust import for real package structure
from 3_core.ast import PromptChunk, ExecutionPlan


class RuntimeEngine:
    def __init__(self, adapter, verbose: bool = True):
        self.adapter = adapter
        self.verbose = verbose

    def build_execution_plan(self, source_text: str) -> ExecutionPlan:
        program = parse_mindscript(source_text)
        chunks: List[PromptChunk] = []

        for stage in program.stages:
            chunks.append(PromptChunk(stage_name=stage.name, content=stage.content))

        return ExecutionPlan(chunks=chunks)

    def run(self, source_text: str) -> Dict[str, Any]:
        plan = self.build_execution_plan(source_text)
        outputs: Dict[str, str] = {}

        for chunk in plan.chunks:
            if self.verbose:
                print(f"\n[Runtime] Executing {chunk.stage_name}...")
            response = self.adapter.generate(chunk.content)
            outputs[chunk.stage_name] = response
            if self.verbose:
                print(f"[Runtime] Output ({chunk.stage_name}):\n{response}\n")

        return {
            "stages_executed": [c.stage_name for c in plan.chunks],
            "outputs": outputs,
        }
