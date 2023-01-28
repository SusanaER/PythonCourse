# Dictionaries
# Su estructura nos sirve para relacionar datos

my_dict = dict()
my_other_dict = {}

print(type(my_dict))                                # dict
print(type(my_other_dict))                          # dict

my_other_dict = {"Nombre" : "Susana", "Apellido" : "Esparza", "Edad" : 22, 1 : "Python"}

print(my_other_dict)

my_dict = {
        "Nombre" : "Susana",
        "Apellido" : "Esparza",
        "Edad" : 22,
        "Lenguajes" : {"Python", "C#", "Java"},
        1 : 1564.4165
    }

print(my_dict)
print(len(my_dict))
print(len(my_other_dict))

print(my_other_dict["Nombre"])
my_other_dict["Nombre"] = "Myriam"
print(my_other_dict["Nombre"])

my_other_dict["Calle"] = "Av. Sur America"
print(my_other_dict)

del my_other_dict["Calle"]
print(my_other_dict)

print("Susana" in my_other_dict)
print("Tom" in my_other_dict) 
print("Nombre" in my_other_dict)                # En este caso lo busca por el indicador no por el valor

print(my_other_dict.items())                    # Listado de cada uno de los items
print(my_other_dict.keys())                     # Nos muestra los identificadores con los que se cuenta
print(my_other_dict.values())                   # Los valores sin identificadores

my_list = ["Nombre", 1]

my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
my_new_dict = dict.fromkeys(my_list)      # También se puede crear con la palabra reservada dict
print(my_new_dict)                              # Se creo un diccionario nuevo pero que no tiene valores

my_new_dict["Terreno"] = "La Loma"
print(my_new_dict) 

my_new_dict = dict.fromkeys(my_new_dict, ("Montaña", "Azul"))
print(my_new_dict) 