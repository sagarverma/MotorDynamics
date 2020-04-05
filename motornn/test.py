import glob 

import numpy as np 

import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

import matplotlib.pyplot as plt

from motor_dynamics.utils.helpers import (get_file_names, initialize_metrics,
                                          get_mean_metrics, set_metrics,
                                          get_model, get_train_loaders, Log)

from motor_dynamics.utils.dataloader import _load_pkl_data, denormalize

from motor_dynamics.utils.metrics import smape, r2, rmsle, rmse, mae

def test(opt):
    torque_model = torch.load('../../weights/deep_fnn/deep_fnn_train__act_tanh_stride_1_window_50_inpQuants_voltage_d,voltage_q,current_d,current_q,statorPuls_outQuants_torque_lr_0.01_batchSize_10000_epochs_500_loss_mse.pt').cuda(1)
    speed_model = torch.load('../../weights/deep_fnn/deep_fnn_train__act_tanh_stride_1_window_50_inpQuants_voltage_d,voltage_q,current_d,current_q,statorPuls_outQuants_speed_lr_0.01_batchSize_10000_epochs_500_loss_mse.pt').cuda(1)
    
    torque_model.eval()
    speed_model.eval()
    
    pkls = glob.glob(opt.val_sim_dir + '*.pkl')

    for pkl_path in pkls:
        print (pkl_path)
        norm_data, data = _load_pkl_data(pkl_path)
        
        trq_outs = []
        spd_outs = []
        
        batch = []
        
        for i in range(0, norm_data['voltage_d'].shape[0], 1):
            if i + opt.window <= norm_data['voltage_d'].shape[0]:
                u_d = norm_data['voltage_d'][i:i+opt.window]
                u_q = norm_data['voltage_q'][i:i+opt.window]
                i_d = norm_data['current_d'][i:i+opt.window]
                i_q = norm_data['current_q'][i:i+opt.window]
                stp = norm_data['statorPuls'][i:i+opt.window]

                inp = np.stack([u_d, u_q, i_d, i_q, stp])
                inp = np.asarray(inp.flatten())
                
                batch.append(inp)
                
        batch = np.asarray(batch)
        
        for i in range(0, batch.shape[0], 10000):
            inp = torch.from_numpy(batch[i:i+10000, :]).cuda(1)

            trq_out = torque_model(inp)
            spd_out = speed_model(inp)

            trq_out = trq_out.data.cpu().numpy()
            spd_out = spd_out.data.cpu().numpy()

            trq_outs.append(trq_out[:,0])
            spd_outs.append(spd_out[:,0])

        trq_outs = np.hstack(trq_outs)
        spd_outs = np.hstack(spd_outs)

        
        trq_outs = denormalize(trq_outs, 'torque')
        spd_outs = denormalize(spd_outs, 'speed')
        
        trq_outs = np.hstack([data['torque'][:49], trq_outs])
        spd_outs = np.hstack([data['speed'][:49], spd_outs])
        
        print (trq_outs.shape, data['torque'].shape)
        
        plt.plot(data['time'], trq_outs)
        plt.plot(data['time'], data['torque'])
        
        plt.savefig(pkl_path.split('/')[-1].split('.')[0] + 'torque.png')
        plt.close()
        
        plt.plot(data['time'], spd_outs)
        plt.plot(data['time'], data['speed'])
        plt.savefig(pkl_path.split('/')[-1].split('.')[0] + 'speed.png')
        
        plt.close()
            
