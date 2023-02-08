text = 'Ella sabe programar en PYTHON'

print('JavaScript' in text)#valida si la palabra Java se incluye en el texto 

size = len(text) # cuenta longitud del texto
print(size)

print(text)
print(text.upper()) #pasa texto a mayusculo
print(text.lower()) #pasa texto a minuscula
print(text.count('a')) #cuenta las letras indicadas del texto
print(text.swapcase()) #invierte lo q esta en mayus a minus y al contrario
print(text.startswith('Ella')) #devuelve vlr booleano, si el texto contiene el texto indicado
print(text.endswith(''))
print(text.replace('python', 'Go')) #Remplaza el texto por otra palabra

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())#si el texto es un digito
print('398'.isdigit())#si el texto es un digito
