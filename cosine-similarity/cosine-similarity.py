import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    vec_a = np.array(a , dtype=float)
    vec_b = np.array(b , dtype = float)
    dot_prod = np.dot(vec_a , vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    if norm_a==0 or norm_b==0:
        return 0.0
    cos = dot_prod/(norm_a*norm_b)
    return float(cos)
    pass