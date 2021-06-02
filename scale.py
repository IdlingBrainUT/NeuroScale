import numpy as np
from numpy.core.numeric import zeros_like

def scale_data(data:np.ndarray):
    n = (data > 0).sum(axis=0)
    lamb = n / data.sum(axis=0)
    return data * lamb

def scale_data_session(data:np.ndarray, session_sizes:list):
    stack = []
    row = 0
    mu = data.mean()
    epsilon = mu * 1e-7
    for ni in session_sizes:
        d = data[row:row+ni, :]
        lamb = ni / (d.sum(axis=0) + epsilon)
        stack.append(d * lamb)
    return np.vstack(stack)