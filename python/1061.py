def toSegundos(dia, horas, minutos, segundos):

    tempo = segundos
    tempo+= minutos * 60
    tempo+= horas * 3600
    tempo+= dia * 24 * 3600

    return tempo

def imprimirDuracao(tempo):
    dias = tempo // (24 * 3600)
    tempo = tempo % (24 * 3600)
    horas = tempo // 3600
    tempo = tempo % 3600
    minutos = tempo // 60
    segundos = tempo % 60

    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")




def main():

    t, diaInicio = input().split()
    diaInicio = int(diaInicio)
    horasInicio, minutosInicio, segundosInicio = map(int,input().split(":"))

    t, diaFim = input().split()
    diaFim = int(diaFim)
    horasFim, minutosFim, segundosFim = map(int, input().split(":"))

    fim = toSegundos(diaFim, horasFim, minutosFim, segundosFim)
    inicio = toSegundos(diaInicio, horasInicio, minutosInicio, segundosInicio)

    tempo = fim - inicio

    imprimirDuracao(tempo)

main()
