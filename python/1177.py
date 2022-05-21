def main():

    n = int(input())
    vetor = []
    counter = 0
    for i in range(1000):
        if counter >= n:
            counter = 0
        vetor.append(counter)
        counter+=1

    for i in range(1000):
        print(f"N[{i}] = {vetor[i]}")

main()
