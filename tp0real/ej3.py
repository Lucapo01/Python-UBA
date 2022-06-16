def calcular_traza(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    print(suma)


calcular_traza([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
calcular_traza([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
