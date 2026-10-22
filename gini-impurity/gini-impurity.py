import numpy as np

def gini_impurity(y_left: list, y_right: list) -> float:
    """
    Returns the impurity as a float.
    """
    # Write code here
    if len(y_left) == 0 and len(y_right) == 0:
        return 0
    y_left = np.array(y_left)
    y_right = np.array(y_right)
    _ , l_freq = np.unique(y_left , return_counts = True)
    _ , r_freq = np.unique(y_right , return_counts = True)
    if len(y_left) == 0:
        p_left = 0
    else:
        p_left = l_freq / len(y_left)
    if len(y_right) == 0:
        p_right = 0
    else:
        p_right = r_freq / len(y_right)
    gini_left = 1 - np.sum(p_left**2)
    gini_right = 1 - np.sum(p_right**2)
    n = len(y_left) + len(y_right)
    return (len(y_left) / n)*gini_left + (len(y_right) / n)*gini_right
    pass