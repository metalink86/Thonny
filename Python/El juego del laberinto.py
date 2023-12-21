def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(" ".join(fila))

def encontrar_inicio_y_salida(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 'S':
                inicio = (i, j)
            elif laberinto[i][j] == 'E':
                salida = (i, j)
    return inicio, salida

def moverse(laberinto, posicion, direccion):
    fil, col = posicion
    if direccion == 'arriba' and fil > 0 and laberinto[fil - 1][col] != '#':
        return fil - 1, col
    elif direccion == 'abajo' and fil < len(laberinto) - 1 and laberinto[fil + 1][col] != '#':
        return fil + 1, col
    elif direccion == 'izquierda' and col > 0 and laberinto[fil][col - 1] != '#':
        return fil, col - 1
    elif direccion == 'derecha' and col < len(laberinto[fil]) - 1 and laberinto[fil][col + 1] != '#':
        return fil, col + 1
    else:
        return fil, col

def jugar_laberinto():
    laberinto = [
        ['S', '#', '.', '#', '#'],
        ['.', '.', '.', '#', '#'],
        ['#', '#', '.', '#', '#'],
        ['#', '#', '.', '#', '#'],
        ['.', '.', '.', '.', 'E']
    ]

    inicio, salida = encontrar_inicio_y_salida(laberinto)
    posicion_actual = inicio

    while posicion_actual != salida:
        imprimir_laberinto(laberinto)
        print(f"Tu posición actual es: {posicion_actual}")
        print("¿Hacia dónde quieres moverte? (arriba, abajo, izquierda, derecha)")
        direccion = input()

        posicion_actual = moverse(laberinto, posicion_actual, direccion)

    print("¡Felicidades, has llegado a la salida!")

if __name__ == "__main__":
    jugar_laberinto()