def signo_zodiaco(dia, mes):

    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        return "Aries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        return "Géminis"
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 23):
        return "Cáncer"
    elif (mes == 7 and dia >= 24) or (mes == 8 and dia <= 23):
        return "Leo"
    elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
        return "Virgo"
    elif (mes == 9 and dia >= 24) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
        return "Escorpio"
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        return "Capricornio"
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        return "Acuario"
    elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 20):
        return "Piscis"
    else:
        return "Fecha incorrecta"


def main():
    '''
    El programa pide al usuario su dia y mes de nacimiento e imprime por pantalla su signo zodiacal
    '''
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    print(signo_zodiaco(dia, mes))


main()
