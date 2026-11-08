"""Finite, deterministic Horn inference with derivation provenance."""
from src.logic_engine import Atom, _unify

def infer_with_provenance(facts, rules, max_facts=10000):
    known = set(facts)
    provenance = {fact: None for fact in known}
    if len(known) > max_facts:
        raise RuntimeError("fact limit exceeded")
    while True:
        additions = {}
        for rule in rules:
            candidates = [({}, ())]
            for pattern in rule.body:
                candidates = [(merged, parents + (fact,))
                              for binding, parents in candidates
                              for fact in sorted(known, key=repr)
                              if (merged := _unify(pattern, fact, binding)) is not None]
            for binding, parents in candidates:
                if any(arg.startswith("?") and arg not in binding for arg in rule.head.args):
                    raise ValueError("unsafe rule")
                head = Atom(rule.head.predicate, tuple(binding.get(a, a) for a in rule.head.args))
                if head not in known and head not in additions:
                    additions[head] = parents
        if not additions:
            return known, provenance
        if len(known) + len(additions) > max_facts:
            raise RuntimeError("fact limit exceeded")
        known.update(additions)
        provenance.update(additions)
