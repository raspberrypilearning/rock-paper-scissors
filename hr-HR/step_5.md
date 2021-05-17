\--- challenge \---

## Izazov: ASCII umjetnost

Možeš li, umjesto slova k, s i p koja predstavljaju kamen, škare i papir, koristiti ASCII umjetnost?

Na primjer:

![screenshot](images/rps-ascii-challenge.png)

Gdje je:

    kamen: O
    papir: ___
    škare: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Pomoć:

![screenshot](images/rps-ascii-rock.png)

![screenshot](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Hint:

![screenshot](images/rps-player-ascii.png)

Ne zaboravi da dodavanjem `end=' '` na kraju `print` naredbe, naredba završava razmakom, a ne novim redom.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---