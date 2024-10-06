"""
Una empresa factura a sus clientes el último día de cada mes. 
Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, 
tiene un descuento de $120 o del 2% de la factura, lo que resulte más conveniente para el cliente. 
Si paga en los siguientes 10 días del mes deberá pagar el importe original de la factura,
mientras que si paga después del día 20 deberá abonar una multa de $150 o del 10% de su factura, 
lo que resulte mayor. 
Escriba un algoritmo que lea el número del cliente y el total de la factura,
y emita un informe donde conste el número del cliente y los tres importes que podrá abonar según la fecha de pago.  
"""
"""
INICIALIZAR amount_discount <- 120
INICIALIZAR percentage_discount <- 0.02
INICIALIZAR calc_discount <- 0
INICIALIZAR amount_penalty <- 150
INICIALIZAR percentage_penalty <- 0.10
INICIALIZAR calc_penalty <- 0

LEER client_id
LEER invoice_total

MIENTRAS invoice_total <= 0 HACER
    MOSTRAR "Total de la factura debe ser positivo"
    LEER invoice_total
FIN MIENTRAS

CALCULAR calc_discount <- percentage_discount * invoice_total
CALCULAR calc_penalty <- percentage_penalty * invoice_total

SI calc_discount < amount_discount ENTONCES
    ASIGNAR discount <- amount_discount
SINO
    ASIGNAR discount <- calc_discount
FIN SI

SI calc_penalty < amount_penalty ENTONCES
    ASIGNAR penalty <- amount_penalty
SINO
    ASIGNAR penalty <- calc_penalty
FIN SI

ASIGNAR payment_early <- invoice_total - discount
ASIGNAR payment_overdue <- invoice_total + penalty

SI payment_early <= 0 ENTONCES
    ASIGNAR payment_early <- 0
FIN SI

MOSTRAR "ID de cliente: " + client_id
MOSTRAR "Pago Temprano (Primeros 10 días): " + payment_early
MOSTRAR "Pago Regular (Día 11 a 20 de mes): " + invoice_total
MOSTRAR "Pago Tardío (Día 21 a fin de mes): " + payment_overdue

"""


amount_discount = 120
percentage_discount = 0.02
calc_discount = 0
amount_penalty = 150
percentage_penalty = 0.10
calc_penalty = 0


client_id = input("Ingrese el ID del cliente:\n")
invoice_total = float(input("Ingrese el Total de la factura:\n"))

while invoice_total <= 0:
    print("Total de la factura debe ser positivo")
    invoice_total = float(input("Ingrese el Total de la factura:\n"))
    
calc_discount = percentage_discount * invoice_total
calc_penalty = percentage_penalty * invoice_total

if calc_discount < amount_discount:
    discount = amount_discount
else: 
      discount = calc_discount
if calc_penalty < amount_penalty:
     penalty  = amount_penalty
else: 
  penalty = calc_penalty
payment_early = invoice_total - discount
payment_overdue = invoice_total + penalty    

if payment_early <= 0: payment_early = 0

print(f"ID de cliente: {client_id}")
print(f"Pago Temprano (Primeros 10 dias): {payment_early}")
print(f"Pago Regular (Dia 11  a 20 de mes): {invoice_total}")
print(f"Pago Tardio (21  a fin de mes): {payment_overdue} ")





   
            
    


