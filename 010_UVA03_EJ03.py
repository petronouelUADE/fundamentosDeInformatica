#Ingresar el valor de un producto. Luego, calcular el IVA (21%) y obtener el total de la factura
print("Ingrese Valor del Producto: ")
precioProducto = float(input())
ivaProducto = float(precioProducto * 0.21)
totalFactura = precioProducto + ivaProducto
print("Total de Factura : ", totalFactura)