import numpy as np

def knn_distance(X_train: list, X_test: list, k: int) -> np.ndarray:
    """
    Returns a NumPy array with shape (n_test, k).
    """
    # Write code here
    train = np.array(X_train)
    test = np.array(X_test)
    if train.ndim == 1:
        train = train[: , np.newaxis]
    if test.ndim == 1:
        test = test[: , np.newaxis]
    n_train = train.shape[0]
    n_test = test.shape[0]
    d = test[: , None , :] - train[None , : , :]
    d = np.sqrt(np.sum(d**2 , axis=2))
    indices = np.argsort(d , axis=1)
    if k > n_train:
        padded = np.full((n_test , k) , -1 , indices.dtype)
        padded[: , :n_train] = indices[: , :n_train]
        return padded[: , :k]
    else:
        return indices[: , :k]
    pass