import numpy as np
from util import check_session_range

def binning_data(data:np.ndarray, bin_size:int=4, mode="mean"):
    n_row, n_col = data.shape
    n = int(np.ceil(n_row/bin_size))
    data_bin = np.zeros((n, n_col))
    for i in range(n):
        if mode == "mean":
            data_bin[i, :] = data[bin_size*i:bin_size*(i+1)].mean(axis=0)
        elif mode == "max":
            data_bin[i, :] = data[bin_size*i:bin_size*(i+1)].max(axis=0)
        else:
            raise ValueError("Unknown mode!")
    return data_bin

def binning_data_sessions(
        data:np.ndarray, bin_size:int=4,
        sessions:list=[], mode="mean"):
    check_session_range(data, sessions)
    _, n_col = data.shape
    binned_sizes = [int(np.ceil(i/bin_size)) for i in sessions]
    n = sum(binned_sizes)
    data_bin = np.zeros((n, n_col))
    t = 0
    bt = 0
    for s, bs in zip(sessions, binned_sizes):
        data_bin[bt:bt+bs] = binning_data(data[t:t+s], bin_size=bin_size, mode=mode)
        bt += bs
        t += s
    return data_bin