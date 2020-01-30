
from collections import defaultdict
from collections.abc import Iterable

def twoSum(array, x):
    resultDict = defaultdict(set)
    for index, value in enumerate(array):
        resultDict[value].add(index)

    for value in resultDict:
        if x-value in resultDict:
            if x-value == value and len(resultDict[value]) > 1:
                return sorted([resultDict[value].pop()+1, resultDict[value].pop()+1])
            elif x-value != value:
                return sorted([resultDict[value].pop()+1, resultDict[x-value].pop()+1])

    return -1


def main():
    with open('rosalind_2sum.txt') as input_data:
        k, n = map(int, input_data.readline().strip().split())
        arrays = [map(int, line.strip().split()) for line in input_data.readlines()]

    indicesTwoSum = list(list())
    for array in arrays:
        indicesTwoSum.append(twoSum(list(array),0))

    for i in range(len(indicesTwoSum)):
        if isinstance(indicesTwoSum[i], Iterable):
            print(*indicesTwoSum[i], sep=' ')
        else:
            print(indicesTwoSum[i])
            


if __name__ == '__main__':
    main()