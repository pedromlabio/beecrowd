n1, n2, n3 = map(int,input().split())

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f"{maior} eh o maior")
