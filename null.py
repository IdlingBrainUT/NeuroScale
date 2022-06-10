import numpy as np
from numpy import random

def add_null(data:np.ndarray, null_size=100):
    n_row, _ = data.shape
    n = (data > 0).sum(axis=0)
    pr = n / n_row
    pr_mu = pr.mean()
    pr_sigma = pr.std()

    null_pr = np.random.normal(size=null_size, loc=pr_mu, scale=pr_sigma)
    null_uni = np.random.random((n_row, null_size))
    null_exp = -np.log(np.random.random((n_row ,null_size))) * 10
    null = null_exp
    null[null_uni >= null_pr] = 0
    return np.hstack((data, null))

def gen_null(data:np.ndarray, session_sizes:list, null_size=100, z_th = 0.001):
    n_row, n_col = data.shape
    r = np.random.randint(n_col, size=null_size)
    null = np.zeros((n_row, null_size))
    for i, ri in enumerate(r):
        row = 0
        for ni in session_sizes:
            lamb_inv = 1.0
            tau_inv = 1.0
            nla = 0
            nla_pre = 0
            spike = []
            nta = 0
            pre = 0.0
            for xi in data[row:row+ni, ri]:
                if xi > 0:
                    la_rand = np.random.exponential(scale=lamb_inv)
                    ta_rand = np.random.exponential(scale=tau_inv)
                    c_neg = pre * np.exp(-ta_rand)
                    c_pos = la_rand + pre * np.exp(-ta_rand)
                    is_neg = np.inf
                    if c_neg > 0:
                        is_neg = c_neg / xi - np.log(c_neg / xi) - 1
                    is_pos = c_pos / xi - np.log(c_pos / xi) - 1
                    if xi > pre or is_pos < is_neg:
                        la_new = xi - c_neg
                        lamb_inv = (nla * lamb_inv + la_new) / (nla + 1)
                        tau_inv = (nta * tau_inv + ta_rand) / (nta + 1)
                        nla += 1
                        nta += 1
                    else:
                        ta_new = -np.log(xi / pre)
                        tau_inv = (nta * tau_inv + ta_new) / (nta + 1)
                        nta += 1
                spike.append(nla - nla_pre)
                nla_pre = nla
                pre = xi
            s_num = np.array([0, 0])
            s_den = np.array([0, 0])
            for j in range(ni - 1):
                s_num[spike[j]] += spike[j+1]
                s_den[spike[j]] += 1
            rate = s_num / s_den

            now = 0
            rate_pre = 0
            for j in range(ni):
                now *= np.exp(-1/np.random.exponential(scale=tau_inv))
                if np.random.random() < rate[rate_pre]:
                    now += random.exponential(scale=lamb_inv)
                    rate_pre = 1
                else:
                    rate_pre = 0
                if now < z_th:
                    now = 0
                null[row+j, i] = now
            row += ni

    return np.hstack((data, null))