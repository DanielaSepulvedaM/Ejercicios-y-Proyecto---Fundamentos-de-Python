name = "Daniela"
last_name = "sepulveda"
age = '26'
country = "Colombia"

#format 1
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1',template)

#format 2
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name )
print('v2',template)

#format 3 -> la mas usada 
template = f"Hola, mi nombre es {name} {last_name} tengo {age} años y vivo en {country}"
print('v3',template)
