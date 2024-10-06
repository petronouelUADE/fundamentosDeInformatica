"""
Escribir la función obtener_mes_texto, que retorne una cadena que representa un mes
expresado en letras según un número entero entre 1 y 12 recibido como parámetro. 
Si el parámetro no es válido, devolver una cadena vacía. 
Ejemplo: se invoca obtener_mes_texto(4) → devuelve “Abril”.  
"""
"""
INICIO función obtener_mes_texto(mes)
    SI mes ES IGUAL A 1 ENTONCES
        IMPRIMIR "Enero"
    SINO SI mes ES IGUAL A 2 ENTONCES
        IMPRIMIR "Febrero"
    SINO SI mes ES IGUAL A 3 ENTONCES
        IMPRIMIR "Marzo"
    SINO SI mes ES IGUAL A 4 ENTONCES
        IMPRIMIR "Abril"
    SINO SI mes ES IGUAL A 5 ENTONCES
        IMPRIMIR "Mayo"
    SINO SI mes ES IGUAL A 6 ENTONCES
        IMPRIMIR "Junio"
    SINO SI mes ES IGUAL A 7 ENTONCES
        IMPRIMIR "Julio"
    SINO SI mes ES IGUAL A 8 ENTONCES
        IMPRIMIR "Agosto"
    SINO SI mes ES IGUAL A 9 ENTONCES
        IMPRIMIR "Septiembre"
    SINO SI mes ES IGUAL A 10 ENTONCES
        IMPRIMIR "Octubre"
    SINO SI mes ES IGUAL A 11 ENTONCES
        IMPRIMIR "Noviembre"
    SINO SI mes ES IGUAL A 12 ENTONCES
        IMPRIMIR "Diciembre"
    SINO
        RETORNAR vacío
FIN función

INICIO
    LLAMAR función obtener_mes_texto con argumento 2
FIN
"""

def obtener_mes_texto(mes):
    if mes == 1:
        return print("Enero")
    elif mes == 2:
        return print("Febrero")
    elif mes == 3:
        return print("Marzo")
    elif mes == 4:
        return print("Abril")
    elif mes == 5:
        return print("Mayo")
    elif mes == 6:
        return print("Junio")
    elif mes == 7:
        return print("Julio")
    elif mes == 8:
        return print("Agosto")
    elif mes == 9:
        return print("Septiembre")
    elif mes == 10:
        return print("Octubre")
    elif mes == 11:
        return print("Noviembe")
    elif mes == 12:
        return print("Diciembre")
    else:
        return "" 
    
obtener_mes_texto(2)    