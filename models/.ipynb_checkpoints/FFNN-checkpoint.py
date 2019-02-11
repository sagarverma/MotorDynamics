import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

class FFNet1(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(FFNet1, self).__init__()
        self.linear1 = nn.Linear(input_dim, 1024)
        self.linear2 = nn.Linear(1024, 512)
        self.linear3 = nn.Linear(512, 256)
        self.linear4 = nn.Linear(256, output_dim)
        self.dropout = nn.Dropout(0.5)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, x):
        out = self.act(self.linear1(x))
        out = self.dropout(self.act(self.linear2(out)))
        out = self.act(self.linear3(out))
        out = self.linear4(out)
        return out


class FFNet2(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(FFNet2, self).__init__()
        self.linear1 = nn.Linear(input_dim, 1024)
        self.linear2 = nn.Linear(1024, 512)
        self.linear3 = nn.Linear(512, 256)
        self.linear4 = nn.Linear(256, 128)
        self.linear5 = nn.Linear(128, output_dim)
        self.dropout = nn.Dropout(0.5)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, x):
        out = self.act(self.linear1(x))
        out = self.dropout(self.act(self.linear2(out)))
        out = self.act(self.linear3(out))
        out = self.act(self.linear4(out))
        out = self.linear5(out)
        return out
