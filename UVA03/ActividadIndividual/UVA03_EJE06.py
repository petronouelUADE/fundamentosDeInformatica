"""Leer una medida en metros e imprimir esta medida expresada en 
centímetros, pulgadas, pies y yardas. Los factores de conversión son:  
"""
#Se decidio usar tabla de conversion directa de metros a otras unidades mas simple de leer y comprender
quantity_mts = float(input("Ingrese Metros:\n"))
quantity_cms = quantity_mts * 100
quantity_ins = quantity_mts * 39.3701
quantity_fts = quantity_mts * 3.28084
quantity_yds = quantity_mts * 1.09361

print(f"La Medida {quantity_mts}mts equivale a: {quantity_cms:.2f} Centimetros\n")
print(f"La Medida {quantity_mts}mts equivale a: {quantity_ins:.2f} Pulgadas\n")
print(f"La Medida {quantity_mts}mts equivale a: {quantity_fts:.2f} Pies\n")
print(f"La Medida {quantity_mts}mts equivale a: {quantity_yds:.2f} Yardas\n")






