import numpy as np

def matrix_multiply(A: list, B: list) -> np.ndarray:
    """
    Returns the matrix product as a float64 array.
    """

    res = np.zeros((len(A), len(B[0])), dtype='float64')
    B = np.array(B)

    for i, row in enumerate(A):
        for j in range(len(B[0])):
            res[i, j] = np.dot(row, B[:, j])

    return res
            
        
    