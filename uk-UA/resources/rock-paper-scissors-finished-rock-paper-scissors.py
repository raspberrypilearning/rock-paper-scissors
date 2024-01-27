#!/bin/python3

from random import randint
  
hravets = input('камінь (к), ножниці (н) чи папір (п)?')

if(hravets == 'к'):
  print('O', end=' ')
  
elif(hravets == 'п'):
  print('___', end=' ')
  
elif(hravets == 'н'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('проти', end=' ')

vybir = randint(1,3)

if(vybir == 1):
  computer = 'к'
  print('O')
  
if(vybir == 2):
  computer = 'п'
  print('___')
  
else:
  computer = 'н'
  print('>8')

if(hravets == computer):
  print('НІЧИЯ!')
  
elif(hravets == 'к' and computer == 'н'):
  print('Гравець перемагає!')
  
elif(hravets == 'к' and computer == 'п'):
  print("Комп'ютер перемагає!")
  
elif(hravets == 'р' and computer == 'к'):
  print('Гравець перемагає!')
  
elif(hravets == 'п' and computer == 'н'):
  print("Комп'ютер перемагає!")

elif(hravets == 'н' and computer == 'п'):
  print('Гравець перемагає!')
  
elif(hravets == 'н' and computer == 'к'):
  print("Комп'ютер перемагає!")

else:
  print('Що?')
  
  
