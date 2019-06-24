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

from utils.parser import get_parser_with_args
from utils.helper import get_file_names
from utils.dataloader import *
from models.EncDec import *

random.seed(1234)

"""
Intialize Parser and define arguments
"""

parser = get_parser_with_args()
opt = parser.parse_args()

"""
Set up environment: define paths, get dataloader, and set device
"""
weight_path, log_path = get_file_names(opt)
dev = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
logging.info('GPU AVAILABLE? ' + str(torch.cuda.is_available()))
train_loader, val_loader, test_loader = get_loaders(opt)


fout = open(log_path, 'w')

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
