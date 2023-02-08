numbers = (1, 2, 3, 5)#tupla de numeros viene dada por los parentesis
strings = ('nico', 'zule', 'santi')
print(numbers)
print('0 =>', numbers[0])
print('-1 ->', numbers[-1])
print(type(numbers))

print(strings)#tupa con diferentes tipos de datos
print(type(strings))

#en la tupla se crea y se asignan datos son inmutables no se pueden modificar, las tuplas solo son de lectura

#**METODOS DE LA TUPLA***
print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

#TRANSFORMACION 
mi_list = list(strings)
print(mi_list)
print(type(mi_list))

mi_list[1] = 'juli'
print(mi_list)

#lista a tupla
my_tuple = tuple(mi_list)
print(my_tuple)