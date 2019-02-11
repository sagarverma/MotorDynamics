import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

class EncDecNet1(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecNet1, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 32, kernel_size=5, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=5, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=3, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)
                        
        self.dcnn4 = nn.ConvTranspose1d(256, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(128, 64, kernel_size=3, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(64, 32, kernel_size=5, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(32, output_dim, kernel_size=5, stride=1)
        
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.cnn3(x))
        x = self.act(self.dcnn3(x))
        x = self.act(self.dcnn2(x))
        x = self.dcnn1(x)
        return x.view(-1, x.size()[-1])