# 8-roadmap.md  
## mindscript-runtime Roadmap

### v0.1 — Minimal Runtime (This Repo)
- [x] Basic parser for <STAGE_X> blocks
- [x] Execution engine with sequential stages
- [x] Simple CLI: `run`
- [x] Mock adapters: OpenAI, Gemini, local stub
- [x] Example MindScript files

### v0.2 — Real API Integration
- [ ] Real HTTP calls to OpenAI / Gemini
- [ ] Configurable system prompts per stage
- [ ] Logging & basic error handling

### v0.3 — Packaging & Distribution
- [ ] Publish as a Python package (`pip install mindscript-runtime`)
- [ ] `mindscript` global CLI command
- [ ] Better help and interactive flags

### v1.0 — Ecosystem Integration
- [ ] Tight integration with `mindscript-ledger`
- [ ] Integration with `mindscript-templates`
- [ ] Example notebooks and end-to-end demos
