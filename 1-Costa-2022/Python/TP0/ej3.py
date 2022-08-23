def numeros_amigos(a: int, b: int) -> bool:
    '''
    Determina si los números a y b son amigos
    '''
    suma_a = 0
    suma_b = 0
    for i in range(1, a-1):
        if a % i == 0:
            suma_a += i

    for i in range(1, b-1):
        if b % i == 0:
            suma_b += i

    if suma_a == b and suma_b == a:
        return True
    else:
        return False


def main():
    a = int(input("Ingrese el número 'a': "))
    b = int(input("Ingrese el número 'b': "))
    print(numeros_amigos(a, b))


main()
