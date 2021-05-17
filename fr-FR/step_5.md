\--- challenge \---

## Défi : L'art ASCII

Au lieu d'utiliser les lettres p, f et c pour représenter pierre, feuille et ciseaux, peux-tu utiliser l'art ASCII ?

Par exemple :

![capture d'écran](images/rps-ascii-challenge.png)

Où :

    pierre: O
    feuille: ___
    ciseaux: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Astuces :

![capture d'écran](images/rps-ascii-rock.png)

![capture d'écran](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Indice :

![capture d'écran](images/rps-player-ascii.png)

Rappelle-toi qu'en ajoutant `end=' '` à la fin des paramètres de la fonction `print` la fera se terminer par un espace à la place d'une nouvelle ligne.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---