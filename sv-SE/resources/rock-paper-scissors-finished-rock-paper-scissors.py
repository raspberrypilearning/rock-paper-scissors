#!/bin/python3

from random import randint
  
spelare = input('sten (st), påse (p) eller sax (s)?)

if (spelare == 'st'):
  print('O', end=' ')
  
elif (spelare == 'p'):
  print('___', end=' ')
  
elif (spelare == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'st'
  print('O')
  
elif(chosen == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if (spelare == computer):
  print('oavgjort')
  
elif (spelare == 'st' and computer == 's'):
  print ('Spelaren vinner!')
  
elif (spelare == 'st' and computer == 'p'):
  print ('Datorn vinner!')
  
elif (spelare == 'p' and computer == 'st'):
  print ('Spelaren vinner!')
  
elif (spelare == 'p' and computer == 's'):
  print ('Datorn vinner!')

elif (spelare == 's' and computer == 'p'):
  print ('Spelaren vinner!')
  
elif (spelare == 's' and computer == 'st'):
  print ('Datorn vinner!')

else:
  print (Va?)
  
  
