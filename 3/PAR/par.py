
def two_way_partition(a):
    result = list()
    for value in a[1:]:
        if value <= a[0]:
            result.append(value)
            
    result.append(a[0])

    for value in a[1:]:
        if value > a[0]:
            result.append(value)
    
    return result


def main():
    with open('rosalind_par.txt') as input_data:
        input_data.readline()
        a = map(int, input_data.readline().strip().split())

    result = list(two_way_partition(list(a)))

    with open('par.txt', 'w') as output_data:
        output_data.write(' '.join(map(str,result)))

if __name__ == '__main__':
    main()