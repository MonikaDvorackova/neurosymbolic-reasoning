"""Small stratified Datalog-style forward-chaining evaluator.

Rules are positive Horn clauses; no negation or recursion limit.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Atom:
    predicate: str
    args: tuple[str, ...]

@dataclass(frozen=True)
class Rule:
    head: Atom
    body: tuple[Atom, ...]

def _unify(pattern, fact, bindings):
    if pattern.predicate != fact.predicate or len(pattern.args) != len(fact.args):
        return None
    b = dict(bindings)
    for p, v in zip(pattern.args, fact.args):
        if p.startswith("?"):
            if p in b and b[p] != v:
                return None
            b[p] = v
        elif p != v:
            return None
    return b

def infer(facts, rules, max_facts=10000):
    known = set(facts)
    while True:
        additions = set()
        for rule in rules:
            bindings = [{}]
            for atom in rule.body:
                bindings = [candidate for b in bindings for f in known
                            if (candidate := _unify(atom, f, b)) is not None]
            for b in bindings:
                if any(a.startswith("?") and a not in b for a in rule.head.args):
                    raise ValueError("unsafe rule: unbound head variable")
                additions.add(Atom(rule.head.predicate, tuple(b.get(a, a) for a in rule.head.args)))
        new = additions - known
        if not new:
            return known
        known |= new
        if len(known) > max_facts:
            raise RuntimeError("fact limit exceeded")
