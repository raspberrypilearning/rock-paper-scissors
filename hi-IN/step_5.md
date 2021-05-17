\--- challenge \---

## चुनौती: ASCII आर्ट

रॉक, पेपर और कैंची का दर्शाने करने के लिए आर, पी और एस (r, p and s) अक्षर का उपयोग करने के बजाय, क्या आप ASCII आर्ट का उपयोग कर सकते हैं?

उदाहरण के लिए:

![स्क्रीनशॉट](images/rps-ascii-challenge.png)

कहाँ पे:

    rock: O
    paper: ___
    scissors: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

Hints:

![स्क्रीनशॉट](images/rps-ascii-rock.png)

![स्क्रीनशॉट](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

Hint:

![स्क्रीनशॉट](images/rps-player-ascii.png)

याद रखें कि `print` के ाद `end=' '` लगाने से यहएक नई पंक्ति के बजाय एक स्थान(स्पेस) के साथ समाप्त होता है।

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---