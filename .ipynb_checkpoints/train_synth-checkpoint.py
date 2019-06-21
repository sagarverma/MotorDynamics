import sys, glob, cv2, random, math, argparse
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from tqdm import trange

import torch
import torch.utils.data
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable

from utils.dataloader import *
from models.EncDec import *

random.seed(1234)

parser = argparse.ArgumentParser(description='Train a model on electric motor simulink data')

parser.add_argument('--train_sim_dir', default='../datasets/data/train_sim/', required=False)
parser.add_argument('--train_raw_dir', default='../datasets/data/train_raw/', required=False)
parser.add_argument('--val_sim_dir', default='../datasets/data/val_sim/', required=False)
parser.add_argument('--test_raw_dir', default='../datasets/data/test_raw/', required=False)
parser.add_argument('--weight_dir', default='../weights/', required=False)
parser.add_argument('--log_dir', default='../logs/', required=False)
parser.add_argument('--epochs', type=int, default=20, required=False)
parser.add_argument('--batch_size', type=int, default=1024, required=False)
parser.add_argument('--lr', type=float, default=0.01, required=False)
parser.add_argument('--inp_quants', default='Voltage1,Voltage2,Speed', required=False)
parser.add_argument('--out_quants', default='Current1,Current2,Torque', required=False)
parser.add_argument('--stride', type=int, default=1)
parser.add_argument('--window', type=int, default=100)
parser.add_argument('--model', default='encdec1', help='encdecBilstmSkip')
parser.add_argument('--act', default='relu', help='relu/tanh')
parser.add_argument('--hidden', type=int, default=32, help='rnn/lstm hidden size')

opt = parser.parse_args()

if 'cnn' in opt.model or 'encdec' in opt.model:
    path = 'modelNewLawDQSynthData_' + opt.model + '_act_' + opt.act + '_stride_' + str(opt.stride) + '_window_' + \
    str(opt.window) + '_inpQuants_'  + opt.inp_quants + '_outQuants_' + opt.out_quants + '_lr_' + str(opt.lr) + \
        '_batchSize_' + str(opt.batch_size) + '_epochs_' + str(opt.epochs)
    
weight_path = opt.weight_dir + path + '.pt'
log_path = opt.log_dir + path + '.log'

fout = open(log_path, 'w')

if 'ffnn' in opt.model:
    flatten = True
else:
    flatten = False
    
if 'encdec' in opt.model:
    enc_dec = True
else:
    enc_dec = False
    
train_sim_dataset, index_quant_map = load_synth_data(opt.train_sim_dir)
train_raw_dataset, index_quant_map = load_synth_data(opt.train_raw_dir)
val_sim_dataset, index_quant_map = load_synth_data(opt.val_sim_dir)
test_raw_dataset, index_quant_map = load_synth_data(opt.test_raw_dir)

train_sim_samples = get_sample_metadata(train_sim_dataset, opt.stride, opt.window)
train_raw_samples = get_sample_metadata(train_raw_dataset, opt.stride, opt.window)
val_sim_samples = get_sample_metadata(val_sim_dataset, opt.stride, opt.window)
test_raw_samples = get_sample_metadata(test_raw_dataset, opt.stride, opt.window)

print ('train sim samples : ', len(train_sim_samples))
print ('train raw samples : ', len(train_raw_samples))
print ('val sim samples : ', len(val_sim_samples))
print ('test raw samples : ', len(test_raw_samples))

train_sim_loader = SignalPreloader(train_sim_dataset, index_quant_map, train_sim_samples, opt.inp_quants.split(','), opt.out_quants.split(','), flatten, enc_dec)
train_raw_loader = SignalPreloader(train_raw_dataset, index_quant_map, train_raw_samples, opt.inp_quants.split(','), opt.out_quants.split(','), flatten, enc_dec)
val_sim_loader = SignalPreloader(val_sim_dataset, index_quant_map, val_sim_samples, opt.inp_quants.split(','), opt.out_quants.split(','), flatten, enc_dec)
test_raw_loader = SignalPreloader(test_raw_dataset, index_quant_map, test_raw_samples, opt.inp_quants.split(','), opt.out_quants.split(','), flatten, enc_dec)

train_sim_loader = torch.utils.data.DataLoader(train_sim_loader, batch_size=opt.batch_size, shuffle=True, num_workers=32)
train_raw_loader = torch.utils.data.DataLoader(train_raw_loader, batch_size=opt.batch_size, shuffle=False, num_workers=32)
val_sim_loader = torch.utils.data.DataLoader(val_sim_loader, batch_size=opt.batch_size, shuffle=False, num_workers=32)
test_raw_loader = torch.utils.data.DataLoader(test_raw_loader, batch_size=opt.batch_size, shuffle=False, num_workers=32)

if opt.model == 'encdec1':
    model = EncDecNet1(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdec2':
    model = EncDecNet2(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdec3':
    model = EncDecNet3(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdecSkip':
    model = EncDecSkipNet(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdecBilstmSkip':
    model = EncDecBiLSTMSkipNet(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
#     model = torch.load('../weights/modelNewLawDQSynthData_encdecBilstmSkip_act_relu_stride_1_window_100_inpQuants_Voltage1,Voltage2,Speed_outQuants_Current2_lr_0.0001_batchSize_8000_epochs_2000.pt')
if opt.model == 'encdecBilstmSkip2':
    model = EncDecBiLSTMSkipNet2(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdecBilstmSkip3':
    model = EncDecBiLSTMSkipNet3(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdecBilstmSkip4':
    model = EncDecBiLSTMSkipNet4(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdecBilstmSkip5':
    model = EncDecBiLSTMSkipNet5(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdecBilstmSkip6':
    model = EncDecBiLSTMSkipNet6(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
if opt.model == 'encdecBilstmSkip7':
    model = EncDecBiLSTMSkipNet7(len(opt.inp_quants.split(',')), len(opt.out_quants.split(',')), act=opt.act).cuda()
    
print ('Parameters :', sum(p.numel() for p in model.parameters()))

fout.write(str(model))
fout.write('\n')

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=opt.lr)

best_loss = 1000000000000
for epoch in range(opt.epochs):
    train_sim_losses = []
    val_sim_losses = []
    test_raw_losses = []
    
    model.train()

#     t = trange(len(train_loader))    
    for inp, out in train_sim_loader:
        inp = Variable(inp).cuda()
        out = Variable(out).cuda()

        optimizer.zero_grad()
        preds = model(inp)
        loss = criterion(preds, out)
        loss.backward()
        optimizer.step()

        train_sim_losses.append(loss.item())
        
#         t.set_postfix(loss=loss.data.tolist())
#         t.update()

    train_sim_loss = np.mean(train_sim_losses)
#     t.set_postfix(loss=train_loss)
#     t.update()


    model.eval()

#     t = trange(len(test_loader))
    for inp, out in val_sim_loader:
        inp = Variable(inp).cuda()
        out = Variable(out).cuda()

        preds = model(inp)
        loss = criterion(preds, out)
        val_sim_losses.append(loss.item())
        
#         t.set_postfix(loss=loss.data.tolist())
#         t.update()

    val_sim_loss = np.mean(val_sim_losses)
#     t.set_postfix(loss=test_loss)
#     t.update()
    
    for inp, out in test_raw_loader:
        inp = Variable(inp).cuda()
        out = Variable(out).cuda()
        
        preds = model(inp)
        loss = criterion(preds, out)
        test_raw_losses.append(loss.item())
        
    test_raw_loss = np.mean(test_raw_losses)
    
    print ('train sim loss : ' + str(train_sim_loss) + ' val sim loss : ' + str(val_sim_loss) + ' test raw loss : ' + str(test_raw_loss))
    fout.write('train sim loss : ' + str(train_sim_loss) + ' val sim loss : ' + str(val_sim_loss) +  'test raw loss : ' + str(test_raw_loss) + '\n')
    
    if best_loss > test_raw_loss:
        torch.save(model, weight_path)
        best_loss = test_raw_loss
        
fout.close()
