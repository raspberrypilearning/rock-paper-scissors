\--- challenge \---

## आव्हान: ASCII Art

रॉक, पेपर आणि कात्री यांचे प्रतिनिधित्व करण्यासाठी r, p आणि s अक्षरे वापरण्याऐवजी आपण ASCII Art वापरु शकता का?

उदाहरणार्थ:

![screenshot](images/rps-ascii-challenge.png)

जिथे:

    रॉक: O
    पेपर: ___
    कात्री: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

इशारे:

![screenshot](images/rps-ascii-rock.png)

![screenshot](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

इशारा:

![screenshot](images/rps-player-ascii.png)

लक्षात ठेवा ` print ` च्या शेवटी` end =' '`जोडल्याने तो नवीन लाइनऐवजी स्पेससह समाप्त होतो.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---