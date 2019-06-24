import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable


class ShallowRNN(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim, act='relu'):
        super(ShallowRNN, self).__init__()

        self.rnn = nn.RNN(input_dim, hidden_dim, 1,
                          batch_first=True, nonlinearity=act)
        self.linear1 = nn.Linear(hidden_dim, 256)
        self.linear2 = nn.Linear(256, output_dim)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, seq):
        out = self.rnn(seq)[0]
        out = self.act(self.linear1(out))
        out = self.linear2(out)
        return out


class DeepRNN(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim, act='relu'):
        super(DeepRNN, self).__init__()

        self.rnn1 = nn.RNN(input_dim, hidden_dim, 1,
                           batch_first=True, nonlinearity=act)
        self.rnn2 = nn.RNN(hidden_dim, hidden_dim, 1,
                           batch_first=True, nonlinearity=act)
        self.linear1 = nn.Linear(hidden_dim, 256)
        self.linear2 = nn.Linear(256, output_dim)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, seq):
        out = self.rnn1(seq)[0]
        out = self.rnn2(seq)[0]
        out = self.act(self.linear1(out))
        out = self.linear2(out)
        return out
