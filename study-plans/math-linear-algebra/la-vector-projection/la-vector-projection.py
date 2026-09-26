import numpy as np

def vector_projection(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 projection of u onto v.
    """
    return ((np.dot(u, v) / np.dot(v, v)) * np.array(v, dtype='float64'))