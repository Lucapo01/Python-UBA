def comparar_enteros(a:int, b:int):
    if a>b:
        return a
    elif a<b:
        return b

def main():
    a = int(input("Ingrese el número 'a': "))
    b = int(input("Ingrese el número 'b': "))
    print(comparar_enteros(a, b))

main()