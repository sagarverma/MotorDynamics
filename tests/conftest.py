import os
import pytest
from urllib.request import urlretrieve
import tarfile

from motor_dynamics.utils.parser import get_parser_with_args

@pytest.fixture(scope="session")
def setup_data_dir(tmpdir_factory):
    data_url = 'https://sagarverma.github.io/others/motor_data.tar'
    fname, headers = urlretrieve(data_url,
                                os.path.join(tmpdir_factory.getbasetemp(),
                                "motor_data.tar"))

    tar = tarfile.open(fname)
    tar.extractall(path=tmpdir_factory.getbasetemp())
    tar.close()

    return os.path.join(tmpdir_factory.getbasetemp(), "data")


@pytest.fixture(scope="session")
def setup_weights_dir(tmpdir_factory):
    fn = tmpdir_factory.mktemp("weights", numbered=False)
    return fn.strpath


@pytest.fixture(scope="session")
def setup_logs_dir(tmpdir_factory):
    fn = tmpdir_factory.mktemp("logs", numbered=False)
    return fn.strpath


@pytest.fixture(scope="session")
def setup_args(setup_data_dir, setup_weights_dir, setup_logs_dir):
    args = {'--gpu': 0,
            '--task': 'train_sim',
            '--train_sim_dir': os.path.join(setup_data_dir, 'train_sim'),
            '--train_raw_dir': os.path.join(setup_data_dir, 'train_raw'),
            '--val_sim_dir': os.path.join(setup_data_dir, 'val_sim'),
            '--test_raw_dir': os.path.join(setup_data_dir, 'test_raw'),
            '--weights_dir': setup_weights_dir,
            '--logs_dir': setup_logs_dir,
            '--model': 'shallow_fnn',
            '--epochs': '1',
            '--batch_size': '2',
            '--lr': '0.01',
            '--inp_quants': 'voltage_d,voltage_q,speed',
            '--out_quants': 'current_d,current_q,torque',
            '--stride': '1',
            '--window': '100',
            '--act': 'relu',
            '--hidden_size': '32',
            '--num_workers': '8'}
    return args
