from itertools import takewhile
from scripts import ProteinTranslator


def toProtein(rna):
    translate = ProteinTranslator()
    not_stop = lambda rna_base: translate.rna_to_protein(rna_base) != 'Stop'

    continuousRNA = takewhile(not_stop, (rna[3*i:3*i+3] for i in range(len(rna)//3)))
    
    proteins = list(map(translate.rna_to_protein, continuousRNA))

    return ''.join(proteins)


def main():
    with open('prot/rosalind_prot.txt') as input_data:
        s = input_data.read().strip()

    protein = toProtein(s)

    print(protein)

if __name__ == '__main__':
    main()