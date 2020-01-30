
from numpy import zeros
from scripts import ReadFASTA

dnas = [fasta[1] for fasta in ReadFASTA('pdst/rosalind_pdst.txt')]

dnaLen = len(dnas[0])

M = zeros((len(dnas),len(dnas)))
for i in range(len(dnas)):
	for j in range(len(dnas)):
		if i < j:
			for k in range(dnaLen):
				if dnas[i][k] != dnas[j][k]:
					M[i][j] += 1.0/dnaLen

		elif i > j:
			M[i][j] = M[j][i]

for i in range(len(M)):
    print(*M[i],sep=' ')