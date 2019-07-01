import sys, glob, cv2, random, math, argparse
import numpy as np
import pandas as pd
from tqdm import tqdm_notebook as tqdm
from sklearn.metrics import classification_report

import torch
import torch.utils.data
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable

from utils.dataloader import *
from models.FFNN import *
from models.RNN import *
from models.LSTM import *
from models.CNN import *
from models.EncDec import *

parser = argparse.ArgumentParser(description='Train a model on electric motor simulink data')

parser.add_argument('--data_dir', default='../datasets/test_simulink/', required=False)
parser.add_argument('--result_dir', default='../results/', required=False)
parser.add_argument('--gpu_id', default=0, type=int, required=False)
parser.add_argument('--batch_size', default=2048, type=int, required=False)
parser.add_argument('--stride', default=1, type=int, required=False)
opt = parser.parse_args()

# torque_model = torch.load('../weights/modelNewLawDQRawData_encdecBilstmSkip_act_relu_stride_1_window_100_inpQuants_Voltage1,Voltage2,Speed_outQuants_Torque_lr_0.0001_batchSize_8000_epochs_2000.pt')
# torque_model.eval()

# current2_model = torch.load('../weights/modelNewLawDQRawData_encdecBilstmSkip_act_relu_stride_1_window_100_inpQuants_Voltage1,Voltage2,Speed_outQuants_Current2_lr_0.0001_batchSize_8000_epochs_2000.pt')
# current2_model.eval()

# current1_model = torch.load('../weights/modelNewLawDQRawData_encdecBilstmSkip_act_relu_stride_1_window_100_inpQuants_Voltage1,Voltage2,Speed_outQuants_Current1_lr_0.0001_batchSize_4096_epochs_2000.pt')
# current1_model.eval()

# torque_model = torch.load('../weights/modelNewLawDQSynthData_encdecBilstmSkip_act_relu_stride_1_window_100_inpQuants_Voltage1,Voltage2,Speed_outQuants_Torque_lr_0.0001_batchSize_8000_epochs_2000.pt')
# torque_model.eval()

# current2_model = torch.load('../weights/modelNewLawDQSynthData_encdecBilstmSkip_act_relu_stride_1_window_100_inpQuants_Voltage1,Voltage2,Speed_outQuants_Current2_lr_0.0001_batchSize_8000_epochs_2000.pt')
# current2_model.eval()

# current1_model = torch.load('../weights/modelNewLawDQSynthData_encdecBilstmSkip_act_relu_stride_1_window_100_inpQuants_Voltage1,Voltage2,Speed_outQuants_Current1_lr_0.0001_batchSize_8000_epochs_2000.pt')
# current1_model.eval()

torque_model = torch.load('../weights/modelNewLawDQSynthDataCompact_encdec3_act_relu_stride_1_window_1000_inpQuants_Voltage1,Voltage2,Speed_outQuants_Torque_lr_0.01_batchSize_800_epochs_2000.pt')
torque_model.eval()

current2_model = torch.load('../weights/modelNewLawDQSynthDataCompact_encdec3_act_relu_stride_1_window_1000_inpQuants_Voltage1,Voltage2,Speed_outQuants_Current2_lr_0.01_batchSize_800_epochs_2000.pt')
current2_model.eval()

current1_model = torch.load('../weights/modelNewLawDQSynthDataCompact_encdec3_act_relu_stride_1_window_1000_inpQuants_Voltage1,Voltage2,Speed_outQuants_Current1_lr_0.01_batchSize_800_epochs_2000.pt')
current1_model.eval()

dates = os.listdir(opt.data_dir)

for date in dates:
    print (date)
#     dataset, index_quant_map = load_data_test(opt.data_dir + date + '/')
    dataset, index_quant_map = load_raw_data(opt.data_dir + date)
    print (dataset.shape)
    
    torque_true_out = []
    current2_true_out = []
    current1_true_out = []
    
    time_out = []
    voltage1_out = []
    voltage2_out = []
#     statorPuls_out = []
    speed_out = []
    
    torque_pred_out = []
    current2_pred_out = []
    current1_pred_out = []
    
    samples = get_test_sample_metadata([dataset], 1, 1000)

    for i in range(0,len(samples),5000):
        batch_inp = []
        batch_out = []
        for j in range(i,i+5000):
            if j < len(samples):
                batch_inp.append(dataset[:3,samples[j][1]:samples[j][2]])
                batch_out.append(dataset[3:,samples[j][1]:samples[j][2]])
        
        batch_inp = np.asarray(batch_inp)
        batch_out = np.asarray(batch_out)
        batch = torch.from_numpy(batch_inp.transpose(0,2,1)).cuda()
        
        torque_preds = torque_model(batch)
        current2_preds = current2_model(batch)
        current1_preds = current1_model(batch)
        
        torque_pred_out += list(torque_preds.data.cpu().numpy()[:,500,0])
        current2_pred_out += list(current2_preds.data.cpu().numpy()[:,500,0])
        current1_pred_out += list(current1_preds.data.cpu().numpy()[:,500,0])
        
        torque_true_out += list(batch_out[:,2,500])
        current2_true_out += list(batch_out[:,1,500])
        current1_true_out += list(batch_out[:,0,500])
        
        voltage1_out += list(batch_inp[:,0,500])
        voltage2_out += list(batch_inp[:,1,500])
#         statorPuls_out += list(batch_inp[:,2,50])
        speed_out += list(batch_inp[:,2,500])
        time_out += list(batch_out[:,3,500])
        
        del batch
        del torque_preds
        del current1_preds
        del current2_preds
        
    
    torque_pred_out = np.asarray(torque_pred_out)
    toreuq_true_out = np.asarray(torque_true_out)
    
    current2_pred_out = np.asarray(current2_pred_out)
    current2_true_out = np.asarray(current2_true_out)
    
    current1_pred_out = np.asarray(current1_pred_out)
    current1_ture_out = np.asarray(current1_true_out)
    
    time_out = np.asarray(time_out)
    speed_out = np.asarray(speed_out)
#     statorPuls_out = np.asarray(statorPuls_out)
    voltage2_out = np.asarray(voltage2_out)
    voltage1_out = np.asarray(voltage1_out)
    
    quants = np.vstack((time_out, voltage1_out, voltage2_out, speed_out, current1_true_out, current1_pred_out, current2_true_out, current2_pred_out, torque_true_out, torque_pred_out))
    
    print (quants.shape)
    
    quants = rev_test_output(quants)
    
    sio.savemat(opt.result_dir + date, quants)
    