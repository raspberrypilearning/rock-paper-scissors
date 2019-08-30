## Na vrsti je računalnik

Zdaj je na vrsti računalnik. Za ustvarjanje naključnega števila, ki bo odločalo med kamnom, škarjami in papirjem, lahko uporabiš funkcijo `randint`.

+ Uporabi `randint`, da ustvariš naključno število, ki bo odločalo o tem ali je računalnik izbral kamen, škarje ali papir.
    
    ![screenshot](images/rps-randint.png)

+ Svojo skripto zaženi večkrat (vsakič boš moral vnesti 'k', 'š' ali 'p').
    
    Moral bi videti ali je spremenljivka 'izbrano' naključno določena kot 1, 2 ali 3.

+ Recimo da je:
    
    + 1 = kamen (k)
    + 2 = papir (p)
    + 3 = škarje (š)
    
    Uporabi `if`, da preveriš ali je izbrana številka `1`(`==` se uporablja za preverjanje, če sta dve stvari enaki).
    
    ![screenshot](images/rps-if-1.png)

+ Python uporablja **zamik** (pomikanje kode v desno), da prikaže, katera koda se nahaja znotraj `if`. Lahko uporabiš dva presledka (dvakrat pritisneš preslednico) ali enkrat pritisneš **tabulator** (ta se ponavadi nahaja nad tipko za zaklepanje velikosti črk tj. tipko CAPSLOCK).
    
    Set `computer` to 'r' inside the `if` using indentation:
    
    ![screenshot](images/rps-indent.png)

+ You can add an alternative check using `elif` (short for *else if*):
    
    ![screenshot](images/rps-elif-2.png)
    
    This condition will only be checked if the first condition fails (if the computer didn't choose `1`)

+ And finally, if the computer didn't choose `1` or `2` then it must have chosen `3`.
    
    This time we can just use `else` which means otherwise.
    
    ![screenshot](images/rps-else-3.png)

+ Now, instead of printing out the random number that the computer chose you can print the letter.
    
    ![screenshot](images/rps-print-computer.png)
    
    You can either delete the line `print(chosen)`, or make the computer ignore it by adding a `#` at the start of the line.

+ Test your code by clicking Run and choosing your option.

+ Hmm, the computer's choice gets printed on a new line. You can fix that by adding `end=' '` after `vs`, that tells Python to end with a space instead of a new line.
    
    ![screenshot](images/rps-same-line.png)

+ Play the game a few times by clicking Run and making a choice.
    
    For now you'll have to work out who won yourself. Next you'll add the Python code to work this out.