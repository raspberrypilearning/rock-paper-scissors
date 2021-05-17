\--- challenge \---

## Výzva: ASCII Art

Dokážete použít ASCII art pro prezentaci kamene, nůžek a papíru místo písmen 'k', 'n', a 'p'?

Například:

![screenshot](images/rps-ascii-challenge.png)

Kde:

    kámen: O
    papír: ___
    nůžky: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Tipy:

![screenshot](images/rps-ascii-rock.png)

![screenshot](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Tip:

![screenshot](images/rps-player-ascii.png)

Nezapomeňte, že přidání `end=' '` na konec `print` zajistí, že výpis bude končit mezerou namísto novým řádkem.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---