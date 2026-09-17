import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    Xv = np.array(X)
    n = Xv.shape[0]
    mu = np.mean(Xv , axis = 0)
    Xc = Xv - mu
    return np.dot(np.transpose(Xc) , Xc) / (n-1)
    pass