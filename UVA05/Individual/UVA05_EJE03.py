"""
 Una empresa aplica el siguiente procedimiento en la comercialización de sus productos: 

Aplica el precio base a la primera docena de unidades. 

Aplica un 10% de descuento a todas las unidades entre 13 y 100. 

Aplica un 25% de descuento a todas las unidades por encima de las 100. 

Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería: 

100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04 

Escribir un algoritmo que lea la cantidad solicitada de un producto y su precio base, y
muestre el valor total de la venta y el precio promedio por unidad.
El fin de carga se determina ingresando -1 como cantidad solicitada. 

Al finalizar informar: 

Cantidad de ventas realizadas total. 

Cantidad de ventas que se aplicaron un 10% de descuento. 

Cantidad de ventas que SOLO se aplicó el precio base, a los productos que no se le realizaron descuentos. 
"""
"""
Pseudocodigo: 
INICIALIZAR sales_total <- 0
INICIALIZAR sale_total <- 0
INICIALIZAR sales_total_discount_10 <- 0
INICIALIZAR sales_no_discount <- 0
INICIALIZAR product_price <- 0
INICIALIZAR product_qty <- 0
INICIALIZAR product_price_avg <- 0
INICIALIZAR message_error <- "Las cantidades y precios deben ser positiva"

LEER product_qty

MIENTRAS product_qty != -1 HACER
    LEER product_price
    SI product_price <= 0 O product_qty <= 0 ENTONCES
        MOSTRAR message_error
        ASIGNAR product_qty <- 0
        ASIGNAR product_price <- 0
    SINO
        SI product_qty > 100 ENTONCES
            ASIGNAR sale_total <- sale_total + (12 * product_price)
            ASIGNAR sale_total <- sale_total + (88 * product_price * 0.90)
            ASIGNAR sale_total <- sale_total + ((product_qty - 100) * product_price * 0.75)
            INCREMENTAR sales_total_discount_10
        SINO SI product_qty > 12 ENTONCES
            ASIGNAR sale_total <- sale_total + (12 * product_price)
            ASIGNAR sale_total <- sale_total + ((product_qty - 12) * product_price * 0.90)
            INCREMENTAR sales_total_discount_10
        SINO
            ASIGNAR sale_total <- sale_total + (product_qty * product_price)
            INCREMENTAR sales_no_discount
            INCREMENTAR sales_total
        FIN SI

        ASIGNAR product_price_avg <- sale_total / product_qty

        MOSTRAR "Valor Total de la Venta:" + sale_total
        MOSTRAR "Valor Promedio de Producto:" + product_price_avg
    FIN SI

    LEER product_qty
FIN MIENTRAS

MOSTRAR "Cantidad Total de Ventas Realizadas: " + sales_total
MOSTRAR "Cantidad Total de Ventas con 10% de descuento: " + sales_total_discount_10
MOSTRAR "Cantidad de Ventas sin descuento: " + sales_no_discount
"""

sales_total = 0
sale_total = 0
sales_total_discount_10 = 0
sales_no_discount = 0
product_price = 0
product_qty = 0
product_price_avg = 0 
message_error = "Las cantidades y precios deben ser positiva\n"

product_qty = int(input('Ingrese Cantidad de Productos (-1 para salir):\n'))


while product_qty != -1:
    product_price = float(input('Ingrese Precio de Producto (-1 para salir):\n'))
    if product_price <= 0 or product_qty <= 0:
        print(message_error)
        product_qty = 0 
        product_price = 0
    else:     
        if product_qty > 100:
            sale_total += 12 * product_price  
            sale_total += 88 * product_price * 0.90  
            sale_total += (product_qty - 100) * product_price * 0.75 
            sales_total_discount_10 += 1
        elif product_qty > 12:
            sale_total += 12 * product_price
            sale_total += (product_qty - 12) * product_price * 0.90
            sales_total_discount_10 += 1
        else:
            sale_total += product_qty * product_price
            sales_no_discount += 1
            sales_total += 1
    
        product_price_avg = sale_total / product_qty 
    
    print(f'Valor Total de la Venta:{sale_total}')
    print(f'Valor Promedio de Producto:{product_price_avg}')    
        
    product_qty = int(input('Ingrese Cantidad de Productos (-1 para salir):\n'))
    
print(f'Cantidad Total de Ventas Realizadas: {sales_total}')
print(f'Cantidad Total de Ventas con 10% de descuento: {sales_total_discount_10}')
print(f'Cantidad de Ventas sin descuento: {sales_no_discount}')





