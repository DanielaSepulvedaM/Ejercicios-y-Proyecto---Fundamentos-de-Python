#Proyecto condicionales: Juego piedra, Papel, tijera
import random
options = ('piedra','papel','tijera')

computer_wins = 0
user_wins = 0
rounds = 1


while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('**Puntos del Computador**', computer_wins)
  print('**Puntos del usuario**,',user_wins )

  user_opcion = input('Piedra, papel o tijera => ')
  user_opcion =user_opcion.lower()
  rounds += 1
  
  if not user_opcion in options:
      print('Opcion invalida')
      continue

  computer_opcion = random.choice(options)


  print('User option => ',user_opcion)
  print('computer option => ',computer_opcion)

  if user_opcion == computer_opcion:
    print('Empate!')
  elif user_opcion == 'piedra':
    if computer_opcion == 'tijera':
      print('piedra gana a tijera')
      print('user gano')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Computer gano')
      computer_wins += 1
  elif user_opcion == 'papel':
    if computer_opcion == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_opcion == 'tijera':
    if computer_opcion == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!') 
      computer_wins += 1
  if computer_wins == 2:
    print('***El ganador es la computadora')
    break
  if user_wins == 2:
    print('***El ganador es la computadora')
    break
  

