"""
Desarrollar un programa que solicite ingresar tres números distintos, 
e indique por pantalla cuál de ellos es el menor número ingresado. 
Deberán verificar que los tres números ingresados sean distintos.   
""" 

"""
INICIAR
    DEFINIR smallest COMO NULO
    DEFINIR greatest COMO NULO
    LEER number_A COMO ENTERO
    LEER number_B COMO ENTERO
    LEER number_C COMO ENTERO

    SI number_A ES IGUAL A number_B Y number_B ES IGUAL A number_C ENTONCES
        ASIGNAR smallest A number_A
        IMPRIMIR "Los numeros son iguales"
    SINO
        SI number_B ES MENOR QUE number_A ENTONCES
            ASIGNAR smallest A number_B
        SINO
            ASIGNAR smallest A number_A
        FIN SI

        SI number_C ES MENOR QUE smallest ENTONCES
            ASIGNAR smallest A number_C
        FIN SI

        IMPRIMIR "El menor es: " + smallest
    FIN SI
FIN
"""
smallest = None
greatest = None
number_A = int(input("Ingrese Primer Numero:\n"))
number_B = int(input("Ingrese Segundo Numero:\n"))
number_C = int(input("Ingrese Tercer Numero\n"))

if(number_A == number_B == number_C):
    smallest == number_A
    print("Los numeros son iguales") 
else:   
    if number_B < number_A:
        smallest = number_B
    else:
        smallest = number_A
    if number_C < smallest:
        smallest = number_C
    print("El menor es: ",smallest)    

    
    
        

    

    

