"""
Una empresa cuenta con N empleados, divididos en tres categorías A, B y C.
Por cada empleado se lee su legajo, categoría y salario.
Se solicita elaborar un informe que contenga: 

Importe total de salarios pagados por la empresa. 
Cantidad de empleados que ganan más de $20000. 
Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”. 
Legajo del empleado que más gana. 
Sueldo más bajo. 
Importe total de sueldos por cada categoría. 
Salario promedio. 
"""
"""
Pseudocodigo: 
INICIALIZAR salaries_total <- 0
INICIALIZAR salaries_top_tier <- 0
INICIALIZAR salaries_bottom_tier <- 0
INICIALIZAR salary_highest <- 0
INICIALIZAR salary_lowest <- 0
INICIALIZAR cat_A_total_amount <- 0
INICIALIZAR cat_B_total_amount <- 0
INICIALIZAR cat_C_total_amount <- 0
INICIALIZAR salaries_avg <- NULO
INICIALIZAR id_highest_salary <- NULO

LEER employee_qty
MIENTRAS employee_qty <= 0 HACER
    MOSTRAR "Cantidad Inválida"
    LEER employee_qty
FIN MIENTRAS

PARA cada empleado DESDE 0 HASTA employee_qty - 1 HACER
    LEER employee_id
    LEER category
    MIENTRAS category NO SEA "A" Y NO SEA "B" Y NO SEA "C" HACER
        MOSTRAR "Categoría inválida"
        LEER category
    FIN MIENTRAS
    
    LEER salary
    MIENTRAS salary <= 0 HACER
        MOSTRAR "Cantidad inválida"
        LEER salary
    FIN MIENTRAS

    SI salary > 20000 ENTONCES
        INCREMENTAR salaries_top_tier EN 1
    FIN SI

    SI salary < 5000 Y category = "C" ENTONCES
        INCREMENTAR salaries_bottom_tier EN 1
    FIN SI

    SI employee_id = 0 ENTONCES
        ASIGNAR salary_highest <- salary
        ASIGNAR salary_lowest <- salary
    FIN SI

    SI salary < salary_lowest ENTONCES
        ASIGNAR salary_lowest <- salary
    FIN SI

    SI salary > salary_highest ENTONCES
        ASIGNAR salary_highest <- salary
        ASIGNAR id_highest_salary <- employee_id
    FIN SI

    INCREMENTAR salaries_total EN salary

    SEGÚN category HACER
        CASO "A":
            INCREMENTAR cat_A_total_amount EN salary
        CASO "B":
            INCREMENTAR cat_B_total_amount EN salary
        CASO "C":
            INCREMENTAR cat_C_total_amount EN salary
    FIN SEGÚN
FIN PARA

CALCULAR salaries_avg <- salaries_total / employee_qty

MOSTRAR "Cantidad de empleados que ganan más de $20000: " + salaries_top_tier
MOSTRAR "Cantidad de empleados que ganan menos de $5000 en categoría C: " + salaries_bottom_tier
MOSTRAR "Legajo del empleado que más gana: " + id_highest_salary
MOSTRAR "Total de sueldos en categoría A: " + cat_A_total_amount
MOSTRAR "Total de sueldos en categoría B: " + cat_B_total_amount
MOSTRAR "Total de sueldos en categoría C: " + cat_C_total_amount
MOSTRAR "Sueldo más bajo: " + salary_lowest
MOSTRAR "Salario promedio: " + salaries_avg
|
"""

salaries_total = 0
salaries_top_tier = 0 
salaries_bottom_tier = 0 
salary_highest = 0
salary_lowest = 0
cat_A_total_amount = 0
cat_B_total_amount = 0
cat_C_total_amount = 0

salaries_avg = None
id_highest_salary = None

employee_qty = int(input("Ingrese Cantidad de empleados\n"))
while employee_qty <= 0:   
    print("Cantidad Invalida")
    employee_qty = int("Ingrese Cantidad de empleados\n")
    
for salaries in range(employee_qty):
    employee_id = int(input("Ingrese Numero de legajo\n"))

    category = input("Ingrese Categoria A, B o C(Mayuscula)\n")
    while category not in ["A","B","C"]:
        category = input("Ingrese Categoria A, B o C(Mayuscula)\n")

    salary = int(input("Ingrese Salario\n"))
    while salary <= 0:
        print("Cantidad Invalida")
        salary = int(input("Ingrese un Importe Positivo"))
        
    if salary > 20000:
        salaries_top_tier += 1
        
    if salary < 5000 and category == "C":
        salaries_bottom_tier += 1
    
    if salaries == 0:
        salary_highest = salary
        salary_lowest = salary
             
    if salary_lowest > salary:
        salary_lowest = salary
        
    if salary_highest < salary:
        salary_highest = salary
        id_highest_salary = employee_id
            
    salaries_total += salary
    match category:
        case "A":
            cat_A_total_amount += salary
        case "B":
            cat_B_total_amount += salary   
        case "C":
            cat_C_total_amount += salary
salaries_avg = salaries_total / employee_qty
            
print(f"Cantidad de Empleados que ganan mas de $20000:{salaries_top_tier}")
print(f"Cantidad de Empleados que ganan menos de $5000 Categoria C:{salaries_bottom_tier}")
print(f"Legajo de Empleado que mas gana:{id_highest_salary}")
print(f"Total Categoria A:{cat_A_total_amount}")
print(f"Total Categoria B:{cat_B_total_amount}")
print(f"Total Categoria C:{cat_C_total_amount}")
print(f"Sueldo mas Bajo:{salary_lowest}")
print(f"Salario Promedio:{salaries_avg}")    
    


