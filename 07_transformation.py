"""
name = 'Daniela'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

#Str a int
age = 12
print('Mi edad es ' + str(age))
print(f'Mi edad es {age}')

#int a str
age = input('escribe tu edad -> ')
print(type(age))
age = int(age)
age += 10
print(f'Tu  edad en 10 años sera {age}')
"""
name = input('Cual es tu nombre? ')
age = input('Cuantos años tienes? ')
ageActual = int(age) + 10
print(f'Tu nombre es {name} actualmente tienes {age} años y en 10 años tendras {ageActual} años')


name = 'Daniela'
print(name)
age = '26'
print(age)
ageActual = int(age) + 10
print(ageActual)


template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {ageActual} años"
print(template)