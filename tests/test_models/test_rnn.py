import pytest

import torch
import torch.nn as nn

from motor_dynamics.models.rnn import ShallowRNN, DeepRNN


class Test_ShallowRNN(object):
    """
    Test model intialization and forward function.
    """

    def test__init(self):
        model = ShallowRNN(1, 1, 32)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 1, 100)
        model = ShallowRNN(1, 1, 32)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 3
        assert out.size()[0] == 8 and out.size()[1] == 100


class Test_DeepRNN(object):
    """
    Test model initialization and forward function.
    """

    def test__init(self):
        model = DeepRNN(1, 1, 32)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 1, 100)
        model = DeepRNN(1, 1, 32)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 3
        assert out.size()[0] == 8 and out.size()[1] == 100
