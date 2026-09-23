import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """

    res = np.zeros(len(vectors[0]))
    
    for i, value in enumerate(vectors):
        for j, v in enumerate(value):
            res[j] += v * coefficients[i]
    return res