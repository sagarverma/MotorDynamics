"""
This module implement bidirectional independent RNN from the paper
http://openaccess.thecvf.com/content_cvpr_2018/papers/Li_Independently_Recurrent_Neural_CVPR_2018_paper.pdf
"""
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.nn import Parameter, ParameterList


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
