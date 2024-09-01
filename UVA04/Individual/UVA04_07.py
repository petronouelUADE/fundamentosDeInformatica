"""
Leer un número correspondiente a un año e imprimir un mensaje
indicando si es bisiesto o no. 
Se recuerda que un año es bisiesto cuando es divisible por 4.
Sin embargo, aquellos años que sean divisibles por 4 y 
también por 100 no son bisiestos, a menos que también sean 
divisibles por 400. Por ejemplo, 1900 no fue bisiesto, pero sí el 2000.     
"""
"""
Pseudocodigo:
INICIO
  Solicitar al usuario que ingrese un año (year)
  SI (year es divisible por 4 Y year no es divisible por 100) O (year es divisible por 400) ENTONCES
    IMPRIMIR "Es bisiesto"
  SINO
    IMPRIMIR "No es bisiesto"
  FIN SI
FIN
"""
year = int(input("Ingrese año:\n"))
if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 400 == 0:
    print("Es bisiesto")
else: print("No es bisiesto")
    
