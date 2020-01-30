from scripts import ReadFASTA, ReverseComplementDNA

dna = ReadFASTA('revp/rosalind_revp.txt')[0][1]
positions = []

for length in range(4,13):
	for position in range(len(dna)-length+1):
		if dna[position:position+length] == ReverseComplementDNA(dna[position:position+length]):
			print(position+1, length)
			positions.append(str(position+1)+' '+str(length))

