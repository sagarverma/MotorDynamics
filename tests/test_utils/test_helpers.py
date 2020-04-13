import os
import pytest

import numpy as np
import torch
import torch.nn as nn

from motornn.utils.parser import get_parser_with_args
from motornn.utils.helpers import (get_file_names, initialize_metrics,
                                          get_mean_metrics, set_metrics,
                                          get_model, _get_prelaoder_class,
                                          get_dataloaders)

from motornn.models.cnn import ShallowCNN, DeepCNN
from motornn.models.ffnn import ShallowFNN, DeepFNN
from motornn.models.rnn import ShallowRNN, DeepRNN
from motornn.models.lstm import ShallowLSTM, DeepLSTM
from motornn.models.encdec import (ShallowEncDec, DeepEncDec, EncDecSkip,
                          EncDecRNNSkip, EncDecBiRNNSkip,
                          EncDecDiagBiRNNSkip)

from motornn.utils.dataloader import (FlatInFlatOut, SeqInFlatOut,
                                             SeqInSeqOut)

def test__get_file_name_fnn(setup_args, tmpdir_factory):
    weight_path, log_path = get_file_names(setup_args)

    assert isinstance(weight_path, str)
    assert isinstance(log_path, str)
    assert weight_path
    assert log_path

    assert weight_path == os.path.join(tmpdir_factory.getbasetemp(), 'weights',
                        setup_args.model,
                        f"shallow_fnn_act_relu_stride_1_window_100"\
                        f"_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_"\
                        f"speed,torque_lr_0.01_batchSize_2_"\
                        f"epochs_1_loss_mse.pt")
    assert log_path == os.path.join(tmpdir_factory.getbasetemp(), 'logs',
                        setup_args.model,
                       f"shallow_fnn_act_relu_stride_1_window_100"\
                      f"_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_"\
                      f"speed,torque_lr_0.01_batchSize_2_"\
                       f"epochs_1_loss_mse.log")

def test__get_intialize_metrics():
    metrics = initialize_metrics()

    assert isinstance(metrics, dict)


def test__get_mean_metrics():
    metrics = {'loss':[1, 2], 'smape':[100, 50]}
    mean_metrics = get_mean_metrics(metrics)

    assert isinstance(mean_metrics, dict)
    assert mean_metrics['loss'] == 1.5
    assert mean_metrics['smape'] == 75


def test__set_metrics():
    metrics = {'loss':[1, 2], 'smape':[100, 50], 'r2': [1, 2],
                'rmsle': [3, 4], 'rmse': [5, 6], 'mae': [7, 8]}
    metrics = set_metrics(metrics, loss=torch.tensor(3), smape=0,
                            r2=1, rmsle=2,
                            rmse=3, mae=4)

    assert isinstance(metrics, dict)
    assert isinstance(metrics['loss'], list)
    assert isinstance(metrics['smape'], list)
    assert metrics['loss']
    assert metrics['smape']
    assert metrics['loss'] == [1, 2, 3]
    assert metrics['smape'] == [100, 50, 0]
    assert metrics['r2'] == [1, 2, 1]
    assert metrics['rmsle'] == [3, 4, 2]
    assert metrics['rmse'] == [5, 6, 3]
    assert metrics['mae'] == [7, 8, 4]


def test__get_model_shallow_fnn(setup_args):
    setup_args.model = 'shallow_fnn'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowFNN)


def test__get_model_deep_fnn(setup_args):
    setup_args.model = 'deep_fnn'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepFNN)


def test__get_model_shallow_cnn(setup_args):
    setup_args.model = 'shallow_cnn'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowCNN)


def test__get_model_deep_cnn(setup_args):
    setup_args.model = 'deep_cnn'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepCNN)


def test__get_model_shallow_rnn(setup_args):
    setup_args.model = 'shallow_rnn'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowRNN)


def test__get_model_deep_rnn(setup_args):
    setup_args.model = 'deep_rnn'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepRNN)


def test__get_model_shallow_lstm(setup_args):
    setup_args.model = 'shallow_lstm'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowLSTM)


def test__get_model_deep_lstm(setup_args):
    setup_args.model = 'deep_lstm'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepLSTM)

def test__get_model_shallow_encdec(setup_args):
    setup_args.model = 'shallow_encdec'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowEncDec)


def test__get_model_deep_encdec(setup_args):
    setup_args.model = 'deep_encdec'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepEncDec)


def test__get_model_encdec_skip(setup_args):
    setup_args.model = 'encdec_skip'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, EncDecSkip)


def test__get_model_encdec_rnn_skip(setup_args):
    setup_args.model = 'encdec_rnn_skip'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, EncDecRNNSkip)


def test__get_model_encdec_birnn_skip(setup_args):
    setup_args.model = 'encdec_birnn_skip'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, EncDecBiRNNSkip)


def test__get_model_encdec_diag_birnn_skip(setup_args):
    setup_args.model = 'encdec_diag_birnn_skip'
    model = get_model(setup_args)

    assert isinstance(model, nn.Module)
    assert isinstance(model, EncDecDiagBiRNNSkip)


def test__get_loader_fnn(setup_args):
    setup_args.model = 'shallow_fnn'
    train_loader, val_loader = get_dataloaders(setup_args)

    assert isinstance(train_loader, torch.utils.data.DataLoader)
    assert isinstance(train_loader.dataset, FlatInFlatOut)

    assert isinstance(val_loader, torch.utils.data.DataLoader)
    assert isinstance(val_loader.dataset, FlatInFlatOut)


def test__get_loader_cnn(setup_args):
    setup_args.model = 'shallow_cnn'
    train_loader, val_loader = get_dataloaders(setup_args)

    assert isinstance(train_loader, torch.utils.data.DataLoader)
    assert isinstance(train_loader.dataset, SeqInFlatOut)

    assert isinstance(val_loader, torch.utils.data.DataLoader)
    assert isinstance(val_loader.dataset, SeqInFlatOut)


def test__get_loader_encdec(setup_args):
    setup_args.model = 'shallow_encdec'
    train_loader, val_loader = get_dataloaders(setup_args)

    assert isinstance(train_loader, torch.utils.data.DataLoader)
    assert isinstance(train_loader.dataset, SeqInSeqOut)

    assert isinstance(val_loader, torch.utils.data.DataLoader)
    assert isinstance(val_loader.dataset, SeqInSeqOut)
