# Filter seuqnces which are too short 
import numpy as np 


def filter_seqs(seqs):

	seqs = np.array(seqs[4:-1]) # remove header and convert to numpy array 
	num_seqs = len(seqs)
	filter_vec = [1] * num_seqs
	for i in range(0, num_seqs): # loop on 
		if len(seqs[i]) < 5: # remove short sequences
			filter_vec[i] = 0 	
	seqs_filtered = seqs[np.nonzero(filter_vec)]
	return seqs_filtered
