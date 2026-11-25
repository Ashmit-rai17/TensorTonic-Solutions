import numpy as np

def focal_loss(p: list, y: list, gamma: float = 2.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    eps = 1e-15
    total = 0.0
    for pi, yi in zip(p, y):
        pi = min(max(pi, eps), 1.0 - eps)
        pt = pi if yi == 1 else 1.0 - pi
        total += -((1.0 - pt) ** gamma) * math.log(pt)
    return float(total / len(p))