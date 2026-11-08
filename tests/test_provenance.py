from src.logic_engine import Atom, Rule
from src.provenance import infer_with_provenance

def test_explanation_is_deterministic():
    fact=Atom("parent",("alice","bob"))
    rule=Rule(Atom("ancestor",("?x","?y")),(Atom("parent",("?x","?y")),))
    known,why=infer_with_provenance({fact},[rule])
    target=Atom("ancestor",("alice","bob"))
    assert target in known
    assert why[target]==(fact,)
    assert why[fact] is None
