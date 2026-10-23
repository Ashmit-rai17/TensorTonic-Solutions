import numpy as np

def information_gain(y: list, split_mask: list) -> float:
    """
    Returns the information gain as a float.
    """
    # Write code here
    y = np.array(y)
    split_mask = np.array(split_mask)
    def prob(x):
        _ , count = np.unique(x , return_counts = True)
        probabilities = count / len(x)
        return probabilities
    yl = y[split_mask]
    yr = y[~split_mask]
    def h(x):
        return -np.sum(prob(x)*np.log2(prob(x)))
    return h(y) - (len(yl)/len(y))*h(yl) - (len(yr)/len(y))*h(yr)
    pass