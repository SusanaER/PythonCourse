# List

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [15, 25, 44, 12, 12]

my_list.append("hola")

print(len(my_list))
print(my_list)

my_other_list = [22, 1.68, "Susana", "Esparza"]
print(my_other_list)
print(type(my_other_list))

print(my_list.count(12))
print(my_list[1])
print(my_list[5])
print(my_list[-3])
print(my_list[-1])
print(len(my_other_list))

# Asignar valores de listas en variables
age, height, name, surname = my_other_list
print(name)
print(age)
print(my_list + my_other_list)
print(type([1, 2, 3, 4]))
print(sum([1, 2, 3, 4, 5]) * sum([9, 8, 7, 6, 5]))

print("")

print(my_other_list)
my_other_list.append("final")       # Agrega elemento al final de la lista
print(my_other_list)

my_other_list.insert(2, "tele")     # Inserta a la lista el elemento en el indice indicado
print(my_other_list)                # y se recorren los demas valores de la lista

my_other_list.remove("tele")        # Elimina el primer elemento que cohencida en la lista
print(my_other_list)

del my_other_list[0]                # Elimina el elemento indicado de la lista
print(my_other_list)

my_other_list.reverse()             # Le da un giro a los elementos de la lista poniendo los primeros al ultimo
print(my_other_list)

#my_other_list.sort()               # Ordena los elementos de menor a mayor
#print(my_other_list)

print(my_other_list.pop())          # Elimina el último elemento de la lista
print(my_other_list)

my_pop_element = my_other_list.pop(2) # El pop también puene eliminar el elemento en el indice indicado
print(my_pop_element)


my_other_list.clear()               # Borra todos los elementos de la lista
print(my_other_list)

my_other_list = my_list.copy()
print(my_other_list)
print("")

# Cambiar valores de las listas

print(my_list)
my_list[1] = "cambio de valor"
print(my_list)


# Revanadas de listas
print(my_list[1:3])
print(my_list[0:4])
print(my_list[0:1])