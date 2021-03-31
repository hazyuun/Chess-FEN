import numpy as np
from collections import Counter


def data_get_occurences(data):
    unique, counts = np.unique(data, return_counts=True)
    return dict(zip(unique, counts))


def data_get_top2(d):
    c = Counter(d)
    most_common = c.most_common(2)
    return most_common


def data_get_last(d):
    c = Counter(d)
    least_common = c.most_common()[-1]
    return least_common


def data_balance1(x, y, ab='.'):
    top2 = data_get_top2(y)
    dots = top2[0][1]
    max = top2[1][1]
    indices = [i for i, x in enumerate(y) if x == ab]
    x = np.delete(x, indices[:(dots-max)], axis=0)
    y = np.delete(y, indices[:(dots-max)], axis=0)
    return x, y


def data_balance2(x, y, ab='.'):
    min = data_get_last(y)[1]
    occ = data_get_occurences(y)
    for t in occ:
        indices = [i for i, x in enumerate(y) if x == t]
        x = np.delete(x, indices[:(occ[t]-min)], axis=0)
        y = np.delete(y, indices[:(occ[t]-min)], axis=0)
    return x, y
