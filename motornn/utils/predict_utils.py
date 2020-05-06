import pickle

import numpy
import torch
import torch.nn as nn

from motornn.utils.dataloader import normalize, denormalize
from motornn.models.ffnn import ShallowFNN
from motornn.models.encdec import EncDecDiagBiRNNSkip

from motormetrics.ml import *
from motormetrics.ee import *

from motorrefgen.experiment import Experiment
from motorrefgen.config import ExperimentConfig

from motorsim.simconfig import SimConfig
from motorsim.simulators.conn_python import Py2Mat


def generate(reference_speed, speed_time,
             reference_torque, torque_time,
             sim_rate):
    """Generate trajectory from the passed argument.

    Parameters
    ----------
    opt : args
        Parsed arguments.

    Returns
    -------
    None

    """
    config = ExperimentConfig(integral=False, simulate=True)
    experiment = Experiment(config)

    reference = {'reference_speed': reference_speed,
                 'speed_time':  speed_time,
                 'reference_torque':  reference_torque,
                 'torque_time':  torque_time}
    experiment.set_manual_reference(reference)

    simconfig = SimConfig()
    simconfig.set_config_from_json({'Data_Ts': sim_rate})
    py2mat = Py2Mat(simconfig)

    experiment.simulate(simulator=py2mat)
    simulation_data = experiment.get_simulation_data()

    return simulation_data


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


def predict(speed_model, torque_model, data, window):
    metadata = {"min": {"voltage_d": -300,
                        "voltage_q": -300,
                        "current_d": -30,
                        "current_q": -30,
                        "torque": -120,
                        "speed": -80,
                        "statorPuls": -80},
                "max": {"voltage_d": 300,
                        "voltage_q": 300,
                        "current_d": 30,
                        "current_q": 30,
                        "torque": 120,
                        "speed": 80,
                        "statorPuls": 80}}

    inp_trf_typ, out_trf_typ = get_loader_transform_types(speed_model)

    inp_data = []
    for inp_quant in ['voltage_d', 'voltage_q', 'current_d', 'current_q']:
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

    speed_preds = []
    torque_preds = []
    for i in range(0, len(samples), 1000):
        batch_inp = torch.tensor(np.asarray(samples[i:i+1000])).float().cuda(0)
        speed_out = speed_model(batch_inp)
        torque_out = torque_model(batch_inp)
        speed_preds.append(speed_out.data.cpu().numpy())
        torque_preds.append(torque_out.data.cpu().numpy())

    speed_preds = np.concatenate(speed_preds, axis=0)
    torque_preds = np.concatenate(torque_preds, axis=0)

    if out_trf_typ == 'seq':
        speed_preds = speed_preds[:, 0, window//2].flatten()
        torque_preds = torque_preds[:, 0, window//2].flatten()
    if out_trf_typ == 'flat':
        speed_preds = speed_preds[:, 0].flatten()
        torque_preds = torque_preds[:, 0].flatten()

    speed_true = out_data[0, :].flatten()
    torque_true = out_data[1, :].flatten()

    speed_preds = np.concatenate((speed_true[:window//2], speed_preds,
                                  speed_true[-1 * window//2:]), axis=0)
    torque_preds = np.concatenate((torque_true[:window//2], torque_preds,
                                   torque_true[-1 * window//2:]), axis=0)

    speed_preds = (speed_true + speed_preds) / 2
    torque_preds = (torque_true + torque_preds) / 2
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
    speed_model = torch.load(opt.speed_model_file).cuda(0)
    speed_model = speed_model.eval()

    torque_model = torch.load(opt.torque_model_file).cuda(0)
    torque_model = torque_model.eval()

    return speed_model, torque_model
