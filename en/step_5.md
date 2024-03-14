--- challenge ---
## Challenge: ASCII Art

Instead of using the letters r, p and s to represent rock, paper and scissors, can you use ASCII art?

Where:

```
rock: O
paper: ___
scissors: >8
```

### Hints

--- task ---

Instead of saying `print(computer)` you'll need to add a new line to each of the options in the `if` to print out the correct ASCII art. 

--- code ---
---
language: python
filename: 
line_numbers: false
line_number_start: 
line_highlights: 
---
if(chosen == 1):
    computer = 'r'
    print('O')
--- /code ---

--- /task ---    

--- task ---

Instead of saying `print (player)` you'll need to add a new if statement to check which item the player chose and print out the correct ASCII art:

--- code ---
---
language: python
filename: 
line_numbers: false
line_number_start: 
line_highlights: 
---
if(player == 'r'):
    print('O')
--- /code ---

--- /task ---

--- task ---

Remember that adding `end=' '` to the end of a `print` makes it end with a space instead of a new line. 

--- code ---
---
language: python
filename: 
line_numbers: false
line_number_start: 
line_highlights: 
---
if(player == 'r'):
    print('O', end=' ')
--- /code ---
--- /task ---

--- task ---

Include a line to print `vs` between the player and computer results.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
print('vs', end=' ')
--- /code ---

--- /task ---

--- /challenge ---
