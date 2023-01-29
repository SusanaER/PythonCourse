# Loops 

# While

my_condition = 0

while my_condition < 10:
    if my_condition == 8:
        print("Igual a 8 se detiene la ejecución")
        break
    else:
        print(my_condition, "Diferente de 8")
    print("Valor", my_condition)
    my_condition += 1
else:
    print("Termina condition y entra al else")

print("//////////////////////////////////////////\n")

# For

my_list = [15, 25, 44, 12, 12]
print("         LIST")
for element in my_list:
    print(element)

my_tuple = (22, 1.68, "Susana", "Esparza")
print("         TUPLE")
for element in my_tuple:
    print(element)

my_set = {"Susana", "Esparza", 22}
print("         SET")
for element in my_set:
    print(element)

my_dict = {"Nombre" : "Susana", "Apellido" : "Esparza", "Edad" : 22, 1 : "Python"}
print("         DICT")
for element in my_dict:
    print(element)
    if(element == "Edad"):
        break
else:
    print("en el else del for")


print("         DICT")
for element in my_dict:
    print(element)
    if(element == "Edad"):
        continue
else:
    print("en el else del for")