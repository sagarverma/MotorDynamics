import os
import argparse
import pickle

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
    args = parser.parse_args()
    return args


args = get_arg_parse()
speed_model, torque_model = load_model(args)
data = load_data(args)
speed_denormed, torque_denormed, speed_ml_metrics, torque_ml_metrics = \
        predict(speed_model, torque_model, data, args.window)

print('Speed ML Metrics', speed_ml_metrics)
print('Torque ML Metrics', torque_ml_metrics)
ee_metrics = compute_metrics(data, speed_denormed, torque_denormed)

print('Quantity', 'Simulation', 'Model')
print('2% time', ee_metrics['perc2_times'][0],
      ee_metrics['model_perc2_times'][0])
print('95% time', ee_metrics['perc95_times'][0],
      ee_metrics['model_perc95_times'][0])
print('Overshoot', ee_metrics['overshoot_errs'][0],
      ee_metrics['model_overshoot_errs'][0])
print('Following Error', ee_metrics['following_errs'][0],
      ee_metrics['model_following_errs'][0])
print('Steady State Error', ee_metrics['sse_errs'][0],
      ee_metrics['model_sse_errs'][0])
print('Max Acc Torque', ee_metrics['max_trq_accs'][0],
      ee_metrics['model_max_trq_accs'][0])

save_dir = os.path.join(args.save_dir, args.benchmark_file.split('.')[0])
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

fout = open(os.path.join(save_dir,
            args.speed_model_file.split('/')[-1].replace('.pt', '.pkl')), 'wb')
pickle.dump([speed_denormed, torque_denormed], fout)
fout.close()
