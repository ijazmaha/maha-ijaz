
from itertools import permutations

def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)

with open('perm/rosalind_perm.txt') as input_data:
    perm_set = range(1, int(input_data.read())+1)

perm_list = map(list,list(permutations(perm_set)))

print(factorial(len(perm_set)))

perm_list = list(perm_list)

for i in range(len(perm_list)):
    print(*perm_list[i],sep=' ')