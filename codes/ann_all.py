import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

import scipy.io as sio
from scipy.signal import resample
import os

import csv

import numpy as np
import random

from multilabel_rbm import RBM as MRBM
from rbm import RBM
from class_rbm import ClassRBM

from sklearn import preprocessing

# %matplotlib inline
import matplotlib.pyplot as plt

from scipy.signal import correlate

current = sio.loadmat('../datasets/DATACSdet_simulink_current_dq.mat')
voltage = sio.loadmat('../datasets/DATACSdet_simulink_voltage_dq.mat')
stator_plus = sio.loadmat('../datasets/DATACSdet_simulink_statorplus_dq.mat')
speed = sio.loadmat('../datasets/DATACSdet_simulink_speed_dq.mat')
torque = sio.loadmat('../datasets/DATACSdet_simulink_torque_dq.mat')

dataset = np.hstack((voltage['Voltage'], stator_plus['StatorPuls'], speed['Speed'], current['Current'], torque['Torque']))

scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
scaler.fit(dataset)
dataset = scaler.transform(dataset)

class FFNet(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(FFNet, self).__init__()
        self.linear1 = nn.Linear(input_dim, 360)
        self.linear2 = nn.Linear(360, 120)
        self.linear3 = nn.Linear(120, output_dim)
        self.dropout = nn.Dropout(0.5)

    def forward(self, seq):
        x = seq.view(seq.size()[0], -1)
        out = F.relu6(self.linear1(x))
        out = F.relu6(self.linear2(out))
        out = F.relu6(self.linear3(out))
        return out.view(-1)

        
for w in [5,10,15,20,25,50,100]:
    print w
    stride = 1
    window = w
    batch_size = 512
    lr = 0.1
    num_epochs = 20
    visualize = True

    samples = []
    for i in range(0,dataset.shape[0],stride):
        if i+window < dataset.shape[0]:
            samples.append([dataset[i:i+window,0:4],[dataset[i+window//2,4],dataset[i+window//2,5],dataset[i+window//2,6]]])

    print 'Total samples:',len(samples)

    random.shuffle(samples)
    
    train = samples[:int(len(samples)*0.7)]
    test = samples[int(len(samples)*0.7):]

    print 'Train samples:',len(train), 'Test samples:',len(test)

    model_current1 = FFNet(window*2, 1).cuda()
    model_current2 = FFNet(window*2, 1).cuda()
    model_torque = FFNet(window*2, 1).cuda()

    if not visualize:
        loss_function_current1 = nn.MSELoss()
        loss_function_current2 = nn.MSELoss()
        loss_function_torque = nn.MSELoss()

        optimizer_current1 = optim.SGD(model_current1.parameters(), lr=lr)
        optimizer_current2 = optim.SGD(model_current2.parameters(), lr=lr)
        optimizer_torque = optim.SGD(model_torque.parameters(), lr=lr)

        for epoch in range(num_epochs):
            train = np.random.permutation(train)

            epoch_train_loss_current1 = 0
            epoch_train_loss_current2 = 0
            epoch_train_loss_torque = 0

            for i in range(0, len(train), batch_size):
                inp = []
                current1_true = []
                current2_true = []
                torque_true = []
                
                for t in train[i:i+batch_size]:
                    inp.append(t[0][:,2:])
                    current1_true.append(t[1][0])
                    current2_true.append(t[1][1])
                    torque_true.append(t[1][2])
                
                inp = np.asarray(inp)
                current1_true = np.asarray(current1_true)
                current2_true = np.asarray(current2_true)
                torque_true = np.asarray(torque_true)

                inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())
                current1_true = Variable(torch.from_numpy(current1_true).type(torch.FloatTensor).cuda())
                current2_true = Variable(torch.from_numpy(current2_true).type(torch.FloatTensor).cuda())
                torque_true = Variable(torch.from_numpy(torque_true).type(torch.FloatTensor).cuda())

                model_current1.zero_grad()
                current1_pred = model_current1(inp)
                current1_loss = loss_function_current1(current1_pred, current1_true)
                current1_loss.backward()
                optimizer_current1.step()

                model_current2.zero_grad()
                current2_pred = model_current2(inp)
                current2_loss = loss_function_current2(current2_pred, current2_true)
                current2_loss.backward()
                optimizer_current2.step()

                model_torque.zero_grad()
                torque_pred = model_torque(inp)
                torque_loss = loss_function_torque(torque_pred, torque_true)
                torque_loss.backward()
                optimizer_torque.step()

                epoch_train_loss_current1 += current1_loss.data[0]
                epoch_train_loss_current2 += current2_loss.data[0]
                epoch_train_loss_torque += torque_loss.data[0]

            epoch_test_loss_current1 = 0
            epoch_test_loss_current2 = 0
            epoch_test_loss_torque = 0

            for i in range(0, len(test), batch_size):
                inp = []
                current1_true = []
                current2_true = []
                torque_true = []
                
                for t in test[i:i+batch_size]:
                    inp.append(t[0][:,2:])
                    current1_true.append(t[1][0])
                    current2_true.append(t[1][1])
                    torque_true.append(t[1][2])
                
                inp = np.asarray(inp)
                current1_true = np.asarray(current1_true)
                current2_true = np.asarray(current2_true)
                torque_true = np.asarray(torque_true)

                inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())
                current1_true = Variable(torch.from_numpy(current1_true).type(torch.FloatTensor).cuda())
                current2_true = Variable(torch.from_numpy(current2_true).type(torch.FloatTensor).cuda())
                torque_true = Variable(torch.from_numpy(torque_true).type(torch.FloatTensor).cuda())

                current1_pred = model_current1(inp)
                current1_loss = loss_function_current1(current1_pred, current1_true)

                current2_pred = model_current2(inp)
                current2_loss = loss_function_current2(current2_pred, current2_true)

                torque_pred = model_torque(inp)
                torque_loss = loss_function_torque(torque_pred, torque_true)

                epoch_test_loss_current1 += current1_loss.data[0]
                epoch_test_loss_current2 += current2_loss.data[0]
                epoch_test_loss_torque += torque_loss.data[0]

            print ("Epoch " + str(epoch))
            print ("Current1 train loss = " + str(epoch_train_loss_current1.item()) + ", Current2 train loss = " + str(epoch_train_loss_current2.item()) + ", Torque train loss = " + str(epoch_train_loss_torque.item()))
            print ("Current1 test loss = " + str(epoch_test_loss_current1.item()) + ", Current2 test loss = " + str(epoch_test_loss_current2.item()) + ", Torque test loss = " + str(epoch_test_loss_torque.item()))

        torch.save(model_current1, '../weights/SE_data_current1_ann' + str(window) + '.pt')
        torch.save(model_current2, '../weights/SE_data_current2_ann' + str(window) + '.pt')
        torch.save(model_torque, '../weights/SE_data_torque_ann' + str(window) + '.pt')

    else:
        model_current1 = torch.load('../weights/SE_data_current1_ann' + str(window) + '.pt')
        model_current2 = torch.load('../weights/SE_data_current2_ann' + str(window) + '.pt')
        model_torque = torch.load('../weights/SE_data_torque_ann' + str(window) + '.pt')
        
        model_current1.eval()
        model_current2.eval()
        model_torque.eval()

        out_current1 = []
        out_current2 = []
        out_torque = []
        
        true_current1 = []
        true_current2 = []
        true_torque = []

        for i in range(dataset.shape[0]):
            if i + window < dataset.shape[0]:
                inp = np.asarray([dataset[i:i+window, 2:4]])
                inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())

                current1_pred = model_current1(inp)
                current2_pred = model_current2(inp)
                torque_pred = model_torque(inp)

#                 print (current1_pred.size())
                out_current1.append(current1_pred.data.cpu().numpy()[0])
                out_current2.append(current2_pred.data.cpu().numpy()[0])
                out_torque.append(torque_pred.data.cpu().numpy()[0])
            
                true_current1.append(dataset[i+window//2,4])
                true_current2.append(dataset[i+window//2,5])
                true_torque.append(dataset[i+window//2,6])
        
        print (len(out_current1), len(true_current1))
        out = np.stack([out_current1, true_current1, out_current2, true_current2, out_torque, true_torque])
        
        np.save('../datasets/results_npy/SE_data_ann' + str(window) + '_out.npy', out)

