#!/bin/python3

from random import randint
  
igrac = input('kamen (k), skare (s) ili papir (p)?')

if(igrac == 'k'):
  print('O', end=' ')
  
elif(igrac == 'p'):
  print('___', end=' ')
  
elif(igrac == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

odabir = randint(1,3)

if(odabir == 1):
  racunalo = 'k'
  print('O')
  
elif(odabir == 2):
  racunalo = 'p'
  print('___')
  
else:
  racunalo = 's'
  print('>8')

if(igrac == racunalo):
  print('REZULTAT JE NERIJESEN!')
  
elif(igrac == 'k' and racunalo == 's'):
  print('Igrac je pobjednik!')
  
elif(igrac == 'k' and racunalo == 'p'):
  print('Racunalo je pobjednik!')
  
elif(igrac == 'p' and racunalo == 'k'):
  print('Igrac je pobjednik!')
  
elif(igrac == 'p' and racunalo == 's'):
  print('Racunalo je pobjednik!')

elif(igrac == 's' and racunalo == 'p'):
  print('Igrac je pobjednik!')
  
elif(igrac == 's' and racunalo == 'k'):
  print('Racunalo je pobjednik!')

else:
  print('Huh?')
  
  
