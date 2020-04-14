import os

import numpy
import torch
import torch.nn as nn

from motornn.utils.dataloader import normalize, denormalize
from motornn.models.ffnn import ShallowFNN
from motornn.models.encdec import EncDecDiagBiRNNSkip
from motormetrics.ml import *

def get_loader_transform_types(model):
    if isinstance(model, ShallowFNN):
        return 'flat', 'flat'
    if isinstance(model, EncDecDiagBiRNNSkip):
        return 'seq', 'seq'

def predict(model, data, window):
    metadata = {"min": {"voltage_d": -113.32642347073255, "voltage_q": -326.5986323710904, "current_d": -5.093863046306245, "current_q": -18.620089841080084, "torque": -225.77387560757103, "speed": -78.36573196887844, "statorPuls": -75.49294574023405, "time": 0.0, "reference_torque_interp": -119.85271837136129, "reference_speed_interp": -69.91498492993017, "reference_torque": -119.85271837136129, "reference_speed": -69.91498492993017, "torque_time": 0.0, "speed_time": 0.0}, "max": {"voltage_d": 104.2551972429801, "voltage_q": 326.5986323710904, "current_d": 8.461554137463365, "current_q": 18.160159823846662, "torque": 225.71019912125365, "speed": 77.7049747270389, "statorPuls": 75.09130896631866, "time": 109.4945, "reference_torque_interp": 119.7513513986357, "reference_speed_interp": 69.76198701954684, "reference_torque": 119.7513513986357, "reference_speed": 69.76198701954684, "torque_time": 109.49471143946505, "speed_time": 109.49471143946505}, "mean": {"voltage_d": 9.003071958162886, "voltage_q": -2.4178692534379818, "current_d": 6.308971140979901, "current_q": 0.19328783771928326, "torque": 1.5370578339811476, "speed": 0.18783987142976483, "statorPuls": 0.2299965732910069, "time": 38.94373999999999, "reference_torque_interp": -2.2920262517508387, "reference_speed_interp": 0.19234474366209212, "reference_torque": -3.000290228983823, "reference_speed": -1.5599456580091273, "torque_time": 32.79873976958612, "speed_time": 34.68157650605395}}

    inp_trf_typ, out_trf_typ = get_loader_transform_types(model)

    inp_data = []
    for inp_quant in ['voltage_d','voltage_q','current_d','current_q']:
        quantity = data[inp_quant]
        minn = metadata['min'][inp_quant]
        maxx = metadata['max'][inp_quant]
        inp_data.append(normalize(quantity, minn, maxx))

    inp_data = np.asarray(inp_data)
    if inp_trf_typ == 'flat':
        inp_data = inp_data.flatten()

    out_data = []
    for out_quant in ['speed', 'torque']:
        quantity = data[out_quant]
        minn = metadata['min'][out_quant]
        maxx = metadata['max'][out_quant]
        out_data.append(normalize(quantity, minn, maxx))

    out_data = np.asarray(out_data)

    samples = []
    for i in range(inp_data.shape[1]):
        if (i + window) < inp_data.shape[1]:
            samples.append(inp_data[:, i:i+window])

    preds = []
    for i in range(0, len(samples), 2000):
        batch_inp = torch.tensor(np.asarray(samples[i:i+2000])).float().cuda(0)
        out = model(batch_inp)
        preds.append(out.data.cpu().numpy())

    preds = np.concatenate(preds, axis=0)

    if out_trf_typ == 'seq':
        speed_preds = preds[:, 0, window//2].flatten()
        torque_preds = preds[:, 1, window//2].flatten()
    if out_trf_typ == 'flat':
        speed_preds = preds[:, 0].flatten()
        torque_preds = preds[:, 1].flatten()

    speed_true = out_data[0, :].flatten()
    torque_true = out_data[1, :].flatten()

    speed_preds = np.concatenate((speed_true[:100], speed_preds), axis=0)
    torque_preds = np.concatenate((torque_true[:100], torque_preds), axis=0)

    speed_ml_metrics = {}
    speed_ml_metrics['smape'] = smape(speed_true, speed_preds)
    speed_ml_metrics['r2'] = r2(speed_true, speed_preds)
    speed_ml_metrics['rmse'] = rmse(speed_true, speed_preds)
    speed_ml_metrics['mae'] = mae(speed_true, speed_preds)

    torque_ml_metrics = {}
    torque_ml_metrics['smape'] = smape(torque_true, torque_preds)
    torque_ml_metrics['r2'] = r2(torque_true, torque_preds)
    torque_ml_metrics['rmse'] = rmse(torque_true, torque_preds)
    torque_ml_metrics['mae'] = mae(torque_true, torque_preds)

    minn = metadata['min']['speed']
    maxx = metadata['max']['speed']
    speed_denormed = denormalize(speed_preds, minn, maxx)

    minn = metadata['min']['torque']
    maxx = metadata['max']['torque']
    torque_denormed = denormalize(torque_preds, minn, maxx)

    return speed_denormed, torque_denormed, speed_ml_metrics, torque_ml_metrics
