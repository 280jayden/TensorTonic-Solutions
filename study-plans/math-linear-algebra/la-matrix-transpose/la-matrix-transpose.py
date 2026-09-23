import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transpose as a float64 array.
    """

    x, y = len(A), len(A[0])
    
    res = np.zeros((y, x), dtype='float64')

    for i, v1 in enumerate(A):
        for j, v2 in enumerate(v1):
            res[j][i] = A[i][j]
    return res