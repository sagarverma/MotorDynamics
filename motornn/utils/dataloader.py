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
    if minn > data.min() or maxx < data.max():
        print (quantity, data.min(), data.max())
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

def loader(full_load, sample, metadata, args):
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
        window = full_load[sample[0]][out_quant][sample[1]: sample[2]]
        minn = metadata['min'][out_quant]
        maxx = metadata['max'][out_quant]
        out_data.append(normalize(window, minn, maxx))

    return np.asarray(inp_data), np.asarray(out_data)

class FlatInFlatOut(data.Dataset):
    def __init__(self, full_load, samples, args):
        random.shuffle(samples)
        self.samples = samples
        self.full_load = full_load
        self.inp_quant_ids = [index_quant_map[x] for x in args.inp_quants.split(',')]
        self.out_quant_ids = [index_quant_map[x] for x in args.out_quants.split(',')]


    def __getitem__(self, index):
        mat_no, start, end, infer_index = self.samples[index]

        inp_seq = self.full_load[mat_no][self.inp_quant_ids, start: end]
        out_seq = self.full_load[mat_no][self.out_quant_ids, infer_index]
        inp_seq = inp_seq.flatten()
        out_seq = out_seq.flatten()

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)


class SeqInFlatOut(data.Dataset):
    def __init__(self, full_load, index_quant_map, samples,
                 inp_quants, out_quants):
        """Dataloader class to load samples from signals loaded.

        Args:
            full_load (list): List of numpy array of loaded mat files.
            index_quant_map (dict): Dictionary which maps signal quantity to
                                    to index in full_load arrays.
            samples (list): Metadata used to sample subsequences from
                            full_load.
            inp_quants (list): Input quantities to the model.
            out_quants (list): Output quantities to the model.

        Returns:
            type: Description of returned object.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        random.shuffle(samples)
        self.samples = samples
        self.full_load = full_load
        self.inp_quant_ids = [index_quant_map[x] for x in inp_quants]
        self.out_quant_ids = [index_quant_map[x] for x in out_quants]

    def __getitem__(self, index):
        mat_no, start, end, infer_index = self.samples[index]

        inp_seq = self.full_load[mat_no][self.inp_quant_ids, start: end]
        out_seq = self.full_load[mat_no][self.out_quant_ids, infer_index]
        out_seq = out_seq.flatten()

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)


class SeqInSeqOut(data.Dataset):
    def __init__(self, full_load, index_quant_map, samples,
                 inp_quants, out_quants):
        """Dataloader class to load samples from signals loaded.

        Args:
            full_load (list): List of numpy array of loaded mat files.
            index_quant_map (dict): Dictionary which maps signal quantity to
                                    to index in full_load arrays.
            samples (list): Metadata used to sample subsequences from
                            full_load.
            inp_quants (list): Input quantities to the model.
            out_quants (list): Output quantities to the model.

        Returns:
            type: Description of returned object.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        random.shuffle(samples)
        self.samples = samples
        self.full_load = full_load
        self.inp_quant_ids = [index_quant_map[x] for x in inp_quants]
        self.out_quant_ids = [index_quant_map[x] for x in out_quants]

    def __getitem__(self, index):
        mat_no, start, end, _ = self.samples[index]

        inp_seq = self.full_load[mat_no][self.inp_quant_ids, start: end]
        out_seq = self.full_load[mat_no][self.out_quant_ids, start: end]

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)
