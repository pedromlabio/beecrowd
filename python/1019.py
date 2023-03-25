def convertTime(segundos):

    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60

    horario = (f"{horas}:{minutos}:{segundos}")
    return  horario


def main():

    segundos = int(input())
    tempo = convertTime(segundos)
    print(tempo)
    return 0


#================================
main()
