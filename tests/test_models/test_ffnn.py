import pytest

import torch
import torch.nn as nn

from motor_dynamics.models.ffnn import ShallowFNN, DeepFNN


class Test_ShallowFNN(object):
    """
    Test model intialization and forward function.
    """

    def test__init(self):
        model = ShallowFNN(10, 1)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 10)
        model = ShallowFNN(10, 1)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 2
        assert out.size()[0] == 8 and out.size()[1] == 1


class Test_DeepFNN(object):
    """
    Test model initialization and forward function.
    """

    def test__init(self):
        model = DeepFNN(10, 2)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 10)
        model = DeepFNN(10, 2)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 2
        assert out.size()[0] == 8 and out.size()[1] == 2
