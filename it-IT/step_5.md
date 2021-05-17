\--- challenge \---

## Sfida: Disegni ASCII

Invece di usare le lettere s, c e f per rappresentare sasso, carta e forbici, puoi usare i disegni ASCII?

Per esempio:

![screenshot](images/rps-ascii-challenge.png)

Dove:

    sasso: O
    carta: ___
    forbici: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Suggerimenti:

![screenshot](images/rps-ascii-rock.png)

![screenshot](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Suggerimento:

![screenshot](images/rps-player-ascii.png)

Ricorda che aggiungere `end=' '` alla fine di un `print` lo fa finire con uno spazio invece che con una nuova riga.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---