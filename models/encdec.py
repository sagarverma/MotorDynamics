import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

from indrnn import IndRNN

class ShallowEncDec(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        """Convolutional encoder-decoder network with four layer of
           convolutions in the encoder and four layers of transposed
           convolutions in the decoder.

        Args:
            input_dim (int): Number of input channels.
            output_dim (int): Number of output channels.
            act (str): Activation function to be used.

        Returns:
            nn.Module: ShallowEncDec model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(ShallowEncDec, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 32, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)

        self.dcnn4 = nn.ConvTranspose1d(256, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(128, 64, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(64, 32, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(32, output_dim, kernel_size=10, stride=1)

        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, x):
        x = x.permute(0, 2, 1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.cnn3(x))
        x = self.act(self.cnn4(x))
        x = self.act(self.dcnn4(x))
        x = self.act(self.dcnn3(x))
        x = self.act(self.dcnn2(x))
        x = self.dcnn1(x)
        return x.view(-1, x.size()[-1], x.size()[1])


class DeepEncDec(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        """Deep convolutional encoder-decoder network with five layers of
           convolutions in encoder and five layers of transposed convolutions
           in decoder.

        Args:
            input_dim (int): Number of input channels.
            output_dim (int): Number of output channels.
            act (str): Activation function to be used.

        Returns:
            nn.Module: DeepEncDec model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(DeepEncDec, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 32, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)
        self.cnn5 = nn.Conv1d(256, 512, kernel_size=3, stride=1)

        self.dcnn5 = nn.ConvTranspose1d(512, 256, kernel_size=3, stride=1)
        self.dcnn4 = nn.ConvTranspose1d(256, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(128, 64, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(64, 32, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(32, output_dim,
                                        kernel_size=10, stride=1)

        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, x):
        x = x.permute(0, 2, 1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.cnn3(x))
        x = self.act(self.cnn4(x))
        x = self.act(self.cnn5(x))

        x = self.act(self.dcnn5(x))
        x = self.act(self.dcnn4(x))
        x = self.act(self.dcnn3(x))
        x = self.act(self.dcnn2(x))
        x = self.dcnn1(x)

        return x.view(-1, x.size()[-1], x.size()[1])


class EncDecSkip(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        """Convolutional encoder-decoder network with skip connections.
           Encoder part has four layers of convolutions and
           decoder has four layers of transposed convolutions.

        Args:
            input_dim (int): Number of input channels.
            output_dim (int): Number of output channels.
            act (str): Activation function to be used.

        Returns:
            nn.Module: EncDecSkip model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(EncDecSkip, self).__init__()
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

class EncDecRNNSkip(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        """Convolutional encoder-decoder network with skip connections
           using RNN. Encoder part has four layers of convolutions and
           decoder has four layers of transposed convolutions. For skip
           connections four RNNs are used for each layers in encoder-decoder.

        Args:
            input_dim (int): Number of input channels.
            output_dim (int): Number of output channels.
            act (str): Activation function to be used.

        Returns:
            nn.Module: EncDecSkip model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(EncDecRNNSkip, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 32, kernel_size=10, stride=1)
        self.cnn2 = nn.Conv1d(32, 64, kernel_size=7, stride=1)
        self.cnn3 = nn.Conv1d(64, 128, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(128, 256, kernel_size=3, stride=1)

        self.rnn1 = nn.RNN(32, 32, batch_first=True, bidirectional=False)
        self.rnn2 = nn.RNN(64, 64, batch_first=True, bidirectional=False)
        self.rnn3 = nn.RNN(128, 128, batch_first=True, bidirectional=False)
        self.rnn4 = nn.RNN(256, 256, batch_first=True, bidirectional=False)

        self.dcnn4 = nn.ConvTranspose1d(512, 128, kernel_size=3, stride=1)
        self.dcnn3 = nn.ConvTranspose1d(256, 64, kernel_size=5, stride=1)
        self.dcnn2 = nn.ConvTranspose1d(128, 32, kernel_size=7, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(64, output_dim,
                                        kernel_size=10, stride=1)

        if act == 'relu':
            self.act = torch.relu()
        if act == 'tanh':
            self.act = torch.tanh()

    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        x3 = self.act(self.cnn3(x2))
        x4 = self.act(self.cnn4(x3))

        x1 = x1.permute(0, 2, 1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0, 2, 1)

        x2 = x2.permute(0, 2, 1)
        x2, _ = self.rnn2(x2)
        x2 = x2.permute(0, 2, 1)

        x3 = x3.permute(0, 2, 1)
        x3, _ = self.rnn3(x3)
        x3 = x3.permute(0, 2, 1)

        rx4 = x4.permute(0, 2, 1)
        rx4, _ = self.rnn4(rx4)
        rx4 = rx4.permute(0, 2, 1)

        x5 = self.act(self.dcnn4(torch.cat((x4, rx4), 1)))
        x6 = self.act(self.dcnn3(torch.cat((x5, x3), 1)))
        x7 = self.act(self.dcnn2(torch.cat((x6, x2), 1)))
        x8 = self.dcnn1(torch.cat((x7, x1), 1))

        return x8.view(-1, x8.size()[-1], x8.size()[1])


class EncDecBiRNNSkip(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        """Convolutional encoder-decoder network with skip connections
           using bidirectional RNN. Encoder part has four layers of
           convolutions and decoder has four layers of transposed convolutions.
           For skip connections four RNNs are used for each layers in
           encoder-decoder.

        Args:
            input_dim (int): Number of input channels.
            output_dim (int): Number of output channels.
            act (str): Activation function to be used.

        Returns:
            nn.Module: EncDecSkip model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
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
        self.dcnn1 = nn.ConvTranspose1d(96, output_dim,
                                        kernel_size=10, stride=1)

        if act == 'relu':
            self.act = torch.relu()
        if act == 'tanh':
            self.act = torch.tanh()

    def forward(self, x):
        x = x.permute(0,2,1)
        x1 = self.act(self.cnn1(x))
        x2 = self.act(self.cnn2(x1))
        x3 = self.act(self.cnn3(x2))
        x4 = self.act(self.cnn4(x3))

        x1 = x1.permute(0, 2, 1)
        x1, _ = self.rnn1(x1)
        x1 = x1.permute(0, 2, 1)

        x2 = x2.permute(0, 2, 1)
        x2, _ = self.rnn2(x2)
        x2 = x2.permute(0, 2, 1)

        x3 = x3.permute(0, 2, 1)
        x3, _ = self.rnn3(x3)
        x3 = x3.permute(0, 2, 1)

        rx4 = x4.permute(0, 2, 1)
        rx4, _ = self.rnn4(rx4)
        rx4 = rx4.permute(0, 2, 1)

        x5 = self.act(self.dcnn4(torch.cat((x4, rx4), 1)))
        x6 = self.act(self.dcnn3(torch.cat((x5, x3), 1)))
        x7 = self.act(self.dcnn2(torch.cat((x6, x2), 1)))
        x8 = self.dcnn1(torch.cat((x7, x1), 1))

        return x8.view(-1, x8.size()[-1], x8.size()[1])


class EncDecDiagBiRNNSkip(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        """Convolutional encoder-decoder network with skip connections
           using bidirectional independent RNN. Encoder part has four
           layers of convolutions and decoder has four layers of transposed
           convolutions. For skip connections four RNNs are used for each
           layers in encoder-decoder.

        Args:
            input_dim (int): Number of input channels.
            output_dim (int): Number of output channels.
            act (str): Activation function to be used.

        Returns:
            nn.Module: EncDecSkip model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(EncDecDiagBiRNNSkip, self).__init__()
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
        self.dcnn1 = nn.ConvTranspose1d(96, output_dim,
                                        kernel_size=10, stride=1)

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
