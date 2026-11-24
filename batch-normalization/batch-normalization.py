import numpy as np

def batch_norm_forward(x: list, gamma: list, beta: list, eps: float = 1e-5) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    axes = (0,) if x.ndim==2 else (0,2,3)
    if x.ndim ==4:
        gamma = gamma.reshape(1 , -1 , 1 , 1 )
        beta = beta.reshape(1 , -1 , 1 , 1)
    mu = np.mean(x , axis=axes , keepdims=True)
    std = np.std(x , axis=axes , keepdims=True)
    xcap = (x - mu)/np.sqrt(std**2 + eps)
    return gamma*xcap + beta
    pass