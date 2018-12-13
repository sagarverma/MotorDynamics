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

stride = 1
window = 30
batch_size = 256
lr = 0.1
num_epochs = 200
hidden_size = 32

samples = []
for i in range(0,dataset.shape[0],stride):
    if i+window < dataset.shape[0]:
        samples.append(dataset[i:i+window,:])
    
print 'Total samples:',len(samples)

random.shuffle(samples)
samples = np.asarray(samples)

train = samples[:int(len(samples)*0.7), :, :]
test = samples[int(len(samples)*0.7):, :, :]

print 'Train samples:',train.shape[0], 'Test samples:',test.shape[0]
    
class SimpleRNN(nn.Module):
    def __init__(self, hidden_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size

        self.inp = nn.Linear(3, hidden_size)
        self.rnn = nn.LSTM(hidden_size, hidden_size, 2, dropout=0.05, batch_first=True)
        self.out = nn.Linear(hidden_size, 1)

    def forward(self, x):
        x = self.inp(x)
        x, _ = self.rnn(x)
        x = self.out(x)
        return x.view(x.size()[0],x.size()[1])

model_current1 = SimpleRNN(hidden_size).cuda()
model_current2 = SimpleRNN(hidden_size).cuda()
model_torque = SimpleRNN(hidden_size).cuda()

loss_function = nn.MSELoss()

optimizer_current1 = optim.SGD(model_current1.parameters(), lr=lr)
optimizer_current2 = optim.SGD(model_current2.parameters(), lr=lr)
optimizer_torque = optim.SGD(model_torque.parameters(), lr=lr)

for epoch in range(num_epochs):
    train = np.random.permutation(train)
    
    epoch_train_loss_current1 = 0
    epoch_train_loss_current2 = 0
    epoch_train_loss_torque = 0
    
    for i in range(0, train.shape[0], batch_size):
        inp = train[i:i+batch_size, :, 1:4]
        current1_true = train[i:i+batch_size, :, 4]
        current2_true = train[i:i+batch_size, :, 5]
        torque_true = train[i:i+batch_size, :, 6]
        
        inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())
        current1_true = Variable(torch.from_numpy(current1_true).type(torch.FloatTensor).cuda())
        current2_true = Variable(torch.from_numpy(current2_true).type(torch.FloatTensor).cuda())
        torque_true = Variable(torch.from_numpy(torque_true).type(torch.FloatTensor).cuda())
        
        model_current1.zero_grad()
        current1_pred = model_current1(inp)
        current1_loss = loss_function(current1_pred, current1_true)
        current1_loss.backward()
        optimizer_current1.step()

        model_current2.zero_grad()
        current2_pred = model_current2(inp)
        current2_loss = loss_function(current2_pred, current2_true)
        current2_loss.backward()
        optimizer_current2.step()

        model_torque.zero_grad()
        torque_pred = model_torque(inp)
        torque_loss = loss_function(torque_pred, torque_true)
        torque_loss.backward()
        optimizer_torque.step()

        epoch_train_loss_current1 += current1_loss.data[0]
        epoch_train_loss_current2 += current2_loss.data[0]
        epoch_train_loss_torque += torque_loss.data[0]

    epoch_test_loss_current1 = 0
    epoch_test_loss_current2 = 0
    epoch_test_loss_torque = 0
    
    for i in range(0, test.shape[0], batch_size):
        inp = test[i:i+batch_size, :, 1:4]
        current1_true = test[i:i+batch_size, :, 4]
        current2_true = test[i:i+batch_size, :, 5]
        torque_true = test[i:i+batch_size, :, 6]
        
        inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())
        current1_true = Variable(torch.from_numpy(current1_true).type(torch.FloatTensor).cuda())
        current2_true = Variable(torch.from_numpy(current2_true).type(torch.FloatTensor).cuda())
        torque_true = Variable(torch.from_numpy(torque_true).type(torch.FloatTensor).cuda())
        
        current1_pred = model_current1(inp)
        current1_loss = loss_function(current1_pred, current1_true)
        
        current2_pred = model_current2(inp)
        current2_loss = loss_function(current2_pred, current2_true)
        
        torque_pred = model_torque(inp)
        torque_loss = loss_function(torque_pred, torque_true)

        epoch_test_loss_current1 += current1_loss.data[0]
        epoch_test_loss_current2 += current2_loss.data[0]
        epoch_test_loss_torque += torque_loss.data[0]

    print ("Epoch " + str(epoch))
    print ("Current1 train loss = " + str(epoch_train_loss_current1.item()) + ", Current2 train loss = " + str(epoch_train_loss_current2.item()) + ", Torque train loss = " + str(epoch_train_loss_torque.item()))
    print ("Current1 test loss = " + str(epoch_test_loss_current1.item()) + ", Current2 test loss = " + str(epoch_test_loss_current2.item()) + ", Torque test loss = " + str(epoch_test_loss_torque.item()))
    
    torch.save(model_current1, '../weights/SE_data_current1_rnn' + str(window) + '.pt')
    torch.save(model_current2, '../weights/SE_data_current2_rnn' + str(window) + '.pt')
    torch.save(model_torque, '../weights/SE_data_torque_rnn' + str(window) + '.pt')
