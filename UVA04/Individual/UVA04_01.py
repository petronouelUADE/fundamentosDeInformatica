
"""
Ingresar dos números enteros e indicar si son iguales o distintos.       
"""
"""
Pseudocodigo:
INICIO
  number_A = Solicitar al usuario que ingrese el primer número
  number_B = Solicitar al usuario que ingrese el segundo número

  SI number_A es igual a number_B ENTONCES
    IMPRIMIR "Los números son iguales"
  SINO
    IMPRIMIR "Los números no son iguales"
  FIN SI
FIN
"""
number_A = int("Ingrese el Primer Numero: ")
number_B = int("Ingrese el Segundo Numero: ")

if(number_A == number_B):
  print("Los numero son iguales")
else: print("Los numeros no son iguales")

