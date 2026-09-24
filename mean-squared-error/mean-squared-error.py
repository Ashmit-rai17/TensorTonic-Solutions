import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    y1 = np.array(y_pred)
    y2 = np.array(y_true)
    return np.mean((y1-y2)**2)
    pass