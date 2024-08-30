"""
Crear un programa que pida un número de día (ejemplo: 1) y
escriba el nombre del día en letras ("lunes"). Verificar que el día 
esté entre 1 y 7, e informar en caso de que no lo sea.  
"""
day_digit = int(input("Ingrese el numero del Dia\n"))
if day_digit == 1:
    print("El dia es LUNES")
elif(day_digit == 2):
    print("El dia es MARTES")
elif(day_digit == 3):
    print("El dia es MIERCOLES")
elif(day_digit == 4):
    print("El dia es JUEVES")
elif(day_digit == 5):
    print("El dia es VIERNES")
elif(day_digit == 6):
    print("El dia es SABADO")
elif(day_digit == 7):
    print("El dia es DOMINGO")
else:
    print("El numero no es correcto")
