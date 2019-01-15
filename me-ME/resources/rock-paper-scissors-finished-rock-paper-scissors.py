#!/bin/python3

from random import randint
  
igrac = input('papir (p), kamen (k) ili makaze (m)?')

if(igrac == 'k'):
  print('O', end=' ')
  
elif(igrac == 'p'):
  print('___', end=' ')
  
elif(igrac == 'm'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('protiv', end=' ')

odabran = randint(1,3)

if(odabran == 1):
  racunar = 'k'
  print('O')
  
elif(odabran == 2):
  racunar = 'p'
  print('___')
  
else:
  racunar = 'm'
  print('>8')

if(igrac == racunar):
  print('NERIJEŠEN REZULTAT!')
  
elif(igrac == 'k' and racunar == 'm'):
  print('Igrač je pobjednik!')
  
elif(igrac == 'k' and racunar == 'p'):
  print('Računar je pobjednik!')
  
elif(igrac == 'p' and racunar == 'k'):
  print('Igrač je pobjednik!')
  
elif(igrac == 'p' and racunar == 'm'):
  print('Računar je pobjednik!')

elif(igrac == 'm' and racunar == 'p'):
  print('Igrač je pobjednik!')
  
elif(igrac == "m" and racunar == 'k'):
  print('Računar je pobjednik!')

else:
  print('Ha?')
  
  