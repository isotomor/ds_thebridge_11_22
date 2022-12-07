import numpy as np
import random


def inicializar_tablero(tamaño=10):
    tablero = np.full((tamaño,tamaño), " ")
    return tablero

def colocar_barco(barco, tablero):
    for coordenada in barco:
        tablero[coordenada] = "O"
    return tablero 

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Has acertado")
        tablero[casilla] = "X"
    elif tablero[casilla] == " ":
        print("Hay fallado")
        tablero[casilla] = "-"
    return tablero

def generar_b_aleatorio(eslora):
    barco_random = []

    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    orien = random.choice(["Norte", "Sur", "Este", "Oeste"])
    barco_random.append((fila_random,columna_random))

    while len(barco_random) < eslora:
        if orien == "Norte":
            fila_random = fila_random - 1
        if orien == "Sur":
            fila_random = fila_random + 1
        if orien == "Este":
            columna_random = columna_random + 1
        if orien == "Oeste":
            columna_random = columna_random - 1

        barco_random.append((fila_random,columna_random))

    return barco_random