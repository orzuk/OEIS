import sys
import os
import gzip
from collections import defaultdict
from itertools import combinations

import numpy as np 
import filter_seqs as fs
import features as ftr

__all__ = ["sequences", "descriptions", "names", "features", "duplicates", "duplicates2"]

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
    if (len(seq) > 0) and all([abs(i) < sys.maxint for i in seq]):
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

features = ftr.read_features_file()


# Find perfect duplicates

strings_to_names = defaultdict(lambda: [])

for name in sequences:
    s = sequences[name].tostring()
    strings_to_names[s].append(name)

duplicates = []
for dup in strings_to_names.values():
    if (len(dup) >= 2):
        duplicates.append(sorted(dup))

duplicates2 = set()
for dup in duplicates:
    for n1, n2 in combinations(dup, 2):
        duplicates2.add((n1, n2))
        duplicates2.add((n2, n1))

