import random
import matlab
import matlab.engine as me
import numpy as np
# import matplotlib.pyplot as plt
import pickle as pkl

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
eng.workspace['Psinit'] = matlab.double([ 0.95,  0 ])
eng.workspace['Prinit'] = matlab.double([ 1,  0 ])
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

integral = False
integral_value = 1

torque_range = [-120, 120]
speed_range = [-70, 70]
static_states = [5, 15]
static_duration = [1, 5]

pos_torque_zones = [x for x in range(-120, 120, integral_value)]
pos_speed_zones = [x for x in range(-70, 70, integral_value)]
ramps = [0.00025, 0.0005, 0.001, 0.0025, 0.005, 0.1, 0.2, 0.025, 0.05, 0.2, 0.1, 0.5, 1]

for split in ['train', 'val', 'test']:
    for sample_no in range(0,50):
        print (split, sample_no)

        torque_states = random.randint(static_states[0], static_states[1])
        speed_states =  random.randint(static_states[0], static_states[1])

        if integral:
            torque_points = [0] + random.sample(pos_torque_zones, k=torque_states)
            speed_points = [0] + random.sample(pos_speed_zones, k=speed_states)
        else:
            torque_points = [0] + np.random.uniform(torque_range[0],
                                                    torque_range[1], torque_states)
            speed_points = [0] + np.random.uniform(speed_range[0],
                                                    speed_range[1], speed_states)

        reference_torque = []
        torque_time = [0]
        for tp in torque_points:
            if integral:
                ramp = random.choice(ramps)
            else:
                ramp = np.random.uniform(0.00025, 1, 1)[0]
            duration = np.random.uniform(static_duration[0], static_duration[1], 1)[0]
            torque_time.append(torque_time[-1] + ramp + duration)
            reference_torque.append(tp)
            reference_torque.append(tp)
            duration = np.random.uniform(static_duration[0], static_duration[1], 1)[0]
            torque_time.append(torque_time[-1] + duration + ramp)

        torque_time = torque_time[:-1]

        reference_speed = []
        speed_time = [0]
        for sp in speed_points:
            if integral:
                ramp = random.choice(ramps)
            else:
                ramp = np.random.uniform(0.00025, 1, 1)[0]
            duration = np.random.uniform(static_duration[0], static_duration[1], 1)[0]
            speed_time.append(speed_time[-1] + duration)
            reference_speed.append(sp)
            reference_speed.append(sp)
            duration = np.random.uniform(static_duration[0], static_duration[1], 1)[0]
            speed_time.append(speed_time[-1] + duration + ramp)

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

        reference_torque_act = np.interp(time, torque_time, reference_torque_act)
        reference_speed_rad = np.interp(time, speed_time, reference_speed_rad)

        sample = {'voltage_d': voltage_d, 'voltage_q': voltage_q,
                  'current_d': current_d, 'current_q': current_q,
                  'torque': torque,  'speed': speed,
                  'statorPuls': statorPuls, 'time':time,
                  'reference_torque_act':reference_torque_act,
                  'reference_speed_rad':reference_speed_rad}

        fout = open('../../../datasets/benchmark/' + split + '/' + str(sample_no) + '.pkl','wb')
        pkl.dump(sample, fout)
        fout.close()
        break
    break
