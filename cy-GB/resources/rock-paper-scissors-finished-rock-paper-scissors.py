#!/bin/python3

from random import randint
  
player = input('carreg (c), papur (p) neu sisiwrn (s)?')

if(player == 'c'):
  print('O', end=' ')
  
elif(player == 'p'):
  print('___', end=' ')
  
elif(player == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('yn erbyn', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'c'
  print('O')
  
elif(chosen == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if(player == computer):
  print('CYFARTAL!')
  
elif(player == 'r' and computer == 's'):
  print('Chwareuwr yn ennill!')
  
elif(player == 'r' and computer == 'p'):
  print('Cyfrifiadur yn ennill!')
  
elif(player == 'p' and computer == 'r'):
  print('Chwareuwr yn ennill!')
  
elif(player == 'p' and computer == 's'):
  print('Cyfrifiadur yn ennill!')

elif(player == 's' and computer == 'p'):
  print('Chwareuwr yn ennill!')
  
elif(player == "s" and computer == 'r'):
  print('Cyfrifiadur yn ennill!')

else:
  print('Beth?')
  
  