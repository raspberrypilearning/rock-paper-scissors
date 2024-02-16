## Computer's Turn

Now it's the computer's turn. You can use the `randint` function to generate a random number to decide between rock, paper and scissors. 

--- task ---

Use `randint` to generate a random number to decide whether the computer has chosen rock, paper or scissors.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 7-8
---
player = input('rock (r), paper (p) or scissors (s)?')

print(player, 'vs')

chosen = randint(1,3)
print(chosen)
--- /code ---

--- /task ---

--- task ---

Run your script lots of times (you'll need to enter 'r', 'p' or 's' each time.)

You should see that 'chosen' is randomly set to either 1, 2 or 3. 

--- /task ---  
  
Let's say:
  + 1 = rock (r)
  + 2 = paper (p)
  + 3 = scissors (s)

--- task ---

  Use `if` to check if the chosen number is `1` (`==` is used to see if 2 things are the same). 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 10
---
chosen = randint(1,3)
print(chosen)

if(chosen == 1):
--- /code ---

--- /task ---

Python uses __indentation__ (moving the code to the right) to show which code is inside the `if`. You can either use two spaces (tap the spacebar four times) or tap the __tab key__ (usually above CAPSLOCK on the keyboard.)

--- task ---

Set `computer` to 'r' inside the `if` using indentation:
  
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 11
---
if(chosen == 1):
    computer = 'r'
--- /code ---

--- /task ---
  
--- task ---

You can add an alternative check using `elif` (short for _else if_):

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 13-14
---
if(chosen == 1):
    computer = 'r'

elif(chosen == 2):
    computer = 'p'
--- /code ---

--- /task ---


  This condition will only be checked if the first condition fails (if the computer didn't choose `1`)

--- task ---

Finally, if the computer didn't choose `1` or `2` then it must have chosen `3`. 

This time we can just use `else` which means otherwise. 
  
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 16-17
---
if(chosen == 1):
    computer = 'r'

elif(chosen == 2):
    computer = 'p'

else:
  computer = 's'
--- /code ---

--- /task ---

--- task ---

Now, instead of printing out the random number that the computer chose you can print the letter. 

You can add a `#` to the start of the line `print(chosen)`, to make the computer ignore it.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 8, 19
---
chosen = randint(1,3)
#print(chosen)

if(chosen == 1):
    computer = 'r'

elif(chosen == 2):
    computer = 'p'

else:
  computer = 's'

print(computer)

--- /code ---

--- /task ---

--- task ---

Test your code by clicking Run and choosing your option. 

--- /task ---   

--- task ---

The computer's choice gets printed on a new line. You can fix that by adding `end=' '` after `vs`, that tells Python to end with a space instead of a new line. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 7
---
print('vs', end=' ')

chosen = randint(1,3)
#print(chosen)
--- /code ---
--- /task ---

--- task ---

Play the game a few times by clicking Run and making a choice.

--- /task ---

For now you'll have to work out who won yourself. Next you'll add the Python code to work this out.   
  



