"""
Utilizar la instrucción print para mostrar cada resultado de las siguientes expresiones. 
Explicar en un comentario de una sola línea el orden que ejecuta el intérprete Python en cada una de ellas. Ejemplo: 12*4+4*5 = 68 orden: multiplicación, suma: 
12 * 4 + 4 * 5 
Orden: Multiplicacion, suma
12 * (4 + 4) * 5 
Orden: Parentesis, multiplicacion
5 * 4 / 2 
Orden: Multiplicacion, division
5 * (4 / 2)  
Orden: Division, multiplicacion
(12 + (12 + 6 * 4)) / 3 
Orden: Parentesis Interno, Parentesis externo, Division
3 * ((4 + 5) / (18 / 6) - 4) 
Orden: Los dos Parentesis internos, Division Parentesis externo, Resta Parentesis, Multiplicacion
"""