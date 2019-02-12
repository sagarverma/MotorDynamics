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

parser.add_argument('--data_dir', required=True)
parser.add_argument('--weight_file', required=True)
parser.add_argument('--result_dir', required=True)
parser.add_argument('--gpu_id', default=0, type=int, required=False)
parser.add_argument('--batch_size', default=2048, type=int, required=False)

opt = parser.parse_args()

wf = opt.weight_file[:-3].replace('_quants','Quants').replace('batch_size','batchSize').replace('_skip','Skip').replace('_bilstm','Bilstm')
hpstrings = wf.split('/')[-1].split('_')

hp_map = {}
for i in range(0,len(hpstrings),2):
    if hpstrings[i+1].isdigit():
        hp_map[hpstrings[i]] = int(hpstrings[i+1])
    elif '.' in hpstrings[i+1]:
        hp_map[hpstrings[i]] = float(hpstrings[i+1])
    else:
        hp_map[hpstrings[i]] = hpstrings[i+1]

print (hp_map)

print (opt.result_dir + opt.weight_file[:-3].split('/')[-1] + '.npy')
model = torch.load(opt.weight_file)
model.eval()

dataset, index_quant_map = load_data_test(opt.data_dir)
test_samples = get_sample_metadata(dataset.shape[0], hp_map['stride'], hp_map['window'])

# inp_quant_ids = [index_quant_map[x] for x in hp_map['inpQuants'].split(',')]

# out = []
# true = []

# for i in range(0, len(test_samples), opt.batch_size):
#     batch = []
#     for j in range(i,min(i + opt.batch_size,len(test_samples))):
#         s = test_samples[j][0]
#         e = test_samples[j][1]
#         m = test_samples[j][2]
        
#         batch.append(dataset[s:e, inp_quant_ids])
    
#     batch = np.asarray(batch)
#     batch = Variable(torch.from_numpy(batch).type(torch.FloatTensor).cuda())

#     pred = model(batch)
    
#     out += list(pred.data.cpu().numpy()[:, hp_map['window']//2].flatten())

# print (len(out))
# res_out = np.asarray(out)

# np.save(opt.result_dir + opt.weight_file[:-3].split('/')[-1] + '.npy', res_out)

time = sio.loadmat('../datasets/CS2019_02_08/t.mat')['time']

time_out = []
for ts in test_samples:
    time_out.append(time[ts[-1]])
    
time_out = np.asarray(time_out)

np.save(opt.result_dir + 'time.npy', time_out)