import sys
import os
import prediction.oeis_io as oio
import prediction.repres as rep
from timeit import default_timer as timer

__author__ = "Yoav Wald, Ofer Springer"


if __name__ == "__main__":

    """
    Running this file generates all the sequence representations needed for the
    predicition task and saves them into the OEIS-wide data directory. Currently only
    empty sequences and ones containing big integers are filtered.
    """

    script_fn = os.path.abspath(sys.argv[0])
    script_dir = os.path.dirname(script_fn)
    oeis_dir = os.path.dirname(script_dir)
    seq_vals_fn = os.path.join(oeis_dir, 'data', 'stripped')
    digit_mats_fn = os.path.join(oeis_dir, 'data', 'digit_mats')

    start = timer()
    seqs, _, _ = oio.read_seq_values(seq_vals_fn)
    stop = timer()
    print('Loading took %0.3f secs' % (stop - start))

    start = timer()
    digit_mats = rep.seqs_to_digit_mats(seqs)
    stop = timer()
    print('Processing took %0.3f secs' % (stop - start))

    start = timer()
    oio.write_seq_digit_mats(digit_mats, digit_mats_fn)
    stop = timer()
    print('Saving took %0.3f secs' % (stop - start))
