import numpy as np

def conv2d(x: list, W: list, b: list) -> np.ndarray:
    """
    Returns the convolved batch as a floating-point NumPy array.
    """
    # Write code 
    x = np.array(x)
    w = np.array(W)
    b = np.array(b)
    n = x.shape[0]
    cin = x.shape[1]
    h = x.shape[2]
    width = x.shape[3]
    cout = w.shape[0]
    cin_w = w.shape[1]
    kh = w.shape[2]
    kw = w.shape[3]
    output = np.zeros((n , cout , h-kh+1 , width-kw+1))
    for k in range(n):
        for f in range(cout):
            for i in range(h-kh+1):
                for j in range(width-kw+1):
                    patch = x[k , : , i : i + kh , j:j+kw]
                    output[k , f , i , j] = np.sum(patch*w[f]) + b[f]
    return output
    pass