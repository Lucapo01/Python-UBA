def obtener_substring(cadena: str, caracter_de_corte: str) -> str:
    """
    Esta función recibirá por parámetro una cadena y un carácter,
    y devuelve la cadena a partir de la primera posicion del caracter de corte
    Si no encuentra el caracter devuelve la cadena
    """
    if cadena.find(caracter_de_corte) == -1:
        return cadena
    else:
        return cadena[cadena.find(caracter_de_corte):]


print(obtener_substring("Hola buenas tardes", 'b'))
print(obtener_substring("www.youtube.com/watch?v=dQw4w9WgXcQ", '/'))
print(obtener_substring("Lorem ipsum dolor sit amet consectetur", '$'))
