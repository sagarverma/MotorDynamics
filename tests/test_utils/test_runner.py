import pytest

import torch
import torch.optim as optim

from motornn.models.ffnn import ShallowFNN
from motornn.utils.runner import Runner
from motornn.utils.helpers import get_dataloaders, get_model, get_loss_function


class Test__Runner():
    def test__init__(self, setup_args):
        device = 0
        model = get_model(setup_args)
        optimizer = optim.SGD(model.parameters(), lr=0.1)
        criterion = get_loss_function(setup_args)
        train_loader, val_loader = get_dataloaders(setup_args)

        runner = Runner(device, model, optimizer,
                        criterion, train_loader, val_loader)

        assert isinstance(runner, Runner)
