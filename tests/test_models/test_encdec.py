import pytest

import torch
import torch.nn as nn

from motor_dynamics.models.encdec import (ShallowEncDec, DeepEncDec,
                                          EncDecSkip, EncDecRNNSkip,
                                          EncDecBiRNNSkip, EncDecDiagBiRNNSkip)


class Test_ShallowEncDec(object):
    """
    Test model intialization and forward function.
    """

    def test__init(self):
        model = ShallowEncDec(1, 1)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 1, 100)
        model = ShallowEncDec(1, 1)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 3
        assert out.size()[0] == 8 and out.size()[1] == 1 and \
            out.size()[2] == 100


class Test_DeepEncDec(object):
    """
    Test model intialization and forward function.
    """

    def test__init(self):
        model = DeepEncDec(1, 1)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 1, 100)
        model = DeepEncDec(1, 1)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 3
        assert out.size()[0] == 8 and out.size()[1] == 1 and \
            out.size()[2] == 100


class Test_EncDecSkip(object):
    """
    Test model initialization and forward function.
    """

    def test__init(self):
        model = EncDecSkip(1, 1)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 1, 100)
        model = EncDecSkip(1, 1)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 3
        assert out.size()[0] == 8 and out.size()[1] == 1 and \
            out.size()[2] == 100


class Test_EncDecRNNSkip(object):
    """
    Test model initialization and forward function.
    """

    def test__init(self):
        model = EncDecRNNSkip(1, 1)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 1, 100)
        model = EncDecRNNSkip(1, 1)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 3
        assert out.size()[0] == 8 and out.size()[1] == 1 and \
            out.size()[2] == 100


class Test_EncDecBiRNNSkip(object):
    """
    Test model initialization and forward function.
    """

    def test__init(self):
        model = EncDecBiRNNSkip(1, 1)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 1, 100)
        model = EncDecBiRNNSkip(1, 1)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 3
        assert out.size()[0] == 8 and out.size()[1] == 1 and \
            out.size()[2] == 100


class Test_EncDecDiagBiRNNSkip(object):
    """
    Test model initialization and forward function.
    """

    def test__init(self):
        model = EncDecDiagBiRNNSkip(1, 1)
        assert isinstance(model, nn.Module)

    def test__forward(self):
        inp = torch.randn(8, 1, 100)
        model = EncDecDiagBiRNNSkip(1, 1)
        out = model(inp)
        assert isinstance(out, torch.Tensor)
        assert len(out.size()) == 3
        assert out.size()[0] == 8 and out.size()[1] == 1 and \
            out.size()[2] == 100
