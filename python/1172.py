def substituir(vetor):


    for i in range(10):
        if vetor[i] <= 0:
            vetor[i] = 1

    return vetor


def main():
    vetor = []
    for i in range(10):
        n = int(input())
        vetor.append(n)
    vetor = substituir(vetor)

    for i in range(10):
        print(f"X[{i}] = {vetor[i]}")


main()
