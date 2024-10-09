"""
Diseñar una función que reciba dos números enteros como parámetros enteros A y B,
y permita obtener AB mediante multiplicaciones sucesivas
Desarrollar un programa principal para generar N veces dos valores al azar 
en un rango desde-hasta ingresado por teclado y calcular AB, mostrar por pantalla 
los valores creados y el resultado de la operación. 
"""
import random
def multi(a,b):
    ab = a*b
    return ab

def app(n,min,max):
    result = 0
    for result in range(n):
     a = random.randint(min,max)
     b = random.randint(min,max)
     print(f"Valor a: {a}")
     print(f"Valor b: {b}")
     print(f"Resultado de {a} * {b}: {multi(a,b)}\n")


app(10,2,5)