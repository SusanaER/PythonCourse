# Tuples

# Las tuplas son un conjunto de valores

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.68, "Susana", "Esparza")
my_other_tuple = (22, 1.68, 1, 45, 7864)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Susana"))
print(my_tuple.index("Susana"))
print(my_tuple.index(22))

#my_tuple[0] = 45           #Las tuplas no pueden cambiar ya que son valores constantes
#print(my_tuple)

print(my_other_tuple)
print(my_other_tuple + my_tuple)
print(my_other_tuple[1:4])
print(my_other_tuple[0:2])

print(type(my_tuple))
my_tuple = list(my_tuple)
print(type(my_tuple))
print(my_tuple)
my_tuple[3] = "Teresa"
my_tuple.insert(1, "Morado")
print(tuple(my_tuple))

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined