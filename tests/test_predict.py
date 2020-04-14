import os
import pytest

import numpy as np
import torch

from motornn.predict import get_loader_transform_types, predict



def test__get_loader_transform_types(setup_infer_weight_dir):
    model = torch.load(os.path.join(setup_infer_weight_dir,
            'encdec_diag_birnn_skip',
            f"encdec_diag_birnn_skip_act_relu_stride_1_window_100"\
            f"_inpQuants_voltage_d,voltage_q,current_d,current_q_"\
            f"outQuants_speed,torque_lr_0.01_batchSize_1024_"\
            f"epochs_100_loss_mse.pt"))
    inp_trf_typ, out_trf_typ = get_loader_transform_types(model)
    assert inp_trf_typ == 'seq'
    assert out_trf_typ == 'seq'

    model = torch.load(os.path.join(setup_infer_weight_dir,
            'shallow_fnn',
            f"shallow_fnn_act_relu_stride_1_window_100_"\
            f"inpQuants_voltage_d,voltage_q,current_d,current_q_"\
            f"outQuants_speed,torque_lr_0.01_batchSize_1024_"\
            f"epochs_100_loss_mse.pt"))
    inp_trf_typ, out_trf_typ = get_loader_transform_types(model)
    assert inp_trf_typ == 'flat'
    assert out_trf_typ == 'flat'

def test__predict_shallow_fnn(setup_infer_weight_dir, setup_test_data):
    model = torch.load(os.path.join(setup_infer_weight_dir,
            'encdec_diag_birnn_skip',
            f"encdec_diag_birnn_skip_act_relu_stride_1_window_100"\
            f"_inpQuants_voltage_d,voltage_q,current_d,current_q_"\
            f"outQuants_speed,torque_lr_0.01_batchSize_1024_"\
            f"epochs_100_loss_mse.pt")).cuda(0)
    model = model.eval()

    speed, torque, speed_ml_metrics, torque_ml_metrics = predict(model, setup_test_data, 100)

    assert isinstance(speed, np.ndarray)
    assert isinstance(torque, np.ndarray)
