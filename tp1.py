"""
Aclaraciones

Las piezas se representan con una letra, que puede ser:

# x --> vacio
# r --> ficha roja
# b --> ficha azul
# n --> ficha neutra

turnos:

1 -> roja
2 -> neutra
3 -> azul
4 -> neutra
5 -> neutra modo muerte subita (mueve la neutra 4)
6 -> neutra modo muerte subita (mueve la neutra 2)

en modo normal:

1 -> 2 -> 3 -> 4 -> 1

en muerte subita:

1 -> 2 -> 5 -> 3 -> 4 -> 6 -> 1

En la funcion pre_jeugo() recuerde que los limites son de 0 a 3, no use el numero 4

"""



import random
import msvcrt
import copy
import json

LIMITE_MOVIEMIENTOS:int = 10
LIMITE_TAMAÑO_TABLERO:int = 4
CANT_FICHAS = 4 # rojo, azul, neutra1, neutra2

ROJA = 1
NEUTRA_1 = 2
AZUL = 3
NEUTRA_2 = 4
NEUTRA_1_SUBITA = 5
NEUTRA_2_SUBITA = 6

FICHA_ROJA = "r"
FICHA_AZUL = "b"
FICHA_NEUTRA_1 = "n1"
FICHA_NEUTRA_2 = "n2"

TEXTURA_VACIA = "x"
TEXTURA_ROJA = "r"
TEXTURA_AZUL = "b"
TEXTURA_NEUTRA = "n"



def get_coordenadas(pieza:int, coordenadas:dict) -> list:
    if pieza == ROJA:
        return coordenadas[FICHA_ROJA]
    elif pieza == NEUTRA_1 or pieza == NEUTRA_1_SUBITA:
        return coordenadas[FICHA_NEUTRA_1]
    elif pieza == AZUL:
        return coordenadas[FICHA_AZUL]
    elif pieza == NEUTRA_2 or pieza == NEUTRA_2_SUBITA:
        return coordenadas[FICHA_NEUTRA_2]

def set_coordenadas(pieza:int, coordenadas:dict, new_coordenadas:list):
    if pieza == ROJA:
        coordenadas[FICHA_ROJA] = new_coordenadas
    elif pieza == NEUTRA_1 or pieza == NEUTRA_1_SUBITA:
        coordenadas[FICHA_NEUTRA_1] = new_coordenadas
    elif pieza == AZUL:
        coordenadas[FICHA_AZUL] = new_coordenadas
    elif pieza == NEUTRA_2 or pieza == NEUTRA_2_SUBITA:
        coordenadas[FICHA_NEUTRA_2] = new_coordenadas

    return coordenadas

def get_pieza(pieza) -> str:
    pieza = str(pieza)
    if pieza == str(ROJA) or pieza == FICHA_ROJA:
        return TEXTURA_ROJA
    elif pieza == str(NEUTRA_1) or pieza == str(NEUTRA_1_SUBITA) or pieza == FICHA_NEUTRA_1:
        return TEXTURA_NEUTRA
    elif pieza == str(AZUL) or pieza == FICHA_AZUL:
        return TEXTURA_AZUL
    elif pieza == str(NEUTRA_2) or pieza == str(NEUTRA_2_SUBITA) or pieza == FICHA_NEUTRA_2:
        return TEXTURA_NEUTRA
    else:
        return TEXTURA_VACIA

def show_tablero(tablero:list):
    print("--------------------------------")
    for fila in tablero:
        for columna in fila:
            print(columna, end=" ")
        print()
    print("--------------------------------")

def change_cuadro(tablero:list, coordenadas:list, pieza:int) -> list:
    fil = coordenadas[0]
    col = coordenadas[1]
    tablero[fil][col] = get_pieza(pieza)
    return tablero

def espejar(coordenadas_pieza):
    coordenadas_nuevas:list = []
    for coordenada in coordenadas_pieza:
        coordenadas_nuevas.append([coordenada[1], coordenada[0]])
    return rotar(coordenadas_nuevas)

def rotar(coordenadas_pieza):
    nuevas_coordenadas:list = []
    matrix:list = [[0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]
    for coord in coordenadas_pieza:
        matrix[coord[0]][coord[1]] = 1
    matrix = list(zip(*matrix[::-1]))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                nuevas_coordenadas.append([i,j])
    return nuevas_coordenadas

    


def move(coordenadas:dict, pieza:int, key:str) -> list:
    new_tablero:list = [
        ["x","x","x","x"],
        ["x","x","x","x"],
        ["x","x","x","x"],
        ["x","x","x","x"],
    ]
    mov_valido:bool = True
    # Obtengo coordenadas
    coordenadas_pieza:list = get_coordenadas(pieza, coordenadas)
    
    
    if key == 'w':
        for coordenada in coordenadas_pieza:
            if coordenada[0] - 1 < 0:
                mov_valido = False

        if mov_valido:
            for coordenada in coordenadas_pieza:
                coordenada[0] -= 1
    
    elif key == 'a':
        for coordenada in coordenadas_pieza:
            if coordenada[1] - 1 < 0:
                mov_valido = False
        if mov_valido:
            for coordenada in coordenadas_pieza:
                coordenada[1] -= 1  

    elif key == 's':
        for coordenada in coordenadas_pieza:
            if coordenada[0] + 1 >= LIMITE_TAMAÑO_TABLERO:
                mov_valido = False
        if mov_valido:
            for coordenada in coordenadas_pieza:
                coordenada[0] += 1

    elif key == 'd':
        for coordenada in coordenadas_pieza:
            if coordenada[1] + 1 >= LIMITE_TAMAÑO_TABLERO:
                mov_valido = False
        if mov_valido:
            for coordenada in coordenadas_pieza:
                coordenada[1] += 1
    elif key == 'e':
        coordenadas_pieza = espejar(coordenadas_pieza)
    elif key == 'r':
        coordenadas_pieza = rotar(coordenadas_pieza)
    

    for coordenada in coordenadas_pieza:
        new_tablero = change_cuadro(new_tablero, coordenada, pieza)
    print("Su movimiento")
    show_tablero(new_tablero)

    return coordenadas_pieza

def confirm_move(coordenadas:dict, coordenadas_nuevas:dict, turno:int) -> bool:
    validez:bool = True
    coordenadas_copy:dict = dict(coordenadas)
    pos_prev_pieza:list = []
    if turno == 1:
        pos_prev_pieza = coordenadas_copy.pop(FICHA_ROJA)
    elif turno == 2 or turno == 6:
        pos_prev_pieza = coordenadas_copy.pop(FICHA_NEUTRA_1)
    elif turno == 3:
        pos_prev_pieza = coordenadas_copy.pop(FICHA_AZUL)
    elif turno == 4 or turno == 5:
        pos_prev_pieza = coordenadas_copy.pop(FICHA_NEUTRA_2)
    

    if pos_prev_pieza == coordenadas_nuevas and (turno == ROJA or turno == AZUL):
        print("La pieza roja/azul no puede estar en la misma posicion que la anterior")
        validez = False
    for coords_viejas in coordenadas_copy.values():
        for coord_vieja in coords_viejas:
            if coord_vieja in coordenadas_nuevas:
                validez = False
    return validez

def show_turno(turno:int) -> None:
    if turno == ROJA:
        print("Turno del jugador rojo")
    elif turno == NEUTRA_1 or turno == NEUTRA_1_SUBITA:
        print("Turno del jugador rojo que mueva ficha neutra")
    elif turno == AZUL:
        print("Turno del jugador azul")
    elif turno == NEUTRA_2 or turno == NEUTRA_2_SUBITA:
        print("Turno del jugador azul que mueva ficha neutra")
    else:
        print("Error en el turno")

def cierre_matriz(tablero:list, cuadros_validos:str) -> list:
    fin:int = 0
    #veo condicion de victoria (por filas)
    for fila_i in range(len(tablero)):
        for col_i in range(len(tablero[fila_i])-2):
            if tablero[fila_i][col_i] in cuadros_validos and tablero[fila_i][col_i+1] in cuadros_validos and tablero[fila_i][col_i+2] in cuadros_validos:
                if fila_i+1 < LIMITE_TAMAÑO_TABLERO:
                    if tablero[fila_i+1][col_i] in cuadros_validos:
                        #print("salto 1a")
                        fin += 1
                    if tablero[fila_i+1][col_i+2] in cuadros_validos:
                        #print("salto 1b")
                        fin += 1
                if fila_i-1 >= 0:
                    if tablero[fila_i-1][col_i] in cuadros_validos:
                        #print("salto 2")
                        fin += 1
                    if tablero[fila_i-1][col_i+2] in cuadros_validos:
                        #print("salto 2b")
                        fin += 1

    return fin

def cierre (tablero:list, pieza:str) -> bool:
    
    cuadros_validos:list = [TEXTURA_VACIA, pieza]
    
    fin =+ cierre_matriz(tablero, cuadros_validos)
    
    t_tablero = list(zip(*tablero)) # transpongo la matriz
    
    fin += cierre_matriz(t_tablero, cuadros_validos)

    # si salta una vez es porque toma la pieza sin moverse, solo retorno False si salto 2 veces (osea que la pieza se puede mover a OTRA posicion)
    if fin > 1:
        return False # se puede seguir jugando
    else:
        if pieza == AZUL:
            print("EL JUADOR ROJO GANO")
        else:
            print("EL JUADOR AZUL GANO")

        return True # se termino el juego
        

def game(tablero:list, coordenadas:dict, start_player:int):

    turno:int = start_player # 1 = rojo, 2 = pieza neutra 3 = azul 4 = pieza neutra
    show_turno(turno)
    rondas:float = 0
    coordenadas_nuevas:dict = {}
    coordenadas_pre_move:dict = {}
    invalid_move:bool = True
    fin:bool = False
    while rondas < LIMITE_MOVIEMIENTOS and fin == False:
        if msvcrt.kbhit():
            if turno == ROJA or turno == AZUL:
                fin = cierre(tablero, get_pieza(turno))
            if fin == False:
                key = msvcrt.getch().decode('utf-8')
                if key == 'w' or key == 'a' or key == 's' or key == 'd' or key == 'e' or key == 'e' or key == 'r' or key == ' ':   
                    print("Presione ESPACIO para confirmar el movimiento")
                    coordenadas_pre_move = copy.deepcopy(coordenadas)
                    coordenadas_nuevas = move(coordenadas, turno, key)
                    while invalid_move: # mantengo el loop mientras el movimiento sea invalido
                        if msvcrt.kbhit():
                            key = msvcrt.getch().decode('utf-8')
                            
                            if key == ' ':
                                if confirm_move(coordenadas_pre_move,coordenadas_nuevas,turno): # si el movimiento es valido
                                    for coordenada in get_coordenadas(turno, coordenadas_pre_move):
                                        tablero = change_cuadro(tablero, coordenada, TEXTURA_VACIA)
                                    coordenadas = set_coordenadas(turno, coordenadas, coordenadas_nuevas)
                                    for coordenada in coordenadas_nuevas:
                                        tablero = change_cuadro(tablero, coordenada, turno)
                                    invalid_move = False # turno validado
                                    show_tablero(tablero)
                                else:
                                    print("Movimiento invalido, mire el tablero antes de confirmar")
                                    show_tablero(tablero)       
                            else:
                                coordenadas = set_coordenadas(turno, coordenadas, coordenadas_nuevas)
                                coordenadas_nuevas = move(coordenadas, turno, key)
                                print("Este es el tablero antes de el movimiento")
                                show_tablero(tablero)
                    invalid_move = True            
                else:
                    print("Movimiento invalido")
                

                if fin == False:
                    turno += 1
                    rondas = rondas + 1
                    if turno > CANT_FICHAS:  # solo hay 4 fichas
                        turno = 1
                    
                    show_turno(turno)

    if fin == False:
        print("MODO MUERTE SUBITA!")

    while fin == False:
        if msvcrt.kbhit():
            if turno == ROJA or turno == AZUL:
                fin = cierre(tablero, get_pieza(turno))
            if fin == False:
                key = msvcrt.getch().decode('utf-8')
                if key == 'w' or key == 'a' or key == 's' or key == 'd' or key == 'e' or key == 'e' or key == ' ':   
                    print("Presione ESPACIO para confirmar el movimiento")
                    coordenadas_pre_move = copy.deepcopy(coordenadas)
                    coordenadas_nuevas = move(coordenadas, turno, key)
                    while invalid_move: # mantengo el loop mientras el movimiento sea invalido
                        if msvcrt.kbhit():
                            key = msvcrt.getch().decode('utf-8')
                            
                            if key == ' ':
                                if confirm_move(coordenadas_pre_move,coordenadas_nuevas,turno): # si el movimiento es valido
                                    for coordenada in get_coordenadas(turno, coordenadas_pre_move):
                                        tablero = change_cuadro(tablero, coordenada, TEXTURA_VACIA)
                                    coordenadas = set_coordenadas(turno, coordenadas, coordenadas_nuevas)
                                    for coordenada in coordenadas_nuevas:
                                        tablero = change_cuadro(tablero, coordenada, turno)
                                    invalid_move = False # turno validado
                                    show_tablero(tablero)
                                else:
                                    print("Movimiento invalido, mire el tablero antes de confirmar")
                                    show_tablero(tablero)       
                            else:
                                coordenadas = set_coordenadas(turno, coordenadas, coordenadas_nuevas)
                                coordenadas_nuevas = move(coordenadas, turno, key)
                    invalid_move = True            
                else:
                    print("Movimiento invalido")
                
                # en muerte subita: ROJO -> NEUTRA -> NEUTRA -> AZUL -> NEUTRA -> NEUTRA -> ROJO

                if fin == False:
                    if turno == ROJA:
                        turno = NEUTRA_1
                    elif turno == NEUTRA_1:
                        turno = NEUTRA_1_SUBITA
                    elif turno == NEUTRA_1_SUBITA:
                        turno = AZUL
                    elif turno == AZUL:
                        turno = NEUTRA_2
                    elif turno == NEUTRA_2:
                        turno = NEUTRA_2_SUBITA
                    elif turno == NEUTRA_2_SUBITA:
                        turno = ROJA
                
                    show_turno(turno)

    if turno == ROJA:
        return FICHA_ROJA
    elif turno == AZUL:
        return FICHA_AZUL
            
def menu () -> int:
    print("1. Jugar")
    print("2. Mostrar Ranking")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def ranking(partidas_previas:dict) -> None:
    
    lista:list = list(sorted(partidas_previas.items(), key=lambda item: item[1]))
    print(lista)
    if len(lista) > 4:
        lista = lista[:4]
    for i in lista:
        print(i[0], ": ", i[1])

def pre_juego() -> list:
    coordenadas:dict = {
        FICHA_ROJA: [],
        FICHA_NEUTRA_1: [],
        FICHA_AZUL: [],
        FICHA_NEUTRA_2: [],
    }

    tablero_vacio:list = [
        ["x","x","x","x"],
        ["x","x","x","x"],
        ["x","x","x","x"],
        ["x","x","x","x"],
    ]
    print("A continuacion se muestra un tablero vacio: ")
    show_tablero(tablero_vacio)
    print("Piense en las coordenadas x como filas , y como columnas")
    print("Ejemplo la siguiente coordenada imprimiria el siguiente tablero:")
    print("Coordenadas: [[1,1][2,2]]")
    print("Tablero:")
    show_tablero([
        ["x","x","x","x"],
        ["x","0","x","x"],
        ["x","x","0","x"],
        ["x","x","x","x"],
    ])
    print("Ahora ingrese las coordenadas del jugador rojo ejemplo [[0,0], [0,1], [0,2], [1,2]]: ")
    coordenadas[FICHA_ROJA] = list(json.loads(input()))
    print("Ahora ingrese las coordenadas de su pieza neutra: ")
    coordenadas[FICHA_NEUTRA_1] = list(json.loads(input()))
    print("Ahora ingrese las coordenadas del jugador azul: ")
    coordenadas[FICHA_AZUL] = list(json.loads(input()))
    print("Ahora ingrese las coordenadas de su pieza neutra: ")
    coordenadas[FICHA_NEUTRA_2] = list(json.loads(input()))

    for key, valor in coordenadas.items():
        for cordenada in valor:
            tablero = change_cuadro(tablero_vacio, cordenada, key)
    
    return coordenadas, tablero

def main():

    partidas_previas:dict = {}
    tablero:list = [
        ["n","r","r","x"],
        ["x","b","r","x"],
        ["x","b","r","x"],
        ["x","b","b","n"],
    ]

    coordenadas:dict = {
        FICHA_ROJA: [[0,1],[0,2],[1,2],[2,2]],
        FICHA_NEUTRA_1: [[0,0]],
        FICHA_AZUL: [[1,1],[2,1],[3,1],[3,2]],
        FICHA_NEUTRA_2: [[3,3]],
    }
    print("Bienvenido al juego L, ingrese su nombre y recuerde el color asignado")
    opcion = menu()
    if opcion == 1:

        nombre_rojo:str = input("Ingrese el nombre del jugador rojo: ")
        nombre_azul:str = input("Ingrese el nombre del jugador azul: ")

        start_player = random.choice([1,3])
        opcion2 = input("1. Jugar con el tablero por defecto\n2. Jugar con un tablero personalizado\nIngrese una opcion: ")
        if opcion2 == 2:
            coordenadas, tablero = pre_juego()
        show_tablero(tablero)
        print("Mueva la ficha utilizando las teclas 'w', 'a', 's', 'd', 'r', 'e', 'r' y ESPACIO para confirmar el movieiento")
        ganador = game(tablero, coordenadas, start_player)
        if ganador == FICHA_ROJA:
            if nombre_rojo in partidas_previas.keys():
                partidas_previas[nombre_rojo] = partidas_previas[nombre_rojo] + 1
            else:
                partidas_previas[nombre_rojo] = 1
        elif ganador == FICHA_AZUL:
            if nombre_azul in partidas_previas.keys():
                partidas_previas[nombre_azul] = partidas_previas[nombre_azul] + 1
            else:
                partidas_previas[nombre_azul] = 1
        show_tablero(tablero)
    elif opcion == 2:
        ranking(partidas_previas)

main()