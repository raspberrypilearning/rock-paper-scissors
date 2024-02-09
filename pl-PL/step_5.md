\--- challenge \---

## Wyzwanie: ASCII Art

Czy potrafisz użyć ASCII art do reprezentowania papieru, kamienia i nożyczek zamiast używać liter p, k i n?

Na przykład:

![zrzut ekranu](images/rps-ascii-challenge.png)

Gdzie:

    paper: ___
    kamień: O
    nożyczki: >8
    

+ Zamiast wyświetlać `print(komputer)` musisz dodać nową linię do każdej z opcji w `if`, aby wyświetlić poprawny ASCII art. 

Wskazówka:

![zrzut ekranu](images/rps-ascii-rock.png)

![zrzut ekranu](images/rps-comment-computer.png)

+ Zamiast wyświetlać `print(gracz)` musisz dodać nową instrukcję if, która sprawdzi, co wybrał gracz i wyświetli odpowiedni ASCII art:

Wskazówka:

![zrzut ekranu](images/rps-player-ascii.png)

Pamiętaj, że dodanie `end=''` na końcu polecenia `print` powoduje, że wyświetlanie kończy się spacją, a nie nową linią.

+ Dołącz linię do wydrukowania `vs` pomiędzy wynikami gracza i komputera.

    print('vs', end=' ')
    

\--- /challenge \---