import numpy as np
import math

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """

    res = 0
    
    for i, v in enumerate(x):
        res += (v - y[i])**2
    
    return math.sqrt(res)