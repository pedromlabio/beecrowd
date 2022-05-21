sal = float(input())

percentual = 0
if(sal > 0) and (sal <= 400):
    percentual = 15
elif(sal >= 400.01) and (sal <= 800):
    percentual = 12
elif(sal >= 800.01) and (sal <= 1200):
    percentual = 10
elif(sal >= 1200.01) and (sal <= 2000):
    percentual = 7
elif(sal > 2000):
    percentual = 4

reajuste = sal/100 * percentual
novosal = sal + reajuste

print(f"Novo salario: {novosal:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
