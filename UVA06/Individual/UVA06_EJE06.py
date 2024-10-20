


def title(text):
    asterixs = "*" * (len(text) + 4)
    return print(f"{asterixs}\n\n  {text}\n\n{asterixs}")


# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números por restas sucesivas
def division_por_resta_sucesiva(dividendo, divisor):
    if divisor == 0:
        raise ValueError("¡No se puede dividir por cero! 👑")

    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1

    residuo = dividendo
    return cociente, residuo

# Función para mostrar el menú y realizar la operación elegida
def mostrar_menu():
    opcion = -1
    while opcion !=5:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir por restas sucesivas")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            break

        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = sumar(a, b)
            print(f"Resultado: {a} + {b} = {resultado}")

        elif opcion == "2":
            resultado = restar(a, b)
            print(f"Resultado: {a} - {b} = {resultado}")

        elif opcion == "3":
            resultado = multiplicar(a, b)
            print(f"Resultado: {a} * {b} = {resultado}")

        elif opcion == "4":
            try:
                cociente, residuo = division_por_resta_sucesiva(int(a), int(b))
                print(f"Resultado: Cociente = {cociente}, Residuo = {residuo}")
            except ValueError as e:
                print(e)

        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

def app():
    title("Ejercicio Calculadora")
    mostrar_menu()

app()    