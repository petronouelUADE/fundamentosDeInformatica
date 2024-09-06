"""
Una mueblería necesita un sistema para ingresar 10 productos. 
Se pide ingresar categoría (A, B o C) y precio. 
Validar que el ingreso de la categoría sea de alguna de esas tres letras y que el precio sea positivo. 
Al finalizar, mostrar la cantidad de productos ingresados de cada categoría y el total de importes.  
"""
"""
Pseudocodigo:
INICIALIZAR category_A, category_B, category_C A 0
INICIALIZAR amount_cat_A, amount_cat_B, amount_cat_C A 0
DEFINIR message_category COMO "Ingrese Categoria de producto:"
DEFINIR message_amount COMO "Ingrese monto de producto:"
DEFINIR message_error COMO 'Datos incorrectos, el monto debe ser positivo, las categorías son "A", "B" o "C".'

PARA cada producto DESDE 0 HASTA 2 HACER:
    LEER category DESDE input(message_category)
    LEER amount DESDE input(message_amount)

    MIENTRAS category NO SEA "A" Y NO SEA "B" Y NO SEA "C" O amount < 0 HACER:
        IMPRIMIR message_error
        LEER category DESDE input(message_category)
        LEER amount DESDE input(message_amount)

    SI category ES "A" ENTONCES:
        INCREMENTAR category_A EN 1
        SUMAR amount A amount_cat_A
    SINO SI category ES "B" ENTONCES:
        INCREMENTAR category_B EN 1
        SUMAR amount A amount_cat_B
    SINO SI category ES "C" ENTONCES:
        INCREMENTAR category_C EN 1
        SUMAR amount A amount_cat_C
    FIN SI
FIN PARA

IMPRIMIR "Productos Categoria A: ", category_A, "Monto total: ", amount_cat_A
IMPRIMIR "Productos Categoria B: ", category_B, "Monto total: ", amount_cat_B
IMPRIMIR "Productos Categoria C: ", category_C, "Monto total: ", amount_cat_C

"""
category_A = 0
category_B = 0
category_C = 0
amount_cat_A = 0
amount_cat_B = 0
amount_cat_C = 0
message_category ="Ingrese Categoria de producto:\n"
message_amount = "Ingrese monto de producto:\n"
message_error = 'Datos incorrectos, el monto debe ser positivo, las categoriras son "A","B" o "C"\n'

for products in range(0,2):
    category = input(message_category)
    amount = int(input(message_amount))

    while category != "A" and category != "B" and category != "C" or amount < 0:
        print(message_error)
        category = input(message_category)
        amount = int(input(message_amount))    
    if category == "A": 
        category_A +=1
        amount_cat_A += amount
    elif category == "B":
        category_B +=1       
        amount_cat_B += amount
    elif category == "C":
        category_C += 1       
        amount_cat_C += amount
        
print(f"Productos Categoria A: {category_A} , Monto total:{amount_cat_A}")
print(f"Productos Categoria B: {category_B} , Monto total:{amount_cat_B}")
print(f"Productos Categoria C: {category_C} , Monto total:{amount_cat_C}")




