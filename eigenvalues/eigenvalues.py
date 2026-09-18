import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    X = np.array(matrix)
    return np.sort(np.real(np.linalg.eigvals(matrix)))
    pass