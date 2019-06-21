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
    a = -1
    b = 1
    t = a + ( quant - minn) * ((b - a) / (maxx - minn))
    return t.astype(np.float32)

def rev_normalize(quant, minn, maxx):
    a = minn
    b = maxx
    t = a + (quant - (-1)) * ((b-a) / (1-(-1)))
    return t.astype(np.float32)

def load_synth_data(root):
#     exps = glob.glob(root + 'simulink_output/OldLaw*')
#     exps = [root + 'simulink_output/NewLaw_Exp' + str(x) for x in range(299)]
#     exps = glob.glob(root + 'simulink_output/AlphaBeta*')
    exps = os.listdir(root)
    print (len(exps))
    
    dataset = []
    for exp in exps:
        d = _load_exp_data2(root + '/' + exp)
        dataset.append(d)
        
#     index_quant_map = {'Voltage1':0,'Voltage2':1,'StatorPuls':2,'Speed':3,'Current1':4,'Current2':5,'Torque':6}
    index_quant_map = {'Voltage1':0,'Voltage2':1,'Speed':2,'Current1':3,'Current2':4,'Torque':5}
    
    return dataset, index_quant_map

def _load_exp_data(root):
    current = sio.loadmat(root + 'Current.mat')
    voltage = sio.loadmat(root + 'Voltage.mat')
#     stator_puls = sio.loadmat(root + 'StatorPuls.mat')
    speed = sio.loadmat(root + 'Speed.mat')
    em_torque = sio.loadmat(root + 'Torque.mat')

#     print (voltage['voltage'][:, 0].max(), voltage['voltage'][:, 1].max())
#     print (current['current'][:, 0].max(), current['current'][:, 1].max())
#     print (speed['speed'][:, 0].max())
#     print (em_torque['torque'][:, 0].max())
    
    voltage1 = normalize(voltage['voltage'][:, 0], -200, 200)
    voltage2 = normalize(voltage['voltage'][: ,1], -500, 500)
#     statorPuls = normalize(stator_puls['statorPuls'][:, 0], -350, 350)
    current1 = normalize(current['current'][:, 0], -20, 20)
    current2 = normalize(current['current'][:, 1], -30, 30)
    speed = normalize(speed['speed'][:, 0], -700, 700)
    torque = normalize(em_torque['torque'][:, 0], -70, 70)
    
#     dataset = np.vstack((voltage1, voltage2, statorPuls, speed,
#                         current1, current2, torque))
    dataset = np.vstack((voltage1, voltage2,  speed,
                        current1, current2, torque))
    
    return dataset


def _load_exp_data2(root):
    data = sio.loadmat(root)
#     print (data.keys())
    
    voltage1 = normalize(data['vd'][:, 0], -200, 200)
    voltage2 = normalize(data['vq'][: ,0], -500, 500)
#     statorPuls = normalize(stator_puls['StatorPuls'][:, 0], -350, 350)
    current1 = normalize(data['id'][:, 0], -20, 20)
    current2 = normalize(data['iq'][:, 0], -30, 30)
    
    if 'raw' in root:
        speed = normalize(data['spd'][:, 0] * 2 * math.pi, -700, 700)
        torque = normalize(data['trq'][:, 0] / 100 * 25, -70, 70)
    else:
        speed = normalize(data['spd'][:, 0], -700, 700)
        torque = normalize(data['trq'][:, 0], -70, 70)
        
    it = data['it'][:, 0]
    vt = data['vt'][:, 0]
    
    v1f = interp1d(vt, voltage1)
    v2f = interp1d(vt, voltage2)
    spdf = interp1d(vt, speed)
    trqf = interp1d(vt, torque)
    c1f = interp1d(it, current1)
    c2f = interp1d(it, current2)
    
    if 'NoLM_SpeedVariations2.mat' not in root:
        nvoltage1 = v1f(it[1:])
        nvoltage2 = v2f(it[1:])
        nspeed = spdf(it[1:])
        ntorque = trqf(it[1:])
        ncurrent1 = c1f(it[1:])
        ncurrent2 = c2f(it[1:])
        time = it[1:]
    else:
        it = it[:40977]
        nvoltage1 = v1f(it)
        nvoltage2 = v2f(it)
        nspeed = spdf(it)
        ntorque = trqf(it)
        ncurrent1 = c1f(it)
        ncurrent2 = c2f(it)
        time = it
        
    if nvoltage1.min() < -1 or nvoltage1.max() > 1 or nvoltage2.min() < -1 or nvoltage2.max() > 1 or nspeed.min() < -1 or nspeed.max() > 1 or ncurrent1.min() < -1 or ncurrent1.max() >1 or ncurrent1.min() < -1 or ncurrent1.max() > 1 or ntorque.min() < -1 or ntorque.max() > 1:
        print (root)
    dataset = np.vstack((nvoltage1, nvoltage2, nspeed, ncurrent1, ncurrent2, ntorque, time))
    
    return dataset.astype(np.float32)

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
#     stator_puls = sio.loadmat(root + 'StatorPuls.mat')
    speed = sio.loadmat(root + 'Speed.mat')
    current = sio.loadmat(root + 'Current.mat')
    voltage = sio.loadmat(root + 'Voltage.mat')
    em_torque = sio.loadmat(root + 'Torque.mat')
    time = sio.loadmat(root + 'Time.mat')

    voltage1 = normalize(voltage['Voltage'][:, 0], -200, 200)
    voltage2 = normalize(voltage['Voltage'][: ,1], -500, 500)
#     statorPuls = normalize(stator_puls['StatorPuls'][:, 0], -350, 350)
    speed = normalize(speed['Speed'][:, 0], -700, 700)
    current1 = normalize(current['Current'][:, 0], -20, 20)
    current2 = normalize(current['Current'][:, 1], -30, 30)
    torque = normalize(em_torque['Torque'][:, 0], -70, 70)
    time = time['t'][:,0]
    
#     dataset = np.vstack((voltage1, voltage2, statorPuls, speed, current1, current2, torque, time))
    dataset = np.vstack((voltage1, voltage2, speed, current1, current2, torque, time))

#     index_quant_map = {'Voltage1':0,'Voltage2':1,'StatorPuls':2,'Speed':3,'Current1':4,'Current2':5,'Torque':6,'Time':7}
    index_quant_map = {'Voltage1':0,'Voltage2':1,'Speed':2,'Current1':3,'Current2':4,'Torque':5,'Time':6}

    return dataset.astype(np.float32), index_quant_map

def load_raw_data(root):
    data = sio.loadmat(root)
#     print (data.keys())
    
    voltage1 = normalize(data['vd'][:, 0], -200, 200)
    voltage2 = normalize(data['vq'][: ,0], -500, 500)
#     statorPuls = normalize(stator_puls['StatorPuls'][:, 0], -350, 350)
    speed = normalize(data['spd'][:, 0] * 2 * math.pi, -700, 700)
    current1 = normalize(data['id'][:, 0], -20, 20)
    current2 = normalize(data['iq'][:, 0], -30, 30)
    torque = normalize(data['trq'][:, 0] / 100 * 25, -70, 70)
    it = data['it'][:, 0]
    vt = data['vt'][:, 0]
    
    v1f = interp1d(vt, voltage1)
    v2f = interp1d(vt, voltage2)
    spdf = interp1d(vt, speed)
    trqf = interp1d(vt, torque)
    c1f = interp1d(it, current1)
    c2f = interp1d(it, current2)
    
    if 'NoLM_SpeedVariations2.mat' not in root:
        nvoltage1 = v1f(it[1:])
        nvoltage2 = v2f(it[1:])
        nspeed = spdf(it[1:])
        ntorque = trqf(it[1:])
        ncurrent1 = c1f(it[1:])
        ncurrent2 = c2f(it[1:])
        time = it[1:]
    else:
        it = it[:40977]
        nvoltage1 = v1f(it)
        nvoltage2 = v2f(it)
        nspeed = spdf(it)
        ntorque = trqf(it)
        ncurrent1 = c1f(it)
        ncurrent2 = c2f(it)
        time = it
        
    dataset = np.vstack((nvoltage1, nvoltage2, nspeed, ncurrent1, ncurrent2, ntorque, time))

    index_quant_map = {'Voltage1':0,'Voltage2':1,'Speed':2,'Current1':3,'Current2':4,'Torque':5,'Time':6}

    return dataset.astype(np.float32), index_quant_map

    
def rev_test_output(dataset):
    time = dataset[0,:]
    voltage1 = rev_normalize(dataset[1,:], -200, 200)
    voltage2 = rev_normalize(dataset[2,:], -500, 500)
#     statorPuls = rev_normalize(dataset[3,:], -350, 350)
    speed = rev_normalize(dataset[3,:], -700, 700)
    current1_true = rev_normalize(dataset[4,:], -20, 20)
    current1_pred = rev_normalize(dataset[5,:], -20, 20)
    current2_true = rev_normalize(dataset[6,:], -30, 30)
    current2_pred = rev_normalize(dataset[7,:], -30, 30)
    torque_true = rev_normalize(dataset[8,:], -70, 70)
    torque_pred = rev_normalize(dataset[9,:], -70, 70)
    
    dataset = {'time':time, 'voltage1':voltage1, 'voltage2':voltage2, 'speed':speed, 'current1_true':current1_true, 'current1_pred':current1_pred, 'current2_true':current2_true, 'current2_pred':current2_pred, 'torque_true':torque_true, 'torque_pred':torque_pred}
    
    return dataset
    
def get_sample_metadata(dataset, stride, window):
    samples = []
    
    for sample_no in range(len(dataset)):
        for i in range(0, dataset[sample_no].shape[1], stride):
            if i + window < dataset[sample_no].shape[1]:
                samples.append([sample_no,i,i+window,i+window//2])
    
    return samples

def get_test_sample_metadata(dataset, stride, window):
    samples = []
    
    for sample_no in range(len(dataset)):
        for i in range(0, dataset[sample_no].shape[1], stride):
            if i + window < dataset[sample_no].shape[1]:
                samples.append([sample_no,i,i+window,i+window//2])
    
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
        sno, xi, xj, yi = self.samples[index]

        inp_seq = self.full_load[sno][self.inp_quant_ids,xi:xj].transpose(1,0)
        
        if self.enc_dec:
            out_seq = self.full_load[sno][self.out_quant_ids,xi:xj].transpose(1,0)
        else:
            out_seq = self.full_load[sno][self.out_quant_ids,yi].transpose(1,0)

        if self.flatten:
            inp_seq = inp_seq.flatten()
            out_seq = out_seq.flatten()

        return inp_seq, out_seq

    def __len__(self):
        return len(self.samples)
    

    