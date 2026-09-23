import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """

    res = np.zeros(len(vectors[0]))
    
    for i, v1 in enumerate(vectors):
        for j, v2 in enumerate(v1):
            res[j] += v2 * coefficients[i]
    return res