# 7.1-test_parser.py

from 3_core.parser import parse_mindscript


def test_simple_stage_parse():
    text = """
<MIND_SCRIPT>
<STAGE_1>
Hello
</STAGE_1>
</MIND_SCRIPT>
"""
    program = parse_mindscript(text)
    assert len(program.stages) == 1
    assert program.stages[0].name == "STAGE_1"
    assert "Hello" in program.stages[0].content
