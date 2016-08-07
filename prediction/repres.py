import numpy as np

__author__ = "Yoav Wald, Ofer Springer"


def num_to_digits(num, first_digit, last_digit):
    """
    Convert number to array of base-10 digits
    """
    digit_range = range(first_digit, last_digit+1)
    powers_of_ten = np.power(10, digit_range)
    digits = np.mod(num / powers_of_ten, 10)
    return np.hstack((digits, num > 0))


def seq_to_digit_mat(seq, first_num, last_num, first_digit, last_digit):
    """
    Convert a sequence into a matrix of base-10 digits representation. The rightmost column
    is 1 in rows corresponding to positive sequence integers. Rows corresponding to integers missing
    in the sequence (for sequences shorter than last_num+1) are set to all -1.
    """
    mat_lst = [num_to_digits(num, first_digit, last_digit) for num in seq[first_num:last_num+1]]
    partial_mat = np.asarray(mat_lst)
    mat = -np.ones((last_num-first_num+1, last_digit-first_digit+2))
    mat[0:partial_mat.shape[0], :] = partial_mat
    return mat


def seqs_to_digit_mats(seqs, first_num=0, last_num=30, first_digit=0, last_digit=10):

    digit_mats = np.zeros((len(seqs), last_num-first_num+1, last_digit-first_digit+2), dtype=np.uint8)
    for i, seq in enumerate(seqs.values()):
        digit_mats[i, :, :] = seq_to_digit_mat(seq, first_num, last_num, first_digit, last_digit)
    return digit_mats
