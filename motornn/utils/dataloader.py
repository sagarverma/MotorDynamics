import os
import math
import glob
import pickle
import json

import torch
import torch.utils.data as data
from torch.autograd import Variable

import numpy as np
import random

from sklearn import preprocessing
import scipy.io as sio
from scipy.signal import resample
from scipy.interpolate import interp1d


def normalize(data, minn, maxx):
    """Normalize a quantity using global minima and maxima.

    Args:
        data (np.array): Electrical motor quantity as np.array.
        quantity (str): Name of the quantity

    Returns:
        np.array: Normalized electrical motor quantity.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    a = 0
    b = 1
    t = a + (data - minn) * ((b - a) / (maxx - minn))
    return t.astype(np.float32)


def denormalize(data, minn, maxx):
    """Denormalize a quantity using global minima and maxima.

    Args:
        data (np.array): Normalized electrical motor quantity as np.array.
        quantity (str): Name of the quantity

    Returns:
        np.array: Denormalized electrical motor quantity.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    t = minn + (data - (0)) * ((maxx - minn) / (1 - (0)))
    return t.astype(np.float32)


def load_data(args):
    dataset = {}

    train_pkls = glob.glob(os.path.join(args.data_dir, 'train/*.pkl'))
    val_pkls = glob.glob(os.path.join(args.data_dir, 'val/*.pkl'))

    fin = open(os.path.join(args.data_dir, 'metadata.json'), 'r')
    metadata = json.load(fin)
    fin.close()

    train_samples = []
    val_samples = []

    for train_pkl in train_pkls:
        fin = open(train_pkl, 'rb')
        data = pickle.load(fin)
        dataset[train_pkl] = data

        for i in range(0, data['current_d'].shape[0], args.stride):
            if i + args.window < data['current_d'].shape[0]:
                train_samples.append([train_pkl, i,
                                      i + args.window, i + args.window//2])

    for val_pkl in val_pkls:
        fin = open(val_pkl, 'rb')
        data = pickle.load(fin)
        dataset[val_pkl] = data

        for i in range(0, data['current_d'].shape[0], args.stride):
            if i + args.window < data['current_d'].shape[0]:
                val_samples.append([val_pkl, i,
                                      i + args.window, i + args.window//2])

    return dataset, train_samples, val_samples, metadata

def loader(full_load, sample, metadata, args, type='flat'):
    inp_quants = args.inp_quants.split(',')
    out_quants = args.out_quants.split(',')

    inp_data = []
    for inp_quant in inp_quants:
        window = full_load[sample[0]][inp_quant][sample[1]: sample[2]]
        minn = metadata['min'][inp_quant]
        maxx = metadata['max'][inp_quant]
        inp_data.append(normalize(window, minn, maxx))

    out_data = []
    for out_quant in out_quants:
        if type == 'seq':
            window = full_load[sample[0]][out_quant][sample[1]: sample[2]]
        if type == 'flat':
            window = full_load[sample[0]][out_quant][sample[3]]
        minn = metadata['min'][out_quant]
        maxx = metadata['max'][out_quant]
        out_data.append(normalize(window, minn, maxx))

    return np.asarray(inp_data), np.asarray(out_data)

class FlatInFlatOut(data.Dataset):
    def __init__(self, full_load, samples, metadata, args):
        random.shuffle(samples)
        self.samples = samples
        self.full_load = full_load
        self.metadata = metadata
        self.args = args

    def __getitem__(self, index):
        sample = self.samples[index]

        inp_seq, out_seq = loader(self.full_load, sample, self.metadata, self.args, 'flat')
        inp_seq = inp_seq.flatten()

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)


class SeqInFlatOut(data.Dataset):
    def __init__(self, full_load, samples, metadata, args):
        random.shuffle(samples)
        self.samples = samples
        self.full_load = full_load
        self.metadata = metadata
        self.args = args

    def __getitem__(self, index):
        sample = self.samples[index]

        inp_seq, out_seq = loader(self.full_load, sample, self.metadata, self.args, 'flat')

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)


class SeqInSeqOut(data.Dataset):
    def __init__(self, full_load, samples, metadata, args):
        random.shuffle(samples)
        self.samples = samples
        self.full_load = full_load
        self.metadata = metadata
        self.args = args

    def __getitem__(self, index):
        sample = self.samples[index]

        inp_seq, out_seq = loader(self.full_load, sample, self.metadata, self.args, 'seq')

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)
