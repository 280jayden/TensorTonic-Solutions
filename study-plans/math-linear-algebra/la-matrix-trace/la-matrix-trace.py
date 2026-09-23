import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """
    res = 0

    for i in range(len(A)):
        res += A[i][i]

    return float(res)