def main():
    cod1, n1, valor1 = map(float, input().split())
    cod2, n2, valor2 = map(float, input().split())
    p1 = n1 * valor1
    p2 = n2 * valor2
    total = p1 + p2
    print(f"VALOR A PAGAR: R$ {total:.2f}")

#============================

main()
