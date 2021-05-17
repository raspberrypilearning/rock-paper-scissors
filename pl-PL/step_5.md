\--- challenge \---

## Wyzwanie: ASCII Art

Czy potrafisz użyć ASCII art do reprezentowania papieru, kamienia i nożyczek zamiast używać liter p, k i n?

Na przykład:

![screenshot](images/rps-ascii-challenge.png)

Gdzie:

    paper: ___
    kamień: O
    nożyczki: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Wskazówka:

![screenshot](images/rps-ascii-rock.png)

![screenshot](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Wskazówka:

![screenshot](images/rps-player-ascii.png)

Pamiętaj, że dodanie `end=''` na końcu polecenia `print` powoduje, że wyświetlanie kończy się spacją, a nie nową linią.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---