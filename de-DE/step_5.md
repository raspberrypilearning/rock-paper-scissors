\--- Aufgabe \---

## Aufgabe: ASCII - Bilder

Anstatt die Buchstaben r, p und s zu verwenden, um Stein, Papier und Schere darzustellen, kann man auch ASCII-Bilder verwenden. Das sind kleine Grafiken aus ASCII-Zeichen.

Zum Beispiel:

![screenshot](images/rps-ascii-challenge.png)

Anstelle von:

    Stein: O
    Papier: ___
    Schere: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Hinweise:

![screenshot](images/rps-ascii-rock.png)

![screenshot](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Hinweis:

![screenshot](images/rps-player-ascii.png)

Denke daran, dass `end='  '` am Ende von `print` bewirkt, dass ein Leerzeichen anstelle des Zeilenvorschubs gedruckt wird.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- / Aufgabe \---