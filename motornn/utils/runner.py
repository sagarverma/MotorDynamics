import torch
from torch.autograd import Variable

from motornn.utils.helpers import (initialize_metrics,
                                    get_mean_metrics,
                                    compute_metrics)

class Runner():
    def __init__(self, device, model,
                optimizer, criterion,
                train_loader, val_loader):
        self.device = device
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.train_metrics = initialize_metrics()
        self.val_metrics = initialize_metrics()

    def set_epoch_metrics(self):
        self.train_metrics = initialize_metrics()
        self.val_metrics = initialize_metrics()

    def batch_to_gpu(self, input_tensor, output_tensor):
        input_tensor = Variable(input_tensor).to(self.device)
        output_tensor = Variable(output_tensor).to(self.device)
        return input_tensor, output_tensor

    def train_forward_backward(self, input_tensor, output_tensor):
        # Zero the gradient
        self.optimizer.zero_grad()

        # Get model predictions, calculate loss, backprop
        prediction_tensor = self.model(input_tensor)
        loss = self.criterion(prediction_tensor, output_tensor)
        loss.backward()
        self.optimizer.step()
        return prediction_tensor, loss

    def eval_forward(self, input_tensor, output_tensor):
        # Get predictions and calculate loss
        prediction_tensor = self.model(input_tensor)
        loss = self.criterion(prediction_tensor, output_tensor)
        return prediction_tensor, loss

    def train_model(self):
        self.model.train()

        for input_tensor, output_tensor in self.train_loader:
            input_tensor, output_tensor = self.batch_to_gpu(input_tensor,
                                                          output_tensor)

            prediction_tensor, loss = self.train_forward_backward(input_tensor,
                                                   output_tensor)
            compute_metrics(self.train_metrics, loss, prediction_tensor,
                                                    output_tensor)
            # clear batch variables from memory
            del input_tensor, output_tensor

        return get_mean_metrics(self.train_metrics)

    def eval_model(self):
        self.model.eval()

        for input_tensor, output_tensor in self.train_loader:
            input_tensor, output_tensor = self.batch_to_gpu(input_tensor,
                                                          output_tensor)

            prediction_tensor, loss = self.eval_forward(input_tensor, output_tensor)
            compute_metrics(self.val_metrics, loss, prediction_tensor,
                                                    output_tensor)
            # clear batch variables from memory
            del input_tensor, output_tensor

        return get_mean_metrics(self.val_metrics)
