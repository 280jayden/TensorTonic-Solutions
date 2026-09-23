import numpy as np
import math

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    euclid = 0
    
    for i, v in enumerate(x):
        euclid += (v - y[i])**2

    return math.sqrt(euclid)