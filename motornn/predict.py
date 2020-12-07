import os
import argparse
import pickle
from copy import deepcopy
from scipy.io import savemat

from motornn.utils.predict_utils import (load_model, load_data,
                                         predict, compute_metrics)


def get_arg_parse():
    parser = argparse.ArgumentParser(description='Test on custom benchmark.')
    parser.add_argument('--speed_model_file', required=True, type=str)
    parser.add_argument('--torque_model_file', required=True, type=str)
    parser.add_argument('--benchmark_file', type=str,
                        required=True, help='benchmark file')
    parser.add_argument('--window', type=int,
                        required=True, help='input window')
    parser.add_argument('--save_dir', type=str, required=True,
                        help='directory where results are saved')
    parser.add_argument('--alpha', type=float, default=0.9)
    parser.add_argument('--noise', type=bool, default=False)
    parser.add_argument('--out_name', type=str, required=True)
    args = parser.parse_args()
    return args


args = get_arg_parse()
speed_model, torque_model = load_model(args)
data = load_data(args)
out = deepcopy(data)
print (args.noise)
speed_denormed, torque_denormed, speed_ml_metrics, torque_ml_metrics = \
        predict(speed_model, torque_model, data, args.window, args.alpha, args.noise)

print(args.speed_model_file.split('/')[-1][:30], args.benchmark_file.split('/')[-1])
print('Speed ML Metrics', speed_ml_metrics)
print('Torque ML Metrics', torque_ml_metrics)
torque_metrics, model_torque_metrics, speed_metrics, model_speed_metrics =\
    compute_metrics(data, speed_denormed, torque_denormed)

for i in range(len(speed_metrics['perc2_times'])):
    print('Speed')
    print('Quantity', 'Simulation', 'Model')
    print('2% time', speed_metrics['perc2_times'][i],
          model_speed_metrics['perc2_times'][i])
    print('95% time', speed_metrics['perc95_times'][i],
          model_speed_metrics['perc95_times'][i])
    print('Overshoot', speed_metrics['overshoot_errs'][i],
          model_speed_metrics['overshoot_errs'][i])
    print('Following Error', speed_metrics['following_errs'][i],
          model_speed_metrics['following_errs'][i])
    print('Steady State Error', speed_metrics['sse_errs'][i],
          model_speed_metrics['sse_errs'][i])
    print('Max Acc Torque', speed_metrics['max_trq_accs'][i],
          model_speed_metrics['max_trq_accs'][i])

for i in range(len(torque_metrics['perc2_times'])):
    print('Torque')
    print('Quantity', 'Simulation', 'Model')
    print('2% time', torque_metrics['perc2_times'][i],
          model_torque_metrics['perc2_times'][i])
    print('95% time', torque_metrics['perc95_times'][i],
          model_torque_metrics['perc95_times'][i])
    print('Overshoot', torque_metrics['overshoot_errs'][i],
          model_torque_metrics['overshoot_errs'][i])
    print('Following Error', torque_metrics['following_errs'][i],
          model_torque_metrics['following_errs'][i])
    print('Steady State Error', torque_metrics['sse_errs'][i],
          model_torque_metrics['sse_errs'][i])
    print('Speed Drop', torque_metrics['speed_drops'][i],
          model_torque_metrics['speed_drops'][i])

save_dir = os.path.join(args.save_dir, args.benchmark_file.split('/')[-1].split('.')[0])
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

to_dump = {'pred_speed': speed_denormed,
           'pred_torque': torque_denormed,
           'speed_ml_metrics': speed_ml_metrics,
           'torque_ml_metrics': torque_ml_metrics,
           'speed_metrics': speed_metrics,
           'torque_metrics': torque_metrics,
           'model_speed_metrics': model_speed_metrics,
           'model_torque_metrics': model_torque_metrics}
fout = open(os.path.join(save_dir, args.out_name + '.pkl'), 'wb')
pickle.dump({**to_dump, **out}, fout)
fout.close()

savemat(os.path.join(save_dir, args.out_name + '.mat'), {**to_dump, **out})
