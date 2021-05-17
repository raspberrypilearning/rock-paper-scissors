\--- challenge \---

## التحدي: رسم ASCII

هل يمكنك استخدام رسم ASCII بدلًا من استخدام الأحرف r وp وs لتمثيل الحجر والورقة والمقص؟

مثال:

![لقطة الشاشة](images/rps-ascii-challenge.png)

عندما:

    rock: O
    paper: ___
    scissors: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

تلميحات:

![لقطة الشاشة](images/rps-ascii-rock.png)

![لقطة الشاشة](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

تلميح:

![لقطة الشاشة](images/rps-player-ascii.png)

تذكر أن إضافة `end=' '` إلى نهاية `print` تجعل المقطع البرمجي ينتهي بمسافة بدلًا من سطر جديد.

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---