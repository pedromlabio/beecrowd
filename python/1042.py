a, b, c = map(int, input().split())

menor = c

if b < menor:
    menor = b
if a < menor:
    menor = a

#print(menor)

maior = c

if b > maior:
    maior = b
if a > maior:
    maior = a

meio = 0

if a < maior and a > menor:
    meio = a

if b < maior and b > menor:
    meio = b

if c < maior and c > menor:
    meio = c


print(menor)
print(meio)
print(maior)
print()
print(a)
print(b)
print(c)
