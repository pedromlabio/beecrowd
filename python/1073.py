def main():
    n = int(input())

    for i in range(0, n + 1, 2):
        if (i == 0): continue

        print(f"{i}^2 = {i**2}")


main()
