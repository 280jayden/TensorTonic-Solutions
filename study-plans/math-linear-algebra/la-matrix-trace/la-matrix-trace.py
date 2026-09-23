import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """
    res = 0

    for i, v1 in enumerate(A):
        for j, v2 in enumerate(v1):
            if j == i:
                res += v2

    return float(res)