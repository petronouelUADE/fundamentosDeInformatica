"""
Diseñar el algoritmo para resolver los siguientes problemas y escriba el programa correspondiente en lenguaje Python. 
Ingresar el monto de una factura y calcular el IVA (21%). 
"""
invoice_total = float(input("Ingrese monto de la Factura:\n"))

tax_iva = 21/100
invoice_iva = invoice_total * tax_iva
print("IVA:",invoice_iva)


