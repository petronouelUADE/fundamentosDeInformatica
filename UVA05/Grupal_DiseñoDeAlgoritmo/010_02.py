"""
Un banco otorga a sus clientes una categoría de acuerdo al nivel de depósitos mensuales.
Desarrollar un programa que permita ingresar importes positivos hasta que se ingrese -1. 
Si la suma de esos importes es mayor a 1.000.000 la categoría será “Oro”, 
si está entre 500.000 y 1.000.000 la categoría será “Platino” y en el resto de los casos “Estándar”. 
Mostrar la categoría. Realizar la prueba de escritorio para comprobar el correcto funcionamiento del programa.  
"""
"""
Pseudocodigo:
INICIO
  Solicitar al usuario que ingrese un monto positivo o "-1" para salir (amount)
  Inicializar sum con el valor de amount

  MIENTRAS amount sea diferente de -1 HACER
    SI amount es menor que 0 ENTONCES
      IMPRIMIR "Ingreso un número negativo, intente de nuevo o -1 para salir del programa"
    SINO
      Sumar amount a sum
    FIN SI

    Solicitar al usuario que ingrese un monto positivo o "-1" para salir (amount)
  FIN MIENTRAS

  SI sum es mayor que 0 y menor que 500000 ENTONCES
    IMPRIMIR "Estandar"
  SINO SI sum es mayor o igual a 500000 y menor que 1000000 ENTONCES
    IMPRIMIR "Platino"
  SINO SI sum es mayor o igual a 1000000 ENTONCES
    IMPRIMIR "Gold"
  FIN SI
FIN
"""

amount = float(input('Ingrese un monto positivo, ingrese "-1" para salir del prograna\n'))
sum = amount
while amount != -1:
    if amount < 0:
        print('Ingreso un numero negativo, intente de nuevo o "-1" para salir del programa')
    else:
        sum += amount
    amount = float(input('Ingrese un monto positivo, ingrese "-1" para salir del prograna\n'))
    sum += amount
    
if sum > 0  and sum < 500000:
    print("Estandar")
elif sum >= 500000 and sum < 1000000:
    print("Platino")
elif sum >= 1000000: 
    print("Gold")  
 
    