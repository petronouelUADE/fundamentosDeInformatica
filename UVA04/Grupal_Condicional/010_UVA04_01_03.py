"""
Una remisería requiere un sistema que calcule el precio de un viaje 
a partir de la cantidad de km que desea recorrer el usuario.
Tiene la siguiente tarifa:  
Viaje mínimo $50 
Si recorre entre 0 y 10 km: $20/km 
Si recorre 10 km o más: $15/km 
""" 

"""
Pseudocodigo: 
INICIAR
    DEFINIR MINIMAL_FEE COMO 50
    DEFINIR SHORT_DISTANCE_FEE COMO 20
    DEFINIR LONG_DISTANCE_FEE COMO 15
    DEFINIR invoice COMO NULO

    LEER distanceKM COMO DECIMAL

    SI distanceKM ES MAYOR O IGUAL A 10 ENTONCES
        ASIGNAR invoice A distanceKM * LONG_DISTANCE_FEE
    SINO SI distanceKM ES MAYOR QUE 2.5 Y MENOR QUE 10 ENTONCES
        ASIGNAR invoice A distanceKM * SHORT_DISTANCE_FEE
    SINO SI distanceKM ES MAYOR O IGUAL A 0 Y MENOR O IGUAL A 2.5 ENTONCES
        ASIGNAR invoice A MINIMAL_FEE
    SINO
        IMPRIMIR "Distancia invalida"
    FIN SI

    SI invoice NO ES NULO ENTONCES
        IMPRIMIR "El Costo de servicio es: " + invoice
    FIN SI
FIN
"""
MINIMAL_FEE = 50
SHORT_DISTANCE_FEE = 20
LONTG_DISTANCE_FEE = 15
invoice = None

distanceKM = float(input("Ingrese la Distancia\n"))
if distanceKM >= 10:
    invoice = distanceKM * LONTG_DISTANCE_FEE
elif distanceKM > 2.5 and distanceKM < 10:
    invoice = distanceKM * SHORT_DISTANCE_FEE
elif distanceKM >= 0 and distanceKM <= 2.5:
    invoice = MINIMAL_FEE
else:
    print("Distancia invalida")
    
if invoice: print("El Costo de servicio es: ", invoice)   
    

