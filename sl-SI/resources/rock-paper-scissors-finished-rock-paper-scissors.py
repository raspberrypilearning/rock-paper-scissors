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
  racunalnik = 'k'
  print('O')
  
elif(izbrano == 2):
  racunalnik = 'p'
  print('___')
  
else:
  racunalnik = 'š'
  print('>8')

if(igralec == racunalnik):
  print('IZENAČENO!')
  
elif(igralec == 'k' and racunalnik == 'š'):
  print('Zmagal je igralec!')
  
elif(igralec == 'k' and racunalnik == 'p'):
  print('Zmagal je računalnik!')
  
elif(igralec == 'p' and racunalnik == 'k'):
  print('Zmagal je igralec!')
  
elif(igralec == 'p' and racunalnik == 'š'):
  print('Zmagal je računalnik!')

elif(igralec == 'š' and racunalnik == 'p'):
  print('Zmagal je igralec!')
  
elif(igralec == 'š' and racunalnik == 'k'):
  print('Zmagal je računalnik!')

else:
  print('Eh?')
  
  
