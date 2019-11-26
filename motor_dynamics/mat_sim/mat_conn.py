import random
import matlab
import matlab.engine as me
import numpy as np
import matplotlib.pyplot as plt
import cv2

#Convert speed to Hz and torque to % of nominal torque in the plots.
#Variable flat durations
#Dynamic variations
#Don't change speed and torque at same time

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


pos_torque_zones = [x for x in range(0, 120, 1)]
pos_speed_zones = [x for x in range(0, 50, 1)]
ramps = [0.00025, 0.0005, 0.001, 0.0025, 0.005, 0.1, 0.2, 0.025, 0.05, 0.2, 0.1, 0.5, 1]

torque_points = [0] + random.sample(pos_torque_zones, k=random.randint(5,15))
speed_points = [0] + random.sample(pos_speed_zones, k=random.randint(5,15))

reference_torque = []
torque_time = [0]
for tp in torque_points:
    ramp = random.choice(ramps)
    torque_time.append(torque_time[-1] + 1)
    reference_torque.append(tp)
    reference_torque.append(tp)
    torque_time.append(torque_time[-1] + 1 + ramp)

torque_time = torque_time[:-1]

reference_speed = []
speed_time = [0]
for sp in speed_points:
    ramp = random.choice(ramps)
    speed_time.append(speed_time[-1] + 1)
    reference_speed.append(sp)
    reference_speed.append(sp)
    speed_time.append(speed_time[-1] + 1 + ramp)

speed_time = speed_time[:-1]

if torque_time[-1] > speed_time[-1]:
    speed_time[-1] = torque_time[-1]

if speed_time[-1] > torque_time[-1]:
    torque_time[-1] = speed_time[-1]


reference_torque_act = np.asarray(reference_torque) * 25 / 100.
reference_speed_rad = np.asarray(reference_speed) * 2 * np.pi

reference_torque_act_tosim = str(list(reference_torque_act)).replace(',', '')
reference_speed_rad_tosim = str(list(reference_speed_rad)).replace(',', '')
torque_time_tosim = str(list(torque_time)).replace(',', '')
speed_time_tosim = str(list(speed_time)).replace(',', '')
sim_time = str(speed_time[-1])

data = eng.conn_python(reference_speed_rad_tosim, reference_torque_act_tosim, speed_time_tosim, torque_time_tosim, sim_time)

data = np.asarray(data)
voltage_d = data[:, 0]
voltage_q = data[:, 1]
current_d = data[:, 2]
current_q = data[:, 3]
torque = data[:, 4]
speed = data[:, 5]
statorPuls = data[:, 6]
time = data[:, 7]

reference_torque_act = np.interp(time, torque_time, reference_torque_act)
reference_speed_rad = np.interp(time, speed_time, reference_speed_rad)

plt.plot(time, voltage_d, label=r"$u_d$")
plt.plot(time, voltage_q, label=r"$u_q$")
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend(loc="upper left")
plt.savefig('voltages.png')
plt.clf()

plt.plot(time, current_d, label=r"$i_d$")
plt.plot(time, current_q, label=r"$i_q$")
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend(loc="upper left")
plt.savefig('currents.png')
plt.clf()

plt.plot(time, torque)
plt.xlabel('Time (s)')
plt.ylabel(r'Torque, $\tau_{em}$ (Nm)')
plt.savefig('torque.png')
plt.clf()

plt.plot(time, speed)
plt.xlabel('Time (s)')
plt.ylabel(r'Speed, $\omega_r$ (rad/s)')
plt.savefig('speed.png')
plt.clf()

plt.plot(time, statorPuls)
plt.xlabel('Time (s)')
plt.ylabel(r'StatorPuls, $\omega_w$ (rad/s)')
plt.savefig('statorPuls.png')
plt.clf()


plt.plot(time, torque, label='sim torque')
plt.plot(time, reference_torque_act, label='ref torque')
plt.xlabel('Time (s)')
plt.ylabel(r'Torque, $\tau_{em}$ (Nm)')
plt.legend(loc="upper left")
plt.savefig('ref_sim_torque.png')
plt.clf()

plt.plot(time, speed, label='sim speed')
plt.plot(time, reference_speed_rad, label='ref speed')
plt.xlabel('Time (s)')
plt.ylabel(r'Speed, $\omega_r$ (rad/s)')
plt.legend(loc="upper left")
plt.savefig('ref_sim_speed.png')
plt.clf()
