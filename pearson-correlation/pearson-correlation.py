import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    Xv = np.array(X)
    n = len(Xv)
    #R = Cov / std1*std2
    mu = np.mean(Xv , axis=0)
    Xc = Xv - mu
    cov = np.dot(np.transpose(Xc) , Xc) / (n-1)
    stdf = np.sqrt(np.diag(cov))
    return cov / np.outer(stdf , stdf)
    pass