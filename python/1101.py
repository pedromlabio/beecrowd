def main():


    while True:

        n1, n2 = map(int, input().split())

        if (n1 <= 0) or (n2 <= 0):
            break
        if n2 < n1:
            aux = n1
            n1 = n2
            n2 = aux
        sum = 0
        for i in range(n1, n2 + 1):
            sum+= i
            print(f"{i} ", end="")

        print(f"Sum={sum}")



main()
