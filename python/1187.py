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
    for i in range(5):
        for j in range(i + 1, 6):
            print(i, j)
            soma += matriz[i][j]
    for i in range(5):
        for j in range(6 ,11 - i):
            print("segunda rodada")
            print(i, j)
            soma += matriz[i][j]
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
