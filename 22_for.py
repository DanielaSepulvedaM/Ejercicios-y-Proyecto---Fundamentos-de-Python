"""
for element in range(1,20):
    print(element)
"""

my_list = [23, 45, 67, 89, 43] 
for element in my_list:
    print(element)


#iterar una tupla
my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
    print(element)

#iterar un diccionario
producto = {
    'name':'camisa',
    'price':100,
    'stock':89
}

print('**********************OTROS EJEMPLOS*********************************')
#hizo una iteralcion solo de las llaves
for element in producto:
    print(producto[element])

for key in producto:
    print(key, '=>', producto[key])

print('**********************OTRA FORMA MAS SENCILLA*********************************')
for key, value in producto.items():
    print(key, '=>', value) 

print('**********************OTRA FORMA DE RECORRES DICCIONARIOS DE LISTAS*********************************')
people = [
    {
        'name':'nico',
        'age':34
    },
        {
        'name':'zule',
        'age':45
    },
        {
        'name':'santi',
        'age':4
    }
]
for person in people:
    print('name =>',person['name'])

#RETO 7
print('**********************RETO 7 *********************************')
my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []
for element in my_list:
    if element >= 0:
        new_list.append(element)
print(new_list)
