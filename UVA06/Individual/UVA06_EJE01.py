"""
Diseñar una función que reciba dos parámetros numéricos enteros, 
calcule y devuelva el resultado de la multiplicación de ambos utilizando sólo sumas.  
"""

def multiSuma (a,b):
    result = 0
    multiplicator = 1
    if b < 0:
        multiplicator = -1  
    for num in range(abs(b)):
        result += a
    return result * multiplicator
print(multiSuma(-2,0))