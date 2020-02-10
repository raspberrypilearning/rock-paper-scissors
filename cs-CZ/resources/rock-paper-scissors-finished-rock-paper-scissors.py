#!/bin/python3

from random import randint
  
hrac = input('kamen (k), nuzky (n) nebo papir (p)?')

if(hrac == 'k'):
  print('O', end=' ')
  
elif(hrac == 'p'):
  print('___', end=' ')
  
elif(player == 'n'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

vyber = randint(1,3)

if(vyber == 1):
  pocitac = 'k'
  print('O')
  
elif(vyber == 2):
  pocitac = 'p'
  print('___')
  
else:
  pocitac = 'n'
  print('>8')

if(hrac == pocitac):
  print('REMÍZA!')
  
elif(hrac == 'k' and pocitac == 'n'):
  print('Vyhrává hráč!')
  
elif(hrac == 'k' and pocitac == 'p'):
  print('Vyhrává počítač!')
  
elif(hrac == 'p' and pocitac == 'k'):
  print('Vyhrává hráč!')
  
elif(hrac == 'p' and pocitac == 'n'):
  print('Vyhrává počítač!')

elif(hrac == 'n' and pocitac == 'p'):
  print('Vyhrává hráč!')
  
elif(hrac == 'n' and pocitac == 'k'):
  print('Vyhrává počítač!')

else:
  print('Huh?')
  
  
