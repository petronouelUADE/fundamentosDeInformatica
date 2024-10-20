"""
Diseñar una función para mostrar un título filas de asteriscos, 
la longitud de la fila de asteriscos y el texto del título se recibe como parámetro.
Ejemplo: titulo(“Ejercicio 3”, 15) muestra:
*************** 

Ejercicio 3 

*************** 
"""
import math
import random
def title(text, asterixLenght):
    asterixs = "*" * asterixLenght
    return print(f"{asterixs}\n\n  {text}\n\n{asterixs}")




def sumar(numero):
    resultado = 0
    while numero > 0:
        digito = numero % 10
        numero = int(math.floor(numero)/10)
        resultado += digito
    return(resultado)

def extraer(numero,posicion):
    multiplicador = 1 if numero > 0 else -1
    result = 0
    cantDigitos = int(math.log10(abs(numero))) + 1
    
    if posicion < cantDigitos:
        for digito in range(0,posicion + 1):
            digito = numero % 10
            numero = int(math.floor(abs(numero))/10)
        result = digito    
    else:
        result = -1     
        
    if posicion == cantDigitos : result *= multiplicador 
    
    return(result)

def middleDigit(numero):
    numero = numero/100
    return  numero%10
    
          
def app():
    title("Sumar y Extraer", 40 )
    num = 1
    contador = 0
    while middleDigit(num) != 0:
        num = random.randint(10000,99999)
        print(f"Numero randomizado: {num}")
        print(f"La suma es {sumar(num)}")
        print(f"Extraemos posicion 3 : {extraer(num,3)}")
        contador +=1 
    print(f"Guankata El numero tiene un cero en el centro {num}")
    print(f"Se ejecuto {contador} veces hasta llegar al resultado")
    
app()    
    



    


