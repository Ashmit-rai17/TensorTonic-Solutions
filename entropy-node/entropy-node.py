import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    if not y:
        return 0.0
    y = np.array(y)
    _ , count = np.unique(y , return_counts = True)
    probabilities = count / len(y)
    res = 0
    for p in probabilities:
        res += p*np.log2(p)
    res = 0 - res
    return res 
    pass