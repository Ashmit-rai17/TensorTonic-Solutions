import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)
    rng = np.random.default_rng(seed)
    indices = np.arange(len(X))
    res = rng.shuffle(indices)
    for i in range(0 , len(X) , batch_size):
        batch_idx = indices[i : i + batch_size]
        if drop_last and len(batch_idx) < batch_size:
            break
        X_batch = X[batch_idx]
        y_batch = y[batch_idx]
        yield (X_batch , y_batch)
    pass