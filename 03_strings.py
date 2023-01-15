# String

my_string = "My string"
my_other_string = "My other string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

#\n caracter especial
my_new_line_string = "String con \nsalto de linea"
print(my_new_line_string)

#\t caracter especial
my_tab_string = "String con \t tabulacion"
print(my_tab_string)

#escapar caracteres especiales con doble \\
print("\\t tabulacion \\n salto de linea")

# Formateo
name, surname, age = "Susana", "Esparza", 22
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s quisiera tener %d"%(name, surname, age, 54))

# Inferencia de datos
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# Division
language_slice = language[2:5]
print(language_slice)

language_slice = language[2:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

print(" ")
# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("5".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))
print(language.startswith("Py"))