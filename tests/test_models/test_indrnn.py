import pytest

import torch
import torch.nn as nn

from motor_dynamics.models.indrnn import IndRNNCell, IndRNN


class Test_IndRNNCell(object):
    """
    Test Independent RNN Cell class.
    """

    def test__init(self):
        model = IndRNNCell(3)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        model = IndRNNCell(3)
        inp = torch.randn(8, 3)
        h = torch.randn(8, 3)
        out = model(inp, h)
        assert isinstance(out, torch.Tensor)
        assert out.size()[0] == 8 and out.size()[1] == 3


class Test_IndRNN(object):
    """
    Test Independent RNN class.
    """

    def test__init(self):
        model = IndRNN(3, batch_first=True)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        model = IndRNN(3, batch_first=True)
        inp = torch.randn(8, 100, 3)
        out = model(inp)
        assert isinstance(out, tuple)
        assert isinstance(out[0], torch.Tensor)
        assert isinstance(out[1], torch.Tensor)
        assert len(out[0].size()) == 3
        assert out[0].size()[0] == 8 and out[0].size()[1] == 100 and \
            out[0].size()[2] == 3
