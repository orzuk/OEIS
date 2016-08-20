import os
import sys
import numpy as np
import prediction.oeis_filter as oif
import prediction.oeis_io as oio
import matplotlib.pyplot as plt

__author__ = "Yoav Wald, Ofer Springer"

if __name__ == "__main__":
    """
    Running this file generates figures of the first 32 sequences in the "digit-matrix"
    representation we're currently using. The digits of entries 1-31 of each sequence are
    shown as rows of digits (base-10) if the entries are available. In each row digits
    1-11 are color coded in the matching columns and the sign of each entry is encoded in
    the rightmost column 12.
    """

    script_fn = os.path.abspath(sys.argv[0])
    script_dir = os.path.dirname(script_fn)
    oeis_dir = os.path.dirname(script_dir)
    seq_vals_fn = os.path.join(oeis_dir, 'data', 'stripped')
    digit_mats_fn = os.path.join(oeis_dir, 'data', 'digit_mats')

    digit_mats = oio.read_seq_digit_mats(digit_mats_fn)
    digit_mats = oif.filter_short_digit_mats(digit_mats)

    sp_rows = 4
    sp_cols = 8
    seq_inds = range(sp_rows*sp_cols)

    fig, axes2d = plt.subplots(nrows=sp_rows, ncols=sp_cols,
                               sharex=True, sharey=True, figsize=(11.5, 13.95))
    k = 0
    for i, row in enumerate(axes2d):
        for j, cell in enumerate(row):
            cell.imshow(digit_mats[k, :, :], interpolation='nearest')
            k = k+1
    fig.suptitle('"Digit-matrix" representation of first 32 sequences in OEIS (see repres_gen.py)')
    fig.text(0.5, 0.04, 'digit in number', ha='center')
    fig.text(0.04, 0.5, 'number in sequence', va='center', rotation='vertical')
    plt.show()
