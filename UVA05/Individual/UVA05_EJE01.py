"""
Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. 
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100).  
"""
"""
Pseudocodigo: 
INICIALIZAR underaged = 0
INICIALIZAR adults = 0
INICIALIZAR underaged_sum = 0
INICIALIZAR adults_sum = 0

ESCRIBIR "Ingrese edad o ingrese 999 para salir del programa"
LEER age

MIENTRAS age != 999 HACER
    SI age >= 0 Y age < 100 ENTONCES
        SI age < 18 ENTONCES
            INCREMENTAR underaged EN 1
            SUMAR age A underaged_sum
        SINO
            INCREMENTAR adults EN 1
            SUMAR age A adults_sum
        FIN SI
    SINO
        ESCRIBIR "Edad no válida. Intente de nuevo."
    FIN SI
    ESCRIBIR "Ingrese edad o ingrese 999 para salir del programa"
    LEER age
FIN MIENTRAS

SI underaged > 0 ENTONCES
    underaged_avg = underaged_sum / underaged
SINO
    underaged_avg = 0
FIN SI

SI adults > 0 ENTONCES
    adults_avg = adults_sum / adults
SINO
    adults_avg = 0
FIN SI

ESCRIBIR "Menores de 18: ", underaged
ESCRIBIR "Promedio Menores de 18: ", underaged_avg
ESCRIBIR "Mayores de 18: ", adults
ESCRIBIR "Promedio 18 y mayores: ", adults_avg
"""
underaged = 0
adults = 0
underaged_sum = 0 
underaged_avg = 0
adults_sum = 0 
adults_avg = 0


age = int(input('Ingrese edad o ingrese "999" para Salir del programa:\n'))
while age != 999:
    if age >= 0 and age < 100:
        if age <18: 
            underaged += 1
            underaged_sum += age
        else:  
            adults +=1
            adults_sum += age
            
    else:
        print("Edad no válida. Intente de nuevo.")
        
    age = int(input("Ingrese edad o ingrese 999 para Salir del programa:\n"))
    
if underaged > 0:
    underaged_avg = underaged_sum / underaged
else:   
    underaged_avg = 0
if adults > 0:
    adults_avg = adults_sum / adults
else:
    adults_avg = 0
  
print(f'Menores de 18:{underaged}\n')
print(f'Promedio Menores de 18:{underaged_avg}\n')
print(f'Mayores de 18:{adults}\n')
print(f'Promedio 18 y mayores:{adults_avg}\n')
