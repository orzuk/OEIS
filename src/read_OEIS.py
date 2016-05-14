# Read OEIS data 

seq_file = open("C:/Users/oorzu/Documents/GitHub/OEIS/data/stripped", "r")
names_file = open("C:/Users/oorzu/Documents/GitHub/OEIS/data/names", "r")

seqs = seq_file.readlines()
names = names_file.readlines()

num_seqs = len(seqs)
print num_seqs # print seqs

seq_lens = [0] * num_seqs
for i in range(0,len(seqs)):
#    print i
    tmp_seq = seqs[i].split(",")[1:-1]
    if len(tmp_seq)>1:
        seqs[i] = map(int, tmp_seq)
        seq_lens[i] = len(seqs[i])
names_file.close()

print names[4]
print seqs[4]

seq_file.close()
names_file.close()

