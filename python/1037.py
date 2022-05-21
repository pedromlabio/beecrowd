n = float(input())

if(n >= 0) and (n <= 25):
    #primeiro intervalo
    print("Intervalo [0,25]")
elif(n > 25) and (n <= 50):
    #segundo intervalo
    print("Intervalo (25,50]")
elif(n > 50) and (n <= 75):
    #terceiro intervalo
    print("Intervalo (50,75]")
elif(n > 75) and(n <= 100):
    #quarto intervalo
    print("Intervalo (75,100]")
else:
    #fora do intervalo
    print("Fora de intervalo")
