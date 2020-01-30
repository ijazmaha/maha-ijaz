from scripts import ReadFASTA, ReverseComplementDNA, ProteinDictDNA

dna_list = [ReadFASTA('orf/rosalind_orf.txt')[0][1]]
dna_list.append(ReverseComplementDNA(dna_list[0]))
dna_dict = ProteinDictDNA()

protein_orf = set()
for dna in dna_list:
	for i in range(len(dna)-2):
		if dna[i:i+3] == 'ATG':
			j = i
			current_protein = ''
			while j+3 < len(dna)-1:
				if dna_dict[dna[j:j+3]] == 'Stop':
					protein_orf.add(current_protein)
					break
				else:
					current_protein += dna_dict[dna[j:j+3]]
				j += 3

protein_orf = map(str, protein_orf)

print('\n'.join(protein_orf))