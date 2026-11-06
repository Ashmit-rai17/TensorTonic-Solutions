import math

def xavier_initialization(W: list, fan_in: int, fan_out: int) -> list:
    """
    Returns the weights mapped to the Xavier uniform range.
    """
    # Write code here
    L = math.sqrt(6 / (fan_in + fan_out))
    wdash = [[0.0 for _ in range(len(W[0]))] for _ in range(len(W))]
    for i in range(len(W)):
        for j in range(len(W[0])):
            wdash[i][j] += W[i][j]*2*L - L
    return wdash
    pass