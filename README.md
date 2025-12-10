# mindscript-runtime  
### Minimal Runtime & CLI for MindScript  
by **Peace Thabiwa — SAGEWORKS AI**

---

## What is this?

`mindscript-runtime` is the **first executable engine** for MindScript.

It lets you:

- run MindScript files (`.ms` / `.ms.md`) from the command line  
- interpret stages like `<STAGE_1> ... </STAGE_1>`  
- send composed prompts to a selected LLM backend  
- capture outputs and print or store them

This is meant to be:
- **minimal** enough to read in one sitting  
- **extensible** enough to grow into a full engine  
- **ecosystem-ready** for MindScript Core, Templates, and Ledger.

---

## Quickstart

```bash
git clone https://github.com/PEACEBINFLOW/mindscript-runtime.git
cd mindscript-runtime

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt  # (add later if needed)

cp 2-config/2.1-config.example.yaml config.yaml
# edit config.yaml with your API keys

python 5-cli/5.1-mindscript_cli.py run 6-examples/6.1-simple-names.ms.md
