import os

import numpy as np

from torch.utils.data import DataLoader

from motor_dynamics.utils.dataloader import (load_data, get_sample_metadata, FlatInFlatOut,
                              SeqInFlatOut, SeqInSeqOut)

from motor_dynamics.models.cnn import ShallowCNN, DeepCNN
from motor_dynamics.models.ffnn import ShallowFNN, DeepFNN
from motor_dynamics.models.rnn import ShallowRNN, DeepRNN
from motor_dynamics.models.lstm import ShallowLSTM, DeepLSTM
from motor_dynamics.models.encdec import (ShallowEncDec, DeepEncDec, EncDecSkip,
                          EncDecRNNSkip, EncDecBiRNNSkip,
                          EncDecDiagBiRNNSkip)


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
    suffix = '_' + opt.task + '_'
    suffix += '_act_' + opt.act
    suffix += '_stride_' + str(opt.stride)
    suffix += '_window_' + str(opt.window)
    suffix += '_inpQuants_' + opt.inp_quants
    suffix += '_outQuants_' + opt.out_quants
    suffix += '_lr_' + str(opt.lr)
    suffix += '_batchSize_' + str(opt.batch_size)
    suffix += '_epochs_' + str(opt.epochs)

    if 'fnn' in opt.model:
        fname = opt.model + suffix

    if 'rnn' in opt.model or 'lstm' in opt.model:
        fname = opt.model + suffix
        fname += '_hiddenSize_' + str(opt.hidden_size)

    if 'cnn' in opt.model or 'encdec' in opt.model:
        fname = opt.model + suffix

    weight_path = os.path.join(opt.weights_dir, fname + '.pt')
    log_path = os.path.join(opt.logs_dir, fname + '.log')

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
        'losses': [],
        'smapes': []
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


def set_metrics(metrics_dict, loss, smape):
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
    metrics_dict['losses'].append(loss.item())
    metrics_dict['smapes'].append(smape.item())

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

    return model


def _get_prelaoder_class(opt):
    if 'fnn' in opt.model:
        return FlatInFlatOut
    if 'cnn' in opt.model:
        return SeqInFlatOut
    if 'rnn' in opt.model or 'lstm' in opt.model or 'encdec' in opt.model:
        return SeqInSeqOut


def _get_loader(dir, opt, shuffle):
    dataset, index_quant_map = load_data(dir)
    samples = get_sample_metadata(dataset, opt.stride, opt.window)
    preloader_class = _get_prelaoder_class(opt)
    preloader = preloader_class(dataset, index_quant_map, samples,
                          opt.inp_quants.split(','),
                          opt.out_quants.split(','))
    dataloader = DataLoader(preloader, batch_size=opt.batch_size,
                            shuffle=shuffle, num_workers=opt.num_workers)
    return dataloader


def get_train_loaders(opt):
    """Get dataloaders for training, and validation.

    Args:
        opt (argparse.ArgumentParser): Parsed arguments.

    Returns:
        tuple: train sim dataloader and val sim dataloader

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """

    train_sim_loader = _get_loader(opt.train_sim_dir, opt, True)
    val_sim_loader = _get_loader(opt.val_sim_dir, opt, False)

    print('train sim samples : ', len(train_sim_loader))
    print('val sim samples : ', len(val_sim_loader))

    return train_sim_loader, val_sim_loader


def get_finetune_loaders(opt):
    """Get dataloaders for finetuning, and validation.

    Args:
        opt (argparse.ArgumentParser): Parsed arguments.

    Returns:
        tuple:  train raw dataloader and val sim dataloader.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """

    train_raw_loader = _get_loader(opt.train_raw_dir, opt, True)
    val_sim_loader = _get_loader(opt.val_sim_dir, opt, False)

    print('train raw samples : ', len(train_raw_loader))
    print('val sim samples : ', len(val_sim_loader))


    return train_raw_loader, val_sim_loader



def get_test_loaders(opt):
    """Get dataloader for testing.

    Args:
        opt (argparse.ArgumentParser): Parsed arguments.

    Returns:
        tuple: test dataloader.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """

    test_raw_loader = _get_loader(opt.test_raw_dir, opt, False)

    print('test raw samples : ', len(test_raw_loader))

    return test_raw_loader
