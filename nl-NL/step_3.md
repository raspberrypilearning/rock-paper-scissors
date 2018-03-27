## De beurt van de computer

Nu is het de beurt aan de computer. U kunt de functie `randint` gebruiken om een ​​willekeurig getal te genereren om te kiezen tussen steen, papier en schaar.

+ Gebruik `randint` om een ​​willekeurig getal te genereren om te beslissen of de computer rock, papier of een schaar heeft gekozen.
    
    ![screenshot](images/rps-randint.png)

+ Voer uw script vaak uit (u moet elke keer 'r', 'p' of 's' invoeren.)
    
    Je zou moeten zien dat 'gekozen' willekeurig wordt ingesteld op 1, 2 of 3.

+ Laten we zeggen:
    
    + 1 = rock (r)
    + 2 = papier (p)
    + 3 = schaar (s)
    
    Gebruik `als` om te controleren of het gekozen nummer `1` (`==` is om te zien of 2 dingen hetzelfde zijn).
    
    ![screenshot](images/rps-if-1.png)

+ Python gebruikt **inspringing** (verplaats de code naar rechts) om aan te geven welke code zich binnen de `bevindt als`. Je kunt twee spaties gebruiken (tik twee keer op de spatiebalk) of tik op de **tab-toets** (meestal boven CAPSLOCK op het toetsenbord).
    
    Zet `computer` op 'r' in de `als` met behulp van inspringen:
    
    ![screenshot](images/rps-indent.png)

+ U kunt een alternatieve cheque toevoegen met `elif` (afkorting voor *anders als*):
    
    ![screenshot](images/rps-elif-2.png)
    
    Deze voorwaarde wordt alleen gecontroleerd als de eerste voorwaarde mislukt (als de computer niet `1` heeft gekozen)

+ En ten slotte, als de computer `1` of `2` niet heeft gekozen, moet deze `3` hebben gekozen.
    
    Deze keer kunnen we gewoon `anders` gebruiken, wat anders betekent.
    
    ![screenshot](images/rps-else-3.png)

+ In plaats van het willekeurige nummer af te drukken dat de computer heeft gekozen, kunt u de brief nu afdrukken.
    
    ![screenshot](images/rps-print-computer.png)
    
    U kunt de regel `afdrukken (gekozen)`verwijderen of de computer negeren door een `#` aan het begin van de regel toe te voegen.

+ Test uw code door op Uitvoeren te klikken en uw optie te kiezen.

+ Hmm, de keuze van de computer wordt afgedrukt op een nieuwe regel. Je kunt dit oplossen door `end = ''` toe te voegen na `vs`, waarmee Python eindigt met een spatie in plaats van een nieuwe regel.
    
    ![screenshot](images/rps-same-line.png)

+ Speel het spel een paar keer door op Uitvoeren te klikken en een keuze te maken.
    
    Want nu zul je moeten bepalen wie er gewonnen heeft. Vervolgens voeg je de Python-code toe om dit uit te werken.