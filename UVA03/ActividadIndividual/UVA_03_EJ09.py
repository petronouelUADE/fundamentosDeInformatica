"""
Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.   
"""
seconds = int(input("Ingrese segundos:"))
seconds_calculated = seconds
days = seconds_calculated // 86400
seconds_calculated = seconds_calculated % 86400
hours = seconds_calculated // 3600
seconds_calculated = seconds_calculated % 3600
minutes = seconds_calculated // 60
seconds_calculated = seconds_calculated % 60

print(f"{seconds} segundos equivalen a {days} días, {hours} horas, {minutes} minutos y {seconds_calculated} segundos.")






