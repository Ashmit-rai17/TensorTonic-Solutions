import numpy as np

def clip_gradients(g: list, max_norm: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as g.
    """
    # Write code here
    g = np.array(g)
    g2 = np.sum(g**2)**0.5
    if g2 <= max_norm:
        return g
    else:
        return g*(max_norm/g2)
    pass