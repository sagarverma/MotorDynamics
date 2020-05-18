import os
import argparse
import pickle

import numpy as np

from motornn.utils.predict_utils import (load_model, load_data,
                                         predict, compute_metrics,
                                         generate)


def get_arg_parse():
    parser = argparse.ArgumentParser(description='Test on custom benchmark.')
    parser.add_argument('--speed_model_file', required=True, type=str)
    parser.add_argument('--torque_model_file', required=True, type=str)
    parser.add_argument('--window', type=int,
                        required=True, help='input window')
    parser.add_argument('--save_dir', type=str, required=True,
                        help='directory where results are saved')
    args = parser.parse_args()
    return args


args = get_arg_parse()
speed_model, torque_model = load_model(args)

ramp_overshoot = []

for ramp in [0.01, 0.02, 0.05,
             0.1, 0.2, 0.5, 1.0, 1.1,
             1.2, 1.5, 2, 2.5]:
    reference_speed = [0, 0, 50, 50]
    speed_time = [0, 1, 1+ramp, 5]
    reference_torque = [0, 0, 0, 0]
    torque_time = [0, 1, 1+ramp, 5]
    sim_rate = 0.005
    data = generate(reference_speed, speed_time,
                    reference_torque, torque_time,
                    sim_rate)

    speed_denormed, torque_denormed, speed_ml_metrics, torque_ml_metrics = \
            predict(speed_model, torque_model, data, args.window)

    # print('Speed ML Metrics', speed_ml_metrics)
    # print('Torque ML Metrics', torque_ml_metrics)
    ee_metrics = compute_metrics(data, speed_denormed, torque_denormed, 'speed')

    # print('Quantity', 'Simulation', 'Model')
    # print('2% time', ee_metrics['perc2_times'][0],
    #       ee_metrics['model_perc2_times'][0])
    # print('95% time', ee_metrics['perc95_times'][0],
    #       ee_metrics['model_perc95_times'][0])
    # print('Overshoot', ee_metrics['overshoot_errs'][0],
    #       ee_metrics['model_overshoot_errs'][0])
    # print('Following Error', ee_metrics['following_errs'][0],
    #       ee_metrics['model_following_errs'][0])
    # print('Steady State Error', ee_metrics['sse_errs'][0],
    #       ee_metrics['model_sse_errs'][0])
    # print('Max Acc Torque', ee_metrics['max_trq_accs'][0],
    #       ee_metrics['model_max_trq_accs'][0])

    ramp_overshoot.append([ramp, ee_metrics['overshoot_errs'][0],
                           ee_metrics['model_overshoot_errs'][0]])

    print(ramp, ee_metrics['overshoot_errs'][0],
          ee_metrics['model_overshoot_errs'][0])

    # if not os.path.exists(args.save_dir):
    #     os.makedirs(args.save_dir)
    #
    # fout = open(os.path.join(args.save_dir,
    #             args.speed_model_file.split('/')[-1].replace('.pt',
    #             str(ramp) + '.pkl')), 'wb')
    # pickle.dump([speed_denormed, torque_denormed], fout)
    # fout.close()


fout = open(os.path.join(args.save_dir, 'ramps_overshoots.pkl'), 'wb')
pickle.dump(ramp_overshoot, fout)
fout.close()
