
"""
Realicen un programa que permita leer por teclado N números.
Mostrar cuántos pares se ingresaron, el promedio de los números
impares y la suma de los números mayores a 10.     
"""
"""
Pseudocodigo:
INICIO
  evens = 0
  unEvens = 0
  unEvens_sum = 0
  avg_unEvens = 0
  big_sum = 0
  
  top = Solicitar al usuario cuántos dígitos va a ingresar

  PARA cada digits desde 0 hasta top - 1 HACER
    digit = Solicitar al usuario un valor decimal
    
    SI digits == 0 ENTONCES
      avg_unEvens = digit
    FIN SI
    
    SI digit % 2 == 0 ENTONCES
      evens = evens + 1
    SINO
      unEvens = unEvens + 1
      unEvens_sum = unEvens_sum + digit
      avg_unEvens = unEvens_sum / unEvens
    FIN SI
    
    SI digit > 10 ENTONCES
      big_sum = big_sum + digit
    FIN SI
  FIN PARA

  IMPRIMIR "Cantidad de Pares:" evens
  IMPRIMIR "Promedio Numeros Impares:" avg_unEvens
  IMPRIMIR "Suma de Numeros mayores a 10:" big_sum
FIN

"""
evens = unEvens = unEvens_sum = even_sum = big_sum = 0


top = int(input("\n-Indique cuantos digitos va a ingresar:"))
for digits in range(0,top):
  digit = float(input("Ingrese un Digito: "))
  if digits == 0: avg_unEvens = digit
  if digit%2 == 0:
    evens += 1
  else:
    unEvens += 1
    unEvens_sum += digit 
    avg_unEvens = unEvens_sum/unEvens
  if digit > 10:  
    big_sum += digit
    
print(f"-Cantidad de Pares:{evens}")
print(f"-Promedio Numeros Impares :{avg_unEvens}")
print(f"-Suma de Numeros mayores a 10 :{big_sum}")

      

    
     
    

    

         
    
    

