#!/bin/python3

from random import randint
  
speler = input('steen (t), papier (p) of schaar (s)?')

if(speler == 't'):
  print('O', end=' ')
  
elif speler == 'p':
  print('___', end=' ')
  
elif(speler == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

gekozen = randint(1,3)

if(gekozen == 1):
  computer = 't'
  print('O')
  
elif(gekozen == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if(speler == computer):
  print('Gelijk!')
  
elif(speler == 't' and computer == 's'):
  print('Speler wint!')
  
elif(speler == 't' and computer == 'p'):
  print('Computer wint!')
  
elif(speler == 'p' and computer == 't'):
  print('Speler wint!')
  
elif(speler == 'p' and computer == 's'):
  print('Computer wint!')

elif(speler == 's' and computer == 'p'):
  print('Speler wint!')
  
elif(player == 's' and computer == 'r'):
  print('Computer wint!')

else:
  print('He?')
  
  
