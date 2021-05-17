\--- challenge \---

## 挑戰：ASCII藝術

除了使用字母r、p和s代表石頭、布和剪刀，你可以利用ASCII藝術來表現嗎？

例如：

![截圖](images/rps-ascii-challenge.png)

當：

    石頭: O
    布: ___
    剪刀: >8
    

+ Instead of saying `print (computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

提示：

![截圖](images/rps-ascii-rock.png)

![截圖](images/rps-comment-computer.png)

+ Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

提示:

![截圖](images/rps-player-ascii.png)

記得在 `print` 後面加上 `end=' '` ，這樣才會印在同一行。

+ Include a line to print `vs` between the player and computer results.

    print('vs', end=' ')
    

\--- /challenge \---