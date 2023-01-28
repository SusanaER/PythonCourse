# Sets
# Los sets no son una estructura ordenada
# Cada vez que se manda a inprimir un set puede mostrar los datos en distintas posiciones
# La forma de ordenar los datos es por medio de un hash interno


my_set = set()
my_other_set = {}
                                # Reultado en consola
print(type(my_set))             # set
print(type(my_other_set))       # dict

my_other_set = {"Susana", "Esparza", 22}
print(type(my_other_set))       # set

print(len(my_other_set))        # 3

print(my_other_set)             # {'Esparza', 'Susana', 22}
my_other_set.add("Ziwa")
print(my_other_set)             # {'Esparza', 'Susana', 'Ziwa', 22}
my_other_set.add("Ziwa")
print(my_other_set)             # {'Susana', 'Ziwa', 'Esparza', 22}         ||      UN SET NO ADMITE REPETIDOS
my_other_set.add("Viernes")
print(my_other_set)             # {'Ziwa', 'Esparza', 'Viernes', 'Susana', 22}


print("Ziwa" in my_other_set)   # true
print("Tom" in my_other_set)    # false                                     ||      Esta estructura nos permite realizar busquedas en los sets

my_other_set.remove("Ziwa")
print(my_other_set)             # {'Susana', 'Viernes', 'Esparza', 22}

my_other_set.discard(22)
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))        # 0

del my_other_set                # BORRA COMPLETAMENTE LA VARIABLE


my_set = {"Susana", "Esparza", 22}
my_other_set = {"C#", "JAVA", "Python", 22}

my_new_set = my_set.union(my_other_set)
print(my_new_set)               # Se hace la unión de diferentes sets los datos que esten dobles solo se agregan una vez

print(my_new_set.union(my_new_set).union(my_set).union({"Javascript", "Kotlin"})) 

print(my_new_set.difference(my_set))        # Solo muestra los elementos que no se contiene dentro del otro set