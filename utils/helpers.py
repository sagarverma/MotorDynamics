import numpy as np

from torch.utils.data import DataLoader

from utils.dataloader import (load_data, get_sample_metadata, SignalPreloader)
from models.cnn import ShallowCNN, DeepCNN
from models.fnn import ShallowFNN, DeepFNN
from model.rnn import ShallowRNN, DeepRNN
from model.lstm import ShallowLSTM, DeepLSTM
from model.encdec import (ShallowEncDec, DeepEncDec, EncDecSkip,
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
        fname += '_hiddeSize_' + str(opt.hidden_size)class ThinEncDec(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(ThinEncDec, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 8, kernel_size=3, stride=1)
        self.cnn2 = nn.Conv1d(8, 16, kernel_size=3, stride=1)

        self.dcnn2 = nn.ConvTranspose1d(16, 8, kernel_size=3, stride=1)
        self.dcnn1 = nn.ConvTranspose1d(8, output_dim, kernel_size=3, stride=1)

        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh

    def forward(self, x):
        x = x.permute(0,2,1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.dcnn2(x))
        x = self.dcnn1(x)
        return x.view(-1, x.size()[-1], x.size()[1])


class UltraThinEncDec(nn.Module):
    def __init__(self, input_dim, output_dim, act='relu'):
        super(UltraThinEncDec, self).__init__()
        self.cnn1 = nn.Conv1d(input_dim, 3, kernel_size=3, stride=1, bias=False)
        self.cnn2 = nn.Conv1d(3, 3, kernel_size=3, stride=1, bias=False)

        self.dcnn2 = nn.ConvTranspose1d(3, 3, kernel_size=3, stride=1, bias=False)
        self.dcnn1 = nn.ConvTranspose1d(3, output_dim, kernel_size=3, stride=1, bias=False)

        if act == 'relu':
            self.act = torch.relu
        if act == 'tanh':
            self.act = torch.tanh

    def forward(self, x):
        x = x.permute(0,2,1)
        x = self.act(self.cnn1(x))
        x = self.act(self.cnn2(x))
        x = self.act(self.dcnn2(x))
        x = self.dcnn1(x)
        return x.view(-1, x.size()[-1], x.size()[1])

    if 'cnn' in opt.model or 'encdec' in opt.model:
        fname = opt.model + suffix

    weight_path = opt.weight_dir + fname + '.pt'
    log_path = opt.log_dir + fname + '.log'

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
        model = ShallowFNN(inp_len, out_channels)
    if opt.model == 'deep_fnn':
        inp_len = inp_channels * opt.window
        model = DeepFNN(inp_len, out_channels)
    if opt.model == 'shallow_cnn':
        model = ShallowCNN(inp_channels, out_channels)
    if opt.model == 'deep_cnn':
        model = DeepCNN(inp_channels, out_channels)
    if opt.model == 'shallow_rnn':
        model = ShallowRNN(inp_channels, out_channels)
    if opt.model == 'deep_rnn':
        model = DeepRNN(inp_channels, out_channels)
    if opt.model == 'shallow_lstm':
        model = ShallowLSTM(inp_channels, out_channels)
    if opt.model == 'deep_lstm':
        model = DeepLSTM(inp_channels, out_channels)
    if opt.model == 'shallow_encdec':
        model = ShallowEncDec(inp_channels, out_channels)
    if opt.model == 'deep_encdec':
        model = DeepEncDec(inp_channels, out_channels)
    if opt.model == ''


    print ('Parameters :', sum(p.numel() for p in model.parameters()))

    return model
def get_loaders(opt):
    """Get dataloaders for training, fine tuning, validation, and testing.

    Args:
        opt (argparse.ArgumentParser): Parsed arguments.

    Returns:
        tuple: train sim dataloader, val sim dataloader, train raw dataloader, and
               test dataloader.

    Raises:        ExceptionName: Why the exception is raised.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    if 'ffnn' in opt.model:
        flatten = True
    else:
        flatten = False

    if 'encdec' in opt.model:
        enc_dec = True
    else:
        enc_dec = False

    train_sim_dataset, index_quant_map = load_data(opt.train_sim_dir)
    train_raw_dataset, index_quant_map = load_data(opt.train_raw_dir)
    val_sim_dataset, index_quant_map = load_data(opt.val_sim_dir)
    test_raw_dataset, index_quant_map = load_data(opt.test_raw_dir)

    train_sim_samples = get_sample_metadata(train_sim_dataset,
                                            opt.stride, opt.window)
    train_raw_samples = get_sample_metadata(train_raw_dataset,
                                            opt.stride, opt.window)
    val_sim_samples = get_sample_metadata(val_sim_dataset,
                                          opt.stride, opt.window)
    test_raw_samples = get_sample_metadata(test_raw_dataset,
                                           opt.stride, opt.window)

    print('train sim samples : ', len(train_sim_samples))
    print('train raw samples : ', len(train_raw_samples))
    print('val sim samples : ', len(val_sim_samples))
    print('test raw samples : ', len(test_raw_samples))

    train_sim_loader = SignalPreloader(train_sim_dataset,
                                       index_quant_map, train_sim_samples,
                                       opt.inp_quants.split(','),
                                       opt.out_quants.split(','),
                                       flatten, enc_dec)
    train_raw_loader = SignalPreloader(train_raw_dataset,
                                       index_quant_map, train_raw_samples,
                                       opt.inp_quants.split(','),
                                       opt.out_quants.split(','),
                                       flatten, enc_dec)
    val_sim_loader = SignalPreloader(val_sim_dataset,
                                     index_quant_map, val_sim_samples,
                                     opt.inp_quants.split(','),
                                     opt.out_quants.split(','),
                                     flatten, enc_dec)
    test_raw_loader = SignalPreloader(test_raw_dataset,
                                      index_quant_map, test_raw_samples,
                                      opt.inp_quants.split(','),
                                      opt.out_quants.split(','),
                                      flatten, enc_dec)

    train_sim_loader = DataLoader(train_sim_loader, batch_size=opt.batch_size,
                                  shuffle=True, num_workers=32)
    train_raw_loader = DataLoader(train_raw_loader, batch_size=opt.batch_size,
                                  shuffle=False, num_workers=32)
    val_sim_loader = DataLoader(val_sim_loader, batch_size=opt.batch_size,
                                shuffle=False, num_workers=32)
    test_raw_loader = DataLoader(test_raw_loader, batch_size=opt.batch_size,
                                 shuffle=False, num_workers=32)

    return train_sim_loader, train_raw_loader, val_sim_loader, test_raw_loader
