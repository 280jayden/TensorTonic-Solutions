import numpy as np

def matrix_vector_multiply(A: list, x: list) -> np.ndarray:
    """
    Returns the matrix-vector product as a float64 array.
    """

    res = np.zeros(len(A), dtype='float64')

    for i, v1 in enumerate(A):
        #print(np.dot(v1, x))
        res[i] = np.dot(v1, x)

    return res