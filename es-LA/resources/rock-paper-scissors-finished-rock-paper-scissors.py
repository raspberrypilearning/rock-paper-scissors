#!/bin/python3

from random import randint
  
jugador = input('¿piedra (r), papel (p) o tijeras (s)?')

if(jugador == 'r'):
  print('O', end = ' ')
  
elif(jugador == 'p'):
  print('___', end = ' ')
  
elif(jugador == 's'):
  print('>8', end = ' ')
  
else:
  print('??')
  
print('vs', end=' ')

elegido = randint(1,3)

if(elegido == 1):
  computadora = 'r'
  print('O')
  
elif(elegido == 2):
  computadora = 'p'
  print('___')
  
else:
  computadora = 's'
  print('>8')

if(jugador == computadora):
  print('¡EMPATE!')
  
elif(jugador == 'r' and computadora == 's'):
  print('¡Jugador gana!')
  
elif(jugador == 'r' and computadora == 'p'):
  print('¡La computadora gana!')
  
elif(jugador == 'p' and computadora == 'r'):
  print('¡Jugador gana!')
  
elif(jugador == 'p' and computadora == 's'):
  print('¡La computadora gana!')

elif(jugador == 's' and computadora == 'p'):
  print('¡Jugador gana!')
  
elif(jugador == 's' and computadora == 'r'):
  print('¡La computadora gana!')

else:
  print('¿Eh?')
  
  
