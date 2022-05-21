def fib(n):
    if n == 1:
        n = 2
    b1 = 1
    b2 = 0
    atual = 0
    for i in range(n-1):
        atual = b1 + b2
        b2 = b1
        b1 = atual

    return atual

def imprimirFib(v, n):
    for i in range(n):
        print(f"Fib({v[i]}) = {fib(v[i])}")

def main():
    n = int(input())
    vetor = []
    for i in range(n):
        vetor.append(int(input()))

    imprimirFib(vetor, n)

main()
