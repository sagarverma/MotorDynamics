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


def normalize(quant, minn, maxx):
    """Normalize a quantity using global minima and maxima.

    Args:
        quant (np.array): Electrical motor quantity as np.array.
        minn (float): Global minimum value of the input quantity.
        maxx (float): Global maximum value of the input quantity.

    Returns:
        np.array: Normalized electrical motor quantity.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    a = -1
    b = 1
    t = a + (quant - minn) * ((b - a) / (maxx - minn))
    return t.astype(np.float32)


def denormalize(quant, minn, maxx):
    """Denormalize a quantity using global minima and maxima.

    Args:
        quant (np.array): Normalized electrical motor quantity as np.array.
        minn (float): Global minimum value of the input quantity.
        maxx (float): Global maximum value of the input quantity.

    Returns:
        np.array: Denormalized electrical motor quantity.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    a = minn
    b = maxx
    t = a + (quant - (-1)) * ((b-a) / (1-(-1)))
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
        mat_data = _load_exp_data(root + '/' + exp)[0]
        dataset.append(mat_data)

    index_quant_map = {'Voltage1': 0,
                       'Voltage2': 1,
                       'Speed': 2,
                       'Current1': 3,
                       'Current2': 4,
                       'Torque': 5}

    return dataset, index_quant_map


def _load_exp_data(root):
    data = sio.loadmat(root)

    voltage1 = normalize(data['vd'][:, 0], -200, 200)
    voltage2 = normalize(data['vq'][:, 0], -500, 500)
    current1 = normalize(data['id'][:, 0], -20, 20)
    current2 = normalize(data['iq'][:, 0], -30, 30)

    if 'raw' in root:
        speed = normalize(data['spd'][:, 0] * 2 * math.pi, -700, 700)
        torque = normalize(data['trq'][:, 0] / 100 * 25, -70, 70)
    else:
        speed = normalize(data['spd'][:, 0], -700, 700)
        torque = normalize(data['trq'][:, 0], -70, 70)

    current_time = data['it'][:, 0]
    voltage_time = data['vt'][:, 0]

    v1f = interp1d(voltage_time, voltage1)
    v2f = interp1d(voltage_time, voltage2)
    spdf = interp1d(voltage_time, speed)
    trqf = interp1d(voltage_time, torque)
    c1f = interp1d(current_time, current1)
    c2f = interp1d(current_time, current2)

    if 'NoLM_SpeedVariations2.mat' not in root:
        nvoltage1 = v1f(current_time[1:])
        nvoltage2 = v2f(current_time[1:])
        nspeed = spdf(current_time[1:])
        ntorque = trqf(current_time[1:])
        ncurrent1 = c1f(current_time[1:])
        ncurrent2 = c2f(current_time[1:])
        time = current_time[1:]
    else:
        current_time = current_time[:40977]
        nvoltage1 = v1f(current_time)
        nvoltage2 = v2f(current_time)
        nspeed = spdf(current_time)
        ntorque = trqf(current_time)
        ncurrent1 = c1f(current_time)
        ncurrent2 = c2f(current_time)
        time = current_time

    dataset = (nvoltage1, nvoltage2, nspeed,
               ncurrent1, ncurrent2, ntorque, time)
    dataset = np.vstack(dataset)

    index_quant_map = {'Voltage1': 0,
                       'Voltage2': 1,
                       'Speed': 2,
                       'Current1': 3,
                       'Current2': 4,
                       'Torque': 5,
                       'Time': 6}

    return dataset.astype(np.float32), index_quant_map


def rev_test_output(dataset):
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
    time = dataset[0, :]
    voltage1 = denormalize(dataset[1, :], -200, 200)
    voltage2 = denormalize(dataset[2, :], -500, 500)
    speed = denormalize(dataset[3, :], -700, 700)
    current1_true = denormalize(dataset[4, :], -20, 20)
    current1_pred = denormalize(dataset[5, :], -20, 20)
    current2_true = denormalize(dataset[6, :], -30, 30)
    current2_pred = denormalize(dataset[7, :], -30, 30)
    torque_true = denormalize(dataset[8, :], -70, 70)
    torque_pred = denormalize(dataset[9, :], -70, 70)

    dataset = {'time': time,
               'voltage1': voltage1,
               'voltage2': voltage2,
               'speed': speed,
               'current1_true': current1_true,
               'current1_pred': current1_pred,
               'current2_true': current2_true,
               'current2_pred': current2_pred,
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


class SignalPreloader(data.Dataset):
    def __init__(self, full_load, index_quant_map, samples,
                 inp_quants, out_quants, flatten=False, enc_dec=False):
        """Dataloader class to load samples from signals loaded.

        Args:
            full_load (list): List of numpy array of loaded mat files.
            index_quant_map (dict): Dictionary which maps signal quantity to
                                    to index in full_load arrays.
            samples (list): Metadata used to sample subsequences from
                            full_load.
            inp_quants (list): Input quantities to the model.
            out_quants (list): Output quantities to the model.
            flatten (bool): Should input be flattened for feedforward network.
            enc_dec (bool): Input length equals to output length in case of
                            encoder-decoder architecture.

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
        self.flatten = flatten
        self.enc_dec = enc_dec

    def __getitem__(self, index):
        mat_no, start, end, infer_index = self.samples[index]

        inp_seq = self.full_load[mat_no][self.inp_quant_ids, start: end]
        inp_seq = inp_seq.transpose(1, 0)

        if self.enc_dec:
            out_seq = self.full_load[mat_no][self.out_quant_ids, start: end]
            out_seq = out_seq.transpose(1, 0)
        else:
            out_seq = self.full_load[mat_no][self.out_quant_ids, infer_index]
            out_seq = out_seq.transpose(1, 0)

        if self.flatten:
            inp_seq = inp_seq.flatten()
            out_seq = out_seq.flatten()

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)
