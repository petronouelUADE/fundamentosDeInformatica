"""Una persona quiere invertir su capital en un banco y
 quiere saber cuánto dinero gana en un mes si el banco paga 2% mensual. 
 ¿Cuánto ganará en seis meses si deja su dinero invertido?    
"""
#Para este programa se ASUMIO que el interes siempre sera sobre el capital inicial
capital = float(input("Ingrese el Capital a Invertir:\n"))
periodo = int(input("Ingrese el periodo de inversion:\n"))
interes = 2/100
retorno_inversion_mensual = capital*interes
capital += retorno_inversion_mensual * periodo
print(f"El Capital despues de {periodo} meses es:  {capital:.2f}")




