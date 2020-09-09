import os
import pytest

import numpy as np
import torch
import torch.nn as nn

from motor_dynamics.utils.parser import get_parser_with_args
from motor_dynamics.utils.helpers import (get_file_names, initialize_metrics,
                                          get_mean_metrics, set_metrics,
                                          get_model, _get_prelaoder_class,
                                          _get_loader, get_train_loaders,
                                          get_finetune_loaders,
                                          get_test_loaders)

from motor_dynamics.models.cnn import ShallowCNN, DeepCNN
from motor_dynamics.models.ffnn import ShallowFNN, DeepFNN
from motor_dynamics.models.rnn import ShallowRNN, DeepRNN
from motor_dynamics.models.lstm import ShallowLSTM, DeepLSTM
from motor_dynamics.models.encdec import (ShallowEncDec, DeepEncDec, EncDecSkip,
                          EncDecRNNSkip, EncDecBiRNNSkip,
                          EncDecDiagBiRNNSkip)

from motor_dynamics.utils.dataloader import (FlatInFlatOut, SeqInFlatOut,
                                             SeqInSeqOut)

def test__get_file_name_fnn(setup_args, tmpdir_factory):
    parser = get_parser_with_args()
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    weight_path, log_path = get_file_names(opt)

    assert isinstance(weight_path, str)
    assert isinstance(log_path, str)
    assert weight_path
    assert log_path
    assert weight_path == os.path.join(tmpdir_factory.getbasetemp(), 'weights',
                        f"shallow_fnn/"\
                        f"shallow_fnn_train_sim_act_relu_stride_1_window_100"\
                        f"_inpQuants_voltage_d,voltage_q,speed_outQuants_"\
                        f"current_d,current_q,torque_lr_0.01_batchSize_2_"\
                        f"epochs_1_loss_mse.pt")
    assert log_path == os.path.join(tmpdir_factory.getbasetemp(), 'logs',
                       f"shallow_fnn/"\
                       f"shallow_fnn_train_sim_act_relu_stride_1_window_100_"\
                       f"inpQuants_voltage_d,voltage_q,speed_outQuants_"\
                       f"current_d,current_q,torque_lr_0.01_batchSize_2_"\
                       f"epochs_1_loss_mse.log")


def test__get_file_name_rnn(setup_args, tmpdir_factory):
    parser = get_parser_with_args()
    setup_args['--model'] = 'deep_rnn'
    setup_args['--hidden_size'] = '64'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    weight_path, log_path = get_file_names(opt)

    assert isinstance(weight_path, str)
    assert isinstance(log_path, str)
    assert weight_path
    assert log_path
    assert weight_path == os.path.join(tmpdir_factory.getbasetemp(), 'weights',
                        f"deep_rnn/",
                        f"deep_rnn_train_sim_act_relu_stride_1_window_100"\
                        f"_inpQuants_voltage_d,voltage_q,speed_outQuants_"\
                        f"current_d,current_q,torque_lr_0.01_batchSize_2_"\
                        f"epochs_1_loss_mse_hiddenSize_64.pt")
    assert log_path == os.path.join(tmpdir_factory.getbasetemp(), 'logs',
                       f"deep_rnn/",
                       f"deep_rnn_train_sim_act_relu_stride_1_window_100_"\
                       f"inpQuants_voltage_d,voltage_q,speed_outQuants_"\
                       f"current_d,current_q,torque_lr_0.01_batchSize_2_"\
                       f"epochs_1_loss_mse_hiddenSize_64.log")


def test__get_file_name_encdec(setup_args, tmpdir_factory):
    parser = get_parser_with_args()
    setup_args['--model'] = 'deep_encdec'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    weight_path, log_path = get_file_names(opt)

    assert isinstance(weight_path, str)
    assert isinstance(log_path, str)
    assert weight_path
    assert log_path
    assert weight_path == os.path.join(tmpdir_factory.getbasetemp(), 'weights',
                        f"deep_encdec/",
                        f"deep_encdec_train_sim_act_relu_stride_1_window_100"\
                        f"_inpQuants_voltage_d,voltage_q,speed_outQuants_"\
                        f"current_d,current_q,torque_lr_0.01_batchSize_2_"\
                        f"epochs_1_loss_mse.pt")
    assert log_path == os.path.join(tmpdir_factory.getbasetemp(), 'logs',
                       f"deep_encdec/",
                       f"deep_encdec_train_sim_act_relu_stride_1_window_100_"\
                       f"inpQuants_voltage_d,voltage_q,speed_outQuants_"\
                       f"current_d,current_q,torque_lr_0.01_batchSize_2_"\
                       f"epochs_1_loss_mse.log")


def test__get_intialize_metrics():
    metrics = initialize_metrics()

    assert isinstance(metrics, dict)


def test__get_mean_metrics():
    metrics = {'loss': [1, 2], 'smape': [100, 50]}
    mean_metrics = get_mean_metrics(metrics)

    assert isinstance(mean_metrics, dict)
    assert mean_metrics['loss'] == 1.5
    assert mean_metrics['smape'] == 75


def test__set_metrics():
    metrics = {'loss': [1, 2], 'smape': [100, 50],
               'r2': [0, 1], 'rmsle': [0, 10],
               'rmse': [0, 5], 'mae': [0, 100]}
    metrics = set_metrics(metrics, loss=torch.tensor(3),
                          smape=torch.tensor(0), r2=torch.tensor(0),
                          rmsle=torch.tensor(0), rmse=torch.tensor(0),
                          mae=torch.tensor(0))

    assert isinstance(metrics, dict)
    assert isinstance(metrics['loss'], list)
    assert isinstance(metrics['smape'], list)
    assert metrics['loss']
    assert metrics['smape']
    assert metrics['loss'] == [1, 2, 3]
    assert metrics['smape'] == [100, 50, 0]
    assert metrics['r2'] == [0, 1, 0]
    assert metrics['rmsle'] == [0, 10, 0]
    assert metrics['rmse'] == [0, 5, 0]
    assert metrics['mae'] == [0, 100, 0]


def test__get_model_shallow_fnn(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_fnn'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowFNN)


def test__get_model_deep_fnn(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'deep_fnn'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepFNN)


def test__get_model_shallow_cnn(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_cnn'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowCNN)


def test__get_model_deep_cnn(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'deep_cnn'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepCNN)


def test__get_model_shallow_rnn(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_rnn'
    setup_args['--hidden_size'] = '64'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowRNN)


def test__get_model_deep_rnn(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'deep_rnn'
    setup_args['--hidden_size'] = '64'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepRNN)


def test__get_model_shallow_lstm(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_lstm'
    setup_args['--hidden_size'] = '64'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowLSTM)


def test__get_model_deep_lstm(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'deep_lstm'
    setup_args['--hidden_size'] = '64'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepLSTM)


def test__get_model_shallow_encdec(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_encdec'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, ShallowEncDec)


def test__get_model_deep_encdec(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'deep_encdec'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, DeepEncDec)


def test__get_model_encdec_skip(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'encdec_skip'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, EncDecSkip)


def test__get_model_encdec_rnn_skip(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'encdec_rnn_skip'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, EncDecRNNSkip)


def test__get_model_encdec_birnn_skip(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'encdec_birnn_skip'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, EncDecBiRNNSkip)


def test__get_model_encdec_diag_birnn_skip(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'encdec_diag_birnn_skip'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    model = get_model(opt)

    assert isinstance(model, nn.Module)
    assert isinstance(model, EncDecDiagBiRNNSkip)


def test__get_loader_fnn(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_fnn'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    loader, _ = _get_loader(opt.train_sim_dir, opt, True)

    assert isinstance(loader, torch.utils.data.dataloader.DataLoader)
    assert isinstance(loader.dataset, FlatInFlatOut)


def test__get_loader_cnn(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_cnn'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    loader, _ = _get_loader(opt.train_sim_dir, opt, True)

    assert isinstance(loader, torch.utils.data.dataloader.DataLoader)
    assert isinstance(loader.dataset, SeqInFlatOut)


def test__get_loader_encdec(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_encdec'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    loader, _ = _get_loader(opt.train_sim_dir, opt, True)

    assert isinstance(loader, torch.utils.data.dataloader.DataLoader)
    assert isinstance(loader.dataset, SeqInSeqOut)


def test__get_train_loaders(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_encdec'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    train_sim_loader, val_sim_loader = get_train_loaders(opt)

    assert isinstance(train_sim_loader, torch.utils.data.DataLoader)
    assert isinstance(val_sim_loader, torch.utils.data.DataLoader)


def test__get_finetune_loaders(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_encdec'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    train_raw_loader, val_sim_loader = get_finetune_loaders(opt)

    assert isinstance(train_raw_loader, torch.utils.data.DataLoader)
    assert isinstance(val_sim_loader, torch.utils.data.DataLoader)


def test__get_test_loaders(setup_args):
    parser = get_parser_with_args()
    setup_args['--model'] = 'shallow_encdec'
    args = sum([list(arg) for arg in setup_args.items()], [])
    opt = parser.parse_args(args)

    test_raw_loader = get_test_loaders(opt)

    assert isinstance(test_raw_loader, torch.utils.data.DataLoader)
