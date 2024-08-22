#4.Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una. 
print("Ingrese el Capital Invertido Primer Socio ")
capitalInversionA = float(input())
print("Ingrese el Capital Invertido Segundo Socio ")
capitalInversionB = float(input())
print("Ingrese el Capital Invertido Tercer Socio ")
capitalInversionC = float(input())

capitalTotal = capitalInversionA + capitalInversionB + capitalInversionC
participacionA = capitalInversionA * 100 /capitalTotal
participacionB = capitalInversionB * 100 /capitalTotal
participacionC = capitalInversionC * 100 /capitalTotal

print("Porcentaje de Participacion Socio A: ", participacionA,"\n") 
print("Porcentaje de Participacion Socio B: ", participacionB,"\n")
print("Porcentaje de Participacion Socio C: ", participacionC)