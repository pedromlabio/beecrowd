def main():

    maior = int(input())
    pos = 1

    for i in range(99):
        n = int(input())
        if (n > maior):
            maior = n
            pos = i + 2

    print(maior)
    print(pos)



main()
