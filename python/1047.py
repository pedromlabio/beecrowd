iHora, iMin, fHora, fMin = map(int, input().split())

mins, horas = 0,0

if fHora > iHora:
    if fMin > iMin:
        mins = fMin - iMin
        horas = fHora - iHora
    elif fMin == iMin:
        mins = 0
        horas = fHora - iHora
    elif fMin < iMin:
        horas = fHora - iHora - 1
        m1 = 60 - iMin
        m2 = fMin
        mins = m1 + m2


elif fHora == iHora:
    if fMin > iMin:
        horas = 0
        mins = fMin - iMin
    elif fMin == iMin:
        horas = 24
        mins = 0
    elif fMin < iMin:
        m1 = 60 - iMin
        m2 = fMin
        horas = 23
        mins = m1 + m2
elif fHora < iHora:

    h1 = 24 - iHora
    h2 = fHora
    m1 = fMin
    m2 = 60 - iMin
    mins = m1 + m2
    horas = h1 + h2 - 1

print(f"O JOGO DUROU {horas} HORA(S) E {mins} MINUTO(S)")
