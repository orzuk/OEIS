# Parse names of sequences to create keywords and labels for each sequence   
import numpy as np 
import matplotlib.pyplot as plt
import os
from numpy.lib.npyio import BagObj
import collections, re

def parse_seqs_names(names):

    num_seqs = len(names)
    name_lens = [0] * num_seqs
    for i in range(0,len(names)):
        name_lens[i] = len(names[i])
    
 
    # List of 'special' keywords 
    
    all_names = '; '.join(names)
    
    all_names = all_names.replace("the", "")

    common_words = ['n', 'the', 'is', 'with', 'that', 'which', 'of', 'are', \
                    'Number', 'n', 'for', 'k', 'number', 'to', 'numbers', 'a', 'x', 'when'] # remove one letter words and words with common 
        

    bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
            for txt in names]
    
    
    rand_perm = np.random.permutation(num_seqs)
    sumbags = sum([bagsofwords[k] for k in rand_perm[1:3000]], collections.Counter()) # get most frequent words
    
    for com_w in common_words:
        del sumbags[com_w]

    

    n_frequent = 100 # take number of most frequent words 
    
    # create labels 
    labels_vec = [0] * num_seqs
    
    frequent_words = sumbags.most_common(n_frequent)
    for i in range(0, n_frequent): # loop on most frequent words  
        for j in range(0, num_seqs): 
            if(frequent_words[i][0] in bagsofwords[j]): 
                labels_vec[j] = i+1
    
    
    
    
    labels_names = [frequent_words[k][0] for k in range(0, n_frequent)]    
    
    # save to file 
    seq_ids = names
    for i in range(0, 4): # loop on most frequent words  
        seq_ids[i] = names[i][1:-1]
    for i in range(4, num_seqs): # loop on most frequent words  
        seq_ids[i] = names[i].partition(' ')[0]
    
    
    os.chdir('C:\Users\oorzu\Documents\GitHub\OEIS\data') # my path 
    
    labels_file = open('labels', 'wb')
    for i in range(0, num_seqs):
        labels_file.write(seq_ids[i] + '\t' + str(labels_vec[i]) + '\n')
    labels_file.close()    

    labels_file = open('label_names', 'wb')
    for i in range(0, n_frequent):
        labels_file.write(str(i+1) + '\t' + labels_names[i] + '\n')
    labels_file.close()    

    
    return (labels_vec, labels_names) # return labels 
