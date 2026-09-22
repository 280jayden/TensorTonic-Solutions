import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    """
    Returns a seeded 2D float64 random array with the requested shape.
    """
    # need a generator
    rng = np.random.default_rng(seed=seed)

    if kind == 'uniform':
        return rng.random((shape[0], shape[1]))
    return rng.normal(0, 1, (shape[0], shape[1]))