import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

from motor_dynamics.utils.helpers import (get_file_names, initialize_metrics,
                                          get_mean_metrics, set_metrics,
                                          get_model, get_train_loaders, Log)
from motor_dynamics.utils.metrics import smape, r2, rmsle, rmse, mae

def test(opt):
    pkls = glob.glob(opt.test_dir + '*.pkl')

    for pkl in pkls:
        
