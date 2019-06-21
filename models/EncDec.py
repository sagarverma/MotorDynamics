import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.nn import Parameter, ParameterList

class EncDecNet1(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecNet1, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 32, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)
                        
        self.dcnn4 = nn.ConvTranspose1d(256, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(128, 64, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(64, 32, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(32, output_dim, kernel_size=10, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.cnn3(x))
        x = self.act(self.cnn4(x))
        x = self.act(self.dcnn4(x))
        x = self.act(self.dcnn3(x))
        x = self.act(self.dcnn2(x))
        x = self.dcnn1(x)
        return x.view(-1, x.size()[-1], x.size()[1])
    
    
class EncDecNet2(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecNet2, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 8, kernel_size=3, stride=1)
        self.cnn2 = nn.Conv1d(8, 16, kernel_size=3, stride=1)
        
        self.dcnn2 = nn.ConvTranspose1d(16, 8, kernel_size=3, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(8, output_dim, kernel_size=3, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.dcnn2(x))
        x = self.dcnn1(x)
        return x.view(-1, x.size()[-1], x.size()[1])
    
class EncDecNet3(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecNet3, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 3, kernel_size=3, stride=1, bias=False)
        self.cnn2 = nn.Conv1d(3, 3, kernel_size=3, stride=1, bias=False)
        
        self.dcnn2 = nn.ConvTranspose1d(3, 3, kernel_size=3, stride=1, bias=False)
        self.dcnn1 = nn.ConvTranspose1d(3, output_dim, kernel_size=3, stride=1, bias=False)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.dcnn2(x))
        x = self.dcnn1(x)
        return x.view(-1, x.size()[-1], x.size()[1])
    
class EncDecSkipNet(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecSkipNet, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 32, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)
                        
        self.dcnn4 = nn.ConvTranspose1d(256, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(256, 64, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(128, 32, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(64, output_dim, kernel_size=10, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        x3 = self.act(self.cnn3(x2))
        x4 = self.act(self.cnn4(x3))
        
        x5 = self.act(self.dcnn4(x4))
        x6 = self.act(self.dcnn3(torch.cat((x5, x3), 1)))
        x7 = self.act(self.dcnn2(torch.cat((x6, x2), 1)))
        x8 = self.dcnn1(torch.cat((x7, x1), 1))
        
        return x8.view(-1, x8.size()[-1], x8.size()[1])
    
    
class EncDecBiLSTMSkipNet(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecBiLSTMSkipNet, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 32, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)
               
        self.rnn1 = nn.RNN(32, 32, batch_first=True, bidirectional=True)
        self.rnn2 = nn.RNN(64, 64, batch_first=True, bidirectional=True)
        self.rnn3 = nn.RNN(128, 128, batch_first=True, bidirectional=True)
        self.rnn4 = nn.RNN(256, 256, batch_first=True, bidirectional=True)
        
        self.dcnn4 = nn.ConvTranspose1d(768, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(384, 64, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(192, 32, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(96, output_dim, kernel_size=10, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        x3 = self.act(self.cnn3(x2))
        x4 = self.act(self.cnn4(x3))
        
        x1 = x1.permute(0,2,1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0,2,1)
        
        x2 = x2.permute(0,2,1)
        x2, _ = self.rnn2(x2)
        x2 = x2.permute(0,2,1)
        
        x3 = x3.permute(0,2,1)
        x3, _ = self.rnn3(x3)
        x3 = x3.permute(0,2,1)
        
        rx4 = x4.permute(0,2,1)
        rx4, _ = self.rnn4(rx4)
        rx4 = rx4.permute(0,2,1)
        
        x5 = self.act(self.dcnn4(torch.cat((x4, rx4), 1)))
        x6 = self.act(self.dcnn3(torch.cat((x5, x3), 1)))
        x7 = self.act(self.dcnn2(torch.cat((x6, x2), 1)))
        x8 = self.dcnn1(torch.cat((x7, x1), 1))
        
        return x8.view(-1, x8.size()[-1], x8.size()[1])

    
class EncDecBiLSTMSkipNet2(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecBiLSTMSkipNet2, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 8, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(8, 8, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(8, 8, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(8, 8, kernel_size=3, stride=1)
               
        self.rnn1 = nn.RNN(8, 8, batch_first=True, bidirectional=False)
        self.rnn2 = nn.RNN(8, 8, batch_first=True, bidirectional=False)
        self.rnn3 = nn.RNN(8, 8, batch_first=True, bidirectional=False)
        self.rnn4 = nn.RNN(8, 8, batch_first=True, bidirectional=False)
        
        self.dcnn4 = nn.ConvTranspose1d(16, 8, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(16, 8, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(16, 8, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(16, output_dim, kernel_size=10, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        x3 = self.act(self.cnn3(x2))
        x4 = self.act(self.cnn4(x3))
        
        x1 = x1.permute(0,2,1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0,2,1)
        
        x2 = x2.permute(0,2,1)
        x2, _ = self.rnn2(x2)
        x2 = x2.permute(0,2,1)
        
        x3 = x3.permute(0,2,1)
        x3, _ = self.rnn3(x3)
        x3 = x3.permute(0,2,1)
        
        rx4 = x4.permute(0,2,1)
        rx4, _ = self.rnn4(rx4)
        rx4 = rx4.permute(0,2,1)
        
        x5 = self.act(self.dcnn4(torch.cat((x4, rx4), 1)))
        x6 = self.act(self.dcnn3(torch.cat((x5, x3), 1)))
        x7 = self.act(self.dcnn2(torch.cat((x6, x2), 1)))
        x8 = self.dcnn1(torch.cat((x7, x1), 1))
        
        return x8.view(-1, x8.size()[-1], x8.size()[1])
    
    
class EncDecBiLSTMSkipNet3(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecBiLSTMSkipNet3, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 4, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(4, 4, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(4, 4, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(4, 4, kernel_size=3, stride=1)
               
        self.rnn1 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        self.rnn2 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        self.rnn3 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        self.rnn4 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        
        self.dcnn4 = nn.ConvTranspose1d(8, 4, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(8, 4, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(8, 4, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(8, output_dim, kernel_size=10, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        x3 = self.act(self.cnn3(x2))
        x4 = self.act(self.cnn4(x3))
        
        x1 = x1.permute(0,2,1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0,2,1)
        
        x2 = x2.permute(0,2,1)
        x2, _ = self.rnn2(x2)
        x2 = x2.permute(0,2,1)
        
        x3 = x3.permute(0,2,1)
        x3, _ = self.rnn3(x3)
        x3 = x3.permute(0,2,1)
        
        rx4 = x4.permute(0,2,1)
        rx4, _ = self.rnn4(rx4)
        rx4 = rx4.permute(0,2,1)
        
        x5 = self.act(self.dcnn4(torch.cat((x4, rx4), 1)))
        x6 = self.act(self.dcnn3(torch.cat((x5, x3), 1)))
        x7 = self.act(self.dcnn2(torch.cat((x6, x2), 1)))
        x8 = self.dcnn1(torch.cat((x7, x1), 1))
        
        return x8.view(-1, x8.size()[-1], x8.size()[1])
    
    
class EncDecBiLSTMSkipNet4(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecBiLSTMSkipNet4, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 4, kernel_size=5, stride=1)
        self.cnn2 = nn.Conv1d(4, 4, kernel_size=5, stride=1)
        self.cnn3 = nn.Conv1d(4, 4, kernel_size=3, stride=1)
        self.cnn4 = nn.Conv1d(4, 4, kernel_size=3, stride=1)
               
        self.rnn1 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        self.rnn2 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        self.rnn3 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        self.rnn4 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        
        self.dcnn4 = nn.ConvTranspose1d(8, 4, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(8, 4, kernel_size=3, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(8, 4, kernel_size=5, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(8, output_dim, kernel_size=5, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        x3 = self.act(self.cnn3(x2))
        x4 = self.act(self.cnn4(x3))
        
        x1 = x1.permute(0,2,1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0,2,1)
        
        x2 = x2.permute(0,2,1)
        x2, _ = self.rnn2(x2)
        x2 = x2.permute(0,2,1)
        
        x3 = x3.permute(0,2,1)
        x3, _ = self.rnn3(x3)
        x3 = x3.permute(0,2,1)
        
        rx4 = x4.permute(0,2,1)
        rx4, _ = self.rnn4(rx4)
        rx4 = rx4.permute(0,2,1)
        
        x5 = self.act(self.dcnn4(torch.cat((x4, rx4), 1)))
        x6 = self.act(self.dcnn3(torch.cat((x5, x3), 1)))
        x7 = self.act(self.dcnn2(torch.cat((x6, x2), 1)))
        x8 = self.dcnn1(torch.cat((x7, x1), 1))
        
        return x8.view(-1, x8.size()[-1], x8.size()[1])
    
    
class EncDecBiLSTMSkipNet5(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecBiLSTMSkipNet5, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 4, kernel_size=3, stride=1)
        self.cnn2 = nn.Conv1d(4, 4, kernel_size=3, stride=1)
               
        self.rnn1 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        self.rnn2 = nn.RNN(4, 4, batch_first=True, bidirectional=False)
        
        self.dcnn2 = nn.ConvTranspose1d(8, 4, kernel_size=3, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(8, output_dim, kernel_size=3, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        
        x1 = x1.permute(0,2,1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0,2,1)
        
        rx2 = x2.permute(0,2,1)
        rx2, _ = self.rnn2(rx2)
        rx2 = rx2.permute(0,2,1)
        

        x3 = self.act(self.dcnn2(torch.cat((x2, rx2), 1)))
        x4 = self.dcnn1(torch.cat((x3, x1), 1))
        
        return x4.view(-1, x4.size()[-1], x4.size()[1])
    
class IndRNNCell(nn.Module):
    def __init__(self, input_dim):
        super(IndRNNCell, self).__init__()
        self.w = Parameter(torch.Tensor(input_dim))
        self.u = Parameter(torch.Tensor(input_dim))
        self.b = Parameter(torch.Tensor(input_dim))
        self.act = F.tanh 
        
        self.reset_parameters()
        
    def reset_parameters(self):
        for name, weight in self.named_parameters():
            if "b" in name:
                weight.data.zero_()
            elif "w" in name:
                nn.init.constant_(weight, 1)
            elif "u" in name:
                nn.init.normal_(weight, 0, 0.01)
            else:
                weight.data.normal_(0, 0.01)
                # weight.data.uniform_(-stdv, stdv)
                
    def forward(self, x, h):
        return self.act(torch.mul(x, self.w) + torch.mul(self.u, h) + self.b)
    
class IndRNN(nn.Module):
    def __init__(self, inp_size, hidden_sizem, batch_first=False, bidirectional=False):
        super(IndRNN, self).__init__()
        self.inp_size = inp_size
        self.batch_first = batch_first
        self.bidirectional = bidirectional
        
        self.num_directions = 2 if self.bidirectional else 1
        
        if batch_first:
            self.time_index = 1
            self.batch_index = 0
        else:
            self.time_index = 0
            self.batch_index = 1
            
        self.cell = IndRNNCell(self.inp_size)
        
        h0 = torch.zeros(self.inp_size * self.num_directions, requires_grad=False)
        self.register_buffer('h0', h0)
        
    def forward(self, x, hidden=torch.tensor(float("nan"))):
        i = 0
        hx = self.h0.unsqueeze(0).expand(x.size(self.batch_index), self.inp_size * self.num_directions).contiguous()
        
        hx_cell = hx[:, : self.inp_size * 1]
        hx_cell_bi = hx[:, self.inp_size: self.inp_size * 2]
        
        outputs = []
        x_T = torch.unbind(x, self.time_index)
        time_frame = len(x_T)
        for t in range(time_frame):
            hx_cell = self.cell(x_T[t], hx_cell)
            outputs.append(hx_cell)
        x_cell = torch.stack(outputs, self.time_index)
        if self.bidirectional:
            outputs_bi = []
            for t in range(time_frame -1, -1, -1):
                hx_cell_bi = self.cell(x_T[t], hx_cell_bi)
                outputs_bi.append(hx_cell_bi)
            x_cell_bi = torch.stack(outputs_bi[::-1], self.time_index)
            x_cell = torch.cat([x_cell, x_cell_bi], 2)
         
        return x_cell, hx_cell
        
        
class EncDecBiLSTMSkipNet6(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecBiLSTMSkipNet6, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 4, kernel_size=3, stride=1)
        self.cnn2 = nn.Conv1d(4, 4, kernel_size=3, stride=1)
               
        self.rnn1 = IndRNN(4, 4, batch_first=True, bidirectional=False)
        self.rnn2 = IndRNN(4, 4, batch_first=True, bidirectional=False)
        
        self.dcnn2 = nn.ConvTranspose1d(8, 4, kernel_size=3, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(8, output_dim, kernel_size=3, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        
        x1 = x1.permute(0,2,1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0,2,1)
        
        rx2 = x2.permute(0,2,1)
        rx2, _ = self.rnn2(rx2)
        rx2 = rx2.permute(0,2,1)
        

        x3 = self.act(self.dcnn2(torch.cat((x2, rx2), 1)))
        x4 = self.dcnn1(torch.cat((x3, x1), 1))
        
        return x4.view(-1, x4.size()[-1], x4.size()[1])
    
class EncDecBiLSTMSkipNet7(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(EncDecBiLSTMSkipNet7, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 32, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)
               
        self.rnn1 = IndRNN(32, 32, batch_first=True, bidirectional=True)
        self.rnn2 = IndRNN(64, 64, batch_first=True, bidirectional=True)
        self.rnn3 = IndRNN(128, 128, batch_first=True, bidirectional=True)
        self.rnn4 = IndRNN(256, 256, batch_first=True, bidirectional=True)
        
        self.dcnn4 = nn.ConvTranspose1d(768, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(384, 64, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(192, 32, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(96, output_dim, kernel_size=10, stride=1)
        
        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh
    
    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        x3 = self.act(self.cnn3(x2))
        x4 = self.act(self.cnn4(x3))
        
        x1 = x1.permute(0,2,1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0,2,1)
        
        x2 = x2.permute(0,2,1)
        x2, _ = self.rnn2(x2)
        x2 = x2.permute(0,2,1)
        
        x3 = x3.permute(0,2,1)
        x3, _ = self.rnn3(x3)
        x3 = x3.permute(0,2,1)
        
        rx4 = x4.permute(0,2,1)
        rx4, _ = self.rnn4(rx4)
        rx4 = rx4.permute(0,2,1)
        
        x5 = self.act(self.dcnn4(torch.cat((x4, rx4), 1)))
        x6 = self.act(self.dcnn3(torch.cat((x5, x3), 1)))
        x7 = self.act(self.dcnn2(torch.cat((x6, x2), 1)))
        x8 = self.dcnn1(torch.cat((x7, x1), 1))
        
        return x8.view(-1, x8.size()[-1], x8.size()[1])