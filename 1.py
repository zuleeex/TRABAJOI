
# 4. Este programa solicita al usuario que ingrese dos números enteros.
# Luego, calcula el cociente y el resto de la división entera entre esos dos números.
# Finalmente, imprime el resultado en el formato: "<n> entre <m> da un cociente <c> y un resto <r>".


n = int(input("Introduce el dividendo : "))
m = int(input("Introduce el divisor : "))

cociente = n // m
resto = n % m

print(f"\nRESULTADO: \n"
      f"  Dividendo: {n}"
      f"  Divisor:   {m}\n"
      f"  Cociente:  {cociente}\n"
      f"  Resto:     {resto}\n")