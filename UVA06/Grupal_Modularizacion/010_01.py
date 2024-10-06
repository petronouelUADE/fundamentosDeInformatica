"""
Diseñar una función para mostrar como título filas de asteriscos; 
la longitud de la fila de asteriscos y el texto del título se recibe como parámetro.
Ejemplo: titulo(“Ejercicio 1”, 15) muestra:
""" 
def title(text, asterixLenght):
    asterixs = "*" * asterixLenght
    return print(f"{asterixs}\n\n  {text}\n\n{asterixs}")

title("Ejercicio 1", 15)