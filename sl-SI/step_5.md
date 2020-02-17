--- challenge ---

## Izziv: ASCII umetnost

Ali lahko namesto črk k, š in p uporabiš ASCII umetnost, da prikažeš kamen, papir in škarje?

Na primer:

![posnetek zaslona](images/rps-ascii-challenge.png)

Kjer je:

    skala: O
    papir: ___
    škarje: >8
    

+ Namesto, da bi dejal `print racunalnik`, boš moral v `if` za vsako možnost dodati novo vrstico, ki bo izpisala parvo ASCII umetnost. 

Namigi:

![posnetek zaslona](images/rps-ascii-rock.png)

![posnetek zaslona](images/rps-comment-computer.png)

+ Namesto tega, da bi dejal `print igralec`, boš moral dodati nov if stavek, ki bo preveril, katero stvar je igralec izbral in ki bo izpisal ustrezno ASCII umetnost:

Namig:

![posnetek zaslona](images/rps-player-ascii.png)

Zapomni si, da dodatek `end=' '` na koncu `print` povzroči, da se izpis konča s presledkom in ne z novo vrstico.

--- /challenge ---