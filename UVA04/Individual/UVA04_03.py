
"""
Crear un programa que pida un número de mes (ejemplo 4) y 
escriba el nombre del mes en letras ("abril"). 
Verificar que el mes sea válido e informar en caso de que no lo sea.      
"""
"""
Pseudocodigo:
INICIO
  Solicitar al usuario que ingrese el número del mes (month_digit)

  MIENTRAS month_digit sea menor o igual a 0 O mayor que 12 HACER
    Solicitar al usuario que ingrese un número de mes válido (1 a 12)
  FIN MIENTRAS

  HACER coincidir month_digit CON
    CASO 1: IMPRIMIR "Enero"
    CASO 2: IMPRIMIR "Febrero"
    CASO 3: IMPRIMIR "Marzo"
    CASO 4: IMPRIMIR "Abril"
    CASO 5: IMPRIMIR "Mayo"
    CASO 6: IMPRIMIR "Junio"
    CASO 7: IMPRIMIR "Julio"
    CASO 8: IMPRIMIR "Agosto"
    CASO 9: IMPRIMIR "Septiembre"
    CASO 10: IMPRIMIR "Octubre"
    CASO 11: IMPRIMIR "Noviembre"
    CASO 12: IMPRIMIR "Diciembre"
  FIN HACER COINCIDIR
FIN
"""
month_digit = int(input("Ingrese el numero del Mes\n"))

while month_digit <= 0 or month_digit > 12:
  month_digit = int(input("Ingrese Numero de Mes Valido (1 a 12)\n"))
match month_digit:
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4:
       print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")    
    case 10:
        print("Octubre")    
    case 11:
       print("Noviembre")    
    case 12:
        print("Diciembre")

      
    


