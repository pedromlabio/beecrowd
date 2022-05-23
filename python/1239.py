def format(t: str) -> str:
    abreItalico = "<i>"
    fechaItalico = "</i>"
    abreNegrito = "<b>"
    fechaNegrito = "</b>"
    italico = negrito = False
    t = list(t)
    for i in range(len(t)):

        if t[i] == "_":
            if italico:
                t[i] = fechaItalico
                italico = False
            else:
                t[i] = abreItalico
                italico = True
        elif t[i] == "*":
            if negrito:
                t[i] = fechaNegrito
                negrito = False
            else:
                t[i] = abreNegrito
                negrito = True

    return "".join(t)



#=======================

def main():

    while True:
        try:
            texto = input()
            final = format(texto)
            print(final)
        except EOFError:
            break

main()
