--- challenge ---

## Udfordring: ASCII Art

I stedet for at bruge bogstaverne r, s, og p til at repræsentere sten, saks, og papir, kan du bruge ASCII art?

For eksempel:

![screenshot](images/rps-ascii-challenge.png)

Hvor:

	sten: O
	saks: >8
	papir: ___


+ I stedet for at skrive `print computer`, bliver du nødt til at tilføje en ny linje til hver mulighed i `if`-betingelsen for at udskrive den korrekte ASCII art.

Hints:

![screenshot](images/rps-ascii-rock.png)

![screenshot](images/rps-comment-computer.png)

+ I stedet for at skrive `print player`, bliver du nødt til at tilføje en ny if-sætning til at checke, hvad spilleren har valgt, og derefter udskrive den korrekte ASCII art:

Hint:

![screenshot](images/rps-player-ascii.png)

Husk at når man tilføjer `end=' '` for enden af `print`, får man den til at afslutte med et mellemrum i stedet for en ny linje.

+ Opret en linje til at udskrive `vs` mellem spillerens og computerens resultater.

```
print('vs', end=' ')
```

--- /challenge ---
