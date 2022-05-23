def calcularFrequencia(t: str):

    cont = [0] * 26

    for l in t:
        cod = ord(l)
        if cod >= 97 and cod <= 122:
            cont[cod - 97] += 1
        elif cod >= 65 and cod <= 90:
            cont[cod - 65] += 1

    m = maior(cont)
    mostrarResultados(cont, m)

def maior(cont: list) -> int:
    maior = cont[0]
    for i in range(1, len(cont)):
        if cont[i] > maior:
            maior = cont[i]

    return maior

def mostrarResultados(cont: list, m: int):
    for i in range(len(cont)):
        if cont[i] == m:
            print(chr(i + 97), end="")
    print("")






def main():
    n = int(input())

    for i in range(n):
        texto = input()
        calcularFrequencia(texto)

#=======================
main()
