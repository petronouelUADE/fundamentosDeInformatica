"""
Ingresar las notas de los dos parciales de un alumno e indicar si
promociona, aprueba o debe recuperar.
Si el valor de la nota no está entre 0 y 10, debe informar un error.  
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7. 
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4. 

Recupera cuando al menos una de las dos notas es menor a 4. 
""" 
partial_grade_A = float(input("Ingrese la Nota del Primer Parcial\n"))
partial_grade_B = float(input("Ingrese la Nota del Segundo Parcial\n"))
MIN_SCORE = 0
MAX_SCORE = 10
PROMOTION_SCORE = 7


if partial_grade_A > MAX_SCORE and partial_grade_A < MIN_SCORE or partial_grade_B > MAX_SCORE and partial_grade_B < MIN_SCORE:
    print("Una de las notas no es valida")
elif partial_grade_A >= PROMOTION_SCORE and partial_grade_B >= PROMOTION_SCORE:
    print("Aprueba Y Promociona")
elif partial_grade_A >= 4 and partial_grade_B >= 4:
    print("Aprobado")
else:
    print("Recupera")
    

    

