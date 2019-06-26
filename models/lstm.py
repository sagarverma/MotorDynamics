import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable


class ShallowLSTM(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim, act='relu'):
        """Three layered network with frist layer as LSTM and last two layers
           are feedforward layers.

        Args:
            input_dim (int): Number of input channels.
            output_dim (int): Number of output channels.
            hidden_dim (int): LSTM hidden vector length.
            act (str): Activation function to be used for feedforward layers.

        Returns:
            nn.Module: ShallowLSTM model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(ShallowLSTM, self).__init__()

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
        return out


class DeepLSTM(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim, act='relu'):
        """Four layered network with frist two as LSTM and last two layers
           are feedforward layers.

        Args:
            input_dim (int): Number of input channels.
            output_dim (int): Number of output channels.
            hidden_dim (int): LSTM hidden vector length.
            act (str): Activation function to be used for feedforward layers.

        Returns:
            nn.Module: DeepLSTM model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(DeepLSTM, self).__init__()

        self.lstm1 = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.lstm2 = nn.LSTM(hidden_dim, hidden_dim, batch_first=True)
        self.linear1 = nn.Linear(hidden_dim, 256)
        self.linear2 = nn.Linear(256, output_dim)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, seq):
        out = self.lstm1(seq)[0]
        out = self.lstm2(seq)[0]
        out = self.act(self.linear1(out))
        out = self.linear2(out)
        return out
