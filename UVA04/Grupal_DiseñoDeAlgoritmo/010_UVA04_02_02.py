
"""
Mostrar las tablas de multiplicar (entre 1 y 10) del número 5. 
¿Cómo cambiarían el algoritmo para que el usuario pueda decidir 
la tabla de multiplicar a mostrar?  
"""
"""
Pseudocodigo:
INICIAR
    LEER number COMO ENTERO

    PARA i DESDE 1 HASTA 10 HACER
        IMPRIMIR number + " x " + i + " = " + (number * i)
    FIN PARA
FIN

"""
number = int(input("Ingrese un numero:"))
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

