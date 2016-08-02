import os
import sys
import oeis_io as oio

__author__ = "Yoav Wald, Ofer Springer"


if __name__ == "__main__":

    script_fn = os.path.abspath(os.path. sys.argv[0])
    script_dir = os.path.dirname(script_fn)
    oeis_dir = os.path.dirname(script_dir)
    digit_mats_fn = os.path.join(oeis_dir, 'data', 'digit_mats')

    digit_mats = oio.read_seq_digit_mats(digit_mats_fn)
    print digit_mats[0:10,:,:]
    # TODO: add some visualizations for digit_mats