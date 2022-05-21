x = int(input())
y = int(input())
soma = 0
if x >= y:
    incremento = -1
else:
    incremento = 1

for i in range(x, y, incremento):
    if i % 2 != 0 and i != x and i != y:
        soma+= i

print(soma)
