def main():
    nome = input()
    salarioFixo = float(input())
    vendasMensal = float(input())
    comissao = (vendasMensal/100) * 15
    total = salarioFixo + comissao
    print(f"TOTAL = R$ {total:.2f}")


#=============================
main()
