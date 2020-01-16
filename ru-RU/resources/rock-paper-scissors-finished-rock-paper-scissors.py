#!/bin/python3

from random import randint
  
player = input('камень (к), ножницы (н) или бумага (б)?')

if(player == 'к'):
  print('O', end=' ')
  
elif(player == 'б'):
  print('___', end=' ')
  
elif(player == 'н'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('против', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'к'
  print('O')
  
elif(chosen == 2):
  computer = 'б'
  print('___')
  
else:
  computer = 'н'
  print('>8')

if(player == computer):
  print('НИЧЬЯ!')
  
elif(player == 'к' and computer == 'н'):
  print('Игрок выиграл!')
  
elif(player == 'к' and computer == 'б'):
  print('Компьютер выиграл!')
  
elif(player == 'б' and computer == 'к'):
  print('Игрок выиграл!')
  
elif(player == 'б' and computer == 'н'):
  print('Компьютер выиграл!')

elif(player == 'н' and computer == 'б'):
  print('Игрок выиграл!')
  
elif(player == 'н' and computer == 'к'):
  print('Компьютер выиграл!')

else:
  print('Чтоо?')
  
  
