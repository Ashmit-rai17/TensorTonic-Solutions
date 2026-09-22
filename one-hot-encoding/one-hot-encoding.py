import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    if num_classes is None:
        res = np.zeros((len(y), max(y)+1), dtype=float)
    else:
        res = np.zeros((len(y) , num_classes) , dtype=float)
    for i in range(0 , len(y)):
        res[i][y[i]] = 1
    return res
    # Write code here
    pass