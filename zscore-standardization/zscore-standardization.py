import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # 1. Convert to a float NumPy array
    X = np.array(X, dtype=float)
    mn = np.mean(X, axis=axis, keepdims=True)
    st = np.std(X, axis=axis, keepdims=True)
    return np.where(st <= eps , 0.0 , (X - mn) / (st))
