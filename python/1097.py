def updateI(i):
    return i + 2

i = 1
for j in range(7, 16, 2):
    print(f"I={i} J={j}")
    print(f"I={i} J={j-1}")
    print(f"I={i} J={j-2}")
    i = updateI(i)
