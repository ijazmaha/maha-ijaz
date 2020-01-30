
def population(n,k):
    totalPopulation = [0,1]
    for i in range(n-1):
        totalPopulation[i % 2] = totalPopulation[(i-1) % 2] + k*totalPopulation[i % 2]

    return totalPopulation[n % 2]


def main():
    with open('fib/rosalind_fib.txt') as input_data:
        n, k = map(int, input_data.read().strip().split())

    rabbits = str(population(n,k))

    print(rabbits)


if __name__ == '__main__':
    main()