import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    vec = np.array(matrix)
    if norm_type=="l1":
        type = 1
    elif norm_type=="l2":
        type = 2
    else:
        type = np.inf
    if axis is None:
        norm = np.linalg.norm(vec.ravel() , ord = type)
        np.where(norm==0 , 1.0 , norm)
    else:
        norm = np.linalg.norm(vec , axis=axis , ord=type , keepdims=True)
        norm = np.where(norm==0 , 1.0 , norm)
    return vec/norm
    pass