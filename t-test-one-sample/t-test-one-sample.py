import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x = np.array(x)
    s = np.std(x , ddof=1)
    s = s / np.sqrt(len(x))
    return float((np.mean(x) - mu0) / s)
    # Write code here
    pass