
def title(text):
    asterixs = "*" * (len(text) + 4)
    return print(f"{asterixs}\n\n  {text}\n\n{asterixs}")

def esNat():
    numero =  float(input("Ingrese un numero natural: "))

    while numero <= 0  or numero / int(numero) != 1:
        numero = float(input("Ingrese un numero natural: "))
    
    return   int(numero)

def sumNat(n):
    return  n * (n + 1) // 2

def app():
    title("Ejercicio Numero Naturales")
    cant = int(input(f"Ingrese la cantidad de numeros naturales a sumar"))
    mayor = -1
    total = 0
    for _ in range(cant):
        numero = esNat()
        suma = sumNat(numero)
        
        print(f"Las suma de los primeros {numero} numeros naturales es: {suma}")
        
        if numero > mayor:
            mayor = numero
    total += 1
    
    print(f"\nSe ingresaron {total} valores.")
    print(f"El mayor valor ingresado fue: {mayor}")       

app()