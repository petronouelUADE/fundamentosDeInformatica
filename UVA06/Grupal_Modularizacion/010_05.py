"""
Desarrollar un programa que permita simular un juego de cartas. Las reglas son las siguientes: 
Las cartas pueden valer 1, 2 o 3, su valor se obtiene de forma aleatoria. 

Se pueden obtener 3 juegos: tres números iguales, tres números distintos o dos números iguales y uno distinto. 

Si se obtienen tres números iguales el jugador gana 10 puntos, si se obtienen tres números distintos el jugador 
gana 7 puntos y si se obtienen dos números iguales y uno distinto el jugador gana 4 puntos. 

Crear una sola función que retorne el puntaje de acuerdo a los valores de las cartas. 

Desarrollar un programa principal que permita simular 5 jugadas. En cada jugada deberá informar los números y 
el puntaje obtenido. Al finalizar mostrar el total de puntos acumulados. 
"""

"""
INICIO función obtener_puntaje(carta1, carta2, carta3)
    SI carta1 ES IGUAL A carta2 Y carta2 ES IGUAL A carta3 ENTONCES
        RETORNAR 10
    SINO SI carta1 ES DISTINTO A carta2 Y carta2 ES DISTINTO A carta3 Y carta3 ES DISTINTO A carta1 ENTONCES
        RETORNAR 7
    SINO
        RETORNAR 4
FIN función

INICIO función juego
    total_puntos = 0

    PARA jugada DESDE 1 HASTA 5 HACER
        carta1 = número aleatorio entre 1 y 3
        carta2 = número aleatorio entre 1 y 3
        carta3 = número aleatorio entre 1 y 3

        puntaje = LLAMAR obtener_puntaje(carta1, carta2, carta3)
        total_puntos = total_puntos + puntaje

        IMPRIMIR "Jugada " + jugada + ": Cartas = " + carta1 + ", " + carta2 + ", " + carta3 + " | Puntaje obtenido = " + puntaje
    FIN PARA

    IMPRIMIR "Total de puntos acumulados: " + total_puntos
FIN función

LLAMAR función juego

"""

import random

def obtener_puntaje(carta1, carta2, carta3):
    if carta1 == carta2 == carta3:
        return 10
    elif carta1 != carta2 != carta3 != carta1:  
        return 7
    else:
        return 4

def juego():
    total_puntos = 0

    for jugada in range(1, 6): 
        carta1 = random.randint(1, 3)
        carta2 = random.randint(1, 3)
        carta3 = random.randint(1, 3)

        puntaje = obtener_puntaje(carta1, carta2, carta3)
        total_puntos += puntaje

        print(f"Jugada {jugada}: Cartas = {carta1}, {carta2}, {carta3} | Puntaje obtenido = {puntaje}")
        
    print(f"\nTotal de puntos acumulados: {total_puntos}")

juego()
