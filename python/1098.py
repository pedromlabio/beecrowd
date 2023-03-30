def main():

    for i in range(0, 21, 2):
        for j in range(1, 4, 1):
            if (i % 10 == 0):
                print(f"I={i / 10:.0f} J={j + (i / 10):.0f}")
            else:
                print(f"I={i / 10} J={j + (i / 10)}")


main()
