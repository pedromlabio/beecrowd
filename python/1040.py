def calcularMedia(n1, n2, n3, n4):

    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
    return  media

def aplicarExame(media):

    notaExame = float(input())

    print(f"Nota do exame: {notaExame}")

    mediaFinal = (media + notaExame) / 2

    if mediaFinal >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {mediaFinal:.1f}")



def main():

    n1, n2, n3, n4 = map(float, input().split())

    media = calcularMedia(n1, n2, n3, n4)

    print(f"Media: {media:.1f}")

    if media >= 7:
        print("Aluno aprovado.")
    elif media < 5:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        aplicarExame(media)




#========================
main()
