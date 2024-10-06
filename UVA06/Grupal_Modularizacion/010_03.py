"""
Diseñar dos funciones llamadas descuento y recargo: ambas recibirán un precio y 
un porcentaje (número entero entre 1 y 30). La primera devolverá el precio con el
descuento aplicado, mientras que la segunda lo hará con el recargo aplicado.  
Desarrollar un programa principal que solicite precios hasta ingresar -1.
Además, deberá solicitar el tipo de operación: 1: Descuento y 
2: Recargo. Luego de cada ingreso deberá mostrar el precio con descuento o 
recargo de acuerdo a lo ingresado por el usuario. Validar que puedan ingresar 
solamente esas dos opciones. Mostrar la suma total de precios considerando todos 
los descuentos y recargos aplicados. 
"""
"""
INICIO función descuento(precio, porcentaje)
    RETORNAR precio - (precio * (porcentaje / 100))
FIN función

INICIO función recargo(precio, porcentaje)
    RETORNAR precio + (precio * (porcentaje / 100))
FIN función

INICIO función app
    operacion = LEER valor entero ("Ingrese 1 para aplicar descuento, 2 para aplicar recargo, o -1 para salir")
    monto_total = 0

    MIENTRAS operacion NO SEA IGUAL A -1 HACER
        SI operacion ES IGUAL A 1 O operacion ES IGUAL A 2 ENTONCES
            monto = LEER valor flotante ("Ingrese el monto")
            porcentaje = LEER valor entero ("Ingrese porcentaje (entre 1 y 30)")

            SI porcentaje ES MAYOR O IGUAL A 1 Y porcentaje ES MENOR O IGUAL A 30 ENTONCES
                SI operacion ES IGUAL A 1 ENTONCES
                    monto_final_item = LLAMAR función descuento(monto, porcentaje)
                    tipo_operacion = "Descuento"
                SINO SI operacion ES IGUAL A 2 ENTONCES
                    monto_final_item = LLAMAR función recargo(monto, porcentaje)
                    tipo_operacion = "Recargo"
                FIN SI

                IMPRIMIR "Monto ingresado: " + monto
                IMPRIMIR "Operación: " + tipo_operacion
                IMPRIMIR "Monto final con " + tipo_operacion + ": " + monto_final_item
                
                monto_total = monto_total + monto_final_item
            SINO
                IMPRIMIR "Porcentaje no válido. Debe estar entre 1 y 30."
            FIN SI
        SINO
            IMPRIMIR "Operación no válida. Solo se acepta 1 para descuento, 2 para recargo o -1 para salir."
        FIN SI

        operacion = LEER valor entero ("Ingrese 1 para aplicar descuento, 2 para aplicar recargo, o -1 para salir")
    FIN MIENTRAS

    IMPRIMIR "Monto total acumulado: " + monto_total
FIN función

LLAMAR función app
"""

def descuento(precio, porcentaje):
    return precio - (precio * (porcentaje / 100))

def recargo(precio, porcentaje):
    return precio + (precio * (porcentaje / 100))

def app():
    operacion = int(input("Ingrese 1 para aplicar descuento, 2 para aplicar recargo, o -1 para salir\n"))
    monto_total = 0

    while operacion != -1: 
        if operacion == 1 or operacion == 2:
            monto = float(input("Ingrese el monto\n"))
            porcentaje = int(input("Ingrese porcentaje (entre 1 y 30)\n"))

            if porcentaje >= 1 and porcentaje <= 30: 
                if operacion == 1:
                    monto_final_item = descuento(monto, porcentaje)
                    tipo_operacion = "Descuento"
                elif operacion == 2:
                    monto_final_item = recargo(monto, porcentaje)
                    tipo_operacion = "Recargo"

                print(f"Monto ingresado: {monto}")
                print(f"Operación: {tipo_operacion}")
                print(f"Monto final con {tipo_operacion}: {monto_final_item}")
                
                monto_total += monto_final_item  
            else:
                print("Porcentaje no válido. Debe estar entre 1 y 30.")
        else:
            print("Operación no válida. Solo se acepta 1 para descuento, 2 para recargo o -1 para salir.")

        
        operacion = int(input("Ingrese 1 para aplicar descuento, 2 para aplicar recargo, o -1 para salir\n"))

    print(f"Monto total acumulado: {monto_total}")

app()
