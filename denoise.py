import numpy as np
from scipy.signal import butter, filtfilt

def remove_bg_noise(data:np.ndarray, highpass:float=0.1, ca_fs:int=20, row_is_cell:bool=True):
    b, a = butter(1, highpass/(ca_fs/2), "high")
    if row_is_cell:
        d = filtfilt(b, a, data, axis=0)
    else:
        d = filtfilt(b, a, data, axis=1)
    d[d < 0] = 0
    return d