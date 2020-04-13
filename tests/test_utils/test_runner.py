import pytest

import torch
import torch.optim as optim

from motornn.models.ffnn import ShallowFNN
from motornn.utils.runner import Runner
from motornn.utils.helpers import get_dataloaders, get_model, get_loss_function


class Test__Runner():
    @pytest.fixture(scope='module')
    def test__init__(self, setup_args):
        device = 0
        model = get_model(setup_args)
        optimizer = optim.SGD(model.parameters(), lr=0.1)
        criterion = get_loss_function(setup_args)
        train_loader, val_loader = get_dataloaders(setup_args)

        runner = Runner(device, model, optimizer,
                        criterion, train_loader, val_loader)

        return runner

    def test__set_epoch_metrics(self, test__init__):
        test__init__.set_epoch_metrics()

        assert isinstance(test__init__.train_metrics, dict)
        assert isinstance(test__init__.val_metrics, dict)

    def test__batch_to_gpu(self, test__init__):
        input_tensor, output_tensor = next(iter(test__init__.train_loader))

        input_tensor, output_tensor = test__init__.batch_to_gpu(input_tensor, output_tensor)

        assert isinstance(input_tensor, torch.Tensor)
        assert isinstance(output_tensor, torch.Tensor)
        assert input_tensor.is_cuda
        assert output_tensor.is_cuda

    def test__train_forward_backward(self, test__init__):
        input_tensor, output_tensor = next(iter(test__init__.train_loader))
        input_tensor, output_tensor = test__init__.batch_to_gpu(input_tensor, output_tensor)
        prediction_tensor, loss = test__init__.train_forward_backward(input_tensor, output_tensor)

        assert isinstance(prediction_tensor, torch.Tensor)
        assert prediction_tensor.is_cuda

    def test__eval_forward(self, test__init__):
        input_tensor, output_tensor = next(iter(test__init__.train_loader))
        input_tensor, output_tensor = test__init__.batch_to_gpu(input_tensor, output_tensor)
        prediction_tensor, loss = test__init__.eval_forward(input_tensor, output_tensor)

        assert isinstance(prediction_tensor, torch.Tensor)
        assert prediction_tensor.is_cuda

    def test__train_model(self, test__init__):
        mean_metrics = test__init__.train_model()

        assert isinstance(mean_metrics, dict)

    def test__eval_model(self, test__init__):
        mean_metrics = test__init__.eval_model()

        assert isinstance(mean_metrics, dict)
