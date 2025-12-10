# 3.5-io_types.md  
## Input / Output Types v0.1

For this minimal runtime:

Input:
- raw MindScript string (full file contents)

Internal:
- `MindScriptProgram`
- `ExecutionPlan`
- `PromptChunk`

Output:
- dictionary:
  - `stages_executed`: [list of stage names]
  - `outputs`: { stage_name: llm_output }
