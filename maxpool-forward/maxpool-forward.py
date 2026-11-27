def maxpool_forward(X: list, pool_size: int, stride: int) -> list:
    """
    Returns the maximum value from every pooling window.
    """
    # Write code here
    W = len(X[0])
    H = len(X)
    Hout = ((H-pool_size)//stride)+1
    Wout = ((W-pool_size)//stride)+1
    out = [[0 for _ in range(Wout)] for _ in range(Hout)]
    for i in range(Hout):
        row = []
        for j in range(Wout):
            current_max = float('-inf')
            for a in range(pool_size):
                for b in range(pool_size):
                    val = X[i*stride + a][j*stride + b]
                    if val > current_max:
                        current_max = val
            out[i][j] = current_max
    return out
    pass