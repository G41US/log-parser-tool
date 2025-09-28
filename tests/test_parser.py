import pandas as pd
from src.parser import parse_log

def test_parse_log():
    df = parse_log("sample_logs/access.log")
    assert not df.empty
    assert "ip" in df.columns
    assert "status" in df.columns
