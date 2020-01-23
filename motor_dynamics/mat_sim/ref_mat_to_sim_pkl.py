import random
import matlab
import matlab.engine as me
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
import scipy.io as sio

np.set_printoptions(suppress=True)

quantities_min_max = {'voltage_d': (-200, 200),
                      'voltage_q': (-500, 500),
                      'speed': (-700, 700),
                      'statorPuls': (-700, 700),
                      'current_d': (-30, 30),
                      'current_q': (-30, 30),
                      'torque': (-30, 30)}

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
    a = -1.0
    b = 1.0
    minn, maxx = quantities_min_max[quantity]
    if minn > data.min() or maxx < data.max():
        print (quantity, data.min(), data.max())
    t = a + (data - minn) * ((b - a) / (maxx - minn))
    return t.astype(np.float32)
#
eng = me.connect_matlab()
eng.workspace['Data_Ts'] = float(1/4000)

eng.workspace['Ts'] = float(0.000250)
eng.workspace['Tpwm'] = float(0.000250)
eng.workspace['Tfixe'] = float(500e-6)

eng.workspace['Rs'] = float(1.5)
eng.workspace['Rr'] = float(0.9)
eng.workspace['Ls'] = float(0.160)
eng.workspace['Lr'] = float(0.160)
eng.workspace['Lm'] = float(0.153)
eng.workspace['Lfs'] = float(0.007)
eng.workspace['Lfr'] = float(0.007)
eng.workspace['Lmt'] = float(0.210)
eng.workspace['P1'] = float(0.7)
eng.workspace['P2'] = float(1.5)
eng.workspace['np'] = float(2)
eng.workspace['Psdnom'] = float(0.95)
eng.workspace['Uo'] = float(15)
eng.workspace['Ulim'] = float(415*(2/3)**0.5)
eng.workspace['Psinit'] = matlab.double([ 0,  0 ])
eng.workspace['Prinit'] = matlab.double([ 0,  0 ])
eng.workspace['Inom'] = float(9.1)
eng.workspace['Prdnom'] = float(1)
eng.workspace['SLP_Coeff'] = float(100)
eng.workspace['Vnom'] = float(400)
eng.workspace['SFC_Coeff'] = float(100)

eng.workspace['J'] = float(0.045)
eng.workspace['wrinit'] = float(2*3.14*0)
eng.workspace['thrinit'] = float(0)
eng.workspace['Jm'] = float(0.045)

eng.workspace['tauL'] = float(25)
eng.workspace['wL'] = float(2*3.14*0)

eng.workspace['wCurr'] = float(0)
eng.workspace['wSpeed_PI'] = float(2*3.14*2.5)
eng.workspace['xiSpeed_PI'] = float(1)
eng.workspace['wCurr_PI'] = float(2*3.14*50)
eng.workspace['xiCurr_PI'] = float(1/2)
eng.workspace['wSpeedEst'] = float(2*3.14*500)

eng.workspace['wn'] = float(2*3.14*50)
eng.workspace['Tn'] = float(25)

custom_name = '../../../datasets/RefSynthData/Data8Feb2019.mat'
data = sio.loadmat(custom_name)

if np.abs(data['Kvalv']).max() > 25 * 150/100:
    reference_torque_act = (data['Kvalv'] * 25.0 /100.0).flatten()
else:
    refernece_torque_act = data['Kvalv'].flatten()
if np.abs(data['Speed']).max() < 2*np.pi*50:
    reference_speed_rad = (data['Speed']*2*np.pi).flatten()
else:
    reference_speed_rad = data['Speed'].flatten()
speed_time = torque_time = data['t'].flatten()
print (reference_torque_act.max())

reference_torque_act_tosim = str(list(reference_torque_act)).replace(',', '')
reference_speed_rad_tosim = str(list(reference_speed_rad)).replace(',', '')
torque_time_tosim = str(list(torque_time)).replace(',', '')
speed_time_tosim = str(list(speed_time)).replace(',', '')
sim_time = str(speed_time[-1])

data = eng.conn_python(reference_speed_rad_tosim, reference_torque_act_tosim, speed_time_tosim, torque_time_tosim, sim_time)

data = np.asarray(data)
voltage_d = data[:, 0]
# print (voltage_d.min(), voltage_d.max())
voltage_q = data[:, 1]
# print (voltage_q.min(), voltage_q.max())
current_d = data[:, 2]
# print (current_d.min(), current_d.max())
current_q = data[:, 3]
# print (current_q.min(), current_q.max())
torque = data[:, 4]
# print (torque.min(), torque.max())
speed = data[:, 5]
# print (speed.min(), speed.max())
statorPuls = data[:, 6]
# print (statorPuls.min(), statorPuls.max())
time = data[:, 7]

reference_torque_interp = np.interp(time, torque_time, reference_torque_act)
reference_speed_interp = np.interp(time, speed_time, reference_speed_rad)

sample = {'voltage_d': voltage_d, 'voltage_q': voltage_q,
          'current_d': current_d, 'current_q': current_q,
          'torque': torque,  'speed': speed,
          'statorPuls': statorPuls, 'time':time,
          'reference_torque_act':reference_torque_interp,
          'reference_speed_rad':reference_speed_interp,
          'reference_torque': reference_torque_act,
          'reference_speed': reference_speed_rad,
          'time_org': torque_time}

fout = open('../../../datasets/benchmark/custom/' + custom_name.split('/')[-1][:-4] + '.pkl','wb')
pkl.dump(sample, fout)
fout.close()


# norm_voltage_d = normalize(voltage_d, 'voltage_d')
# norm_voltage_q = normalize(voltage_q, 'voltage_q')
# norm_current_d = normalize(current_d, 'current_d')
# norm_current_q = normalize(current_q, 'current_q')
# norm_torque = normalize(torque, 'torque')
# norm_speed = normalize(speed, 'speed')
# norm_statorPuls = normalize(statorPuls, 'statorPuls')
#
# plt.plot(time, norm_voltage_d, label=r"$u_d$")
# plt.plot(time, norm_voltage_q, label=r"$u_q$")
# plt.plot(time, norm_speed, label=r"$\omega_r$")
# plt.plot(time, norm_statorPuls, label=r"$\omega_s$")
# plt.xlabel('Time (s)')
# plt.ylabel('Scaled Values')
# plt.legend(loc="upper left")
# plt.savefig('inp.png',bbox_inches='tight', transparent="True", pad_inches=0)
# plt.clf()
#
# plt.plot(time, norm_current_d, label=r"$i_d$")
# plt.plot(time, norm_current_q, label=r"$i_q$")
# plt.plot(time, norm_torque, label=r"$\tau_{em}$")
# plt.xlabel('Time (s)')
# plt.ylabel('Scaled Values')
# plt.legend(loc="upper left")
# plt.savefig('out.png',bbox_inches='tight', transparent="True", pad_inches=0)
# plt.clf()


# plt.plot(time, voltage_d, label=r"$u_d$")
# plt.plot(time, voltage_q, label=r"$u_q$")
# plt.xlabel('Time (s)')
# plt.ylabel('Voltage (V)')
# plt.legend(loc="upper left")
# plt.savefig('voltages.png')
# plt.clf()
#
# plt.plot(time, current_d, label=r"$i_d$")
# plt.plot(time, current_q, label=r"$i_q$")
# plt.xlabel('Time (s)')
# plt.ylabel('Current (A)')
# plt.legend(loc="upper left")
# plt.savefig('currents.png')
# plt.clf()
#
# plt.plot(time, torque)
# plt.xlabel('Time (s)')
# plt.ylabel(r'Torque, $\tau_{em}$ (Nm)')
# plt.savefig('torque.png')
# plt.clf()
#
# plt.plot(time, speed)
# plt.xlabel('Time (s)')
# plt.ylabel(r'Speed, $\omega_r$ (rad/s)')
# plt.savefig('speed.png')
# plt.clf()
#
# plt.plot(time, statorPuls)
# plt.xlabel('Time (s)')
# plt.ylabel(r'StatorPuls, $\omega_w$ (rad/s)')
# plt.savefig('statorPuls.png')
# plt.clf()
#
#
# plt.plot(time, torque, label='sim torque')
# plt.plot(time, reference_torque_act, label='ref torque')
# plt.xlabel('Time (s)')
# plt.ylabel(r'Torque, $\tau_{em}$ (Nm)')
# plt.legend(loc="upper left")
# plt.savefig('ref_sim_torque.png')
# plt.clf()
#
# plt.plot(time, speed, label='sim speed')
# plt.plot(time, reference_speed_rad, label='ref speed')
# plt.xlabel('Time (s)')
# plt.ylabel(r'Speed, $\omega_r$ (rad/s)')
# plt.legend(loc="upper left")
# plt.savefig('ref_sim_speed.png')
# plt.clf()
