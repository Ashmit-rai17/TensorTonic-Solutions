import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.array(x)
    maxn = np.max(x , axis=-1 , keepdims = True)
    sum_probs = np.sum(np.exp(x-maxn) , axis=-1 , keepdims = True)
    return np.exp(x-maxn)/sum_probs
    pass