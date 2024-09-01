"""
Diseñar un programa que calcule y muestre el sueldo neto de un empleado en 
base a su sueldo básico y su antigüedad en años. 
Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año 
de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del 
bruto por cada año de antigüedad. También se le realizan los siguientes 
descuentos: Jubilación: 11%, Obra Social: 3%, Sindicato: 3%. 

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y 
estado civil (‘s’ o ‘c’). Se debe informar: (reemplazar los 9 por los valores 
que correspondan)

Estado Civil: Soltero/Casado  
"""
"""
Pseudocodigo:
"""
net_salary = None
single_tenure_increase = 0.05
married_tenure_increase = 0.07
retirement_tax = 0.11
union_tax = 0.03
insurance_tax = 0.03

basic_salary = float(input("Ingrese el Sueldo Base:\n"))
while basic_salary <= 0:
    basic_salary = float(input("Ingrese un Sueldo Base válido:\n"))

tenure = int(input("Ingresa Años de antigüedad:\n"))
while tenure < 0:
    tenure = int(input("Ingrese una antigüedad mayor o igual a 0:\n"))

marital_status = input("Indique estado Civil (s)Soltero | (c)Casado:\n")
while marital_status != "s" and marital_status != "c":
    marital_status = input('Ingrese "s" para Soltero y "c" para Casado\n')

if marital_status == "s":
    salary_increase = single_tenure_increase
    marital_status = "Soltero(a)"
else:
    salary_increase = married_tenure_increase
    marital_status = "Casado(a)"

gross_salary = basic_salary
for _ in range(tenure):
    gross_salary += gross_salary * salary_increase

retirement_discount = gross_salary * retirement_tax
insurance_discount = gross_salary * insurance_tax
union_discount = gross_salary * union_tax
net_salary = gross_salary - retirement_discount - union_discount - insurance_discount

print(f"Estado Civil: {marital_status}\n")
print(f"-Sueldo Básico: ${basic_salary:.2f} | Antigüedad: {tenure} Años | Importe Bruto: ${gross_salary:.2f}\n")
print(f"-Descuentos:\n")
print(f"--Jubilación:  -${retirement_discount:.2f}\n")
print(f"--Obra Social: -${insurance_discount:.2f}\n")
print(f"--Sindicato:   -${union_discount:.2f}\n")
print(f"Sueldo Neto:    ${net_salary:.2f}\n")