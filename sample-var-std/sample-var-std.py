import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    vec_x = np.array(x)
    n = len(x)
    return {"variance" : float(np.var(vec_x , ddof=1)) , "standard_deviation" : float(np.std(vec_x , ddof = 1))}
    pass