import numpy as np

def check_session_range(data:np.ndarray, sessions:list):
    row, _ = data.shape
    all_session = sum(sessions)
    if row == all_session:
        return
    else:
        raise ValueError("Inconsistent length of data!: data={} sum_of_sessions={}".format(row, all_session))
