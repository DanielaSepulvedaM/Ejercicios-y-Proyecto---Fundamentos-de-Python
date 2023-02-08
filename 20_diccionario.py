
person = {
    'name': 'nico',
    'last_name':'molina',
    'langs': ['python', 'javascript'], #lista de lenguajes
    'age': 99
}

#Actualizar
print(person)
person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

#eliminar un elemento clave valor
del person['last_name'] #elimino el atributo 
person.pop('age')#otra forma de eliminar, se envio la llave del atributo
print(person)

#metodos 

#devulve en un array en pares de tuplas, sirve para iterar o recorrer un diccionario
print('items')
print(person.items())

#lista con las llaves q se usan
print('keys')
print(person.keys())

#retorna una lista de los valores
print('values')
print(person.values())




#Reto 6
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}
person['twitter'] = '@nicobytes' #Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
print(person)
print(type(person))
person['name'] = 'Felipe' #Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
del person['age'] #Eliminar el elemento del diccionario con la llave "age"
print(list(person.keys()))#Imprimir una lista con las llaves del diccionario.
print(list(person.values())) #Imprimir una lista con los valores del diccionario.

