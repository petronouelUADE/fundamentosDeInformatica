
"""
Realicen un programa que permita leer por teclado N números.
Mostrar cuántos pares se ingresaron, el promedio de los números 
impares y la suma de los números mayores a 10.     
"""
"""
Pseudocodigo:
INICIO
  sum = 0
  greatest = Ninguno
  greatest_position = 1

  PARA cada digits desde 1 hasta 10 HACER
    IMPRIMIR "Digitos Ingresados:" (digits - 1)
    
    digit = Solicitar al usuario un valor decimal
    
    SI digits == 1 ENTONCES
      greatest = digit
    FIN SI
    
    SI digit > greatest ENTONCES
      greatest = digit
      greatest_position = digits
    FIN SI
    
    sum = sum + digit
    avg = sum / digits
    
    IMPRIMIR "Sumatoria:" sum " | Promedio:" avg
    IMPRIMIR "Mayor:" greatest " | Posicion:" greatest_position
  FIN PARA
FIN
"""

for digits in range(1,11):

    print(f"\n-Digitos Ingresados:{digits-1}")
    
    digit  = float(input(f"-Ingrese Digito:")) 
    
    if digits == 1: 
        greatest = digit 
        sum = 0
        greatest_position = 1
    if digit > greatest:
        greatest = digit
        greatest_position = digits
        
    sum += digit
    avg = sum/digits
        
    print(f"-Sumatoria:{sum} | Promedio: {avg}")
    print(f"-Mayor:{greatest}| Posicion: {greatest_position}\n")

         
    
    

