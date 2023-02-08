"""
lives = 3
print(type(lives))

temperature = 12.12
print(type(temperature))

lives = 12 +15
print(lives)

lives = lives -1
print(lives)

lives -= 1
print(lives)

number = 45000000000000000000.1
print(number)
"""

#Reto: calcula el promedio segun presupuesto de cada mes
budget_january = int(input("Ingresa el presupuesto de enero: "))
budget_february = int(input("Ingresa el presupuesto de febrero: "))
budget_march = int(input("Ingresa el presupuesto de marzo: "))
total = budget_january + budget_february + budget_march
print('--> Tu presupuesto total es de  -> '+ str(total))
prom = total / 3
print('--> El promedio del presupuesto es -> '+ str(prom))
