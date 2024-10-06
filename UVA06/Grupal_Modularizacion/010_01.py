"""
Diseñar una función para mostrar como título filas de asteriscos; 
la longitud de la fila de asteriscos y el texto del título se recibe como parámetro.
Ejemplo: titulo(“Ejercicio 1”, 15) muestra:
""" 
"""
INICIO función title(texto, longitudAsteriscos)
    asteriscos = repetir_caracter('*', longitudAsteriscos)
    IMPRIMIR asteriscos
    IMPRIMIR salto_de_linea
    IMPRIMIR "  " + texto
    IMPRIMIR salto_de_linea
    IMPRIMIR asteriscos
FIN función

INICIO
    LLAMAR función title con argumentos ("Ejercicio 1", 15)
FIN
"""
def title(text, asterixLenght):
    asterixs = "*" * asterixLenght
    return print(f"{asterixs}\n\n  {text}\n\n{asterixs}")

title("Ejercicio 1", 15)