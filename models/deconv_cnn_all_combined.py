import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim import lr_scheduler
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

time = np.asarray([[0.005 * x] for x in range(current['Current'].shape[0])])

dataset = np.hstack((voltage['Voltage'], stator_plus['StatorPuls'], speed['Speed'], current['Current'], torque['Torque']))

scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
scaler.fit(dataset)
dataset = scaler.transform(dataset)

dataset = np.hstack((dataset, time))

class DCNNet(nn.Module):
    def __init__(self):
        super(DCNNet, self).__init__()
        self.cnn1 = nn.Conv1d(3, 32, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)
                        
        self.dcnn4 = nn.ConvTranspose1d(256, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(128, 64, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(64, 32, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(32, 3, kernel_size=10, stride=1)
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x = F.relu(self.cnn1(x))
#         print (x.size())
        x = F.relu(self.cnn2(x))
#         print (x.size())
        x = F.relu(self.cnn3(x))
#         print (x.size())
        x = F.relu(self.dcnn3(x))
#         print (x.size())
        x = F.relu(self.dcnn2(x))
#         print (x.size())
        x = self.dcnn1(x)
#         print (x.size())
        return x.permute(0,2,1)

        
for w in [100]:
    print w
    stride = 1
    window = w
    batch_size = 2048
    lr = 0.01
    num_epochs = 2000
    step_size = 100
    gamma = 1
    visualize = True

    samples = []
    for i in range(0,dataset.shape[0],stride):
        if i+window < dataset.shape[0]:
            samples.append(dataset[i:i+window, :])
            
    print 'Total samples:',len(samples)

#     random.shuffle(samples)
    
    train = samples[:int(len(samples)*0.7)]
    test = samples[int(len(samples)*0.7):]
    
    print 'Train samples:',len(train), 'Test samples:',len(test)

    model = DCNNet().cuda()
    

    if not visualize:
        loss_function = nn.MSELoss()

        optimizer = optim.SGD(model.parameters(), lr=lr)
        scheduler = lr_scheduler.StepLR(optimizer, step_size=step_size, gamma=gamma)
        
        for epoch in range(num_epochs):
            scheduler.step()
            random.shuffle(train)

            epoch_train_loss = 0

            for i in range(0, len(train), batch_size):
                inp = []
                out = []
                
                for t in train[i:i+batch_size]:
                    inp.append(t[:,1:4])
                    out.append(t[:,4:7])
                
                inp = np.asarray(inp)
                out = np.asarray(out)
                
                inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())
                out = Variable(torch.from_numpy(out).type(torch.FloatTensor).cuda())
                
                model.zero_grad()
                pred = model(inp)
                loss = loss_function(pred, out)
                loss.backward()
                optimizer.step()

                epoch_train_loss += loss.data[0]

            epoch_test_loss = 0

            for i in range(0, len(test), batch_size):
                inp = []
                out = []
                
                for t in train[i:i+batch_size]:
                    inp.append(t[:,1:4])
                    out.append(t[:,4:7])
                
                inp = np.asarray(inp)
                out = np.asarray(out)
                
                inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())
                out = Variable(torch.from_numpy(out).type(torch.FloatTensor).cuda())
                
                pred = model(inp)
                loss = loss_function(pred, out)

                epoch_test_loss += loss.data[0]

            print ("Epoch " + str(epoch))
            print ("train loss = " + str(epoch_train_loss.item()))
            print ("test loss = " + str(epoch_test_loss.item()))

            torch.save(model, '../weights/SE_data_ccombined_relu_dcnn_4layers' + str(window) + '.pt')

    else:
        model = torch.load('../weights/SE_data_ccombined_relu_dcnn_4layers' + str(window) + '.pt')
       
        model.eval()
       
        out_current1 = []
        out_current2 = []
        out_torque = []
        
        true_current1 = []
        true_current2 = []
        true_torque = []
        true_time = []
        
        true_voltage1 = []
        true_voltage2 = []
        true_statorpuls = []
        true_speed = []

        for i in range(0, len(test), batch_size):
                inp = []
                current1_true = []
                current2_true = []
                torque_true = []
                times_this = []
                
                voltage1_true = []
                voltage2_true = []
                statorpuls_true = []
                speed_true = []

                for t in test[i:i+batch_size]:
                    inp.append(t[:,1:4])
                    current1_true.append(t[:,4])
                    current2_true.append(t[:,5])
                    torque_true.append(t[:,6])
                    times_this.append(t[:,7])
                    
                    voltage1_true.append(t[:,0])
                    voltage2_true.append(t[:,1])
                    statorpuls_true.append(t[:,2])
                    speed_true.append(t[:,3])
                    
                
                inp = np.asarray(inp)
                inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())
                
                pred = model(inp)
                pred = pred.data.cpu().numpy()
                
                out_current1.append(pred[:,:,0])
                out_current2.append(pred[:,:,1])
                out_torque.append(pred[:,:,2])
            
                true_current1.append(current1_true)
                true_current2.append(current2_true)
                true_torque.append(torque_true)
                true_time.append(times_this)
        
                true_voltage1.append(voltage1_true)
                true_voltage2.append(voltage2_true)
                true_statorpuls.append(statorpuls_true)
                true_speed.append(speed_true)
       
        out = np.stack([np.vstack(out_current1), np.vstack(true_current1), np.vstack(out_current2), np.vstack(true_current2), np.vstack(out_torque), np.vstack(true_torque), np.vstack(true_voltage1), np.vstack(true_voltage2), np.vstack(true_statorpuls), np.vstack(true_speed), np.vstack(true_time),])
        
        np.save('../datasets/results_npy/SE_data_combined_relu_dcnn_4layers' + str(window) + '_out.npy', out)

