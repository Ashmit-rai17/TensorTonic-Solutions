import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    Am = np.array(A)
    return np.transpose(Am)
    pass
