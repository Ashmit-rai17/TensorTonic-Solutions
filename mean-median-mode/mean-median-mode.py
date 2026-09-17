from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x_vec = np.array(x)
    x_count = Counter(x)
    dict = {"mean" : float(np.mean(x_vec)) , "median" : float(np.median(x_vec))  , "mode": float(max(x_count , key = x_count.get)) }
    return dict
    pass