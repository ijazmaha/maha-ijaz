from scripts import ReadFASTA

string1, string2 = [fasta[1] for fasta in ReadFASTA('tran/rosalind_tran.txt')]

trans = transver = 0.0
for i in range(len(string1)):
	if string1[i] == string2[i]:
		pass
	elif string1[i] in [['A', 'G'],['C', 'T']][string2[i] in ['C', 'T']]:
		trans += 1
	else:
		transver +=1

print(trans/transver)