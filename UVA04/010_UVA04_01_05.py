"""
Desarrollar un programa que solicite ingresar tres números distintos, 
e indique por pantalla cuál de ellos es el menor número ingresado. 
Deberán verificar que los tres números ingresados sean distintos.   
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

    
    
        

    

    

