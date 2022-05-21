def main():
    vetor = []
    n = int(input())
    vetor.append(n)
    for i in range(9):
        vetor.append(vetor[i] * 2)

    for i in range(10):
        print(f"N[{i}] = {vetor[i]}")

main()
