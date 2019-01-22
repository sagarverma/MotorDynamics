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

parser = argparse.ArgumentParser(description='Train a model on electric motor simulink data')

parser.add_argument('--data_dir', required=True)
parser.add_argument('--weight_dir', required=True)
parser.add_argument('--log_dir', required=True)
parser.add_argument('--gpu_id', type=int, default=0, required=False)
parser.add_argument('--epochs', type=int, default=10, required=False)
parser.add_argument('--batch_size', type=int, default=128, required=False)
parser.add_argument('--lr', type=float, default=0.01, required=False)
parser.add_argument('--inp_quants', default='Voltage1,Voltage2,StatorPuls,Speed', required=False)
parser.add_argument('--out_quants', default='Current1,Current2,Torque', required=False)
parser.add_argument('--stride', type=int, default=1)
parser.add_argument('--window', type=int, default=100)
parser.add_argument('--model', default='ffnn', help='fnn,cnn,enc_dec,lst,rnn,gru')

opt = parser.parse_args()

path = 'model_' + opt.model + '_stride_' + str(opt.stride) + '_window_' + str(opt.window) + \
        '_inp_quants_'  + opt.inp_quants + '_out_quants_' + opt.out_quants + '_lr_' + str(opt.lr) + \
        '_batch_size_' + str(opt.batch_size)

weight_path = opt.weight_dir + path + '.pt'
log_path = opt.log_dir + path + '.log'

fout = open(log_path, 'w')

dataset, index_quant_map = load_data(opt.data_dir)
samples = get_sample_metadata(dataset.shape[0], opt.stride, opt.window)
train_samples = samples[:int(len(samples)*0.7)]
test_samples = samples[int(len(samples)*0.7):]

if opt.model == 'ffnn':
    flatten = True

train_dataset = SignalPreloader(dataset, index_quant_map, train_samples, opt.inp_quants.split(','), opt.out_quants.split(','), flatten)
test_dataset = SignalPreloader(dataset, index_quant_map, test_samples, opt.inp_quants.split(','), opt.out_quants.split(','), flatten)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=opt.batch_size, shuffle=True, num_workers=4)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=opt.batch_size, shuffle=True, num_workers=4)

if opt.model == 'ffnn':
    model = FFNet1(len(opt.inp_quants.split(',')) * opt.window, len(opt.out_quants.split(','))).cuda()
if opt.model == 'cnn':
    model = CNN(len(opt.inp_quants.split(',')), len(opt.out_quants.split(','))).cuda()
if opt.model == 'enc_dec':
    model = EncDec(len(opt.inp_quants.split(',')), len(opt.out_quants.split(','))).cuda()

fout.write(str(model))
fout.write('\n')

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=opt.lr)

for epoch in range(opt.epochs):
    train_losses = []
    model.train()

    for inp, out in train_loader:
        inp = Variable(inp).cuda()
        out = Variable(out).cuda()

        optimizer.zero_grad()
        preds = model(inp)
        loss = criterion(preds, out)
        loss.backward()
        train_losses.append(loss.item())

    train_loss = np.mean(train_losses)
    print ('train loss : ', train_loss)

    optimizer.zero_grad()
    test_losses = []
    model.eval()

    for inp, out in test_loader:
        inp = Variable(inp).cuda()
        out = Variable(out).cuda()

        preds = model(inp)
        loss = criterion(preds, out)
        test_losses.append(loss.item())

    test_loss = np.mean(test_losses)
    print ('test loss : ', test_loss)

    fout.write('train loss : ' + str(train_loss) + ' test loss : ' + str(test_loss) + '\n')
    torch.save(model, weight_path)


fout.close()
