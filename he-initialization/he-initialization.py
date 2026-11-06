import math

def he_initialization(W: list, fan_in: int) -> list:
    """
    Returns the weights mapped to the He uniform range.
    """
    # Write code here
    L = math.sqrt(6 / (fan_in))
    wdash = [[0.0 for _ in range(len(W[0]))] for _ in range(len(W))]
    for i in range(len(W)):
        for j in range(len(W[0])):
            wdash[i][j] += W[i][j]*2*L - L
    return wdash
    pass