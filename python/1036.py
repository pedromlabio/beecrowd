import math

a, b, c = map(float, input().split())



delta = ((b**2) - (4 * a * c))

if(a == 0):
    print('Impossivel calcular')
else:

    if (delta <= 0 ):
        print('Impossivel calcular')
    else:

        deltar1 = math.sqrt(delta)

        deltar2 = -(math.sqrt(delta))


        raiz1 = (-b + deltar1)/(2 * a)
        raiz2 = (-b + deltar2)/(2 * a)

        print(f"R1 = {raiz1:.5f}")
        print(f"R2 = {raiz2:.5f}")
