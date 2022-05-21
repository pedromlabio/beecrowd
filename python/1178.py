def imprimirVetor(vetor):
    for i in range(100):
        print(f"N[{i}] = {vetor[i]:.4f}")



def main():
    n = float(input())
    vetor = []
    vetor.append(n)
    for i in range(99):
        n = n/2
        vetor.append(n)

    imprimirVetor(vetor)


main()
