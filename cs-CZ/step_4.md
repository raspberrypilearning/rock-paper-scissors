## Zkontrolujte výsledek

Pojďme teď přidat kód, který nám ukáže, kdo vyhrál.

+ Abychom zjistili, kdo vyhrál. je třeba porovnat proměnné `hrac` a `pocitac`.
    
    Pokud jsou stejné, je to nerozhodně:
    
    ![screenshot](images/rps-draw.png)

+ Otestujte svůj kód tím, že si několikrát hru zahrajete, dokud nedosáhnete remízy.
    
    Abyste spustili novou hru, budete muset kliknout na `Run`.

+ Nyní se podívejme na případy, kdy hráč zvolil 'k' (kámen), ale počítač ne.
    
    Pokud si počítač vybral 'n' (nůžky), vyhrává hráč (kámen tupí nůžky).
    
    Pokud si počítač zvolil 'p' (papír), vyhrává počítač (papír zabalí kámen).
    
    Můžeme zkontrolovat výběr hráče *a* počítače pomocí `and`.
    
    ![screenshot](images/rps-player-rock.png)

+ Jako další se podívejme na případy, kdy hráč zvolil 'p' (papír), ale počítač ne:
    
    ![screenshot](images/rps-player-paper.png)

+ A nakonec - můžete přidat kód pro zjištění vítěze, když hráč zvolil 'n' (nůžky) a počítač si vybral kámen nebo papír?

+ Nyní si hru zahrajte, abyste otestovali svůj kód.
    
    ![screenshot](images/rps-play.png)
    
    Abyste spustili novou hru, klikněte na `Run`.