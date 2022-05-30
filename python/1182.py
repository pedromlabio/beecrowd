def criarMatriz():
    matriz = []

    for i in range(12):
        matriz.append([])
        for j in range(12):
            valor = float(input())
            matriz[i].append(valor)

    return matriz

def somar(matriz, coluna):
    soma = 0
    for i in range(12):
        soma+= matriz[i][coluna]

    return soma

def media(matriz, coluna):
    soma = somar(matriz, coluna)
    return soma/12


def main():
    n = int(input())
    opcao = input()
    matriz = criarMatriz()

    if opcao == "S":
        resultado = somar(matriz,n)
    elif opcao == "M":
        resultado = media(matriz,n)

    print(f"{resultado:.1f}")

main()
