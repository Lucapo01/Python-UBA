palabra: str = input("Ingrese una palabra: ")

a_cambiar = "."
print("Ingrese una plabra vacia para salir")
while a_cambiar != "":

    a_cambiar: str = input("Ingrese una palabra a cambiar: ")
    cambio: str = input(
        "Ingrese una palabra para reemplazar la palabra previa: ")

    palabra = palabra.replace(a_cambiar, cambio)
    print(palabra)
