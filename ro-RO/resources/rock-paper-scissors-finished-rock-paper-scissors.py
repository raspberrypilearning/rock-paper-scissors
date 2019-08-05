#!/bin/python3

from random import randint
  
jucator = input('piatra (p), hartie (h) sau foarfece (f)?')

if jucator == 'p':
  print('O', end=' ')
  
elif jucator == 'h':
  print('___', end=' ')
  
elif jucator == 'f':
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

ales = randint(1,3)

if ales == 1:
  calculator = 'p'
  print('O')
  
elif ales == 2:
  calculator = 'h'
  print('___')
  
else:
  calculator = 'f'
  print('>8')

if jucator == calculator:
  print('EGALITATE!')
  
elif jucator == 'p' and jucator == 'f':
  print('Jucatorul castiga!')
  
elif jucator == 'p' and calculator == 'h':
  print('Calculatorul castiga!')
  
elif jucator == 'h' and calculator == 'p':
  print('Jucatorul castiga!')
  
elif jucator == 'h' and calculator == 'f':
  print('Calculatorul castiga!')

elif jucator == 'f' and calculator == 'h':
  print('Jucatorul castiga!')
  
elif(player == 's' and computer == 'r'):
  print('Calculatorul castiga!')

else:
  print('Huh?')
  
  
