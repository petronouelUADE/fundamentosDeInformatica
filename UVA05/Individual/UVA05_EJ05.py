"""
El factorial de un número entero N mayor que cero se define como el producto de todos los enteros X tales que 0 < X <= N.
Desarrollar un programa para calcular el factorial de un número dado hasta ingresar -1.
Deberán rechazarse las entradas inválidas (menores que 0). 

Al finalizar informar cuantas veces se calculó el factorial.  
"""
"""
Pseudocodigo: 
LEER number

MIENTRAS number != -1 HACER
    
    SI number < -1 ENTONCES
        MOSTRAR "Número Inválido, debe ingresar un entero positivo"
    SINO
        ASIGNAR factorial <- 1
        PARA numbers DESDE 1 HASTA number HACER
            ASIGNAR factorial <- factorial * numbers
        FIN PARA
        MOSTRAR "Factorial: " + factorial
    FIN SI
    
    LEER number
FIN MIENTRAS

"""

number = int(input("Ingrese un numero o -1 para salir del programa:\n"))

while number != -1:
    
    if(number < -1):
        print("Numero Invalido, debe ingresar un entero positivo")

    else:
        factorial = 1
        for numbers in range(1, number + 1):
            factorial *= numbers          
        print(f"Factorial: {factorial}")
             
    number = int(input("Ingrese un numero o -1 para salir del programa:\n"))    
        
