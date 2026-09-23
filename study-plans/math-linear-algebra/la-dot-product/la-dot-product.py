import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """

    res = 0
    
    for i, v in enumerate(x):
        res += v * y[i]

    return float(res)
        