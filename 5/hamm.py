from operator import ne


def hamming_distance(string1, string2):
    if len(string1) != len(string2):
        raise Exception('Undefined for sequences of unequal length.')
    return sum(list(map(ne, string1, string2)))


def main():
    with open('hamm/rosalind_hamm.txt') as input_data:
        string1, string2 = [line.strip() for line in input_data]

    h_dist = str(hamming_distance(string1,string2))

    print(h_dist)

if __name__ == '__main__':
    main()