# Conditionals

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")


my_condition = 5*2
if my_condition == 10:
    print("Si vale 10")

if my_condition >= 15:
    print("Si esta en el rango += 15")
else:
    print("Es menor a 10")

if my_condition <= 15:
    print("Si esta en el rango -= 15")
else:
    print("Es mayor a 15")

print("La ejecución continua")

if my_condition < 10 and my_condition > 5:
    print("Menor que 10 y mayor que 5")
elif my_condition == 10:
    print("El valor es igual a 10")


my_string = "Hola"

if my_string:
    print("No es vacio el string")

if my_string != "Holaa":
    print("Esta cadena no es Holaa")

if not my_string:
    print("ESTA VACIA")
elif my_string:
    print("NO VACIA")