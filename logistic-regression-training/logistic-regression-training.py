import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    X = np.array(X)
    y = np.array(y)
    w = np.zeros(X.shape[1])
    b = 0.0
    for _ in range(steps):
        p = _sigmoid((np.dot(X , w) + b))
        L = -1/(len(X))*(y*np.log(p) + (1-y)*np.log(1-p))
        dldw = np.dot(np.transpose(X) , (p-y))/len(X)
        dldb = np.sum((p-y))/len(X)
        w -= lr*dldw
        b -= lr*dldb
    return [w , b]
    # Write code here
    pass