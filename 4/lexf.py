from itertools import product

with open('lexf/rosalind_lexf.txt') as input_data:
	letters, n = input_data.readlines()
	letters = ''.join(letters.split())
	n = int(n)

kMers = list()
for item in product(letters,repeat=n):
	kMers.append(''.join(item))


print(*kMers, sep='\n')
