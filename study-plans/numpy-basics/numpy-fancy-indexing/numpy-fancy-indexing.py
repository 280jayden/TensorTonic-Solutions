import numpy as np

def select_by_index(arr: list, indices: list, axis: int) -> np.ndarray:

    arr = np.array(arr, dtype='float64')
    
    if axis == 0: # rows
        return arr[indices, :]
    else:
        return arr[:, indices]
    