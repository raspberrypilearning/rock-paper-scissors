## Der Computer ist dran

Jetzt ist der Computer an der Reihe. Du kannst die `randint` Funktion verwenden, um eine Zufallszahl zu erzeugen, die dann über Schere, Stein oder Papier entscheidet.

+ Verwende die `randint` Funktion, um eine Zufallszahl zu erzeugen, die dann entscheidet, ob der Computer sich für Schere, Stein oder Papier entschieden hat.
    
    ![screenshot](images/rps-randint.png)

+ Führe dein Skript mehrmals aus (Du musst jedes Mal 's, 'r' oder 'p' eingeben)
    
    Di wirst sehen, dass die zufällig ausgewählte Zahl auf 1, 2 oder 3 gesetzt ist.

+ Sagen wir:
    
    + 1 = Stein(r)
    + 2 = Papier (p)
    + 3 = Schere (s)
    
    Verwende `if` um zu überprüfen, ob die gewählte Nummer `1` ist (`==` wird verwendet, um zu sehen, ob 2 Dinge gleich sind).
    
    ![screenshot](images/rps-if-1.png)

+ Python verwendet **Einrückung** (bewegen des Codes nach rechts), um zu zeigen, welcher Code innerhalb der `if` Verzweigung liegt. Du kannst entweder zwei Leerzeichen verwenden (zweimal auf die Leertaste tippen) oder auf die **Tabulatortaste** tippen(normalerweise über der CAPSLOCK-Taste auf der Tastatur.)
    
    Weise innerhalb der `if`-Abfrage der Variablen `computer` den Wert 'r' zu und verwende eine Einrückung dabei:
    
    ![screenshot](images/rps-indent.png)

+ Du kannst eine weitere Prüfung mit `elif` hinzufügen (Kurzform von * else if *):
    
    ![screenshot](images/rps-elif-2.png)
    
    Diese Bedingung wird nur überprüft, wenn die erste Bedingung fehlschlägt (wenn der Computer nicht `1` gewählt hat). Weise hier innerhalb der Einrückung der Variablen <0>computer</0> den Wert 'p' zu

+ Und schließlich, wenn der Computer weder `1` noch `2` gewählt hat, dann muss er `3` gewählt haben.
    
    Diesmal können wir einfach `else` verwenden, was "ansonsten" bedeutet. Weise hier innerhalb der Einrückung der Variablen <0>computer</0> den Wert 's' zu.
    
    ![screenshot](images/rps-else-3.png)

+ Anstatt die vom Computer gewählte Zufallszahl auszudrucken, kannst du nun den jeweiligen Buchstaben drucken.
    
    ![screenshot](images/rps-print-computer.png)
    
    Du kannst nun die Zeile `print(zufall)` löschen oder die Zeile mit einer Raute `#` am Anfang "auskommentieren", so dass sie vom Computer ignoriert wird.

+ Teste den Code, indem du auf "Run" klickst und deine Option auswählst.

+ Hmm, die Wahl des Computers wird in einer neuen Zeile gedruckt. Du kannst das beheben, indem du `end=' '` nach dem `vs` hinzufügst. Damit wird Python gesagt, dass es mit einem Leerzeichen anstelle einer neuen Zeile enden soll.
    
    ![screenshot](images/rps-same-line.png)

+ Spiele das Spiel ein paar Mal, indem du auf "Run" klickst und eine Auswahl triffst.
    
    Jetzt müssen wir herausfinden, wer gewonnen hat. Als Nächstes fügen wir den Python-Code hinzu, um dies zu erledigen.