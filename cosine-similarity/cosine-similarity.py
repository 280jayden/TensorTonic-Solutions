import numpy as np
import math

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dot_prod = 0
    for i, v in enumerate(a):
        dot_prod += v * b[i]

    norm_a, norm_b = 0, 0

    for i in a:
        norm_a += i ** 2
    norm_a = math.sqrt(norm_a)

    for i in b:
        norm_b += i ** 2
    norm_b = math.sqrt(norm_b)

    if norm_b == 0 or norm_a == 0:
        return 0.0

    res = dot_prod / (norm_a * norm_b)
    return res
    
    