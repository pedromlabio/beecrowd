def main():

    n = int(input())

    for i in range(n):
        val = int(input())

        if (val == 0):
            print("NULL")

        elif (val < 0):
            if (val % 2 == 0):
                print("EVEN NEGATIVE")
            else:
                print("ODD NEGATIVE")

        else:
            if (val % 2 == 0):
                print("EVEN POSITIVE")
            else:
                print("ODD POSITIVE")


main()
