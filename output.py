import numpy as np
from util import check_session_range

def save_sessions(data:np.ndarray, session_sizes:list, session_names:list):
    check_session_range(data, session_sizes)
    t = 0
    for s, n in zip(session_sizes, session_names):
        np.savetxt(n+".csv", data[t:t+s], delimiter=",")
        t += s
    return