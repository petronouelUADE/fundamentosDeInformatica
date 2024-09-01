"""
Una editorial determina el precio de un libro según la cantidad 
de páginas que contiene. El costo básico del libro es de $500, 
más $20,20 por página con encuadernación rústica. 
Si el número de páginas supera las 300 la encuadernación debe ser en tela,
lo que incrementa el costo en $200. Además, si el número de páginas
sobrepasa las 600 se hace necesario un procedimiento especial de 
encuadernación que incrementa el costo en $336. 
Desarrollar un programa que calcule el costo de un libro dado el 
número de páginas.     
"""
"""
Pseudocodigo:
Inicializar book_cost en Ninguno
  Establecer page_cost en 20.20
  Establecer basic_cost en 500
  Establecer materials_fabric_cost en 200
  Establecer premium_process_cost en 336

  Solicitar al usuario que ingrese el número de páginas (pages)

  MIENTRAS pages sea menor o igual a 0 HACER
    Solicitar al usuario que ingrese un número de páginas positivo (pages)
  FIN MIENTRAS

  SI pages es menor o igual a 300 ENTONCES
    book_cost = basic_cost + pages * page_cost
  SINO SI pages es menor o igual a 600 ENTONCES
    book_cost = basic_cost + materials_fabric_cost + pages * page_cost
  SINO
    book_cost = basic_cost + materials_fabric_cost + premium_process_cost + pages * page_cost
  FIN SI

  IMPRIMIR "Costo del Libro:", book_cost
FIN
"""

book_cost = None
page_cost = 20.20
basic_cost = 500
materials_fabric_cost = 200
premium_process = 336

pages = int(input("Ingrese numero de paginas:\n"))

while pages <= 0: 
 pages = int(input("Ingrese numero de paginas Positivo:\n"))
 
if pages <= 300: 
    book_cost = basic_cost + pages * page_cost
elif pages <= 600:
    book_cost =   basic_cost + materials_fabric_cost + pages * page_cost
else: book_cost = basic_cost + materials_fabric_cost + premium_process + pages * page_cost      

print("Costo Libro: ", book_cost)

