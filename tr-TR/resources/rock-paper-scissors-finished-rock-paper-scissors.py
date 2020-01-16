#!/bin/python3

from random import randint
  
oyuncu = input('taş (t), kağıt (k), makas (m)?')

if(oyuncu == 't'):
  print('O', end=' ')
  
elif(oyuncu == 'k'):
  print('___', end=' ')
  
elif(oyuncu == 'm'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('karşısında', end=' ')

tercih = randint(1,3)

if(tercih == 1):
  bilgisayar = 't'
  print('O')
  
elif(tercih == 2):
  bilgisayar = 'k'
  print('___')
  
else:
  bilgisayar = 'm'
  print('>8')

if(oyuncu == bilgisayar):
  print('BERABERE!')
  
elif(oyuncu == 't' and bilgisayar == 'm'):
  print('Oyuncu kazandı!')
  
elif(oyuncu == 't' and bilgisayar == 'k'):
  print('Bilgisayar kazandı!')
  
elif(oyuncu == 'k' and bilgisayar == 't'):
  print('Oyuncu kazandı!')
  
elif(oyuncu == 'k' and bilgisayar == 'm'):
  print('Bilgisayar kazandı!')

elif(oyuncu == 'm' and bilgisayar == 'k'):
  print('Oyuncu kazandı!')
  
elif(oyuncu == 'm' and bilgisayar == 't'):
  print('Bilgisayar kazandı!')

else:
  print('Ne??')
  
  
