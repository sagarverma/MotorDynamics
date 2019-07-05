import math

import numpy as np

from sklearn.metrics import r2_score, mean_absolute_error


def r2(y_true, y_pred):
    return r2_score(y_true, y_pred)


def rmsle(y_true, y_pred):
	assert len(y_true) == len(y_pred)
	terms_to_sum = [(math.log(y_pred[i] + 1) - math.log(y_true[i] + 1)) ** 2.0 \
                    for i, pred in enumerate(y_pred)]
	return (sum(terms_to_sum) * (1.0/len(y_true))) ** 0.5


def rmse(y_true, y_pred):
    return np.sqrt(((y_pred - y_true) ** 2).mean())


def mae(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)


def smape(y_true, y_pred):
    return 100.0/ len(y_true) * np.sum(2.0 * np.abs(y_pred - y_true) / \
           (np.abs(y_true) + np.abs(y_pred) + 0.00001))


def sc(signal):
    return np.sum(abs(signal[1:] - signal[:-1]))


def smape_vs_sc(y_true, y_pred, window):
    smape_vs_sc_all_windows = []

    for i in range(0, y_true.shape[0]):
        if i + window + 1 < y_true.shape[0]:
            smape_val = smape(y_true[i: i + window], y_pred[i: i + window])
            sc_val = sc(y_true[i : i + window])
            smape_vs_sc_all_windows.append([smape_val, sc_val])

    return np.asarray(smape_vs_sc_all_windows)
