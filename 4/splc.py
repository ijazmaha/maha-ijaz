from scripts import ReadFASTA, ProteinDictDNA

dna_list = ReadFASTA('splc/rosalind_splc.txt')
print(dna_list)
exon = dna_list[0][1]

for intron in dna_list[1:]:
	exon = exon.replace(intron[1], '')

dna_dict = ProteinDictDNA()
exon_protein = ''
for index in range(0, len(exon), 3):
	exon_protein += dna_dict[exon[index:index+3]] if dna_dict[exon[index:index+3]]  != 'Stop' else ''

print(exon_protein)
