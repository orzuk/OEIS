import os
import numpy as np

dim_logval = 31
dim_x = 30
dim_y = 1

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


def init_sets(logval_vecs, train_ratio):

    samples = logval_vecs[:, 0:dim_x].reshape((-1, dim_x))
    labels = logval_vecs[:, dim_x].reshape((-1, dim_y))
    num_samples = logval_vecs.shape[0]
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
