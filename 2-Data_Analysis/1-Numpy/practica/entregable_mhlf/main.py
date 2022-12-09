from functions import *

tablero = inicializar_tablero()
barco_aleatorio = generar_b_aleatorio(3)
tablero = colocar_barco(barco_aleatorio, tablero)
tablero = disparar((1,3), tablero)
tablero = disparar((1,4), tablero)
tablero = disparar((1,5), tablero)
tablero = disparar((1,6), tablero)
tablero = disparar((3,4), tablero)
print(tablero)