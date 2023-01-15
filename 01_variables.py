string_variable = "Variable tipo string"
print(string_variable)

int_variable = 5
print(int_variable)

bool_variable = False
print(bool_variable)

#Concatenar variables
print(string_variable, int_variable, bool_variable)
print("Valor variable bool:", bool_variable)

#Convertir datos
print(type(int_variable))
int_to_string = str(int_variable)
print(type(int_to_string))

#Contar caracteres en un string
print(len(string_variable))

#Variables en una sola linea
#No es tan recomendable usar esta sintaxis
name, surname, alias, age = "Susana", "Esparza", "Ziwa", 22
print("Nombre:", name, surname,", Con una edad de:", age,", Le llaman:", alias)
print("Hola " + name + ".")

#inputs
"""
name = input('Cuál es tu nombre?')
age = input('Cuál es tu edad?')
print("El nuevo nombre es: ", name)
print("La nueva edad es: ", age)
"""

#Cambiar tipos
name = 123
age = "Delia"
print(name)
print(age)

#Se puede especificar el tipado pero se puede cambiar de tipo de dato
addres: str = "MI dirección"
addres = 32
print(type(addres))