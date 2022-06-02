def criarMatriz():
    matriz = []

    for i in range(12):
        matriz.append([])
        for j in range(12):
            valor = float(input())
            matriz[i].append(valor)

    return matriz

def somar(matriz):
    soma = 0
    for i in range(6):
        for j in range(11, 11 - i, -1):
            soma+= matriz[i][j]
            #print(i, j)

    for i in range(6, 12):
        for j in range(i + 1, 12):
            soma += matriz[i][j]
            #print(i, j)


    return soma

def media(matriz):
    soma = somar(matriz)
    return soma/30


def main():
    opcao = input()
    matriz = criarMatriz()

    if opcao == "S":
        resultado = somar(matriz)
    elif opcao == "M":
        resultado = media(matriz)

    print(f"{resultado:.1f}")

main()
