import numpy as np

def hadamard_product(A: list, B: list) -> np.ndarray:
    """
    Returns the element-wise product as a float64 array.
    """

    res = np.zeros((len(A), len(A[0])))

    for i, row in enumerate(A):
        for j, col in enumerate(row):
            res[i][j] = A[i][j] * B[i][j]

    return res
        