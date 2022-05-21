n = 0
i = 0

while i < 5:
    i+=1
    num = int(input())
    if num % 2 == 0:
        n+=1

print(f"{n} valores pares")
