import numpy as np
import math

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """

    dot = 0

    for i, v in enumerate(a):
        dot += v * b[i]


    norm1= 0

    for i in a:
        norm1 += i**2

    norm2 = 0
    for i in b:
        norm2 += i**2

    norm1, norm2 = math.sqrt(norm1), math.sqrt(norm2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot / (norm1 * norm2)