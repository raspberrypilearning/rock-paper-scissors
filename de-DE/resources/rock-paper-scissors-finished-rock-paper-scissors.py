#! /usr/bin/python3

from random import randint
  
Spieler = input('Schere (s), Stein (r) oder Papier (p)?')

if(Spieler == 'r'):
    print('O', end=' ')
  
elif(Spieler == 'p'):
    print('___', end=' ')
  
elif(Spieler == 's'):
    print('>8', end=' ')
  
else:
    print('??')
  
print('vs', end=' ')

zufall = randint(1,3)

if(zufall == 1):
  computer = 'r'
  print('O')
  
elif(zufall == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if(Spieler == computer):
    print('Unentschieden!')
  
elif(Spieler == 'r' and computer == 's'):
  print('Spieler gewinnt!')
  
elif(Spieler == 'r' and computer == 'p'):
  print('Computer gewinnt!')
  
elif(Spieler == 'p' and computer == 'r'):
  print('Spieler gewinnt!')
  
elif(Spieler == 'p' and computer == 's'):
  print('Computer gewinnt!')

elif(Spieler == 's' and computer == 'p'):
  print('Spieler gewinnt!')
  
elif(player == 's' and computer == 'r'):
  print('Computer gewinnt!')

else:
  print('Huh?')
  
  
