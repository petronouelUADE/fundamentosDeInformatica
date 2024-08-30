"""
Crear un programa que pida un número de día (ejemplo: 1) y
escriba el nombre del día en letras ("lunes"). Verificar que el día 
esté entre 1 y 7, e informar en caso de que no lo sea.  
"""
"""
Pseudocodigo:
INICIAR
    LEER day_digit COMO ENTERO
    
    SI day_digit ES IGUAL A 1 ENTONCES
        IMPRIMIR "El dia es LUNES"
    SINO SI day_digit ES IGUAL A 2 ENTONCES
        IMPRIMIR "El dia es MARTES"
    SINO SI day_digit ES IGUAL A 3 ENTONCES
        IMPRIMIR "El dia es MIERCOLES"
    SINO SI day_digit ES IGUAL A 4 ENTONCES
        IMPRIMIR "El dia es JUEVES"
    SINO SI day_digit ES IGUAL A 5 ENTONCES
        IMPRIMIR "El dia es VIERNES"
    SINO SI day_digit ES IGUAL A 6 ENTONCES
        IMPRIMIR "El dia es SABADO"
    SINO SI day_digit ES IGUAL A 7 ENTONCES
        IMPRIMIR "El dia es DOMINGO"
    SINO
        IMPRIMIR "El numero no es correcto"
    FIN SI
FIN
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
