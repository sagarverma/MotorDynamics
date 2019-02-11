import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

class LSTMNet1(nn.Module):

    def __init__(self, input_dim, output_dim, hidden_dim, act='relu'):
        super(LSTMNet1, self).__init__()

        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.linear1 = nn.Linear(hidden_dim, 256)
        self.linear2 = nn.Linear(256, output_dim)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, seq):
        out = self.lstm(seq)[0]
        out = self.act(self.linear1(out))
        out = self.linear2(out)
        out = torch.mean(out, dim=1)
        return out

class LSTMNet2(nn.Module):

    def __init__(self, input_dim, output_dim, hidden_dim, act='relu'):
        super(LSTMNet2, self).__init__()

        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.linear1 = nn.Linear(hidden_dim, 256)
        self.linear2 = nn.Linear(256, 128)
        self.linear3 = nn.Linear(128, output_dim)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, seq):
        out = self.lstm(seq)[0]
        out = self.act(self.linear1(out))
        out = self.act(self.linear2(out))
        out = self.linear3(out)
        out = torch.mean(out, dim=1)
        return out
    

    
