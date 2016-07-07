# Read OEIS data 

import numpy as np 
import filter_seqs as fs
import plot_basic_seq_stats as pb

seq_file = open("C:/Users/oorzu/Documents/GitHub/OEIS/data/stripped", "r")
names_file = open("C:/Users/oorzu/Documents/GitHub/OEIS/data/names", "r")

seqs = seq_file.readlines()
names = names_file.readlines()

num_seqs = len(seqs)
print "Total: " +str(num_seqs) +" sequences" 

seq_lens = [0] * num_seqs
for i in range(0,len(seqs)):
#    print i
    tmp_seq = seqs[i].split(",")[1:-1]
    if len(tmp_seq)>1:
        seqs[i] = map(int, tmp_seq)
        seq_lens[i] = len(seqs[i])
names_file.close()

# Print example 
print "Example seq #4:"
print names[4]
print seqs[4]

seq_file.close()
names_file.close()


# Filter sequences 
filtered_seqs = fs.filter_seqs(seqs)

print "Num. filtered="+str(len(filtered_seqs)) # print seqs


# Display basic statistics for sequneces 
pb.plot_basic_seq_stats(filtered_seqs)




# Cluster sequences



# Visualize sequences 



# Textual analysis 


# Predict missing values 


