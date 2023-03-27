def ordenar(lista: list):

    for i in range(len(lista)):
        lista[i] = float(lista[i])

    lista.sort()
    lista.reverse()

    return lista[0], lista[1], lista[2]



def main():

    lista = input().split()

    A, B, C = ordenar(lista)




    if(A >= (B + C)):
        print("NAO FORMA TRIANGULO")
    elif(A**2 == (B**2 + C**2)):
        print("TRIANGULO RETANGULO")
    elif(A**2 > (B**2 + C**2)):
        print("TRIANGULO OBTUSANGULO")
    elif(A**2 < (B**2 + C**2)):
        print("TRIANGULO ACUTANGULO")


    if(A == B == C):
        print("TRIANGULO EQUILATERO")
    elif(A == B) or (A == C) or (B == C):
        print("TRIANGULO ISOSCELES")



#=======================
main()
