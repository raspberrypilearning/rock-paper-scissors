\--- challenge \---

## Испытание: ASCII-графика

Можешь ли ты вместо того, чтобы использовать буквы к, н и б для обозначения камня, ножниц и бумаги, задействовать ASCII-графику?

Например:

![снимок экрана](images/rps-ascii-challenge.png)

Где:

    камень: O
    ножницы: >8
    бумага: ___
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Подсказка:

![снимок экрана](images/rps-ascii-rock.png)

![снимок экрана](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Подсказка:

![снимок экрана](images/rps-player-ascii.png)

Помни, что добавление `end=' '` в конце `print` завершает вывод строки пробелом, а не переходом к новой строке.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---