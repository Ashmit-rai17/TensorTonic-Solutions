import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    # Write code here
    x = np.array(x)
    if rng is None:
        randoms = np.random.random(x.shape)
    else:
        randoms = rng.random(x.shape)
    pattern = np.where(randoms < p , 0.0 , 1/(1-p))
    x = x*pattern
    return (x , pattern)
    pass