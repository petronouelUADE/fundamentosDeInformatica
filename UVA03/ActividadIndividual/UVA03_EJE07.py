"""
Una inmobiliaria paga a sus vendedores un salario base, 
más una comisión fija por cada venta realizada, más el 5% del valor de
esas ventas. Realizar un programa que imprima el número del vendedor y
el salario que le corresponde en un determinado mes. Se leen por teclado
el número del vendedor, la cantidad de ventas que realizó y el valor total.   
"""
base_salary = 10000
sale_comission_fixed = 1
total_sales_comission_rate = 5/100

employee_number = int(input("Ingrese numero de Empleado\n"))
sales_qty = int(input("Ingrese cantidad de Ventas\n"))
sales_amount = float(input("Ingrese monto total de Ventas\n"))
salary = base_salary + sale_comission_fixed * sales_qty + total_sales_comission_rate * sales_amount

print(f"Numero de vendedor:{employee_number}\n")
print(f"Salario del Mes es:{salary}\n")







