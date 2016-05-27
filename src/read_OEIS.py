# Read OEIS data 

import sys
import gzip
import numpy as np 
import filter_seqs as fs
import features as ftr

sequences_file = open("data/stripped", "r").readlines()
sequences = {}

big_ints = 0
zero_length = 0

for line in sequences_file[4:]: # skip header lines
    name = line[:7]
    if line[9:-2] == "":
        zero_length += 1
        continue
        
    seq = map(int, line[9:-2].split(","))
    if (len(seq) > 0) and all(abs(i) < sys.maxint for i in seq):
        sequences[name] = np.array(seq, int)
    else:
        big_ints += 1

print zero_length, "sequences were filtered because of length=0"
print big_ints, "sequences were filtered because they contained big integers"

descriptions_file = open("data/names", "r").readlines()
descriptions = {}

for line in descriptions_file[4:]: # skip header lines
    name, desc = line.strip().split(" ", 1)
    if name in sequences:
        descriptions[name] = desc

names = sorted(sequences.keys())

features = np.rec.fromstring(gzip.open("data/features.bin.gz").read(), dtype = ftr.RecordType)

# Filter sequences 
# filtered_seqs = fs.filter_seqs(seqs)

# print "Num. filtered="+str(len(filtered_seqs)) # print seqs


# Cluster sequences



# Visualize sequences 




# Predict missing values 


