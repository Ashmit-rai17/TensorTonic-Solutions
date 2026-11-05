def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    # Write code here
    res = [[0.0 for _ in range(len(W[0]))] for _ in range(len(X))]
    for i  in range(len(X)):
        for j in range(len(W[0])):
            for k in range(len(X[0])):
                res[i][j] += X[i][k]*W[k][j]
            res[i][j] += b[j]
    return res
            
    pass