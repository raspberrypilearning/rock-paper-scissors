\--- challenge \---

## ಸವಾಲು: ಆಸ್ಕೀ (ASCII) ಕಲೆ

ಬಂಡೆ(rock), ಕಾಗದ(paper) ಮತ್ತು ಕತ್ತರಿಗಳನ್ನು(scissors) ಪ್ರತಿನಿಧಿಸಲು r, p ಮತ್ತು s ಅಕ್ಷರಗಳನ್ನು ಬಳಸುವ ಬದಲು, ನೀವು ಆಸ್ಕೀ (ASCII) ಕಲೆಯನ್ನು ಕೂಡ ಬಳಸಬಹುದೇ?

ಉದಾಹರಣೆಗೆ:

![screenshot](images/rps-ascii-challenge.png)

ಎಲ್ಲಿ:

    rock: O
    paper: ___
    scissors: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

ಸುಳಿವುಗಳು:

![screenshot](images/rps-ascii-rock.png)

![screenshot](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

ಸುಳಿವು:

![screenshot](images/rps-player-ascii.png)

` end = ' ' `ಅನ್ನು `print` ಕೊನೆಯಲ್ಲಿ ಸೇರಿಸುವುದನ್ನು ನೆನಪಿಡಿ ಇದರಿಂದ ಹೊಸ ಸಾಲಿನ ಬದಲಿಗೆ ಅದನ್ನು ಸ್ವಲ್ಪ ಜಾಗ ಬಿಟ್ಟು ಕೊನೆಗೊಳಿಸುತ್ತದೆ.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---