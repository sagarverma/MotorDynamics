import os
import pytest

import numpy as np

from motornn.utils.dataloader import (normalize, denormalize,
                                             load_data, loader,
                                             FlatInFlatOut, SeqInFlatOut,
                                             SeqInSeqOut)


def test__normalize():
    quantity = np.random.rand(1000) * 30
    normalized = normalize(quantity, -300, 300)
    assert normalized.min() >= -1
    assert normalized.max() <= 1


def test__denormalize():
    normalized_quantity = np.random.rand(1000)
    denormalized = denormalize(normalized_quantity, -1, 1)
    assert denormalized.min() >= -30
    assert denormalized.max() <= 30

def test__load_data(setup_args):
    full_load, train_samples, val_samples, metadata = load_data(setup_args)

    assert full_load
    assert isinstance(full_load, dict)
    for k in full_load.keys():
        assert 'train' in k or 'val' in k
        assert '0001.pkl' in k

    first_data = full_load[list(full_load.keys())[0]]
    assert isinstance(first_data, dict)
    assert 'voltage_d' in first_data
    assert 'voltage_q' in first_data
    assert 'current_d' in first_data
    assert 'current_q' in first_data
    assert 'statorPuls' in first_data
    assert 'speed' in first_data
    assert 'torque' in first_data
    assert 'time' in first_data
    assert 'reference_torque_interp' in first_data
    assert 'reference_speed_interp' in first_data
    assert 'reference_torque' in first_data
    assert 'reference_speed' in first_data
    assert 'torque_time' in first_data
    assert 'speed_time' in first_data

    assert isinstance(train_samples, list)
    assert isinstance(val_samples, list)

    assert train_samples
    assert val_samples

    assert isinstance(train_samples[0], list)
    assert isinstance(val_samples[0], list)

    assert len(train_samples[0]) == 4

    assert isinstance(metadata, dict)

def test__loader(setup_args):
    full_load, train_samples, val_samples, metadata = load_data(setup_args)

    x, y = loader(full_load, train_samples[0], metadata, setup_args)

    assert isinstance(x, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert x.shape == (4, setup_args.window)
    assert y.shape == (2, setup_args.window)
    assert x.min() >= -1
    assert x.max() <= 1
    assert y.min() >= -1
    assert y.max() <= 1

class Test_FlatInFlatOut(object):
    def test__init(self, setup_args):
        dataset, train_samples, _, metadata = load_data(setup_args)
        dataloader = FlatInFlatOut(dataset, train_samples, setup_args)

        assert isinstance(dataloader.samples, list)
        assert isinstance(dataloader.inp_quant_ids, list)
        assert isinstance(dataloader.out_quant_ids, list)

    def test__getitem__(self, setup_args):
        dataset, index_quant_map = load_data(setup_args)

        dataloader = FlatInFlatOut(dataset, index_quant_map,
                                     samples, inp_quants,
                                     out_quants)

        inp_seq, out_seq = dataloader.__getitem__(0)

        assert isinstance(inp_seq, np.ndarray)
        assert isinstance(out_seq, np.ndarray)
        assert len(inp_seq.shape) == 1
        assert inp_seq.shape[0] == 300
        assert len(out_seq.shape) == 1
        assert out_seq.shape[0] == 3


class Test_SeqInFlatOut(object):
    def test__init(self, setup_data_dir):
        data_dir = os.path.join(setup_data_dir, "train_raw")
        dataset, index_quant_map = load_data(data_dir)
        samples = get_sample_metadata(dataset, 1, 100)
        inp_quants = ['voltage_d', 'voltage_q', 'speed']
        out_quants = ['current_d', 'current_q', 'torque']

        dataloader = SeqInFlatOut(dataset, index_quant_map,
                                     samples, inp_quants,
                                     out_quants)

        assert isinstance(dataloader.samples, list)
        assert isinstance(dataloader.inp_quant_ids, list)
        assert isinstance(dataloader.out_quant_ids, list)

    def test__getitem__(self, setup_data_dir):
        data_dir = os.path.join(setup_data_dir, "train_raw")
        dataset, index_quant_map = load_data(data_dir)
        samples = get_sample_metadata(dataset, 1, 100)
        inp_quants = ['voltage_d', 'voltage_q', 'speed']
        out_quants = ['current_d', 'current_q', 'torque']

        dataloader = SeqInFlatOut(dataset, index_quant_map,
                                     samples, inp_quants,
                                     out_quants)

        inp_seq, out_seq = dataloader.__getitem__(0)

        assert isinstance(inp_seq, np.ndarray)
        assert isinstance(out_seq, np.ndarray)
        assert len(inp_seq.shape) == 2
        assert inp_seq.shape[0] == 3
        assert inp_seq.shape[1] == 100
        assert len(out_seq.shape) == 1
        assert out_seq.shape[0] == 3


class Test_SeqInSeqOut(object):
    def test__init(self, setup_data_dir):
        data_dir = os.path.join(setup_data_dir, "train_raw")
        dataset, index_quant_map = load_data(data_dir)
        samples = get_sample_metadata(dataset, 1, 100)
        inp_quants = ['voltage_d', 'voltage_q', 'speed']
        out_quants = ['current_d', 'current_q', 'torque']

        dataloader = SeqInSeqOut(dataset, index_quant_map,
                                     samples, inp_quants,
                                     out_quants)

        assert isinstance(dataloader.samples, list)
        assert isinstance(dataloader.inp_quant_ids, list)
        assert isinstance(dataloader.out_quant_ids, list)

    def test__getitem__(self, setup_data_dir):
        data_dir = os.path.join(setup_data_dir, "train_raw")
        dataset, index_quant_map = load_data(data_dir)
        samples = get_sample_metadata(dataset, 1, 100)
        inp_quants = ['voltage_d', 'voltage_q', 'speed']
        out_quants = ['current_d', 'current_q', 'torque']

        dataloader = SeqInSeqOut(dataset, index_quant_map,
                                     samples, inp_quants,
                                     out_quants)

        inp_seq, out_seq = dataloader.__getitem__(0)

        assert isinstance(inp_seq, np.ndarray)
        assert isinstance(out_seq, np.ndarray)
        assert len(inp_seq.shape) == 2
        assert inp_seq.shape[0] == 3
        assert inp_seq.shape[1] == 100
        assert len(out_seq.shape) == 2
        assert out_seq.shape[0] == 3
        assert out_seq.shape[1] == 100
