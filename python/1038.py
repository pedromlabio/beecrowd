cod,  quant = map(int, input().split())

valor = 0
if cod == 1:
    valor = quant * 4
elif cod == 2:
    valor = quant * 4.5
elif cod == 3:
    valor = quant * 5
elif cod == 4:
    valor = quant * 2
elif cod == 5:
    valor = quant * 1.5

print(f"Total: R$ {valor:.2f}")
