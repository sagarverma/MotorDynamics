import os
import argparse
import pickle as pkl
import numpy as np


def get_args():
    parser = argparse.ArgumentParser(description=f"""
                                     Add noise to already generated samples.""")
    parser.add_argument('--data_dir', type=str, required=True)
    parser.add_argument('--id_std_mean', type=float, default=0.24705127)
    parser.add_argument('--iq_std_mean', type=float, default=0.25241439)
    parser.add_argument('--ud_std_mean', type=float, default=2.20696924)
    parser.add_argument('--uq_std_mean', type=float, default=2.89078961)

    args = parser.parse_args()
    return args


def process_split(out_dir, split, args):
    if not os.path.exists(os.path.join(out_dir, split)):
        os.mkdir(os.path.join(out_dir, split))

    samples = os.listdir(os.path.join(args.data_dir, split))
    for sample in samples:
        fin = open(os.path.join(args.data_dir, split, sample), 'rb')
        data = pkl.load(fin)
        fin.close()

        data['noisy_current_d'] = np.random.normal(data['current_d'],
                                                   scale=args.id_std_mean)
        data['noisy_current_q'] = np.random.normal(data['current_q'],
                                                   scale=args.iq_std_mean)
        data['noisy_voltage_d'] = np.random.normal(data['voltage_d'],
                                                   scale=args.ud_std_mean)
        data['nosiy_voltage_q'] = np.random.normal(data['voltage_q'],
                                                   scale=args.uq_std_mean)

        fout = open(os.path.join(out_dir, split, sample), 'wb')
        pkl.dump(data, fout)
        fout.close()


def process_data_dir(args):
    out_dir = args.data_dir + '_noisy'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    for root, splits, files in os.walk(args.data_dir):
        for split in splits:
            process_split(out_dir, split, args)


args = get_args()
process_data_dir(args)
