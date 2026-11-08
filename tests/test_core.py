from src.core import select_allowed

def test_constraint():
    assert select_allowed({"unsafe": 9, "safe": 2}, {"safe"}) == "safe"
