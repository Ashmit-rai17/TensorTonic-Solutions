import numpy as np

def focal_loss(p, y, gamma=2.0):
    p = np.asarray(p, dtype=float)
    y = np.asarray(y, dtype=float)
    p = np.clip(p, 1e-15, 1.0 - 1e-15)
    positive = (1.0 - p) ** gamma * y * np.log(p)
    negative = p ** gamma * (1.0 - y) * np.log1p(-p)
    return float(np.mean(-(positive + negative)))