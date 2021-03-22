import numpy as np

def add_null(data:np.ndarray, null_size=100):
    n_row, _ = data.shape
    n = (data > 0).sum(axis=0)
    pr = n / n_row
    pr_mu = pr.mean()
    pr_sigma = pr.std()

    null_pr = np.random.normal(size=null_size, loc=pr_mu, scale=pr_sigma)
    null_uni = np.random.random((n_row, null_size))
    null_exp = -np.log(np.random.random((n_row ,null_size)))
    null = null_exp
    null[null_uni >= null_pr] = 0
    return np.hstack((data, null))