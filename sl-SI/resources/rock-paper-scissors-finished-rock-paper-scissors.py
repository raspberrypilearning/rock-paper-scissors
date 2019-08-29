#!/bin/python3

from random import randint
  
igralec = input('kamen (k), papir (p) ali škarje (š)?')

if(igralec == 'k'):
  print('O', end=' ')
  
elif(igralec == 'p'):
  print('___', end=' ')
  
elif(igralec == 'š'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('proti', end=' ')

izbrano = randint(1,3)

if(izbrano == 1):
  racunalnik = 'r'
  print('O')
  
elif(izbrano == 2):
  racunalnik = 'p'
  print('___')
  
else:
  racunalnik = 's'
  print('>8')

if(player == computer):
  print('DRAW!')
  
elif(player == 'r' and computer == 's'):
  print('Player wins!')
  
elif(player == 'r' and computer == 'p'):
  print('Computer wins!')
  
elif(player == 'p' and computer == 'r'):
  print('Player wins!')
  
elif(player == 'p' and computer == 's'):
  print('Computer wins!')

elif(player == 's' and computer == 'p'):
  print('Player wins!')
  
elif(player == 's' and computer == 'r'):
  print('Computer wins!')

else:
  print('Huh?')
  
  
