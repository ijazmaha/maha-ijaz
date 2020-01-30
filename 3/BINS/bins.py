


def binarySearch(arr, start, end, value): 
    while start <= end: 
        mid = start + (end - start) // 2; 
          
        if arr[mid] == value: 
            return mid 
  
        elif arr[mid] < value: 
            start = mid + 1
  
        else: 
            end = mid - 1
      
    return -1


if __name__ == '__main__':

    with open('rosalind_bins.txt') as input_data:
        n, m = [int(input_data.readline().strip()) for repeat in range(2)]
        array = list(map(int, input_data.readline().strip().split()))
        values = list(map(int, input_data.readline().strip().split()))

    indices = list()
    for value in values:
        indices.append(binarySearch(array,0,len(array) - 1,value))

    indices = [index + 1 if index >= 0 else -1 for index in indices]


    print(*indices, sep=' ')
