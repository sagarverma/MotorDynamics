import os
import pytest

import numpy as np

from motor_dynamics.utils.dataloader import (normalize, denormalize,
                                             load_data, _load_exp_data,
                                             rev_test_output,
                                             get_sample_metadata,
                                             FlatInFlatOut, SeqInFlatOut,
                                             SeqInSeqOut)


def test__normalize():
    quantity = np.random.rand(1000) * 30
    normalized = normalize(quantity, 'current_d')
    assert normalized.min() >= -1
    assert normalized.max() <= 1


def test__denormalize():
    normalized_quantity = np.random.rand(1000)
    denormalized = denormalize(normalized_quantity, 'current_d')
    assert denormalized.min() >= -30
    assert denormalized.max() <= 30


def test__load_exp_data(setup_data_dir):
    data_dir = os.path.join(setup_data_dir, "train_raw",
                            "LM50.mat")
    dataset, index_quant_map = _load_exp_data(data_dir)

    assert isinstance(dataset, np.ndarray)
    assert dataset.shape[0] == 7
    assert dataset.shape[1] > 100

    assert isinstance(index_quant_map, dict)
    assert index_quant_map
    assert 'voltage_d' in index_quant_map
    assert 'voltage_q' in index_quant_map
    assert 'speed' in index_quant_map
    assert 'current_d' in index_quant_map
    assert 'current_q' in index_quant_map
    assert 'torque' in index_quant_map
    assert 'time' in index_quant_map


def test__load_data(setup_data_dir):
    train_sim_dir = os.path.join(setup_data_dir, "train_sim")
    val_sim_dir = os.path.join(setup_data_dir, "val_sim")
    train_raw_dir = os.path.join(setup_data_dir, "train_raw")
    test_raw_dir = os.path.join(setup_data_dir, "test_raw")

    train_sim_dataset, index_quant_map = load_data(train_sim_dir)
    val_sim_dataset, index_quant_map = load_data(val_sim_dir)
    train_raw_dataset, index_quant_map = load_data(train_raw_dir)
    test_raw_dataset, index_quant_map = load_data(test_raw_dir)

    assert train_sim_dataset
    assert val_sim_dataset
    assert train_raw_dataset
    assert test_raw_dataset

    assert isinstance(index_quant_map, dict)
    for data in train_sim_dataset:
        assert isinstance(data, np.ndarray)
        assert data[0:6, :].min() >= -1.0
        assert data[0:6, :].max() <= 1.0

    for data in val_sim_dataset:
        assert isinstance(data, np.ndarray)
        assert data[0:6, :].min() >= -1.0
        assert data[0:6, :].max() <= 1.0

    for data in train_raw_dataset:
        assert isinstance(data, np.ndarray)
        assert data[0:6, :].min() >= -1.0
        assert data[0:6, :].max() <= 1.0

    for data in test_raw_dataset:
        assert isinstance(data, np.ndarray)
        assert data[0:6, :].min() >= -1.0
        assert data[0:6, :].max() <= 1.0


def test__rev_test_output(setup_data_dir):
    data_dir = os.path.join(setup_data_dir, "train_raw",
                            "LM50.mat")
    dataset, index_quant_map = _load_exp_data(data_dir)

    dataset = np.vstack((dataset[-1, :],
                         dataset[0:3, :],
                         dataset[3, :],
                         dataset[3, :],
                         dataset[4, :],
                         dataset[4, :],
                         dataset[5, :],
                         dataset[5, :]))

    denormalized_dataset = rev_test_output(dataset)

    assert isinstance(denormalized_dataset, dict)
    assert 'time' in denormalized_dataset
    assert 'voltage_d' in denormalized_dataset
    assert 'voltage_q' in denormalized_dataset
    assert 'speed' in denormalized_dataset
    assert 'current_d_true' in denormalized_dataset
    assert 'current_d_pred' in denormalized_dataset
    assert 'current_q_true' in denormalized_dataset
    assert 'current_q_pred' in denormalized_dataset
    assert 'torque_true' in denormalized_dataset
    assert 'torque_pred' in denormalized_dataset


def test__get_sample_metadata(setup_data_dir):
    data_dir = os.path.join(setup_data_dir, "train_raw")
    dataset, index_quant_map = load_data(data_dir)
    samples = get_sample_metadata(dataset, 1, 100)

    assert isinstance(samples, list)
    assert len(samples)

    for sample in samples:
        assert len(sample) == 4
        assert sample[1] + 100 == sample[2]
        assert sample[2] == sample[3] + 50


class Test_FlatInFlatOut(object):
    def test__init(self, setup_data_dir):
        data_dir = os.path.join(setup_data_dir, "train_raw")
        dataset, index_quant_map = load_data(data_dir)
        samples = get_sample_metadata(dataset, 1, 100)
        inp_quants = ['voltage_d', 'voltage_q', 'speed']
        out_quants = ['current_d', 'current_q', 'torque']

        dataloader = FlatInFlatOut(dataset, index_quant_map,
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
