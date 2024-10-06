"""
Escribir un algoritmo que permita ingresar los números de legajo de los alumnos 
de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo. 
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. 
Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar: 

Cantidad de alumnos que aprobaron con nota mayor o igual a 4. 

Cantidad de alumnos que desaprobaron el examen. Nota menor a 4. 

Porcentaje de alumnos que están aplazados (tienen 1 en el examen). 
"""
"""
Pseudocodigo: 
INICIALIZAR approved = 0
INICIALIZAR failed = 0
INICIALIZAR failed_full = 0
INICIALIZAR total_students = 0
INICIALIZAR message_error = "Datos incorrectos. Legajo debe ser positivo. Nota debe ser entre 1 y 10."

ESCRIBIR "Ingrese Legajo (-1 para salir):"
LEER student_Id

MIENTRAS student_Id != -1 HACER
    ESCRIBIR "Ingrese Nota:"
    LEER grade
    
    SI student_Id <= 0 O grade < 1 O grade > 10 ENTONCES
        ESCRIBIR message_error
    SINO
        INCREMENTAR total_students EN 1
        
        SI grade < 4 ENTONCES
            SI grade == 1 ENTONCES
                INCREMENTAR failed_full EN 1
            FIN SI
            INCREMENTAR failed EN 1
        SINO
            INCREMENTAR approved EN 1
        FIN SI
    FIN SI

    ESCRIBIR "Ingrese Legajo (-1 para salir):"
    LEER student_Id
FIN MIENTRAS

SI total_students > 0 ENTONCES
    failed_full_percentage = (failed_full / total_students) * 100
SINO
    failed_full_percentage = 0
FIN SI

ESCRIBIR "Aprobados: ", approved
ESCRIBIR "Reprobados: ", failed
ESCRIBIR "Aplazados (nota 1): ", failed_full
ESCRIBIR "Porcentaje de aplazados: ", failed_full_percentage
"""

approved = 0 
failed = 0
failed_full = 0
total_students = 0
message_error = "Datos incorrectos\nLegajo debe ser positivo\nNota debe ser entre 1 y 10\n"

student_Id = int(input('Ingrese Legajo (-1 para salir):\n'))
while student_Id != -1:
    grade = int(input('Ingrese Nota:\n'))
    if student_Id <= 0 or grade < 1 or grade > 10:
        print(message_error)
    else:
        total_students += 1
        if grade < 4:
            if grade == 1:
                failed_full += 1 
            failed += 1    
        else:
            approved += 1  
    student_Id = int(input('Ingrese Legajo (-1 para salir):\n'))

if total_students > 0:
    failed_full_percentage = (failed_full / total_students) * 100
else:
    failed_full_percentage = 0

print(f'Aprobados: {approved}')
print(f'Reprobados: {failed}')
print(f'Aplazados (nota 1): {failed_full}')
print(f'Porcentaje de aplazados: {failed_full_percentage:.2f}%')
