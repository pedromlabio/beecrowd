def decomporValor(valor):

    lista = []

    notas100 = valor // 100
    list.append(lista, notas100)
    valor = valor % 100

    notas50 = valor // 50
    list.append(lista, notas50)
    valor = valor % 50

    notas20 = valor // 20
    list.append(lista, notas20)
    valor = valor % 20

    notas10 = valor // 10
    list.append(lista, notas10)
    valor = valor % 10

    notas5 = valor // 5
    list.append(lista, notas5)
    valor = valor % 5

    notas2 = valor // 2
    list.append(lista, notas2)
    valor = valor % 2

    moeda1 = valor // 1
    lista.append(moeda1)
    valor = valor - moeda1

    # now we gotta treat the data to make sure it works on conversion
    valor = valor * 100

    moeda50 = valor // 50
    lista.append(moeda50)
    valor = valor % 50

    moeda25 = valor // 25
    lista.append(moeda25)
    valor = valor % 25

    moeda10 = valor // 10
    lista.append(moeda10)
    valor = valor % 10

    moeda5 = valor // 5
    lista.append(moeda5)
    valor = valor % 5

    moeda1 = valor # we can do this since it will be an integer from 0 to 4
    lista.append(moeda1)

    return lista

def main():

    valor = float(input())

    valores = decomporValor(valor)

    imprimirValores(valores)

    return 0


#=========================
main()