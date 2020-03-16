#!/bin/python3

from random import randint
  
player = input('حجر (r), ورق (p) أو مقص (s)?')

if(player == 'r'):
  print('O', end=' ')
  
elif(player == 'p'):
  print('___', end=' ')
  
elif(player == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('ضد', end=' ')

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
  print('تعادل!')
  
elif(player == 'r' and computer == 's'):
  print('يفوز اللاعب!')
  
elif(player == 'r' and computer == 'p'):
  print('يفوز الحاسوب!')
  
elif(player == 'p' and computer == 'r'):
  print('يفوز اللاعب!')
  
elif(player == 'p' and computer == 's'):
  print('يفوز الحاسوب!')

elif(player == 's' and computer == 'p'):
  print('يفوز اللاعب!')
  
elif(player == 's' and computer == 'r'):
  print('يفوز الحاسوب!')

else:
  print('ماذا؟')
  
  
