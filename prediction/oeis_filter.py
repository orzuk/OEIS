""" TODO: nothing here yet """
import numpy as np

# filters sequences where we do not know or have the first 30 numbers
def filter_short_seqs(dataset):
    good_samples = np.array([],dtype="int32")
    for i in range(len(dataset)):
        if(np.all(dataset[i,:,:]<255)):
            good_samples = np.append(good_samples,[int(i)])
    # print(good_samples[7])
    # print(dataset[good_samples[7],:,:])
    return dataset[good_samples,:,:]
