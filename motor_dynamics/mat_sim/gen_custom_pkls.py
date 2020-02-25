import random
import matlab
import matlab.engine as me
import numpy as np
import pickle as pkl

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


pos_torque_zones = [x for x in range(0, 120, 1)]
pos_speed_zones = [x for x in range(-80, 80, 1)]
ramps = [0.00025, 0.0005, 0.001, 0.0025, 0.005, 0.1, 0.2, 0.025, 0.05, 0.2, 0.1, 0.5, 1]


s1 = [[0, 1, 1.5, 4], [0, 0, 0, 0], [0, 0, 100, 100], 4]
s2 = [[0, 1, 1.5, 4], [0, 0, 50, 50], [0, 0, 100, 100], 4]
s3 = [[0, 1, 1.5, 1.50025, 4], [0, 0, 25, 25, 25], [0, 0, 0, 150, 150], 4]
s4 = [[0, 1, 1.5, 3.1, 4], [0, 0, 80, -80, -80], [0, 0, 0, 0, 0], 4]
s5 = [[0, 1, 1.5, 3, 4.6, 5], [0, 0, 80, 80, -80, -80], [0, 0, 0, 50, 50, 50], 5]
s6 = [[0, 1, 1.5, 3, 4], [0, 0, 80, 80, 80], [0, 0, 0, 120, 120], 4]
s7 = [[0, 1, 1.5, 3, 4], [0, 0, 0, 80, 80], [0, 0, 120, 120, 120], 4]

samples = [s1, s2, s3, s4, s5, s6, s7]
for sample_no in range(len(samples)):
    print (sample_no)
    sample = samples[sample_no]
    print (len(sample), len(sample[0]), len(sample[1]), len(sample[2]))
    speed_time = torque_time = sample[0]
    reference_speed = sample[1]
    reference_torque = sample[2]

    reference_torque_act = np.asarray(reference_torque) * 25 / 100.
    reference_speed_rad = np.asarray(reference_speed) * 2 * np.pi


    reference_torque_act_tosim = str(list(reference_torque_act)).replace(',', '')
    reference_speed_rad_tosim = str(list(reference_speed_rad)).replace(',', '')
    torque_time_tosim = str(list(torque_time)).replace(',', '')
    speed_time_tosim = str(list(speed_time)).replace(',', '')
    sim_time = str(sample[3])

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

    fout = open('../../../datasets/benchmark/custom/' + str(sample_no) + '.pkl','wb')
    pkl.dump(sample, fout)
    fout.close()
