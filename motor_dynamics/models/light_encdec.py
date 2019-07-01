import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

from indrnn import IndRNN


class ThinEncDec(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(ThinEncDec, self).__init__()
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


class UltraThinEncDec(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(UltraThinEncDec, self).__init__()
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

class ThinEncDecDiagBiRNNSkip(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(ThinEncDecDiagBiRNNSkip, self).__init__()
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
