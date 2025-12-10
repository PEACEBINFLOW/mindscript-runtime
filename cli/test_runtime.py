# 7.2-test_runtime.py

from 3_core.runtime_engine import RuntimeEngine
from 4_adapters.local_stub_adapter import LocalStubAdapter


def test_runtime_executes_single_stage():
    text = """
<MIND_SCRIPT>
<STAGE_1>
Say hello.
</STAGE_1>
</MIND_SCRIPT>
"""
    adapter = LocalStubAdapter()
    engine = RuntimeEngine(adapter=adapter, verbose=False)
    result = engine.run(text)

    assert "STAGE_1" in result["outputs"]
    assert "Say hello" in result["outputs"]["STAGE_1"]
