def lerVetor():
    vetor = []
    for i in range(20):
        n = int(input())
        vetor.append(n)
    return vetor

def trocarVetor(v):
    vetor2 = []
    for i in range(20):
        vetor2.append(v[19 - i])
    return vetor2

def imprimirVetor(v):
    for i in range(20):
        print(f"N[{i}] = {v[i]}")


def main():
    v = lerVetor()
    v = trocarVetor(v)
    imprimirVetor(v)

main()
