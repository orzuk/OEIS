__author__ = "Yoav Wald, Ofer Springer"

"""
Convert numbers in a sequence into matrix of digits representation.
TODO: replace sequence loading (currently using code snippet taken from data.py)
"""

import sys

sys.path.append("../src")

import os, gzip
from collections import defaultdict
from itertools import combinations
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import filter_seqs as fs
import features as ftr

sequences_file = open("../data/stripped", "r").readlines()
sequences = {}

big_ints = 0
zero_length = 0

for line in sequences_file[4:]: # skip header lines
    name = line[:7]
    if line[9:-2] == "":
        zero_length += 1
        continue

    seq = map(int, line[9:-2].split(","))
    if (len(seq) > 0) and all([abs(i) < sys.maxint for i in seq]):
        sequences[name] = np.array(seq, int)
    else:
        big_ints += 1

print zero_length, "sequences were filtered because of length=0"
print big_ints, "sequences were filtered because they contained big integers"

def num_to_digits(num, first_digit, last_digit):
    digit_range = range(first_digit, last_digit)
    powers_of_ten = np.power(10, digit_range)
    digits = np.mod(num / powers_of_ten, 10)
    return digits

def seq_to_mat(seq, first_num=0, last_num=30, first_digit=0, last_digit=10):
    mat_lst = [num_to_digits(num, first_digit, last_digit) for num in seq[first_num:last_num]]
    mat = np.asarray(mat_lst)
    return mat

subplot_ind = 1
for _,seq in sequences.items()[0:18]:
    mat = seq_to_mat(seq)
    plt.subplot(3, 6, subplot_ind)
    plt.imshow(mat, interpolation='nearest')
    subplot_ind += 1
plt.show()
