#!/bin/python3

from random import randint
  
hrac = input('kamen (k), nuzky (n) nebo papir (p)?')

if(hrac == 'k'):
  print('O', end=' ')
  
elif(hrac == 'n'):
  print('___', end=' ')
  
elif(hrac == 'p'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'r'
  print('O')
  
elif(chosen == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
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
  
  
