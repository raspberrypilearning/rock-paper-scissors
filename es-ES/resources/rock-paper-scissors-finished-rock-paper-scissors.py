#!/bin/python3

from random import randint
  
jugador = input('¿piedra (r), papel (p) o tijera (t)?')

if(jugador == 'r'):
  print('O', end = ' ')
  
elif(jugador == 'p'):
  print('___', end = ' ')
  
elif(jugador == 't'):
  print('>8', end = ' ')
  
else:
  print('¿?')
  
print('contra', end = ' ')

elegido = randint(1,3)

if(elegido == 1):
  ordenador = 'r'
  print('O')
  
elif(elegido == 2):
  ordenador = 'p'
  print('___')
  
else:
  ordenador = 't'
  print('>8')

if(jugador == ordenador):
  print('¡EMPATE!')
  
elif(jugador == 'r' and ordenador == 't'):
  print('¡El jugador gana!')
  
elif(jugador == 'r' and ordenador == 'p'):
  print('¡El ordenador gana!')
  
elif(jugador == 'p' and ordenador == 'r'):
  print('¡El jugador gana!')
  
elif(jugador == 'p' and ordenador == 't'):
  print('¡El ordenador gana!')

elif(jugador == 't' and ordenador == 'p'):
  print('¡El jugador gana!')
  
elif(player == 's' and computer == 'r'):
  print('¡El ordenador gana!')

else:
  print('¿Eh?')
  
  
