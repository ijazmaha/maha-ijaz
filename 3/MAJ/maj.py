def majority_element(a):

    candidate, count = a[0], 0

    for element in a:
        if element == candidate:
            count += 1
        else:
            count += -1
        if count == 0:
            candidate, count = element, 1

    if a.count(candidate) > len(a)/2:
        return candidate
    else:
        return -1
    


def main():
    with open('rosalind_maj.txt') as input_data:
        next(input_data)
        arrays = [map(int, line.strip().split()) for line in input_data]

    maj_element = list()
    for a in arrays:
        maj_element.append(majority_element(list(a)))
        

    # Print and save the answer.
    print(*maj_element,sep=' ')

if __name__ == '__main__':
    main()