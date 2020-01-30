import random

def partition(array):
    pivot = array[0]
    start, end = 0, len(array) - 1
    while start != end:
        while end != start and array[end] > pivot:
            end -= 1
        array[start], array[end] = array[end], array[start]
        while start != end and array[start] <= pivot:
            start += 1
        array[start], array[end] = array[end], array[start]
    return start

def findKthSmallestElement(array, k):
    index = random.randrange(len(array))
    array[0], array[index] = array[index], array[0]
    
    pos = partition(array)
    if pos == k - 1:
        return array[pos]
    elif pos < k - 1:
        return findKthSmallestElement(array[pos + 1:], k - pos - 1)
    else:
        return findKthSmallestElement(array[:pos], k)

def main():
    with open("rosalind_med.txt") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))
        k = int(f.readline())

    print(findKthSmallestElement(array, k))

if __name__ == '__main__':
    main()