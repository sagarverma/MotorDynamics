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

current = sio.loadmat('../datasets/CS2018_12_14/Current.mat')
voltage = sio.loadmat('../datasets/CS2018_12_14/Voltage.mat')
stator_plus = sio.loadmat('../datasets/CS2018_12_14/StatorPuls.mat')
speed = sio.loadmat('../datasets/CS2018_12_14/Speed.mat')
torque = sio.loadmat('../datasets/CS2018_12_14/Torque.mat')

dataset = np.hstack((voltage['Voltage'], stator_plus['StatorPuls'], speed['Speed'], current['Current'], torque['Torque']))

scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
scaler.fit(dataset)
dataset = scaler.transform(dataset)

class CNNet(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(CNNet, self).__init__()
        self.cnn1 = nn.Conv1d(3, 64, kernel_size=10, stride=3)
        self.cnn2 = nn.Conv1d(64, 128, kernel_size=7, stride=2)
        self.cnn3 = nn.Conv1d(128, 256, kernel_size=5, stride=1)
        self.linear1 = nn.Linear(256, 128)
        self.linear2 = nn.Linear(128, 1)

    def forward(self, x):
        x = x.permute(0,2,1)
        x = F.avg_pool1d(F.relu6(self.cnn1(x)), kernel_size=5, stride=1)
#         print (x.size())
        x = F.avg_pool1d(F.relu6(self.cnn2(x)), kernel_size=3, stride=1)
#         print (x.size())
        x = F.avg_pool1d(F.relu6(self.cnn3(x)), kernel_size=5, stride=1)
#         print (x.size())
        x = x.view(-1, 256)
        x = F.relu6(self.linear1(x))
#         print (x.size())
        x = self.linear2(x)
        return x.view(-1)

        
for w in [100]:
    print w
    stride = 1
    window = w
    batch_size = 4096
    lr = 0.1
    num_epochs = 2000
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

    model_current1 = CNNet(window*2, 1).cuda()
    model_current2 = CNNet(window*2, 1).cuda()
    model_torque = CNNet(window*2, 1).cuda()

    if not visualize:
        loss_function_current1 = nn.MSELoss()
        loss_function_current2 = nn.MSELoss()
        loss_function_torque = nn.MSELoss()

        optimizer_current1 = optim.SGD(model_current1.parameters(), lr=lr)
        optimizer_current2 = optim.SGD(model_current2.parameters(), lr=lr)
        optimizer_torque = optim.SGD(model_torque.parameters(), lr=lr)

        for epoch in range(num_epochs):
            random.shuffle(train)

            epoch_train_loss_current1 = 0
            epoch_train_loss_current2 = 0
            epoch_train_loss_torque = 0

            for i in range(0, len(train), batch_size):
                inp = []
                current1_true = []
                current2_true = []
                torque_true = []
                
                for t in train[i:i+batch_size]:
                    inp.append(t[0][:,1:])
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
                    inp.append(t[0][:,1:])
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

            torch.save(model_current1, '../weights/SE_data_current1_cnn' + str(window) + '.pt')
            torch.save(model_current2, '../weights/SE_data_current2_cnn' + str(window) + '.pt')
            torch.save(model_torque, '../weights/SE_data_torque_cnn' + str(window) + '.pt')

    else:
        model_current1 = torch.load('../weights/SE_data_current1_cnn' + str(window) + '.pt')
        model_current2 = torch.load('../weights/SE_data_current2_cnn' + str(window) + '.pt')
        model_torque = torch.load('../weights/SE_data_torque_cnn' + str(window) + '.pt')
        
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
                inp = np.asarray([dataset[i:i+window, 1:4]])
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
        
        np.save('../datasets/results_npy/SE_data_cnn' + str(window) + '_out.npy', out)

