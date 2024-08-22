"""
Un banco necesita para sus cajeros de la sucursal un programa 
que lea una cantidad de dinero que desea retirar el cliente e 
imprima a cuántos billetes equivale, considerando que existen 
billetes de $1000, $500, $200, $100, $50, $20 y el resto en monedas 
de $10, $5, $2 y $1. Desarrollar dicho programa de tal forma que se 
minimice la cantidad de billetes entregados por el cajero.   
"""
amount = int(input("Ingrese la cantidad a retirar:"))
bill_1000 = amount // 1000
amount = amount % 1000
bill_500 = amount // 500
amount = amount % 500
bill_200 = amount // 200
amount = amount % 200
bill_100 = amount // 100
amount = amount % 100
bill_50 = amount // 50
amount = amount % 50
bill_20 = amount // 20
amount = amount % 20
coin_10 = amount // 10
amount = amount % 10
coin_5 = amount // 5
amount = amount % 5
coin_2 = amount // 2
amount = amount % 2
coin_1 = amount

print("Billetes de 1000:",bill_1000)
print("Billetes de 500:",bill_500)
print("Billetes de 200::",bill_200)
print("Billetes de 50:",bill_50)
print("Billetes de 10:",bill_100)
print("Billetes de 20:",bill_20)
print("Monedas de 10:",coin_10)
print("Monedas de 5:",coin_5)
print("Monedas de 2:",coin_2)
print("Monedas de 1:",coin_1)







