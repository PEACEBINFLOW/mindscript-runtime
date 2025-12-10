# 3.4-stage_executor.py
"""
StageExecutor: responsible for applying policies per stage,
like:
- system prompts
- temperature overrides
- formatting
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class StageConfig:
    system_prompt: Optional[str] = None
    temperature: Optional[float] = None


class StageExecutor:
    def __init__(self, adapter, default_temperature: float = 0.3):
        self.adapter = adapter
        self.default_temperature = default_temperature
        self.stage_configs: Dict[str, StageConfig] = {}

    def register_stage_config(self, stage_name: str, config: StageConfig):
        self.stage_configs[stage_name] = config

    def execute_stage(self, stage_name: str, content: str) -> str:
        cfg = self.stage_configs.get(stage_name, StageConfig())
        system_prompt = cfg.system_prompt or ""
        temperature = cfg.temperature or self.default_temperature

        prompt = content
        if system_prompt:
            prompt = system_prompt.strip() + "\n\n" + content.strip()

        return self.adapter.generate(prompt, temperature=temperature)
