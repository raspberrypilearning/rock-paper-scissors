#!/bin/python3

from random import randint
  
player = input(u'グー (r), チョキ (s) or  パー  (p)?')

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
  print(u'ひきわけ!')
  
elif(player == 'r' and computer == 's'):
  print(u'プライヤーの勝！')
  
elif(player == 'r' and computer == 'p'):
  print(u'コンピューターの勝！')
  
elif(player == 'p' and computer == 'r'):
  print(u'プライヤーの勝！')
  
elif(player == 'p' and computer == 's'):
  print(u'コンピューターの勝！')

elif(player == 's' and computer == 'p'):
  print(u'プライヤーの勝！')
  
elif(player == "s" and computer == 'r'):
  print(u'コンピューターの勝！')

else:
  print(u'え?')
  
  