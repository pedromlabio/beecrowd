def main():
    n = int(input())
    horasTrabalhadas = int(input())
    salarioHora = float(input())

    salario = horasTrabalhadas * salarioHora

    print(f"NUMBER = {n}")
    print(f"SALARY = U$ {salario:.2f}")

#============================
main()