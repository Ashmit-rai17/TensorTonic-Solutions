import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    p = np.array(p)
    q = np.array(q)
    return float(np.sum(np.where(p==0 , p , p*np.log(p/q))))
    pass