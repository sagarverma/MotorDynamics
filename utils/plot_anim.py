import scipy.io as sio
import os
import numpy as np

from sklearn import preprocessing

import matplotlib.pyplot as plt

current = sio.loadmat('../datasets/CS2018_12_14/Current.mat')
voltage = sio.loadmat('../datasets/CS2018_12_14/Voltage.mat')
stator_plus = sio.loadmat('../datasets/CS2018_12_14/StatorPuls.mat')
speed = sio.loadmat('../datasets/CS2018_12_14/Speed.mat')
torque = sio.loadmat('../datasets/CS2018_12_14/Torque.mat')

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

result = np.load('../datasets/results_npy/SE_data_relu_dcnn100_out.npy')

smooth = False

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

start = int(0 / 0.005)
end = int(10 / 0.005)


for i in range(start, end):
    fig = plt.figure(figsize=(8, 4))

    plt.subplot(2,3,1)
    plt.plot(time[i:i+120], v1_true[i:i+120], label='Voltage1', color='#44f441')
    plt.plot(time[i:i+120], v2_true[i:i+120], label='Voltage2', color='#f4a341')
    plt.ylim([0, 300])
    plt.xticks([])
    plt.ylabel('Voltages (V)')
    plt.xlabel('Time (s)')

    plt.subplot(2,3,2)
    plt.plot(time[i:i+120], sp_true[i:i+120])
    plt.ylim([0, 315])
    plt.xticks([])
    plt.ylabel('StatorPuls (rad/s)')
    plt.xlabel('Time (s)')

    plt.subplot(2,3,3)
    plt.plot(time[i:i+120], s_true[i:i+120], color='#9141f4')
    plt.ylim([0, 305])
    plt.xticks([])
    plt.ylabel('Speed (rad/s)')
    plt.xlabel('Time (s)')

    plt.subplot(2,3,4)
    plt.plot(time[i:i+120], c1_pred[i:i+120], color='#f44141')
    plt.plot(time[i:i+120], c1_true[i:i+120], color='#34472f', alpha=0.6)
    plt.ylim([0, 15])
    plt.xticks([])
    plt.ylabel('Current1 (A)')
    plt.xlabel('Time (s)')

    plt.subplot(2,3,5)
    plt.plot(time[i:i+120], c2_pred[i:i+120], color='#f44141')
    plt.plot(time[i:i+120], c2_true[i:i+120], color='#34472f', alpha=0.6)
    plt.ylim([-1, 17])
    plt.xticks([])
    plt.ylabel('Current2 (A)')
    plt.xlabel('Time (s)')

    plt.subplot(2,3,6)
    plt.plot(time[i:i+120], t_pred[i:i+120], label='Pred', color='#f44141')
    plt.plot(time[i:i+120], t_true[i:i+120], label='True', color='#34472f', alpha=0.6)
    plt.ylim([-2, 40])
    plt.xticks([])
    plt.ylabel('TorqueLoad (Nm)')
    plt.xlabel('Time (s)')

    fig.legend(loc='upper right')
    plt.tight_layout()

#     plt.show()
    plt.savefig('../datasets/plot_anim/' + str(i).zfill(3) + '.png')
    plt.close()
