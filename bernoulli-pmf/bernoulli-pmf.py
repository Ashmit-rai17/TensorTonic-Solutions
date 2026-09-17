import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = []
    for i in x:
        if i == 1:
            pmf.append(p)
        elif i==0:
            pmf.append(1-p)
    pmf = np.array(pmf)
    return {"pmf" : pmf , "mean" : float(p) , "variance" : float(p*(1-p))}
    pass