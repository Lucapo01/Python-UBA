def main():
    n = int(input("Ingrese un número n: "))
    m = int(input("Ingrese un número m: "))
    while m < 0:
        m = int(input("Ingrese numero m: "))
    get_tablas(n, m)


def get_tablas(n, m):
    for i in range(n, m + 1):
        str_final = str(n) + " x " + str(i) + " = " + str(i * n)
        print(str_final)


main()
