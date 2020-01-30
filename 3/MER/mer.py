
def mergeArrays(array1, array2):
    
    i, j = 0, 0
    result = []

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    result += array1[i:] + array2[j:]

    return result


def main():

    with open('rosalind_mer.txt') as input_data:
        n, array1, m, array2 = [int(line.strip()) if i % 2 == 0 else map(int, line.strip().split()) for i, line in enumerate(input_data.readlines())]

    result = mergeArrays(list(array1), list(array2))

    print(*result,sep=' ')

if __name__ == '__main__':
    main()