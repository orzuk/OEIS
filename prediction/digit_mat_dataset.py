import os
import numpy as np

digit_mat_sz = np.array([31, 12])
x_mat_sz = np.array([30, 12])
dim_x = (digit_mat_sz[0] - 1) * digit_mat_sz[1]
dim_y = 10

class Dataset(object):

    def next_batch(self, batch_size):

        batch_inds = np.random.choice(self._x.shape[0], batch_size, replace=False)
        batch = {'x': self._x[batch_inds, :], 'y': self._y[batch_inds, :]}
        self._epoch_samples_used += batch_size
        if self._epoch_samples_used >= self._x.shape[0]:
            self._epochs_performed += 1
            self._epoch_samples_used = 0
        return batch

    def __init__(self, x, y):

        self._x = x;
        self._y = y;
        self._epoch_samples_used = 0
        self._epochs_performed = 0


def to_indicator(y_val):

    n = y_val.shape[0]
    y_indicator = np.zeros((n, dim_y))
    y_indicator[range(n), y_val] = 1
    return y_indicator.reshape((n, -1))


def init_sets(digit_mats, train_ratio):

    samples = digit_mats[:, 0:(digit_mat_sz[0] - 1), :].reshape((-1, dim_x))
    labels = to_indicator(digit_mats[:, digit_mat_sz[0] - 1, 0])
    num_samples = digit_mats.shape[0]
    num_train = int(train_ratio * num_samples)
    p = np.random.permutation(num_samples)
    train_inds = p[0:num_train]
    test_inds = p[num_train:-1]
    train_samples = samples[train_inds, :]
    test_samples = samples[test_inds, :]
    train_labels = labels[train_inds, :]
    test_labels = labels[test_inds, :]
    train = Dataset(train_samples, train_labels)
    test = Dataset(test_samples, test_labels)

    return train, test
