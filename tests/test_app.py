# tests/test_app.py
# Initial minimal tests—will ask Copilot to expand.
from calculate_stats import calc

def test_calc_basic():
    data = [1, 2, 3]
    r = calc(data)
    assert r["sum"] == 6
    assert r["average"] == 2
    assert r["max"] == 3
    assert r["min"] == 1