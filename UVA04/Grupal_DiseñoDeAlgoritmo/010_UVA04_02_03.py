
"""
Realicen un programa que calcule la sumatoria de números
enteros ingresados por teclado, además de mostrar la cantidad 
de números ingresados. 
Finaliza el programa ingresando 0.
"""
"""
Pseudocodigo:
INICIAR
    DEFINIR number COMO NULO
    DEFINIR result COMO 0

    MIENTRAS number NO SEA IGUAL A 0 HACER
        LEER number COMO ENTERO
        SUMAR number A result
        IMPRIMIR "Resultado Sumatoria: " + result
    FIN MIENTRAS
FIN
"""
number = None
result = 0
while number != 0:
    number = int(input("Ingresa un numero:\n"))
    result= result + result
    print(f"Resultado Sumatoria: {result}")

