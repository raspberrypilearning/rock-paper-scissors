\--- challenge \---

## 挑战：ASCII 艺术图形

你能使用ASCII码图像替代字母r，p和s，来代表石头，布和剪刀吗？

例如：

![截图](images/rps-ascii-challenge.png)

其中：

    石头：O
    布：___
    剪刀：>8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

提示：

![截图](images/rps-ascii-rock.png)

![截图](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

提示：

![截图](images/rps-player-ascii.png)

记得在`print`中添加`end =' '`使它以空格结束而不是另起一行。

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- challenge \---