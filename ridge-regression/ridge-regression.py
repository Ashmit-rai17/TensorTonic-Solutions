import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)
    if lam != 0:
        return np.dot(np.linalg.inv(np.dot(np.transpose(X) , X) + lam*np.eye(X.shape[1])) , np.dot(np.transpose(X) , y))
    else:
        return np.dot(np.linalg.inv(np.dot(np.transpose(X) , X))  , np.dot(np.transpose(X) , y))
    pass