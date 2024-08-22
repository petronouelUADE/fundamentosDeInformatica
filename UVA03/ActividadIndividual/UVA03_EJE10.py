"""
Escribir un programa para convertir un número binario de 4 
cifras en un número decimal.
Se ingresa como un solo número entero de cuatro dígitos. 
"""
binary_digits = input("Ingrese Numero binario: ")
binary_index_3 = int(binary_digits[0]) * 2**3
binary_index_2 = int(binary_digits[1]) * 2**2
binary_index_1 = int(binary_digits[2]) * 2**1
binary_index_0 = int(binary_digits[3]) * 2**0

print(binary_index_3 + binary_index_2 +binary_index_1 + binary_index_0 )










