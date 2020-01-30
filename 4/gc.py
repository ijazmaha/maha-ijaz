from scripts import ReadFASTA


def max_gc_content(seq_list):
    gc_content = lambda seq: sum([100.0 for base in seq if base in ('G', 'C')])/len(seq)
    gc_list = list()

    for seq_name,seq in seq_list:
        gc_list.append([seq_name,gc_content(seq)])

    return max(gc_list, key=lambda x: x[1])


def main():
    seq_list = ReadFASTA('GC/rosalind_gc.txt')
    highest_gc = map(str, max_gc_content(seq_list))

    print('\n'.join(highest_gc))

if __name__ == '__main__':
    main()