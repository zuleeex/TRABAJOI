
# 19. Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias
# del lenguaje que lo hagan de forma automática. Si le pasamos ’Hola mundo’ nos retornaría
# ’odnum aloH’

cadena = input("Ingresa una cadena de texto: ")
cadena_invertida = ""

for i in range(len(cadena) - 1, -1, -1):
    cadena_invertida += cadena[i]

print("Cadena invertida:", cadena_invertida)