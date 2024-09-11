
# 16. Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

cesta = input('ESCRIBA LOS PRODUCTOS SEPARADOS POR COMAS: ')

print("-----------")
print(cesta.replace("," , "\n"))
print("-----------")