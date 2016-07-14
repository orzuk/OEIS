# Plot seuqnces statistics  
import numpy as np 
import matplotlib.pyplot as plt
import os


def plot_basic_seq_stats(seqs):

    num_seqs = len(seqs)
    seq_lens = [0] * num_seqs
    for i in range(0,len(seqs)):
        seq_lens[i] = len(seqs[i])
    
    
    plt.hist(seq_lens, bins=100)
    plt.title('Lengths of sequences')
    plt.xlabel('Length')
    plt.ylabel('Freq.')
    fig = plt.gcf()
    
    print "Save in dir: "+os.path.dirname(os.path.realpath(__file__))
    plt.savefig('../figs/lengths_hist.png')
    