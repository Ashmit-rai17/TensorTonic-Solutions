import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    vec_x = np.array(x)
    vec_p = np.array(p)
    return float(np.dot(vec_x , vec_p))
    pass