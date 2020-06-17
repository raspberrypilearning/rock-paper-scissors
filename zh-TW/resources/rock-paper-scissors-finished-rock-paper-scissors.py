#!/bin/python3

from random import randint
  
player = input('rock (r), paper (p) or scissors (s)?')

if(player == 'r'):
  print('O', end=' ')
  
elif(player == 'p'):
  print('___', end=' ')
  
elif(player == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'r'
  print('O')
  
elif(chosen == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if(player == computer):
  print('平手!')
  
elif(player == 'r' and computer == 's'):
  print('玩家獲勝!')
  
elif(player == 'r' and computer == 'p'):
  print('電腦獲勝!')
  
elif(player == 'p' and computer == 'r'):
  print('玩家獲勝!')
  
elif(player == 'p' and computer == 's'):
  print('電腦獲勝!')

elif(player == 's' and computer == 'p'):
  print('玩家獲勝!')
  
elif(player == 's' and computer == 'r'):
  print('電腦獲勝!')

else:
  print('恩?')
  
  
