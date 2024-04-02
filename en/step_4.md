## Check the result

Now add the code to see who won. 

--- task ---

You need to compare the `player` and `computer` variables to see who won. 

If they are the same then it is a draw:
  
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 19
line_highlights: 21-22
---
print(computer)

if(player == computer):
    print('DRAW!')
--- /code ---

--- /task ---

--- task ---

Test your code by playing the game a few times until you get a draw. 

You'll need to click **Run** to start a new game. 

--- /task ---

Now look at the cases where the player chose 'r' (rock) but the computer didn't.

If the computer chose 's' (scissors) then the player wins (rock beats scissors). 
  
If the computer chose 'p' (paper) then the computer wins (paper beats rock).

--- task ---

Check the player choice *and* the computer choice using `and`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 24-28
---
if(player == computer):
    print('DRAW!')
  
elif(player == 'r' and computer == 's'):
    print('Player wins!')
  
elif(player == 'r' and computer == 'p'):
    print('Computer wins!')
--- /code ---

--- /task ---

--- task ---

Next look at the cases where the player chose 'p' (paper) but the computer didn't by adding more `elif` conditions.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 30-34
---
elif(player == 'r' and computer == 's'):
    print('Player wins!')
  
elif(player == 'r' and computer == 'p'):
    print('Computer wins!')

elif(player == 'p' and computer == 'r'):
    print('Player wins!')
  
elif(player == 'p' and computer == 's'):
    print('Computer wins!')
--- /code ---

--- /task ---

--- task ---

Finally, add the code to check for the winner when the player chose 's' (scissors) and the computer chose rock or paper.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 30
line_highlights: 36-40
---
elif(player == 'p' and computer == 'r'):
    print('Player wins!')
  
elif(player == 'p' and computer == 's'):
    print('Computer wins!')

elif(player == 's' and computer == 'p'):
    print('Player wins!')
  
elif(player == 's' and computer == 'r'):
    print('Computer wins!')
--- /code ---

--- /task ---

--- task ---

Now play the game to test your code. 

Click **Run** to start a new game. 

--- /task ---


 

  


