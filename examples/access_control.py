"""Explainable access derivation using positive Horn rules."""
from src.logic_engine import Atom, Rule, infer

facts = {
    Atom("member", ("alice", "engineering")),
    Atom("team_access", ("engineering", "reports")),
}
rules = [Rule(Atom("may_read", ("?user", "?resource")),
              (Atom("member", ("?user", "?team")),
               Atom("team_access", ("?team", "?resource"))))]
if __name__ == "__main__":
    for fact in sorted(infer(facts, rules), key=repr):
        print(fact)
