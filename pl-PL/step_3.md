## Ruch komputera

Teraz kolej na komputer. Możesz użyć funkcji `randint` do generowania liczby losowej, aby wybrać papier, kamień lub nożyce.

+ Użyj `randint` do wygenerowania losowej liczby, aby zdecydować, czy komputer wybrał papier, kamień czy nożyce.
    
    ![zrzut ekranu](images/rps-randint.png)

+ Uruchom swój skrypt wiele razy (za każdym razem wpisz "p", "k" lub "n").
    
    Wartość zmiennej "wybrany" będzie wybierana losowo jako 1, 2 lub 3.

+ Powiedzmy, że:
    
    + 1 = papier (p)
    + 2 = kamień (k)
    + 3 = nożyce (n)
    
    Użyj `if` do sprawdzenia, czy wybrana liczba to `1` (do sprawdzenia, czy dwie rzeczy są takie same używamy `==`).
    
    ![zrzut ekranu](images/rps-if-1.png)

+ Python używa **wcięcia** (przesunięcie kodu w prawo), aby pokazać, który kod znajduje się wewnątrz `if`. Możesz użyć dwóch spacji (naciśnij dwa razy spację), albo naciśnij klawisz **Tab** (zazwyczaj znajduje się na klawiaturze nad klawiszem CAPSLOCK).
    
    Ustaw `komputer` na "r" wewnątrz `if` używając do tego wcięcia:
    
    ![zrzut ekranu](images/rps-indent.png)

+ Możesz dodać alternatywne sprawdzenie używając `elif` (skrót od angielskiego *else if*, czyli "w przeciwnym razie, jeżeli"):
    
    ![zrzut ekranu](images/rps-elif-2.png)
    
    Ten warunek zostanie sprawdzony tylko wtedy, gdy pierwszy warunek nie zostanie spełniony (czyli jeśli komputer nie wybrał `1`)

+ Jeśli komputer nie wybrał ani `1` ani `2`, to znaczy, że musiał wybrać `3`.
    
    Tym razem możemy po prostu użyć `else`, co oznacza "w przeciwnym przypadku".
    
    ![zrzut ekranu](images/rps-else-3.png)

+ Teraz, zamiast wyświetlać losową liczbę, którą wybrał komputer, możesz wyświetlić literę.
    
    ![zrzut ekranu](images/rps-print-computer.png)
    
    Możesz usunąć polecenie `print(wybrany)` albo dodać przed nim `#`, aby sprawić, że komputer je zignoruje.

+ Przetestuj swój kod klikając Run i wybierając papier, kamień albo nożyce.

+ Hmm, wybór komputera jest wyświetlany w nowej linii. Możesz to naprawić, dodając `end=' '` po `vs`, co powie Pythonowi, by kończył spacją, a nie nową linią.
    
    ![zrzut ekranu](images/rps-same-line.png)

+ Zagraj kilka razy klikając Run i wybierając papier, kamień albo nożyce.
    
    Póki co to Ty musisz ustalać, kto wygrał. Teraz dodamy kod w Pythonie, który sam to sprawdzi.