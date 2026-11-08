def select_allowed(scores: dict[str, float], allowed: set[str]) -> str:
    """Select highest-scoring candidate that satisfies symbolic allow-list."""
    candidates = [(score, name) for name, score in scores.items() if name in allowed]
    if not candidates:
        raise ValueError("No candidate satisfies constraints")
    return max(candidates)[1]
