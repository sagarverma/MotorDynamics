import os

import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from motormetrics.ml import *

from motornn.utils.dataloader import (load_data, FlatInFlatOut,
                              SeqInFlatOut, SeqInSeqOut)

from motornn.models.cnn import ShallowCNN, DeepCNN
from motornn.models.ffnn import ShallowFNN, DeepFNN
from motornn.models.rnn import ShallowRNN, DeepRNN
from motornn.models.lstm import ShallowLSTM, DeepLSTM
from motornn.models.encdec import (ShallowEncDec, DeepEncDec, EncDecSkip,
                          EncDecRNNSkip, EncDecBiRNNSkip,
                          EncDecDiagBiRNNSkip)

from motormetrics.ml import *

def get_file_names(opt):
    """Get file fully qualified names to write weights and logs.

    Args:
        opt (argparse.ArgumentParser): Parsed arguments.

    Returns:
        tuple: weight path and log path.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    suffix = '_act_' + opt.act
    suffix += '_stride_' + str(opt.stride)
    suffix += '_window_' + str(opt.window)
    suffix += '_inpQuants_' + opt.inp_quants
    suffix += '_outQuants_' + opt.out_quants
    suffix += '_lr_' + str(opt.lr)
    suffix += '_batchSize_' + str(opt.batch_size)
    suffix += '_epochs_' + str(opt.epochs)
    suffix += '_loss_' + str(opt.loss)

    if 'fnn' in opt.model:
        fname = opt.model + suffix

    if 'rnn' in opt.model or 'lstm' in opt.model:
        fname = opt.model + suffix
        fname += '_hiddenSize_' + str(opt.hidden_size)

    if 'cnn' in opt.model or 'encdec' in opt.model:
        fname = opt.model + suffix

    if not os.path.exists(os.path.join(opt.weights_dir, opt.model)):
        os.makedirs(os.path.join(opt.weights_dir, opt.model))

    if not os.path.exists(os.path.join(opt.logs_dir, opt.model)):
        os.makedirs(os.path.join(opt.logs_dir, opt.model))

    weight_path = os.path.join(opt.weights_dir, opt.model, fname + '.pt')
    log_path = os.path.join(opt.logs_dir, opt.model, fname + '.log')

    return weight_path, log_path


def initialize_metrics():
    """Generates a dictionary of metrics with metrics as keys and
       empty lists as values.

    Returns:
        dict: A dictionary of metrics.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """

    metrics = {
        'loss': [],
        'smape': [],
        'r2': [],
        # 'rmsle': [],
        'rmse': [],
        'mae': []
    }

    return metrics


def get_mean_metrics(metrics_dict):
    """Takes a dictionary of lists for metrics and returns dict of mean values.

    Args:
        metrics_dict (dict): A dictionary of metrics.

    Returns:
        dict: Dictionary of floats that reflect mean metric value.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    return {k: np.mean(v) for k, v in metrics_dict.items()}

def transform_tensor(tensor):
    r"""
    Transform all tensor types to numpy ndarray.
    """
    if isinstance(tensor, torch.Tensor):
        if tensor.is_cuda:
            return tensor.data.cpu().numpy()
        else:
            return tensor.data.numpy()
    if isinstance(tensor, np.ndarray):
        return tensor
    if isinstance(tensor, list):
        return np.asarray(tensor)

def compute_metrics(metrics_dict, loss, predicted, target):
    """Updates metrics dictionary with batch metrics.

    Args:
        metric_dict (dict): Dictionary of metrics.
        loss (torch.float): Loss value.
        smape (torch.float): SMAPE value.

    Returns:
        type: Description of returned object.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    metrics_dict['loss'].append(loss.item())

    predicted = transform_tensor(predicted)
    target = transform_tensor(target)

    metrics_dict['smape'].append(smape(target, predicted))
    metrics_dict['r2'].append(r2(target, predicted))
    # metrics_dict['rmsle'].append(rmsle(target, predicted))
    metrics_dict['rmse'].append(rmse(target, predicted))
    metrics_dict['mae'].append(mae(target, predicted))

    return metrics_dict


def get_model(opt):
    """Get model.

    Args:
        opt (argparse.ArgumentParser): Parsed arguments.

    Returns:
        torch.nn.module: Model definition.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    inp_channels = len(opt.inp_quants.split(','))
    out_channels = len(opt.out_quants.split(','))
    act = opt.act

    if opt.model == 'shallow_fnn':
        inp_len = inp_channels * opt.window
        model = ShallowFNN(inp_len, out_channels, act)
    if opt.model == 'deep_fnn':
        inp_len = inp_channels * opt.window
        model = DeepFNN(inp_len, out_channels, act)
    if opt.model == 'shallow_cnn':
        model = ShallowCNN(inp_channels, out_channels, act)
    if opt.model == 'deep_cnn':
        model = DeepCNN(inp_channels, out_channels, act)
    if opt.model == 'shallow_rnn':
        model = ShallowRNN(inp_channels, out_channels, opt.hidden_size, act)
    if opt.model == 'deep_rnn':
        model = DeepRNN(inp_channels, out_channels, opt.hidden_size, act)
    if opt.model == 'shallow_lstm':
        model = ShallowLSTM(inp_channels, out_channels, opt.hidden_size, act)
    if opt.model == 'deep_lstm':
        model = DeepLSTM(inp_channels, out_channels, opt.hidden_size, act)
    if opt.model == 'shallow_encdec':
        model = ShallowEncDec(inp_channels, out_channels, act)
    if opt.model == 'deep_encdec':
        model = DeepEncDec(inp_channels, out_channels, act)
    if opt.model == 'encdec_skip':
        model = EncDecSkip(inp_channels, out_channels, act)
    if opt.model == 'encdec_rnn_skip':
        model = EncDecRNNSkip(inp_channels, out_channels, act)
    if opt.model == 'encdec_birnn_skip':
        model = EncDecBiRNNSkip(inp_channels, out_channels, act)
    if opt.model == 'encdec_diag_birnn_skip':
        model = EncDecDiagBiRNNSkip(inp_channels, out_channels, act)

    print ('Parameters :', sum(p.numel() for p in model.parameters()))

    return model.cuda(opt.gpu)

def get_loss_function(opt):
    if opt.loss == 'mse':
        criterion = nn.MSELoss()
    if opt.loss == 'sc_mse':
        criterion = sc_mse

    return criterion

def get_model_from_weight(opt):
    model = torch.load(opt.weight_file)
    return model


def _get_prelaoder_class(opt):
    if 'fnn' in opt.model:
        return FlatInFlatOut
    if 'cnn' in opt.model:
        return SeqInFlatOut
    if 'rnn' in opt.model or 'lstm' in opt.model or 'encdec' in opt.model:
        return SeqInSeqOut


def get_dataloaders(args):
    dataset, train_samples, val_samples, metadata = load_data(args)
    preloader_class = _get_prelaoder_class(args)

    print ('Train Samples ', len(train_samples))
    print ('Val Samples ', len(val_samples))
    
    train_preloader = preloader_class(dataset, train_samples, metadata, args)
    train_loader = DataLoader(train_preloader, batch_size=args.batch_size,
                            shuffle=True, num_workers=args.num_workers)

    val_preloader = preloader_class(dataset, val_samples, metadata, args)
    val_loader = DataLoader(val_preloader, batch_size=args.batch_size,
                            shuffle=True, num_workers=args.num_workers)

    return train_loader, val_loader

class Log(object):
    """Logger class to log training metadata.

    Args:
        log_file_path (type): Log file name.
        op (type): Read or write.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    Attributes:
        log (type): Description of parameter `log`.
        op

    """
    def __init__(self, log_file_path, op='r'):
        self.log = open(log_file_path, op)
        self.op = op

    def write_model(self, model):
        self.log.write('\n##MODEL START##\n')
        self.log.write(str(model))
        self.log.write('\n##MODEL END##\n')

        self.log.write('\n##MODEL SIZE##\n')
        self.log.write(str(sum(p.numel() for p in model.parameters())))
        self.log.write('\n##MODEL SIZE##\n')

    def log_train_metrics(self, metrics, epoch):
        self.log.write('\n##TRAIN METRICS##\n')
        self.log.write('@epoch:' + str(epoch) + '\n')
        for k, v in metrics.items():
            self.log.write(k + '=' + str(v) + '\n')
        self.log.write('\n##TRAIN METRICS##\n')

    def log_validation_metrics(self, metrics, epoch):
        self.log.write('\n##VALIDATION METRICS##\n')
        self.log.write('@epoch:' + str(epoch) + '\n')
        for k, v in metrics.items():
            self.log.write(k + '=' + str(v) + '\n')
        self.log.write('\n##VALIDATION METRICS##\n')

    def close(self):
        self.log.close()
