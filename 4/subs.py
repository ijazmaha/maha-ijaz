with open('subs/rosalind_subs.txt') as input_data:
	seq1,seq2 = input_data.readlines()
	seq1 = seq1.rstrip()
	seq2 = seq2.rstrip()

locations = []
for i in range(0, len(seq1)-len(seq2)+1):
    if seq1[i:i+len(seq2)] == seq2:
        locations.append(str(i+1))

print(' '.join(locations))