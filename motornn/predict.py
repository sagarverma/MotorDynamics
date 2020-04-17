import os
import argparse
import pickle

import numpy
import torch
import torch.nn as nn

from motornn.utils.dataloader import normalize, denormalize
from motornn.models.ffnn import ShallowFNN
from motornn.models.encdec import EncDecDiagBiRNNSkip
from motormetrics.ml import *
from motormetrics.ee import *


def get_loader_transform_types(model):
    if isinstance(model, ShallowFNN):
        return 'flat', 'flat'
    if isinstance(model, EncDecDiagBiRNNSkip):
        return 'seq', 'seq'

def compute_metrics(data, model_speed, model_torque):
    ref_speed = data['reference_speed']
    ref_torque = data['reference_torque']
    ref_speed_t = data['speed_time']
    ref_torque_t = data['torque_time']

    ref_speed_interp = data['reference_speed_interp']
    ref_torque_interp = data['reference_torque_interp']

    sim_speed = data['speed']
    sim_torque = data['torque']

    sim_time = data['time']

    ramp_scopes = get_ramps_from_raw_reference(ref_speed, ref_speed_t)

    ramp_start_times = []
    perc2_times = []
    model_perc2_times = []
    perc95_times = []
    model_perc95_times = []
    following_errs = []
    model_following_errs = []
    following_times = []
    model_following_times = []
    overshoot_errs = []
    model_overshoot_errs = []
    overshoot_times = []
    model_overshoot_times = []
    sse_errs = []
    model_sse_errs = []
    sse_times = []
    model_sse_times = []
    max_trq_accs = []
    model_max_trq_accs = []
    max_trq_acc_times = []
    model_max_trq_acc_times = []

    for ramp_scope in ramp_scopes:
        sim_ramp_scope = get_ramp_from_sim_reference(sim_time, ramp_scope)

        first_value = ref_speed_interp[sim_ramp_scope[0]]

        ref_speed_scope = ref_speed_interp[sim_ramp_scope[1]: sim_ramp_scope[-1] + 1]
        sim_speed_scope = sim_speed[sim_ramp_scope[1]: sim_ramp_scope[-1] + 1]
        model_speed_scope = model_speed[sim_ramp_scope[1]: sim_ramp_scope[-1] + 1]
        sim_time_scope = sim_time[sim_ramp_scope[1]: sim_ramp_scope[-1] + 1]
        ramp_start_times.append(sim_time[sim_ramp_scope[1]])

        ref_speed_scope, sim_speed_scope = mirror(ref_speed_scope, sim_speed_scope, first_value)
        ref_speed_scope, model_speed_scope = mirror(ref_speed_scope, model_speed_scope, first_value)

        perc2_time = response_time_2perc(ref_speed_scope,
                            sim_speed_scope, sim_time_scope)
        model_perc2_time = response_time_2perc(ref_speed_scope,
                            model_speed_scope, sim_time_scope)
        perc2_times.append(round(perc2_time, 5))
        model_perc2_times.append(round(model_perc2_time, 5))

        perc95_time = response_time_95perc(ref_speed_scope,
                            sim_speed_scope, sim_time_scope)
        model_perc95_time = response_time_95perc(ref_speed_scope,
                            model_speed_scope, sim_time_scope)
        perc95_times.append(round(perc95_time, 5))
        model_perc95_times.append(round(model_perc95_time, 5))

        following_err, following_time = following_error(ref_speed_scope,
                                        sim_speed_scope, sim_time_scope)
        model_following_err, model_following_time = following_error(ref_speed_scope,
                                        model_speed_scope, sim_time_scope)
        following_errs.append(round(following_err,4))
        following_times.append(round(following_time, 5))
        model_following_errs.append(round(model_following_err,4))
        model_following_times.append(round(model_following_time, 5))

        minn = min(ref_speed_scope)
        maxx = max(ref_speed_scope)

        ref_speed_scope = ref_speed_interp[sim_ramp_scope[2]: sim_ramp_scope[-1] + 1]
        sim_speed_scope = sim_speed[sim_ramp_scope[2]: sim_ramp_scope[-1] + 1]
        model_speed_scope = model_speed[sim_ramp_scope[2]: sim_ramp_scope[-1] + 1]
        sim_time_scope = sim_time[sim_ramp_scope[2]: sim_ramp_scope[-1] + 1]

        ref_speed_scope, sim_speed_scope = mirror(ref_speed_scope, sim_speed_scope,
                                                    first_value)
        ref_speed_scope, model_speed_scope = mirror(ref_speed_scope, model_speed_scope,
                                                    first_value)

        overshoot_err, overshoot_time = overshoot(ref_speed_scope, sim_speed_scope,
                                        minn, maxx, sim_time_scope)
        model_overshoot_err, model_overshoot_time = overshoot(ref_speed_scope, model_speed_scope,
                                        minn, maxx, sim_time_scope)

        overshoot_errs.append(round(overshoot_err,4))
        overshoot_times.append(round(overshoot_time, 5))
        model_overshoot_errs.append(round(model_overshoot_err,4))
        model_overshoot_times.append(round(model_overshoot_time, 5))

        sse_err, sse_time = steady_state_error(ref_speed_scope, sim_speed_scope,
                                                sim_time_scope)
        model_sse_err, model_sse_time = steady_state_error(ref_speed_scope, model_speed_scope,
                                                sim_time_scope)

        sse_errs.append(round(sse_err, 4))
        sse_times.append(round(sse_time, 5))
        model_sse_errs.append(round(model_sse_err, 4))
        model_sse_times.append(round(model_sse_time, 5))

        sim_torque_scope = sim_torque[sim_ramp_scope[0]: sim_ramp_scope[-1] + 1]
        sim_time_scope = sim_time[sim_ramp_scope[0]: sim_ramp_scope[-1] + 1]
        model_torque_scope = model_torque[sim_ramp_scope[0]: sim_ramp_scope[-1] + 1]

        max_trq_acc, max_trq_acc_time = max_torque_acceleration(sim_torque_scope,
                                        sim_time_scope)
        model_max_trq_acc, model_max_trq_acc_time = max_torque_acceleration(model_torque_scope,
                                        sim_time_scope)

        max_trq_accs.append(round(max_trq_acc, 4))
        max_trq_acc_times.append(round(max_trq_acc_time, 5))
        model_max_trq_accs.append(round(model_max_trq_acc, 4))
        model_max_trq_acc_times.append(round(model_max_trq_acc_time, 5))

    return {'perc2_times': perc2_times,
            'perc95_times': perc95_times,
            'following_errs': following_errs,
            'following_times': following_times,
            'overshoot_errs': overshoot_errs,
            'overshoot_times': overshoot_times,
            'ramp_start_times': ramp_start_times,
            'sse_errs': sse_errs,
            'sse_times': sse_times,
            'max_trq_accs': max_trq_accs,
            'max_trq_acc_times': max_trq_acc_times,
            'model_perc2_times': model_perc2_times,
            'model_perc95_times': model_perc95_times,
            'model_following_errs': model_following_errs,
            'model_following_times': model_following_times,
            'model_overshoot_errs': model_overshoot_errs,
            'model_overshoot_times': model_overshoot_times,
            'model_sse_errs': model_sse_errs,
            'model_sse_times': model_sse_times,
            'model_max_trq_accs': model_max_trq_accs,
            'model_max_trq_acc_times': model_max_trq_acc_times}

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
            inp_data_mod = inp_data[:, i:i+window]
            if inp_trf_typ == 'flat':
                inp_data_mod = inp_data_mod.flatten()
            samples.append(inp_data_mod)

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

def load_data(opt):
    fin = open(opt.benchmark_file, 'rb')
    data = pickle.load(fin)
    fin.close()

    return data

def load_model(opt):
    model = torch.load(opt.model_file).cuda(0)
    model = model.eval()

    return model

def get_arg_parse():
    parser = argparse.ArgumentParser(description='Test on custom benchmark.')
    parser.add_argument('--model_file', required=True, type=str)
    parser.add_argument('--benchmark_file', type=str, required=True, help='benchmark file')
    parser.add_argument('--window', type=int, required=True, help='input window')
    parser.add_argument('--save_dir', type=str, required=True, help='directory where results are saved')
    args = parser.parse_args()
    return args

args = get_arg_parse()
model = load_model(args)
data = load_data(args)
speed_denormed, torque_denormed, speed_ml_metrics, torque_ml_metrics = predict(model, data, args.window)
print ('Speed ML Metrics', speed_ml_metrics)
print ('Torque ML Metrics', torque_ml_metrics)
ee_metrics = compute_metrics(data, speed_denormed, torque_denormed)

print ('Quantity', 'Simulation', 'Model')
print ('2% time', ee_metrics['perc2_times'][0], ee_metrics['model_perc2_times'][0])
print ('95% time', ee_metrics['perc95_times'][0], ee_metrics['model_perc95_times'][0])
print ('Overshoot', ee_metrics['overshoot_errs'][0], ee_metrics['model_overshoot_errs'][0])
print ('Following Error', ee_metrics['following_errs'][0], ee_metrics['model_following_errs'][0])
print ('Steady State Error', ee_metrics['sse_errs'][0], ee_metrics['model_sse_errs'][0])
print ('Max Acc Torque', ee_metrics['max_trq_accs'][0], ee_metrics['model_max_trq_accs'][0])

if not os.path.exists(args.save_dir):
    os.makedirs(args.save_dir)

fout = open(os.path.join(args.save_dir, args.model_file.split('/')[-1].replace('.pt','.pkl')),'wb')
pickle.dump([speed_denormed, torque_denormed], fout)
fout.close()
