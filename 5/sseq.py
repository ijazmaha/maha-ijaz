from scripts import ReadFASTA

dna, sub_seq = [fasta[1] for fasta in ReadFASTA('sseq/rosalind_sseq.txt')]

sseq_indicies, i = [], 0
for nucleotide in sub_seq:
	while dna[i] != nucleotide:
		i += 1
	sseq_indicies.append(str(i+1))
	i += 1

print(*sseq_indicies,sep=" ")
