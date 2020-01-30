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

def mergeSort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array)//2

    lower = mergeSort(array[:midpoint])
    upper = mergeSort(array[midpoint:])

    return mergeArrays(lower, upper)


def main():
    with open('rosalind_ms.txt') as input_data:
        n = int(input_data.readline().strip())
        array = list(map(int, input_data.readline().strip().split()))

    result = mergeSort(array)

    with open('MS.txt', 'w') as output_data:
        output_data.write(' '.join(map(str,result)))

if __name__ == '__main__':
    main()