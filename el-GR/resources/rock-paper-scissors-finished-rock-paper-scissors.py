#!/bin/python3

from random import randint
  
player = input('πέτρα (π), ψαλίδι (ψ) ή χαρτί (χ);')

if(player == 'π'):
  print('O', end=' ')
  
elif(player == 'χ'):
  print('___', end=' ')
  
elif(player == 'ψ'):
  print('>8', end=' ')
  
else:
  print(';;')
  
print('εναντίον', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'π'
  print('O')
  
elif(chosen == 2):
  computer = 'ψ'
  print('>8')
  
else:
  computer = 'χ'
  print('___')

if(player == computer):
  print('ΙΣΟΠΑΛΙΑ!')
  
elif(player == 'π' and computer == 'ψ'):
  print('Ο Παίκτης κερδίζει!')
  
elif(player == 'π' and computer == 'χ'):
  print('Ο Υπολογιστής κερδίζει!')
  
elif(player == 'χ' and computer == 'π'):
  print('Ο Παίκτης κερδίζει!')
  
elif(player == 'χ' and computer == 'ψ'):
  print('Ο Υπολογιστής κερδίζει!')

elif(player == 'ψ' and computer == 'χ'):
  print('Ο Παίκτης κερδίζει!')
  
elif(player == "ψ" and computer == 'π'):
  print('Ο Υπολογιστής κερδίζει!')

else:
  print('Τώρα;')
  
  