def three_way_partition(values):
    result = list()

    for value in values:
        if value < values[0]:
            result.append(value)
    
    counts = values.count(values[0])

    while counts != 0:
        result.append(values[0])
        counts -= 1


    for value in values:
        if value > values[0]:
            result.append(value)

    return result


def main():
    with open('rosalind_par3.txt') as input_data:
        input_data.readline()  
        values = map(int, input_data.readline().strip().split())

    result = three_way_partition(list(values))

    with open('par3.txt', 'w') as output:
        output.write(' '.join(map(str,result)))

if __name__ == '__main__':
    main()