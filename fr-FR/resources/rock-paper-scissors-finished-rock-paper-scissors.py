#!/bin/python3

from random import randint
  
joueur = input('pierre (p), feuille (f) ou ciseaux (c)?')

if(joueur == 'p'):
  print('O', end=' ')
  
elif(joueur == 'f'):
  print('___', end=' ')
  
elif(joueur == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

choisi = randint(1, 3)

if(choisi == 1):
  ordinateur = 'p'
  print('O')
  
elif(choisi == 2):
  ordinateur = 'f'
  print('___')
  
else:
  ordinateur = 'c'
  print('>8')

if(joueur == ordinateur):
  print('TIRAGE AU SORT!')
  
elif(joueur == 'p' and ordinateur== 'c'):
  print('Le joueur gagne!')
  
elif(joueur == 'p' and ordinateur == 'f'):
  print("L'ordinateur gagne!")
  
elif(joueur == 'f' and ordinateur == 'p'):
  print('Le joueur gagne!')
  
elif(joueur == 'f' and ordinateur == 'c'):
  print("L'ordinateur gagne!")

elif(joueur == 'c' and ordinateur == 'f'):
  print('Le joueur gagne!')
  
elif(player == 'c' and computer == 'p'):
  print("L'ordinateur gagne!")

else:
  print('Huh?')
  
  
