"""
La universidad necesita un sistema para cargar las notas finales de los alumnos. 
Los datos para ingresar son: Legajo (número positivo), mes (solamente se aceptan los números 3, 6 y 12)
y nota (número entre 1 y 10). La carga de datos termina al ingresar -1 como legajo.
Validar los datos pedidos. Al finalizar, informar:  
Cantidad de alumnos que promocionaron la materia (nota 7 o más). 

Cantidad de alumnos que aprobaron (nota 4 o más). 

Porcentaje de alumnos reprobados. 

Promedio de notas obtenidas en el mes 6.
"""
"""
Pseudocodigo: 
INICIALIZAR promoted A 0
INICIALIZAR approved A 0 
INICIALIZAR failed A 0
INICIALIZAR sum_june A 0
INICIALIZAR grades_june A 0
INICIALIZAR avg_june A None
DEFINIR message_error COMO "Datos incorrectos\nLegajo debe ser positivo\nMes debe ser 3, 6 o 12\nNota debe ser entre 1 y 10\n"

LEER student_Id DESDE input('Ingrese Legajo (-1 para salir):\n')

MIENTRAS student_Id NO SEA -1 HACER:
    LEER month DESDE input('Ingrese Mes:\n')
    LEER grade DESDE input('Ingrese Nota:\n')

    SI student_Id <= 0 O month NO ESTÁ EN [3, 6, 12] O grade < 1 O grade > 10 ENTONCES:
        IMPRIMIR message_error
    SINO:
        SI month ES 6 ENTONCES:
            sum_june += grade
            grades_june += 1
        FIN SI
        
        SI grade < 4 ENTONCES:
            failed += 1
        SINO SI grade >= 4 Y grade < 7 ENTONCES:
            approved += 1
        SINO:
            promoted += 1
            approved += 1  # Los promocionados también son aprobados
        FIN SI
    FIN SI
    
    LEER student_Id DESDE input('Ingrese Legajo (-1 para salir):\n')
FIN MIENTRAS

SI grades_june > 0 ENTONCES:
    avg_june = sum_june / grades_june
SINO:
    avg_june = "No hubo notas en Junio"
FIN SI

total_students = promoted + approved + failed

SI total_students > 0 ENTONCES:
    failed_percentage = (failed / total_students) * 100
SINO:
    failed_percentage = 0
FIN SI

IMPRIMIR "Promocionados: ", promoted
IMPRIMIR "Aprobados: ", approved
IMPRIMIR "Reprobados: ", failed, " (", failed_percentage, "%)"
IMPRIMIR "Promedio de notas en Junio: ", avg_june
"""

promoted = 0
approved = 0 
failed = 0
sum_june = 0
grades_june = 0
avg_june = None
message_error = "Datos incorrectos\nLegajo debe ser positivo\nMes debe ser 3,6 o 12\nNote deb ser entre 1 y 10\n"


student_Id = int(input('Ingrese Legajo (-1 para salir):\n'))
while student_Id != -1:
    month = int(input('Ingrese Mes:\n'))
    grade = int(input('Ingrese Nota:\n'))
    if student_Id <= 0 or month not in[3,6,12] or grade < 1 or grade > 10:
        print(message_error)
    else:
        if month == 6:
            sum_june += grade
            grades_june += 1
        if grade < 4:
            failed += 1
        elif grade >= 4 and grade < 7:
            approved += 1
        else:
            promoted += 1
            approved += 1 
            
    student_Id = int(input('Ingrese Legajo (-1 para salir):\n'))

if grades_june > 0: 
    avg_june = sum_june / grades_june
else:
    avg_june = "No hubo notas en Junio"    
    
total_students = promoted + approved + failed

if total_students > 0:
    failed_percentage = (failed / total_students) * 100
else:
    failed_percentage = 0 
            

print(f'Promocionados: {promoted}')
print(f'Aprobados: {approved}')
print(f'Reprobados: {failed} ({failed_percentage:.2f}%)')
print(f'Promedio de notas en Junio: {avg_june}')

