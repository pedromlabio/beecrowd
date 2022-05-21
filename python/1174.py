def main():
    vetor = []
    lista2 = []
    for i in range(100):
        n = float(input())
        vetor.append(n)
        if n <= 10:
            lista2.append(i)

    for j in lista2:
        print(f"A[{j}] = {vetor[j]}")

main()
