import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    vec_x = np.array(x)
    n = len(x)
    mean = np.mean(vec_x)
    sum_diff = sum((i - mean)**2 for i in x)
    var = sum_diff / (n-1)
    std = np.sqrt(var)
    return {
        "variance": float(var), 
        "standard_deviation": float(std)
    }