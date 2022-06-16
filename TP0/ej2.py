def obtener_multiplos(cant_multiplos, numero):
    """ Funcion que obtiene los multiplos de un numero """
    for i in range(1, cant_multiplos + 1):
        print(numero * i)


def main():
    numero_a = input("Ingrese el número 'a': ")
    while numero_a.isnumeric() == False or numero_a == "0":
        numero_a = input("Ingrese el número 'a': ")
    numero_b = input("Ingrese el número 'b': ")
    while numero_b.isnumeric() == False or numero_b == "0":
        numero_b = input("Ingrese el número 'b': ")

    numero_a = int(numero_a)
    numero_b = int(numero_b)
    obtener_multiplos(numero_a, numero_b)


main()
