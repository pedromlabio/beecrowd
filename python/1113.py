def main():

    while True:
        x, y = map(int, input().split())
        if (x == y): break

        if (x < y):
            print(f"Crescente")
        elif(x > y):
            print(f"Decrescente")


main()
