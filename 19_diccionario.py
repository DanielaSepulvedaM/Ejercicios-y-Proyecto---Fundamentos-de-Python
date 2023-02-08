my_dict = {}#definir clave valor
print(type(my_dict))

#definir un diccionario
my_dict = {
    'avion': 'bla bla bla',
    'name': 'Nicolas',
    'last_name': 'Molina Monroy',
    'age': 87
}

print(my_dict)
#cuantos elementos ha en el diccionario
print(len(my_dict))

#leer diccionario
print(my_dict['age'])
print(my_dict['last_name'])
#otra forma de hacerlo
print(my_dict.get('un valor')) #si no se sabe cual es el dato es mejor usar el get

print('avion' in my_dict)
print('otroqueno' in my_dict)