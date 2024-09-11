
# 5. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la F y los hombres con
# un nombre posterior a la O y el grupo B por el resto. Escribir un programa que pregunte al
# usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingresa tu nombre: ").lower()
sexo = input("Ingresa tu sexo (M o F): ").upper()

if sexo not in ("M", "F"):
    print(" Debe ser 'M' o 'F'")
else:
    if sexo == "F":
        if nombre < "f":
            grupo = "A"
        else:
            grupo = "B"
    else: 
        if nombre > "o":
            grupo = "A"
        else:
            grupo = "B"

print(f"\nINFORMACION :\n"
          f"  Nombre: {nombre}\n"
          f"  Sexo: {sexo}\n"
          f"  Tu grupo es el {grupo}.")