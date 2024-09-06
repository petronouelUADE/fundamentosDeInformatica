"""
Desarrollar un programa para cargar 5 notas. Validar que se encuentren entre 1 y 10. 
Al finalizar, mostrar el promedio de las notas.  
"""
"""
Pseudocodigo:
INICIO
  Inicializar grades_sum en 0
  Inicializar grade en Ninguno

  PARA cada grades en el rango de 0 a 4 HACER
    Solicitar al usuario que ingrese una nota (grade)
    
    MIENTRAS grade sea menor que 1 o mayor que 10 HACER
      IMPRIMIR "Ingreso una nota no válida, intente de nuevo"
      Solicitar al usuario que ingrese una nota (grade)
    FIN MIENTRAS

    Sumar grade a grades_sum
  FIN PARA

  Calcular grades_avg como grades_sum dividido entre 5

  IMPRIMIR "El promedio es:", grades_avg
FIN
"""
grades_sum = 0 
grade = None
for grades in range(0,5):
    grade = int(input("Ingrese una nota:\n"))
    while grade < 1 or grade >10:
        print("Ingreso una nota no valida intente de nuevo:\n")
        grade = int(input("Ingrese una nota:\n"))
    grades_sum += grade
grades_avg = grades_sum/5
print("El promedio es : ",grades_avg )    