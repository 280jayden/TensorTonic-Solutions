import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 outer-product matrix.
    """

    res = np.zeros((len(u), len(v)), dtype='float64')

    for i, value1 in enumerate(u):
        for j, value2 in enumerate(v):
            res[i][j] = value1 * value2
    return res
    