n = int(input())
total = 0
coelhos = 0
sapos = 0
ratos = 0

for i in range(n):
    numero, tipo = input().split()

    numero = int(numero)

    total += numero

    if (tipo == "C"):
        coelhos += numero
    elif (tipo == "R"):
        ratos += numero
    elif (tipo == "S"):
        sapos += numero

coelhosp = (coelhos / total) * 100
ratosp = (ratos / total) * 100
saposp = (sapos / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhosp:.2f} %")
print(f"Percentual de ratos: {ratosp:.2f} %")
print(f"Percentual de sapos: {saposp:.2f} %")
