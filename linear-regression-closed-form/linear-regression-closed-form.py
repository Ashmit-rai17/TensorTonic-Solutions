import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)
    return np.dot(np.linalg.inv(np.dot(np.transpose(X) , X)) , np.dot(np.transpose(X) , y))
    pass