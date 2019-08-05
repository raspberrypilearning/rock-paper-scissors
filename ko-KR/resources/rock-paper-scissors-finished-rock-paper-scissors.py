#!/bin/python3

from random import randint
  
player = input('바위(r), 보(p), 가위(s)?: ')

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
  컴퓨터 = 'r'
  print('O')
  
elif(chosen == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if(player == computer):
  print('비겼습니다!')
  
elif(player == 'r' and computer == 's'):
  print('플레이어가 이겼습니다!')
  
elif(player == 'r' and computer == 'p'):
  print('컴퓨터가 이겼습니다!')
  
elif(player == 'p' and computer == 'r'):
  print('플레이어가 이겼습니다!')
  
elif(player == 'p' and computer == 's'):
  print('컴퓨터가 이겼습니다!')

elif(player == 's' and computer == 'p'):
  print('플레이어가 이겼습니다!')
  
elif(player == 's' and computer == 'r'):
  print('컴퓨터가 이겼습니다!')

else:
  print('응?')
  
  
