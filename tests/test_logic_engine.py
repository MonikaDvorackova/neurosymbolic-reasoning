import pytest
from src.logic_engine import Atom, Rule, infer

def test_transitive_access():
    facts = {Atom("edge", ("alice","bob")), Atom("edge", ("bob","carol"))}
    rules = [
        Rule(Atom("path", ("?x","?y")), (Atom("edge", ("?x","?y")),)),
        Rule(Atom("path", ("?x","?z")), (Atom("path", ("?x","?y")), Atom("edge", ("?y","?z"))))
    ]
    assert Atom("path", ("alice","carol")) in infer(facts, rules)

def test_unsafe_rule():
    with pytest.raises(ValueError, match="unsafe"):
        infer(set(), [Rule(Atom("bad", ("?x",)), ())])
