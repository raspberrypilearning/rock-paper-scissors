## Datorns vändning

Nu är det datorns tur. Du kan använda `randint` funktionen för att generera ett slumptal för att bestämma mellan sten, papper och sax.

+ Använd `randint` att generera ett slumptal för att bestämma om datorn har valt rock, papper eller sax.
    
    ![skärmdump](images/rps-randint.png)

+ Kör ditt skript många gånger (du måste ange 'r', 'p' eller 's' varje gång.)
    
    Du bör se att "vald" är slumpmässigt inställd på antingen 1, 2 eller 3.

+ Låt oss säga:
    
    + 1 = rock (r)
    + 2 = papper (p)
    + 3 = sax (s)
    
    Använd `om` att kontrollera om det valda numret är `1` (`==` används för att se om 2 saker är desamma).
    
    ![skärmdump](images/rps-if-1.png)

+ Python använder **indrag** (flyttar koden till höger) för att visa vilken kod som ligger inom `om`. Du kan antingen använda två mellanslag (tryck på mellanslagstangenten två gånger) eller tryck på **knappen** (vanligtvis ovanför CAPSLOCK på tangentbordet.)
    
    Ställ `dator` till 'r' inuti `om` använder indragning:
    
    ![skärmdump](images/rps-indent.png)

+ Du kan lägga till en alternativ kontroll med `elif` (kort för *annat om*):
    
    ![skärmdump](images/rps-elif-2.png)
    
    Detta villkor kontrolleras endast om det första villkoret misslyckas (om datorn inte valde `1`)

+ Och slutligen, om datorn inte valde `1` eller `2` måste den ha valt `3`.
    
    Den här gången kan vi bara använda `else` vilket betyder annars.
    
    ![skärmdump](images/rps-else-3.png)

+ Nu, istället för att skriva ut det slumptal som datorn valde kan du skriva ut brevet.
    
    ![skärmdump](images/rps-print-computer.png)
    
    Du kan antingen ta bort raden `utskrift (vald)`, eller låta datorn ignorera den genom att lägga till en `#` i början av raden.

+ Testa din kod genom att klicka på Kör och välj ditt alternativ.

+ Hmm, datorns val blir tryckt på en ny linje. Du kan fixa det genom att lägga till `end = ''` efter `vs`, som berättar Python att sluta med ett mellanslag istället för en ny rad.
    
    ![skärmdump](images/rps-same-line.png)

+ Spela spelet några gånger genom att klicka på Kör och göra ett val.
    
    För nu måste du utarbeta vem som vann sig själv. Nästa lägger du till Python-koden för att fungera här.