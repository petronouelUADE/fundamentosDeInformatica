"""
Diseñar el algoritmo para resolver los siguientes problemas y escriba el programa correspondiente en lenguaje Python. 
Ingresar tres números y mostrar la suma y el promedio. 
"""
first_number = float(input("Ingrese el primer numero:\n"))
second_number = float(input("Ingrese el segundo numero:\n"))
third_number = float(input("Ingrese el tercer numero:\n"))

add_result = first_number + second_number + third_number
avg_result = add_result / 3

print("Resultado de Suma:",add_result)
print("Resultado Promedio:",avg_result)


