i = 0
n = 0
soma = 0
while i < 6:
    num = float(input())

    if num > 0:
        n+=1
        soma += num
    i+=1
media = soma/n
print(f"{n} valores positivos")
print(f"{media:.1f}")
