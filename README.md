# mindscript-runtime
mindscript-runtime is the minimal, reference implementation of the MindScript engine.  It provides: - a CLI for running .ms / .ms.md files - a parser that converts MindScript into an internal AST - a stage-based runtime that executes each stage sequentially - adapters for different LLM backends (OpenAI, Gemini, local stub)  
