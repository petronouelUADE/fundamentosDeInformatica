"""
El Gran Prix está monitoreando varias carreras de Fórmula 1 en diferentes circuitos alrededor del mundo.
Se necesita un programa en Python que permita al usuario ingresar información sobre cada carrera: 
el nombre del circuito, la distancia en kilómetros del circuito y la velocidad promedio en kilómetros por hora de los autos participantes.
El programa calculará el tiempo que tardaría el ganador de cada carrera en regresar al punto de partida desde el circuito.
Después de ingresar los datos de una carrera, el programa preguntará al usuario si desea ingresar otra carrera. 
Si la respuesta no es 'Si' para continuar o 'No' para terminar, el programa mostrará un mensaje de advertencia y 
volverá a solicitar la entrada.

Al finalizar, el programa también deberá proporcionar la siguiente información:

•	La cantidad de carreras en las que la distancia desde el punto de partida supera los 100 kilómetros.
•	El circuito que tiene la menor cantidad de km en su recorrido, mostrando su nombre, tiempo estimado y cantidad de km de recorrido.
•	El total de carreras ingresadas para verificación.

Se requiere que el programa informe como comentarios lo que va realizando en cada paso que corresponda indicar y también un resumen de lo que realiza el programa explicando el paso a paso. Indicar también las variables utilizadas y de que tipo son.
"""
"""
INICIALIZAR circuit_name a  NULO
INICIALIZAR distance a 0
INICIALIZAR avg_speed a 0
INICIALIZAR lap_time a 0
INICIALIZAR races_total a 0
INICIALIZAR races_over_hundred_km a 0
INICIALIZAR race_shortest_distance a 0 
INICIALIZAR race_shortest_name a NULO
INICIALIZAR race_shortest_ETC a 0
INICIALIZAR option a NULO
INICIALIZAR winner_ETC a 0

LEER circuit_name
LEER distance
MIENTRAS distance <= 0 HACER
    LEER distance
    MOSTRAR "Error: La distancia debe ser positiva"
FIN MIENTRAS

LEER avg_speed
MIENTRAS avg_speed <= 0 HACER
    LEER avg_speed
    MOSTRAR "Error: La velocidad debe ser un valor positivo"
FIN MIENTRAS

ASIGNAR race_shortest_distance a distance
ASIGNAR race_shortest_ETC a avg_speed
ASIGNAR race_shortest_name a circuit_name

ASIGNAR races_total igual 1
ASIGNAR winner_ETC igual distance / avg_speed
MOSTRAR "El Ganador de la carrera" + circuit_name + " debe completar en menos de: " + winner_ETC

LEER option
MIENTRAS option != "Si" Y option != "No" HACER
    LEER option
    MOSTRAR "Error: Las opciones válidas son 'Si' o 'No'"
FIN MIENTRAS

MIENTRAS option = "Si" HACER
    LEER circuit_name
    LEER distance
    MIENTRAS distance <= 0 HACER
        LEER distance
        MOSTRAR "Error: La distancia debe ser positiva"
    FIN MIENTRAS

    LEER avg_speed
    MIENTRAS avg_speed <= 0 HACER
        LEER avg_speed
        MOSTRAR "Error: La velocidad debe ser un valor positivo"
    FIN MIENTRAS

    LEER option
    MIENTRAS option != "Si" Y option != "No" HACER
        LEER option
        MOSTRAR "Error: Las opciones válidas son 'Si' o 'No'"
    FIN MIENTRAS

    SI distance > 100 ENTONCES
        INCREMENTAR races_over_hundred_km EN 1
    FIN SI

    SI race_shortest_distance > distance ENTONCES
        ASIGNAR race_shortest_distance a distance
        ASIGNAR race_shortest_ETC a avg_speed
        ASIGNAR race_shortest_name a circuit_name
    FIN SI

    INCREMENTAR races_total EN 1
    MOSTRAR "El Ganador de la carrera" + circuit_name + " debe completar en menos de: " + winner_ETC
FIN MIENTRAS

MOSTRAR "Preparando Reporte..."
MOSTRAR "Reporte:"
MOSTRAR "Cantidad de Carreras que Superan 100KM: " + races_over_hundred_km
MOSTRAR "Datos de Carrera con menor Recorrido:"
MOSTRAR "-Nombre de Circuito: " + race_shortest_name
MOSTRAR "-Tiempo estimado Circuito con: " + race_short
"""
circuit_name = None
distance = 0
avg_speed = 0
lap_time = 0
races_total = 0
races_over_hundred_km = 0
race_shortest_distance = 0 
race_shortest_name = None
race_shortest_ETC = 0
option = None
winner_ETC = 0

circuit_name = input("Ingrese Nombre de la carrera:\n")

distance = float(input("Ingrese Distancia de la carrera:\n"))
while distance <= 0:
    distance = float(input("Error: La distancia debe ser positiva:\n"))

avg_speed = float(input("Ingrese Velocidad promedio:\n"))
while avg_speed <= 0:
    avg_speed = float(input("Error: La velocidad debe ser un valor positivo:\n"))

race_shortest_distance = distance
race_shortest_ETC = lap_time
race_shortest_name = circuit_name

races_total = 1
winner_ETC = distance / avg_speed 

print(f"El Ganador de la La carrera {circuit_name} debe completar en menos de: {winner_ETC}Hs")

option = input("Desea ingresar otra Carrera?\n")
while option != "Si" and option != "No":
    option = input('Error: Las Opciones Validas son "Si" o "No"\n')

while option == "Si":  
    circuit_name = input("Ingrese Nombre de la carrera:\n")

    distance = float(input("Ingrese Distancia de la carrera:\n"))
    while distance <= 0:
        distance = float(input("Error: La distancia debe ser positiva:\n"))

    avg_speed = float(input("Ingrese Velocidad promedio:\n"))
    while avg_speed <= 0:
     avg_speed = float(input("Error: La velocidad debe ser un valor positivo:\n"))
     
    option = input("Desea ingresar otra Carrera?\n") 
    while option != "Si" and option != "No":
        option = input('Error: Las Opciones Validas son "Si" o "No"\n')
    print("Validando si la carrera tiene mas de 100KM de recorrido...")
    if distance > 100:
     races_over_hundred_km +=1
    print("Validando si la carrera ingresada es la de menor  distancia...")
    if race_shortest_distance > distance:
        race_shortest_distance = distance
        race_shortest_ETC = avg_speed
        race_shortest_name = circuit_name 
    races_total += 1 
    print("Aumentando cantidad Valor de carreras ingresadas...")

    print(f"El Ganador de la La carrera {circuit_name} debe completar en menos de: {winner_ETC}Hs")    

print("Preparando Reporte...\n")
print("Reporte:")
print(f"Cantidad de Carreras que Superan 100KM: {races_over_hundred_km}")
print(f"Datos de Carrera con menor Recorrido:")
print(f"-Nombre de Circuito: {race_shortest_name}")
print(f"-Tiempo estimado Circuito con : {race_shortest_ETC}")
print(f"-Cantidad de KM: {race_shortest_distance}")
print(f"Total Cantidad de carreras Ingresadas: {races_total}")







 


