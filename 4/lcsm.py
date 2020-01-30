from scripts import ReadFASTA

def longestSubstring(dnas):
	longest = ''
	for start in range(len(dnas[0])):
		for finish in range(len(dnas[0]), start, -1):
			if finish - start <= len(longest):
				break
			elif checkSubstring(dnas[0][start:finish], dnas):
				longest =  dnas[0][start:finish]

	return longest

def checkSubstring(find_dna, dnas):
	for dna in dnas:
		if (len(dna) < len(find_dna)) or (find_dna not in dna):
			return False
	return True


if __name__ == '__main__':
	fasta_list = ReadFASTA('lcsm/rosalind_lcsm.txt')
	dna = []
	for fasta in fasta_list:
		dna.append(fasta[1])

	lcsm = longestSubstring(dna)
	print(lcsm)
