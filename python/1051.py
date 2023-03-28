def main():


    salario = float(input())


    if (salario >= 0 and salario <= 2000):
        print("Isento")
    elif(salario > 2000 and salario <= 3000):
        imposto = 0
        valor = salario - 2000
        imposto = (valor / 100) * 8
        print(f"R$ {imposto:.2f}")

    elif (salario > 3000 and salario <= 4500):

        imposto = 80 #herdado do imposto de 2000 a 3000
        valor = salario - 3000
        imposto+= (valor / 100) * 18
        print(f"R$ {imposto:.2f}")

    elif (salario > 4500):

        imposto = 350 # herdado do imposto de 2000 a 3000 e 3000 a 4500
        valor = salario - 4500
        imposto+= (valor / 100) * 28
        print(f"R$ {imposto:.2f}")




#================
main()
