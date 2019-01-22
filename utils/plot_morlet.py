import scipy.io as sio
from scipy import signal
from scipy.stats import pearsonr
from scipy.spatial.distance import euclidean
from sklearn.metrics import mean_squared_error as mse
import os
import numpy as np

from sklearn import preprocessing
from tftb.processing import Scalogram
from tftb.generators import fmconst
from mpl_toolkits.axes_grid1 import make_axes_locatable

import matplotlib.pyplot as plt

current = sio.loadmat('../datasets/CS2018_12_14/Current.mat')
voltage = sio.loadmat('../datasets/CS2018_12_14/Voltage.mat')
stator_plus = sio.loadmat('../datasets/CS2018_12_14/StatorPuls.mat')
speed = sio.loadmat('../datasets/CS2018_12_14/Speed.mat')
torque = sio.loadmat('../datasets/CS2018_12_14/Torque.mat')
smooth = False

start = int(0 / 0.005)
end = int(24 / 0.005)


result = np.load('../datasets/results_npy/SE_data_relu_dcnn100_out.npy')


dataset = np.hstack((voltage['Voltage'], stator_plus['StatorPuls'], speed['Speed'], current['Current'], torque['Torque']))

current1_scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
current1_scaler.fit(dataset[:,4:5])

current2_scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
current2_scaler.fit(dataset[:,5:6])

torque_scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
torque_scaler.fit(dataset[:,6:7])

voltage1_scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
voltage1_scaler.fit(dataset[:,0:1])

voltage2_scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
voltage2_scaler.fit(dataset[:,1:2])

statorpuls_scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
statorpuls_scaler.fit(dataset[:,2:3])

speed_scaler = preprocessing.MinMaxScaler(feature_range=[0,1])
speed_scaler.fit(dataset[:,3:4])




current1_pred = result[0]
current1_true = result[1]
current2_pred = result[2]
current2_true = result[3]
torque_pred = result[4]
torque_true = result[5]

voltage1_true = result[6]
voltage2_true = result[7]
statorpuls_true = result[8]
speed_true = result[9]

if smooth:
    time = np.arange(result[-1][0][0], result[-1][-1][-1], 0.005)
    c1_true = [None for x in range(time.shape[0])]
    c1_pred = [None for x in range(time.shape[0])]
    c2_true = [None for x in range(time.shape[0])]
    c2_pred = [None for x in range(time.shape[0])]
    t_true = [None for x in range(time.shape[0])]
    t_pred = [None for x in range(time.shape[0])]

    for i in range(current1_true.shape[0]):
        for j in range(current1_true[i].shape[0]):
            c1_true[i+j] = current1_true[i,j]

    for i in range(current1_pred.shape[0]):
        for j in range(current1_pred[i].shape[0]):
            if not c1_pred[i+j]:
                c1_pred[i+j] = current1_pred[i,j]
            else:
                c1_pred[i+j] = (c1_pred[i+j] + current1_pred[i,j]) / 2

    for i in range(current2_true.shape[0]):
        for j in range(current2_true[i].shape[0]):
            c2_true[i+j] = current2_true[i,j]

    for i in range(current2_pred.shape[0]):
        for j in range(current2_pred[i].shape[0]):
            if not c2_pred[i+j]:
                c2_pred[i+j] = current2_pred[i,j]
            else:
                c2_pred[i+j] = (c2_pred[i+j] + current2_pred[i,j]) / 2

    for i in range(torque_true.shape[0]):
        for j in range(torque_true[i].shape[0]):
            t_true[i+j] = torque_true[i,j]

    for i in range(torque_pred.shape[0]):
        for j in range(torque_pred[i].shape[0]):
            if not t_pred[i+j]:
                t_pred[i+j] = torque_pred[i,j]
            else:
                t_pred[i+j] = (t_pred[i+j] + torque_pred[i,j]) / 2

else:
    time = []
    c1_true = []
    c1_pred = []
    c2_true = []
    c2_pred = []
    t_true = []
    t_pred = []
    
    v1_true = []
    v2_true = []
    sp_true = []
    s_true = []
    
    loc = 50
    
    for i in range(result.shape[1]):
        time.append(result[-1][i][loc])
        c1_true.append(current1_true[i][loc])
        c1_pred.append(current1_pred[i][loc])
        c2_true.append(current2_true[i][loc])
        c2_pred.append(current2_pred[i][loc])
        t_true.append(torque_true[i][loc])
        t_pred.append(torque_pred[i][loc])
        
        v1_true.append(voltage1_true[i][loc])
        v2_true.append(voltage2_true[i][loc])
        sp_true.append(statorpuls_true[i][loc])
        s_true.append(speed_true[i][loc])

        
c1_pred = current1_scaler.inverse_transform(np.asarray([c1_pred])).flatten()
c1_true = current1_scaler.inverse_transform(np.asarray([c1_true])).flatten()

c2_pred = current2_scaler.inverse_transform(np.asarray([c2_pred])).flatten()
c2_true = current2_scaler.inverse_transform(np.asarray([c2_true])).flatten()

t_pred = torque_scaler.inverse_transform(np.asarray([t_pred])).flatten()
t_true = torque_scaler.inverse_transform(np.asarray([t_true])).flatten()

v1_true = voltage1_scaler.inverse_transform(np.asarray([v1_true])).flatten()
v2_true = voltage2_scaler.inverse_transform(np.asarray([v2_true])).flatten()
sp_true = statorpuls_scaler.inverse_transform(np.asarray([sp_true])).flatten()
s_true = speed_scaler.inverse_transform(np.asarray([s_true])).flatten()

c1_corr = signal.correlate(c1_pred, c1_true)
c2_corr = signal.correlate(c2_pred, c2_true)
t_corr = signal.correlate(t_pred, t_true)

tfr, t, freqs, _ = Scalogram(c1_true[start:end]).run()
tfr = np.abs(tfr) ** 2
threshold = np.amax(tfr) * 0.0000001
tfr[tfr <= threshold] = 0.0
t, f = np.meshgrid(t, freqs)

fig, axContour = plt.subplots(figsize=(5, 4))
axContour.contour(t, f, tfr)
axContour.grid(True)
axContour.set_title("Morlet scalogram")
axContour.set_ylabel('Frequency')
axContour.yaxis.set_label_position('right')
axContour.set_xlabel('Time')

divider = make_axes_locatable(axContour)
axTime = divider.append_axes("top", 1.2, pad=0.5)
axFreq = divider.append_axes("left", 1.2, pad=0.5)
axTime.plot(c1_true[start:end])
axTime.grid(True)
freq_y = np.linspace(0, 0.5, c1_true[start:end].shape[0] / 2)
freq_x = (abs(np.fft.fftshift(np.fft.fft(c1_true[start:end]))) ** 2)[::-1][:freq_y.shape[0]]
print (freq_x.shape, freq_y.shape)
axFreq.plot(freq_x, freq_y)
axFreq.set_yticklabels([])
axFreq.set_xticklabels([])
axFreq.grid(True)
axFreq.set_ylabel('Spectrum')
axFreq.invert_xaxis()
axFreq.grid(True)
plt.show()