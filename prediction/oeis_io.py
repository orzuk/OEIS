__author__ = "Yoav Wald, Ofer Springer"

import sys
import numpy as np
import scipy.io as scio

""" TODO:
def read_label_names(fn):
def read_seq_names(fn):
def read_seq_labels(fn):
"""


def read_seq_values(fn):

    with open(fn, 'r') as fh:
        seq_strings = fh.readlines()

    big_ints = 0
    zero_length = 0
    seqs = {}

    for line in seq_strings[4:]:  # skip header lines
        name = line[:7]
        if line[9:-2] == "":
            zero_length += 1
            continue
        seq = map(int, line[9:-2].split(","))
        if (len(seq) > 0) and all([abs(i) < sys.maxint for i in seq]):
            seqs[name] = np.array(seq, int)
        else:
            big_ints += 1

    return seqs, zero_length, big_ints


def read_seq_digit_mats(fn):

    mat_dict = scio.loadmat(fn)
    return mat_dict['seq_digit_mats']


def write_seq_digit_mats(seq_digit_mats, fn):

    mat_dict = {'seq_digit_mats': seq_digit_mats}
    scio.savemat(fn, mat_dict)
