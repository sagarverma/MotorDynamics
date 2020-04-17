import os
import pytest
from urllib.request import urlretrieve
import tarfile
import pickle

from motornn.utils.parser import get_parser_with_args

@pytest.fixture(scope="session")
def setup_data_dir(tmpdir_factory):
    data_url = 'http://sagarverma.github.io/others/Data_09042020_sm.tar.xz'
    fname, headers = urlretrieve(data_url,
                                os.path.join(tmpdir_factory.getbasetemp(),
                                "Data_09042020_sm.tar.xz"))

    tar = tarfile.open(fname)
    tar.extractall(path=tmpdir_factory.getbasetemp())
    tar.close()

    return os.path.join(tmpdir_factory.getbasetemp(), "Data_09042020_sm")

@pytest.fixture(scope="session")
def setup_weights_dir(tmpdir_factory):
    fn = tmpdir_factory.mktemp("weights", numbered=False)
    return fn.strpath


@pytest.fixture(scope="session")
def setup_infer_weight_dir(setup_weights_dir):
    data_url = 'http://sagarverma.github.io/others/Weights_Data_09042020_sm.tar.xz'
    fname, headers = urlretrieve(data_url,
                                os.path.join(setup_weights_dir,
                                "Weights_Data_09042020_sm.tar.xz"))

    tar = tarfile.open(fname)
    tar.extractall(path=setup_weights_dir)
    tar.close()

    return os.path.join(setup_weights_dir, "Data_09042020_sm")


@pytest.fixture(scope="session")
def setup_logs_dir(tmpdir_factory):
    fn = tmpdir_factory.mktemp("logs", numbered=False)
    return fn.strpath


@pytest.fixture(scope="session")
def setup_args(setup_data_dir, setup_weights_dir, setup_logs_dir):
    default = ['--gpu', 0,
            '--data_dir', os.path.join(setup_data_dir),
            '--weights_dir', setup_weights_dir,
            '--logs_dir', setup_logs_dir,
            '--model', 'shallow_fnn',
            '--epochs', '1',
            '--batch_size', '1000',
            '--lr', '0.01',
            '--inp_quants', 'voltage_d,voltage_q,current_d,current_q',
            '--out_quants', 'speed,torque',
            '--stride', '1',
            '--window', '100',
            '--act', 'relu',
            '--hidden_size', '32',
            '--num_workers', '8',
            '--loss', 'mse']

    parser = get_parser_with_args()
    args = parser.parse_args(default)
    return args

@pytest.fixture(scope="session")
def setup_test_data(setup_data_dir):
    fin = open(os.path.join(setup_data_dir, 'val', '00001.pkl'), 'rb')
    data = pickle.load(fin)
    fin.close()

    return data
