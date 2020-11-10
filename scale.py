import numpy as np

def scale_data(data:np.ndarray):
    n = (data > 0).sum(axis=0)
    lamb = n / data.sum(axis=0)
    return data * lamb