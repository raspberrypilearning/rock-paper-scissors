## Player's turn

First, let the player choose Rock, Paper or Scissors. 

--- task ---
Open the [Rock, Paper, Scissors](https://editor.raspberrypi.org/en/projects/rock-paper-scissors-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.
--- /task ---

The project already contains the code to import a function that you are going to use in this project. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1
---
from random import randint
--- /code ---
  
You'll use `randint` later to generate random numbers.

--- task ---

First, let the player choose Rock, Paper or Scissors by typing the letter 'r', 'p' or 's'. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 3
---
from random import randint
  
player = input('rock (r), paper (p) or scissors (s)?')
--- /code ---

--- /task ---

--- task ---

Now print out what the player chose:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 5
---
player = input('rock (r), paper (p) or scissors (s)?')

print(player, 'vs')
--- /code ---

--- /task ---  

--- task ---

Test your code by clicking `Run`. Click in the editor output window and enter your choice. 

--- /task ---  



