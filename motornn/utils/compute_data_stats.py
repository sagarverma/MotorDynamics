import os
import glob
import argparse

import json
import pickle

import numpy as np

parser = argparse.ArgumentParser(description='Gather dataset statistics.')
parser.add_argument('--data_dir', type=str, required=True)
parser.add_argument('--save_dir', type=str, required=True)
args = parser.parse_args()

train_pkls = glob.glob(os.path.join(args.data_dir, 'train/*.pkl'))
val_pkls = glob.glob(os.path.join(args.data_dir, 'val/*.pkl'))

stats = {'min': {}, 'max': {}, 'mean': {}}

for pkl in train_pkls + val_pkls:
    fin = open(pkl, 'rb')
    data = pickle.load(fin)
    fin.close()
    
    for k in data.keys():
        if k not in stats['min']:
            stats['min'][k] = [np.min(data[k])]
        else:
            stats['min'][k].append(np.min(data[k]))

        if k not in stats['max']:
            stats['max'][k] = [np.max(data[k])]
        else:
            stats['max'][k].append(np.max(data[k]))

        if k not in stats['mean']:
            stats['mean'][k] = [np.mean(data[k])]
        else:
            stats['mean'][k].append(np.mean(data[k]))


for k in stats['min'].keys():
    stats['min'][k] = np.min(stats['min'][k])

for k in stats['max'].keys():
    stats['max'][k] = np.max(stats['max'][k])

for k in stats['mean'].keys():
    stats['mean'][k] = np.mean(stats['mean'][k])


output_path = os.path.join(args.save_dir, 'metadata.json')
fout = open(output_path, 'w')
json.dump(stats, fout)
fout.close()
