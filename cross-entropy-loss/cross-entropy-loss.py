import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    ce = []
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    for x , y in zip(y_true , y_pred):
        ce.append(np.log(y[x]))
    return -np.mean(ce)
    pass