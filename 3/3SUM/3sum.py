
def threeSum(array):
    originalArray = array[:]
    array.sort()
    n = len(array)
    for i in range(n-2):
        value = array[i]
        nextValIndex = i+1
        lastValIndex = n-1
        while nextValIndex < lastValIndex:
            nextVal = array[nextValIndex]
            lastVal = array[lastValIndex]
            if value+nextVal+lastVal == 0:
                return sorted([originalArray.index(value)+1,
                               originalArray.index(nextVal)+1,
                               originalArray.index(lastVal)+1])
            elif value+nextVal+lastVal > 0:
                lastValIndex = lastValIndex-1
            else:
                nextValIndex = nextValIndex+1
    return [-1]

if __name__ == "__main__":
    with open("rosalind_3sum.txt") as f:
        k = int(f.readline().split()[0]) # number of arrays
        for i in range(k):
            array = list(map(int, f.readline().split()))
            result = threeSum(array)
            print(*result,sep=' ')
        