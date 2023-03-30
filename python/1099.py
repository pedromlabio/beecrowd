def main():

    n = int(input())

    for i in range(n):

        x, y = map(int, input().split())
        if (y < x):
            aux = x
            x = y
            y = aux

        sum = 0
        for j in range(x, y):
            if (j == x): continue
            if (j % 2 != 0):
                sum+= j
        print(sum)

main()
