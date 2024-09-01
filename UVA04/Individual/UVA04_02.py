
"""
Leer un número entero e imprimir un mensaje indicando si es par o impar.   
"""
"""
Pseudocodigo:
INICIO
  number = Solicitar al usuario que ingrese un número

  SI number % 2 es igual a 0 ENTONCES
    IMPRIMIR "Número es Par"
  SINO
    IMPRIMIR "Número es Impar"
  FIN SI
FIN
"""
number = int("Ingrese el Numero: ")
if number%2 == 0:
  print("Numero es Par")
else: print("Numero es Impar")

