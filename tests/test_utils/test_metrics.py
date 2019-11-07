import pytest

import numpy as np

from motor_dynamics.utils.metrics import (r2, rmsle, rmse, mae, smape, sc,
                                          smape_vs_sc)


def test__r2():
    y_true = np.asarray([0, 1, 0])
    y_pred = np.asarray([0, 1, 0])

    r2_err = r2(y_true, y_pred)

    assert r2_err == 1.0


def test__rmsle():
    y_true = np.asarray([0, 1, 0])
    y_pred = np.asarray([0, 1, 0])

    rmsle_err = rmsle(y_true, y_pred)

    assert rmsle_err >= 0


def test__rmse():
    y_true = np.asarray([0, 1, 0])
    y_pred = np.asarray([0, 1, 0])

    rmse_err = rmse(y_true, y_pred)

    assert rmse_err == 0


def test__mae():
    y_true = np.asarray([0, 1, 0])
    y_pred = np.asarray([0, 1, 0])

    mae_err = mae(y_true, y_pred)

    assert mae_err == 0


def test__smape():
    y_true = np.asarray([0, 1, 0])
    y_pred = np.asarray([0, 1, 0])

    smape_err = smape(y_true, y_pred)

    assert smape_err == 0


def test__sc():
    y_true = np.asarray([0, 1, 0])

    sc_val = sc(y_true)

    assert sc_val == 2


def test__smape_vs_sc():
    y_true = np.asarray([0, 1, 0, 1])
    y_pred = np.asarray([0, 1, 0, 1])

    smape_vs_sc_vals = smape_vs_sc(y_true, y_pred, 2)

    assert isinstance(smape_vs_sc_vals, np.ndarray)
    assert smape_vs_sc_vals.any()
    assert smape_vs_sc_vals.shape == (1, 2)
