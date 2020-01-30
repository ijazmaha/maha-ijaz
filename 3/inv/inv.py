
def mergeSortedArraysCountingInversions(array1, array2):
    i, j = 0, 0
    count = 0
    result = []

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            count += len(array1) - i
            j += 1

    result += array1[i:] + array2[j:]

    return result, count


def mergeSortInversionCount(array):
    if len(array) <= 1:
        return array, 0

    midpoint = len(array)//2

    lower, lower_inv = mergeSortInversionCount(array[:midpoint])
    upper, upper_inv = mergeSortInversionCount(array[midpoint:])

    combined, combined_inv = mergeSortedArraysCountingInversions(lower, upper)

    return combined, lower_inv+upper_inv+combined_inv


def main():
    with open('rosalind_inv.txt') as input_data:
        input_data.readline()
        array = map(int, input_data.readline().strip().split())

    inversions = str(mergeSortInversionCount(list(array))[1])

    print(inversions)
    

if __name__ == '__main__':
    main()