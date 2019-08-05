#!/bin/python3

from random import randint
  
giocatore = input('sasso (s), carta (c) o forbici(f)?')

if(giocatore == 's'):
  print('O', end=' ')
  
elif(giocatore == 'c'):
  print('___', end=' ')
  
elif(giocatore == 'f'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

scelto = randint(1,3)

if(scelto == 1):
  computer = 's'
  print('O')
  
elif(scelto == 2):
  computer = 'c'
  print('___')
  
else:
  computer = 'f'
  print('>8')

if(giocatore == computer):
  print('PAREGGIO!')
  
elif(giocatore == 's' and computer == 'f'):
  print('Il giocatore vince!')
  
elif(giocatore == 's' and computer == 'c'):
  print('Il computer vince!')
  
elif(giocatore == 'c' and computer == 's'):
  print('Il giocatore vince!')
  
elif(giocatore == 'c' and computer == 'f'):
  print('Il computer vince!')

elif(giocatore == 'f' and computer == 'c'):
  print('Il giocatore vince!')
  
elif(player == 's' and computer == 'r'):
  print('Il computer vince!')

else:
  print('Eh?')
  
  
