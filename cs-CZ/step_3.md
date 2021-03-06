## Tah počítače

Teď je na řadě počítač. Funkci `randint` můžete použít na generování náhodného čísla pro rozhodnutí mezi kamenem, nůžkami a papírem.

+ Použijte funkci `randint` na generování náhodného čísla pro rozhodnutí mezi kamenem, nůžkami a papírem.
    
    ![screenshot](images/rps-randint.png)

+ Spusťte skript vícekrát (vždy budete muset zadat 'k', 'p' nebo 'n').
    
    Měli byste vidět, že 'vybrano' je náhodně nastaveno na 1, 2 nebo 3.

+ Řekněme, že:
    
    + 1 = kámen (k)
    + 2 = papír (p)
    + 3 = nůžky (s)
    
    Použijte `if` ke kontrole, zda je zvolené číslo `1` (`==` se používá ke zjištění zda jsou dvě věci stejné).
    
    ![screenshot](images/rps-if-1.png)

+ Python používá **odsazení** (posunutí kódu doprava) k určení, který kód je uvnitř `if`. Můžete použít dvě mezery (dvakrát stisknout mezerník) nebo stisknout **klávesu tab** (obvykle na klávesnici nad klávesou CAPSLOCK).
    
    Pomocí odsazení nastavte uvnitř `if` `pocitac` na 'k':
    
    ![screenshot](images/rps-indent.png)

+ Můžete přidat alternativní kontrolu pomocí `elif` (zkratka pro *else if*):
    
    ![screenshot](images/rps-elif-2.png)
    
    Tato podmínka se bude kontrolovat pouze v případě selhání první podmínky (pokud počítač nevybral `1`).

+ Nakonec, pokud počítač nevybral `1` ani `2`, musel vybrat `3`.
    
    Tentokrát můžeme pouze použít `else`, což znamená "jinak".
    
    ![screenshot](images/rps-else-3.png)

+ Místo vypsání náhodného čísla, které si počítač vybral, teď můžete vypsat písmeno.
    
    ![screenshot](images/rps-print-computer.png)
    
    Můžete buď odstranit řádek `print(vyber)` nebo přimět počítač řádek ignorovat přidáním `#` na začátek řádku.

+ Otestujte svůj kód kliknutím na tlačítko 'Run' a výběrem jedné z možnosti.

+ Hmm, volba počítače se vypisuje na nový řádek. Můžete to opravit přidáním `end=' '` po `vs` - to Pythonu řekne, že má končit mezerou místo nového řádku.
    
    ![screenshot](images/rps-same-line.png)

+ Zahrajte si hru několikrát kliknutím na tlačítko 'Run' a výběrem jedné z možností.
    
    Prozatím budete muset sami určit, kdo vyhrál. Jako další přidáte kód, který to udělá za vás.