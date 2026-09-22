import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    res = 0
    for i, v in enumerate(x):
        res += abs(v - y[i])
    return float(res)