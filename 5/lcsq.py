from numpy import zeros
from scripts import ReadFASTA

def longest_common_subsequence(string1, string2):
	matrix = zeros((len(string1)+1,len(string2)+1))
	for i in range(len(string1)):
		for j in range(len(string2)):
			if string1[i] == string2[j]:
				matrix[i+1][j+1] = matrix[i][j]+1
			else:
				matrix[i+1][j+1] = max(matrix[i+1][j],matrix[i][j+1])

	longestSeq = ''
	i,j = len(string1), len(string2)
	while i*j != 0:
		if matrix[i][j] == matrix[i-1][j]:
			i -= 1
		elif matrix[i][j] == matrix[i][j-1]:
			j -= 1
		else:
			longestSeq = string1[i-1] + longestSeq
			i -= 1
			j -= 1

	return longestSeq

if __name__ == '__main__':
	string1, string2 = [fasta[1] for fasta in ReadFASTA('lcsq/rosalind_lcsq.txt')]
	
	lcsq = longest_common_subsequence(string1,string2)

	print(lcsq)