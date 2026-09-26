import numpy as np

def matrix_rank(A: list) -> int:
    """
    Returns the numerical rank as a Python integer.
    """
    m = len(A)
    n = len(A[0])

    singular_values = np.linalg.svd(A, compute_uv=False)

    o_max = max(singular_values)
    epsilon = np.finfo(np.float64).eps

    tau = max(m, n) * o_max * epsilon

    print(np.count_nonzero([i for i in singular_values if i > tau]))

    return int(np.count_nonzero(singular_values > tau))

    
    