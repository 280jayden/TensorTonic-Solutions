import numpy as np

def create_filled_array(shape: list, kind: str) -> np.ndarray:
    """
    Returns a 2D float64 array of zeros or ones with the requested shape.
    """
    if kind == 'ones':
        return np.ones((shape[0], shape[1]), dtype='float64')
    return np.zeros((shape[0], shape[1]), dtype='float64')
