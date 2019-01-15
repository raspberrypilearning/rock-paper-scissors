#!/bin/python3

from random import randint
  
player = input('pedra (p), papel (a) ou tesoura (t)?')

if(jogador == 'p'):
  print('O', end=' ')
  
elif(jogador == 'a'):
  print('___', end=' ')
  
elif(jogador == 't'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if(escolhido == 1):
  computador = 'p'
  print('O')
  
elif(escolhido == 2):
  computador = 'a'
  print('___')
  
else:
  computador = 't'
  print('>8')

if(player == computador):
  print('EMPATOU!')
  
elif(jogador == 'p' and computador == 't'):
  print('O jogador venceu!')
  
elif(jogador == 'p' and computador == 'a'):
  print('O computador venceu!')
  
elif(jogador == 'a' and computador == 'p'):
  print('O jogador venceu!')
  
elif(jogador == 'a' and computador == 't'):
  print('O computador venceu!')

elif(jogador == 't' and computador== 'a'):
  print('O jogador venceu!')
  
elif(jogador == "t" and computador == 'p'):
  print('O computador venceu!')

else:
  print('O que?')
  
  