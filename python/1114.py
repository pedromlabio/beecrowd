def main():
    senha = "2002"

    while True:
        word = input()
        if (word == senha):
            print("Acesso Permitido")
            break
        elif (word != senha):
            print("Senha Invalida")


main()
