
from scripts import ReadFASTA

dnas = ReadFASTA('grph/rosalind_grph.txt')

overlaps = []
for i in range(len(dnas)):
    for j in filter(lambda j: j!=i, range(len(dnas))):
        if  dnas[i][1][-3:] == dnas[j][1][0:3]:
            overlaps.append(dnas[i][0]+' '+dnas[j][0])


print(*overlaps,sep='\n')