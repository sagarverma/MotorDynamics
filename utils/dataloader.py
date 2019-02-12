import torch
import torch.utils.data as data
from torch.autograd import Variable

import numpy as np
import random

from sklearn import preprocessing
import scipy.io as sio
from scipy.signal import resample

def load_data(root):
    current = sio.loadmat(root + 'Current.mat')
    voltage = sio.loadmat(root + 'Voltage.mat')
    stator_puls = sio.loadmat(root + 'StatorPuls.mat')
    speed = sio.loadmat(root + 'Speed.mat')
    em_torque = sio.loadmat(root + 'Torque.mat')

    dataset = np.hstack((voltage['Voltage'], stator_puls['StatorPuls'], speed['Speed'],
                        current['Current'], em_torque['Torque']))

    scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
    scaler.fit(dataset)
    dataset = scaler.transform(dataset)
    index_quant_map = {'Voltage1':0,'Voltage2':1,'StatorPuls':2,'Speed':3,'Current1':4,'Current2':5,'Torque':6}
    return dataset.astype(np.float32), index_quant_map

def load_data_test(root):
    voltage = sio.loadmat(root + 'Voltage.mat')
    stator_puls = sio.loadmat(root + 'StatorPuls.mat')
    speed = sio.loadmat(root + 'Speed.mat')
    
    dataset = np.hstack((voltage['voltage'], stator_puls['statorPuls'], speed['speed']))

    scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
    scaler.fit(dataset)
    dataset = scaler.transform(dataset)
    index_quant_map = {'Voltage1':0,'Voltage2':1,'StatorPuls':2,'Speed':3}
    return dataset.astype(np.float32), index_quant_map

def get_sample_metadata(data_len, stride, window):
    samples = []
    for i in range(0, data_len, stride):
        if i + window < data_len:
            samples.append([i,i+window,i+window//2])
    return samples

class SignalPreloader(data.Dataset):
    def __init__(self, full_load, index_quant_map, samples, inp_quants, out_quants, flatten=False, enc_dec=False):
        random.shuffle(samples)
        self.samples = samples
        self.full_load = full_load
        self.inp_quant_ids = [index_quant_map[x] for x in inp_quants]
        self.out_quant_ids = [index_quant_map[x] for x in out_quants]
        self.flatten = flatten
        self.enc_dec = enc_dec

    def __getitem__(self, index):
        xi, xj, yi = self.samples[index]

        inp_seq = self.full_load[xi:xj,self.inp_quant_ids]
        
        if self.enc_dec:
            out_seq = self.full_load[xi:xj,self.out_quant_ids]
        else:
            out_seq = self.full_load[yi,self.out_quant_ids]

        if self.flatten:
            inp_seq = inp_seq.flatten()
            out_seq = out_seq.flatten()

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)
