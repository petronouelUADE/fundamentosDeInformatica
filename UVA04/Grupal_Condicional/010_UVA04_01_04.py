"""
Ingresar las notas de los dos parciales de un alumno e indicar si
promociona, aprueba o debe recuperar.
Si el valor de la nota no está entre 0 y 10, debe informar un error.  
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7. 
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4. 

Recupera cuando al menos una de las dos notas es menor a 4. 
""" 
"""
PSEUDOCODIGO: 
INICIAR
    LEER partial_grade_A COMO DECIMAL
    LEER partial_grade_B COMO DECIMAL
    DEFINIR MIN_SCORE COMO 0
    DEFINIR MAX_SCORE COMO 10
    DEFINIR PROMOTION_SCORE COMO 7

    SI (partial_grade_A ES MAYOR QUE MAX_SCORE O MENOR QUE MIN_SCORE) O (partial_grade_B ES MAYOR QUE MAX_SCORE O MENOR QUE MIN_SCORE) ENTONCES
        IMPRIMIR "Una de las notas no es valida"
    SINO SI partial_grade_A ES MAYOR O IGUAL A PROMOTION_SCORE Y partial_grade_B ES MAYOR O IGUAL A PROMOTION_SCORE ENTONCES
        IMPRIMIR "Aprueba Y Promociona"
    SINO SI partial_grade_A ES MAYOR O IGUAL A 4 Y partial_grade_B ES MAYOR O IGUAL A 4 ENTONCES
        IMPRIMIR "Aprobado"
    SINO
        IMPRIMIR "Recupera"
    FIN SI
FIN
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
    

    

