"""
if True:
  print('deberia ejecutarse')

if False:
  print('nunca se ejecuta')

#Ejercicio de mascota interesante
pet = input('Cual es tu mascota favorita? ')

if pet == 'perro':
  print('genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo maximo')
else:
  print('no tienes una mascota interesante')

""" 
'''
#Ejercicio de Stock
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('El stock es incorrecto')
'''

#Reto 4: evaluar si un numero es par o impar 
num = int(input('Ingresa un numero => '))
print('*')
esPar = num % 2 
if(esPar == 0):
  print(f'El numero {num} es par')
else:
  print(f'El numero {num} es impar')
