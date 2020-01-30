
import math

with open("lgis/rosalind_lgis.txt","r") as lgis:
    size=int(lgis.readline().strip())
    permutations=[int(x) for x in lgis.readline().strip().split(' ')]
    newpermutations=[-1*x for x in permutations]

def lgis(string):
    a=[0]*size
    b=[0]*(size+1)

    c=0

    for i in range(size):
        low=1
        high=c
        while low<=high:
            mid=math.ceil((low+high)/2)
            if string[b[mid]]<string[i]:
                low = mid+1
            else:
                high = mid-1
        new = low
        a[i]=b[new-1]
        b[new] = i
        if new>c:
            c=new

    d=[0]*c
    e=b[c]
    for i in reversed(range(c)):
        d[i]=string[e]
        e=a[e]
    return d

print(' '.join(map(str,lgis(permutations))))
print(' '.join(map(str,[-1*x for x in lgis(newpermutations)])))
