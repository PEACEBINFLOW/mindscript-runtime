# 7.3-test_adapters.py

from 4_adapters.local_stub_adapter import LocalStubAdapter


def test_local_stub_adapter():
    adapter = LocalStubAdapter()
    out = adapter.generate("ping")
    assert "ping" in out
