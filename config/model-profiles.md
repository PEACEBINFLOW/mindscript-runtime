# 2.2-model-profiles.md  
## Model Profiles

Model profiles are named configurations that map to a specific backend.

Format (in `config.yaml`):

```yaml
models:
  openai:gpt-4.1:
    provider: openai
    model_name: gpt-4.1
    api_key_env: OPENAI_API_KEY
