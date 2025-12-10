# 5.1-mindscript_cli.py
"""
Simple CLI for mindscript-runtime.

Usage:
    python 5-cli/5.1-mindscript_cli.py run path/to/file.ms.md --model local:stub
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path

from 3_core.runtime_engine import RuntimeEngine
from 4_adapters.local_stub_adapter import LocalStubAdapter
from 4_adapters.openai_adapter import OpenAIAdapter
from 4_adapters.gemini_adapter import GeminiAdapter


def load_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        print(f"[error] File not found: {path}")
        sys.exit(1)
    return p.read_text(encoding="utf-8")


def build_adapter(model_spec: str):
    """
    Minimal dispatcher:
    - "local:stub"
    - "openai:gpt-4.1"
    - "gemini:pro"
    """
    if model_spec.startswith("local:"):
        return LocalStubAdapter(model_name=model_spec.split(":", 1)[1])
    if model_spec.startswith("openai:"):
        return OpenAIAdapter(model_name=model_spec.split(":", 1)[1])
    if model_spec.startswith("gemini:"):
        return GeminiAdapter(model_name=model_spec.split(":", 1)[1])
    print(f"[error] Unknown model spec: {model_spec}")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="MindScript Runtime CLI")
    subparsers = parser.add_subparsers(dest="command")

    run_cmd = subparsers.add_parser("run", help="Run a MindScript file")
    run_cmd.add_argument("file", help="Path to .ms or .ms.md file")
    run_cmd.add_argument("--model", default="local:stub", help="Model spec (e.g. local:stub, openai:gpt-4.1)")

    args = parser.parse_args()

    if args.command == "run":
        text = load_file(args.file)
        adapter = build_adapter(args.model)
        engine = RuntimeEngine(adapter=adapter, verbose=True)
        engine.run(text)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
