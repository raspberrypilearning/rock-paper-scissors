\--- challenge \---

## Desafío: Arte ASCII

En lugar de usar las letras r, p y t para representar piedra, papel y tijera, ¿puedes usar el arte ASCII?

Por ejemplo:

![captura de pantalla](images/rps-ascii-challenge.png)

Donde:

    piedra:  O
    papel: ___
    tijeras: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Hints:

![captura de pantalla](images/rps-ascii-rock.png)

![captura de pantalla](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Hint:

![captura de pantalla](images/rps-player-ascii.png)

Recuerda que añadir `end = ' '` al final de la línea `print` hace que termine con un espacio en lugar de terminar con una nueva línea.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---