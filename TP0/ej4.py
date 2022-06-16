def maximo_producto(num_1, num_2, num_3, num_4):
    '''
    Devuelve el maximo producto de cualquier 2 numeros
    '''
    maximo = 0

    if (num_1 * num_2) > maximo:
        maximo = num_1 * num_2
    if (num_1 * num_3) > maximo:
        maximo = num_1 * num_3
    if (num_1 * num_4) > maximo:
        maximo = num_1 * num_4
    if (num_2 * num_3) > maximo:
        maximo = num_2 * num_3
    if (num_2 * num_4) > maximo:
        maximo = num_2 * num_4
    if (num_3 * num_4) > maximo:
        maximo = num_3 * num_4

    return maximo


def main():
    a = int(input("Ingrese el número 'a': "))
    b = int(input("Ingrese el número 'b': "))
    c = int(input("Ingrese el número 'c': "))
    d = int(input("Ingrese el número 'd': "))
    print(maximo_producto(a, b, c, d))


main()
