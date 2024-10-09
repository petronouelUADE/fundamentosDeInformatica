"""
Diseñar una función para mostrar un título filas de asteriscos, 
la longitud de la fila de asteriscos y el texto del título se recibe como parámetro.
Ejemplo: titulo(“Ejercicio 3”, 15) muestra:
*************** 

Ejercicio 3 

*************** 
"""

def title(text, asterixLenght):
    asterixs = "*" * asterixLenght
    return print(f"{asterixs}\n\n  {text}\n\n{asterixs}")

title("Aprendiendo Funciones", 15)