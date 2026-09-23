import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    # Write code here
    X = np.array(X)
    mask = np.isnan(X)
    mean = np.nanmean(X , axis=0)
    median = np.nanmedian(X , axis=0)
    if strategy == "mean":
        imp_X = np.where(mask , mean , X)
    elif strategy == "median":
        imp_X = np.where(mask , median , X)
    imp_X[np.isnan(imp_X)] = 0.0
    return imp_X
    pass