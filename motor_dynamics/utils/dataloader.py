import os
import math
import glob
import torch
import torch.utils.data as data
from torch.autograd import Variable

import numpy as np
import random

from sklearn import preprocessing
import scipy.io as sio
from scipy.signal import resample
from scipy.interpolate import interp1d

quantities_min_max = {'voltage_d': (-500, 500),
                      'voltage_q': (-500, 500),
                      'speed': (-700, 700),
                      'current_d': (-30, 30),
                      'current_q': (-30, 30),
                      'torque': (-250, 250)}


def normalize(data, quantity):
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
    if data.max() > quantities_min_max[quantity][1] or \
        data.min() < quantities_min_max[quantity][0]:
        print (quantity, data.max(), data.min())
    a = 0
    b = 1
    minn, maxx = quantities_min_max[quantity]
    if minn > data.min() or maxx < data.max():
        print (quantity, data.min(), data.max())
    t = a + (data - minn) * ((b - a) / (maxx - minn))
    return t.astype(np.float32)


def denormalize(data, quantity):
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
    a, b = quantities_min_max[quantity]
    t = a + (data - (0)) * ((b-a) / (1-(0)))
    return t.astype(np.float32)


def load_data(root):
    """Load synthetic dataset.

    Args:
        root (type): Dataset directory to load the dataset.

    Returns:
        tuple: dataset, index_quant_map.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    exps = os.listdir(root)

    dataset = []
    for exp in exps:
        mat_data, index_quant_map = _load_exp_data(os.path.join(root, exp))
        dataset.append(mat_data)

    return dataset, index_quant_map


def _load_exp_data(root):
    data = sio.loadmat(root)

    voltage_d = normalize(data['voltage_d'][0, :], 'voltage_d')
    voltage_q = normalize(data['voltage_q'][0, :], 'voltage_q')
    current_d = normalize(data['current_d'][0, :], 'current_d')
    current_q = normalize(data['current_q'][0, :], 'current_q')
    speed = normalize(data['speed'][0, :], 'speed')
    torque = normalize(data['torque'][0, :], 'torque')
    time = data['time'][0, :]


    dataset = (voltage_d, voltage_q, speed,
               current_d, current_q, torque, time)
    dataset = np.vstack(dataset)

    index_quant_map = {'voltage_d': 0,
                       'voltage_q': 1,
                       'speed': 2,
                       'current_d': 3,
                       'current_q': 4,
                       'torque': 5,
                       'time': 6}

    return dataset.astype(np.float32), index_quant_map


def rev_test_output(data):
    """Denormalize the inference output.

    Args:
        dataset (np.asarray): Output from inference.

    Returns:
        np.asarray: Denormalized inference output.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    time = data[0, :]
    voltage_d = denormalize(data[1, :], 'voltage_d')
    voltage_q = denormalize(data[2, :], 'voltage_q')
    speed = denormalize(data[3, :], 'speed')
    current_d_true = denormalize(data[4, :], 'current_d')
    current_d_pred = denormalize(data[5, :], 'current_d')
    current_q_true = denormalize(data[6, :], 'current_q')
    current_q_pred = denormalize(data[7, :], 'current_q')
    torque_true = denormalize(data[8, :], 'torque')
    torque_pred = denormalize(data[9, :], 'torque')

    dataset = {'time': time,
               'voltage_d': voltage_d,
               'voltage_q': voltage_q,
               'speed': speed,
               'current_d_true': current_d_true,
               'current_d_pred': current_d_pred,
               'current_q_true': current_q_true,
               'current_q_pred': current_q_pred,
               'torque_true': torque_true,
               'torque_pred': torque_pred}

    return dataset


def get_sample_metadata(dataset, stride, window):
    """Get sample metadata from dataset based on sampling stride and window.

    Args:
        dataset (list): List of np.array extracted from different mat files.
        stride (int): Sampling stride.
        window (int): Sampling window length.

    Returns:
        list: List of samples where each item in list is a tuple with
              mat no, index in mat data, index + window and index + window//2.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    samples = []

    for sample_no in range(len(dataset)):
        for i in range(0, dataset[sample_no].shape[1], stride):
            if i + window < dataset[sample_no].shape[1]:
                samples.append([sample_no, i, i+window, i+window//2])

    return samples


class FlatInFlatOut(data.Dataset):
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
