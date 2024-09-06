"""
Leer números que representan edades de un grupo de personas, 
finalizando la lectura cuando se ingrese el número 999. 
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y
la cantidad de edades ingresadas. 
Descartar valores que no representan una edad válida (se considera válido una edad entre 0 y 100). 
Utilizar el depurador de Thonny para visualizar las variables y detectar posibles errores en tiempo de ejecución.  
"""
"""
INICIALIZAR underaged A 0
INICIALIZAR adults A 0
INICIALIZAR ages A 0

LEER age DESDE input('Ingrese edad o ingrese "999" para Salir del programa:')

MIENTRAS age NO SEA 999 HACER:
    SI age ES MAYOR O IGUAL A 0 Y age ES MENOR QUE 100 ENTONCES:
        INCREMENTAR ages EN 1
        SI age ES MENOR QUE 18 ENTONCES:
            INCREMENTAR underaged EN 1
        SINO:
            INCREMENTAR adults EN 1
        FIN SI
    SINO:
        ages SE MANTIENE IGUAL
    FIN SI
    
    LEER age DESDE input('Ingrese edad:')
FIN MIENTRAS

IMPRIMIR "Menores de 18: ", underaged
IMPRIMIR "Mayores de 18: ", adults
IMPRIMIR "Edades Ingresadas: ", ages
"""
underaged = 0
adults = 0
ages = 0

age = int(input('Ingrese edad o ingrese "999" para Salir del programa:\n'))
while age != 999:
    if age >= 0 and age < 100:
        ages+= 1
        if age <18: 
            underaged += 1
        else:  
            adults +=1
    else:
        ages = ages
    age = int(input("Ingrese edad:\n"))
print(f'Menores de 18:{underaged}\n')
print(f'Mayores de 18:{adults}\n')
print(f'Edades Ingresadas:{ages}\n')

