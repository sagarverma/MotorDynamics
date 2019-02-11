import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

class RNNNet1(nn.Module):

    def __init__(self, input_dim, output_dim, hidden_dim, act='relu'):
        super(RNNNet1, self).__init__()

        self.rnn = nn.RNN(input_dim, hidden_dim, 2, batch_first=True, nonlinearity=act)
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
        out = torch.mean(out, dim=1)
        return out
    
class RNNNet2(nn.Module):

    def __init__(self, input_dim, output_dim, hidden_dim, act='relu'):
        super(RNNNet2, self).__init__()

        self.rnn = nn.RNN(input_dim, hidden_dim, 2, batch_first=True, nonlinearity=act)
        self.linear1 = nn.Linear(hidden_dim, 256)
        self.linear2 = nn.Linear(256, 128)
        self.linear3 = nn.Linear(128, output_dim)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, seq):
        out = self.rnn(seq)[0]
        out = self.act(self.linear1(out))
        out = self.act(self.linear2(out))
        out = self.linear3(out)
        out = torch.mean(out, dim=1)
        return out
    

    
