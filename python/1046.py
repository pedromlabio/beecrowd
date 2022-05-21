inicio, fim = map(int, input().split())

if (fim > inicio):
    tempo = fim - inicio
elif (fim == inicio):
    tempo = 24
elif (fim < inicio):
    t1 = 24 - inicio
    t2 = fim
    tempo = t1 + t2

print(f"O JOGO DUROU {tempo} HORA(S)")
