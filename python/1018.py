def main():

    n = int(input())
    notasAtual = n

    notas100 = notasAtual // 100
    notasAtual-= notas100 * 100

    notas50 = notasAtual // 50
    notasAtual-= notas50 * 50

    notas20 = notasAtual // 20
    notasAtual-= notas20 * 20

    notas10 = notasAtual // 10
    notasAtual-= notas10 * 10

    notas5 = notasAtual // 5
    notasAtual-= notas5 * 5

    notas2 = notasAtual // 2
    notasAtual-= notas2 * 2

    notas1 = notasAtual

    print(n)
    print(f"{notas100} nota(s) de R$ 100,00")
    print(f"{notas50} nota(s) de R$ 50,00")
    print(f"{notas20} nota(s) de R$ 20,00")
    print(f"{notas10} nota(s) de R$ 10,00")
    print(f"{notas5} nota(s) de R$ 5,00")
    print(f"{notas2} nota(s) de R$ 2,00")
    print(f"{notas1} nota(s) de R$ 1,00")



    return


#===============================
main()
