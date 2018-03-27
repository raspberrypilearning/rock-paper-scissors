#!/bin/python3

from random import randint
  
gracz = input('papier (p), kamień (k) czy nożyce (n)?')

if(gracz == 'p'):
  print('___', end=' ')
  
elif(gracz == 'k'):
  print('O', end=' ')
  
elif(gracz == 'n'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

wybrany = randint(1,3)

if(wybrany == 1):
  komputer = 'p'
  print('___')
  
elif(wybrany == 2):
  komputer = 'k'
  print('O')
  
else:
  komputer = 'n'
  print('>8')

if(gracz == komputer):
  print('REMIS!')
  
elif(gracz == 'k' and komputer == 'n'):
  print('Wygrywa gracz!')
  
elif(gracz == 'k' and komputer == 'p'):
  print('Wygrywa komputer!')
  
elif(gracz == 'p' and komputer == 'k'):
  print('Wygrywa gracz!')
  
elif(gracz == 'p' and komputer == 'n'):
  print('Wygrywa komputer!')

elif(gracz == 'n' and komputer == 'p'):
  print('Wygrywa gracz!')
  
elif(gracz == 'n' and komputer == 'k'):
  print('Wygrywa komputer!')

else:
  print('Hę?')
  
  