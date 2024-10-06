"""
Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y un número entero N que representa una cantidad de días. 
Realizar un programa que imprima la nueva fecha que resulta de sumar N días a la fecha dada. 
Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica de estructura condicional de la UVA 4. 
"""
"""
LEER day
LEER month
LEER year
LEER days

SI month < 1 O month > 12 O day < 1 O day > 31 O year < 0 ENTONCES
    MOSTRAR "Datos Invalidos"
SINO
    MIENTRAS days > 0 HACER
        SI (year % 4 = 0 Y year % 100 ≠ 0) O (year % 400 = 0) ENTONCES
            ASIGNAR february_days <- 29
        SINO
            ASIGNAR february_days <- 28
        FIN SI

        SI month = 1 O month = 3 O month = 5 O month = 7 O month = 8 O month = 10 O month = 12 ENTONCES
            ASIGNAR dias_en_mes <- 31
        SINO SI month = 4 O month = 6 O month = 9 O month = 11 ENTONCES
            ASIGNAR dias_en_mes <- 30
        SINO SI month = 2 ENTONCES
            ASIGNAR dias_en_mes <- february_days
        FIN SI

        SI day + days <= dias_en_mes ENTONCES
            ASIGNAR day <- day + days
            ASIGNAR days <- 0
        SINO
            ASIGNAR days <- days - (dias_en_mes - day + 1)
            ASIGNAR day <- 1
            ASIGNAR month <- month + 1

            SI month > 12 ENTONCES
                ASIGNAR month <- 1
                ASIGNAR year <- year + 1
            FIN SI
        FIN SI
    FIN MIENTRAS

    MOSTRAR "Nueva fecha: " + day + "-" + month + "-" + year
FIN SI

"""

day = int(input("Ingrese el día (D): "))
month = int(input("Ingrese el mes (M): "))
year = int(input("Ingrese el año (A): "))
days = int(input("Ingrese la cantidad de dias a sumar (N): "))

if month < 1 or month > 12 or day < 1 or day > 31 or year < 0:
    print("Datos Invalidos")
else:
    while days > 0:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            february_days = 29
        else:
            february_days = 28

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            dias_en_mes = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            dias_en_mes = 30
        elif month == 2:
            dias_en_mes = february_days

        if day + days <= dias_en_mes:
            day += days
            days = 0
        else:
            days -= (dias_en_mes - day + 1)  
            day = 1  
            month += 1
            
            if month > 12:
                month = 1
                year += 1
    print(f"Nueva fecha: {day}-{month}-{year}")
