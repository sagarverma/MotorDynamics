import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

class ShallowCNN(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        """Five layered network where first three are convolutional layers and
           last two are feedforward layers.

        Args:
            input_dim (int): Number of channels in the input.
            output_dim (int): Output length.
            act (int): Activation function to be used.

        Returns:
            nn.Module: ShallowCNN model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(ShallowCNN, self).__init__()

        self.cnn1 = nn.Conv1d(input_dim, 64, kernel_size=10, stride=3)
        self.cnn2 = nn.Conv1d(64, 128, kernel_size=7, stride=2)
        self.cnn3 = nn.Conv1d(128, 256, kernel_size=5, stride=1)
        self.linear1 = nn.Linear(256 * 9, 128)
        self.linear2 = nn.Linear(128, output_dim)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, x):
        x = x.permute(0,2,1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.cnn3(x))
        x = x.view(-1, 256 * 9)
        x = self.act(self.linear1(x))
        x = self.linear2(x)
        return x

class DeepCNN(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        """Six layered network where first four are convolutional layers and
           last two are feedforward layers.

        Args:
            input_dim (int): Number of channels in the input.
            output_dim (int): Output length.
            act (int): Activation function to be used.

        Returns:
            nn.Module: DeepCNN model.

        Raises:            ExceptionName: Why the exception is raised.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        """
        super(DeepCNN, self).__init__()

        self.cnn1 = nn.Conv1d(input_dim, 64, kernel_size=10, stride=3)
        self.cnn2 = nn.Conv1d(64, 128, kernel_size=7, stride=2)
        self.cnn3 = nn.Conv1d(128, 256, kernel_size=5, stride=1)
        self.cnn4 = nn.Conv1d(256, 256, kernel_size=3, stride=1)
        self.linear1 = nn.Linear(256 * 9, 128)
        self.linear2 = nn.Linear(128, output_dim)
        if act == 'relu':
            self.act = nn.ReLU()
        if act == 'tanh':
            self.act = nn.Tanh()

    def forward(self, x):
        x = x.permute(0,2,1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.cnn3(x))
        x = self.act(self.cnn4(x))
        x = x.view(-1, 256 * 9)
        x = self.act(self.linear1(x))
        x = self.linear2(x)
        return x
