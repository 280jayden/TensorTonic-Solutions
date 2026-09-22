import numpy as np
import math

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    l1 = 0
    l2 = 0
    linf = 0

    for i in v:
        l1 += abs(i)
        l2 += i**2

    l2 = math.sqrt(l2)
    
    linf = max(abs(i) for i in v)
    
    return np.array([l1, l2, linf], dtype='float64')