#Ingresar dos números enteros e indicar si son iguales o distintos. 
"""
Seudocodigo:
INICIAR
    LEER number_A COMO ENTERO
    LEER number_B COMO ENTERO

    SI number_A ES IGUAL A number_B ENTONCES
        IMPRIMIR "Los numeros son iguales"
    SINO
        IMPRIMIR "Los numeros no son iguales"
    FIN SI
FIN
"""

number_A = int(input("Ingrese el Primer numero\n"))
number_B = int(input("Ingrese el Segundo numero\n"))
if  number_A == number_B:
    print("Los numeros son iguales")
else:   
    print("Los numeros no son iguales")