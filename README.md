# Wordle-Clone
- Description: A recreation of the popular game [Wordle](https://wordlegame.org/about) in python
- Contributor(s): Ari Palanjian
- [GitHub](https://github.com/aripalanjian/PLs-Proj-2.git)
## About
This project was created to demonstrate object-oriented design of a game using python and a popular 2-D
library pygame. Wordle-Clone is a multi-threaded application that is separated into two threads, one to manage 
displaying content to the screen and one to handle the game loop. The game loop is event driven and reacts according
 to user input, thus the user experience is not hampered by being singly threaded while the application waits for the next user move.
## Getting Started
- It is suggested to have at least python version 3.12 installed and on path
- Clone the repo into an appropriate repository
- If you wish for necessary packages to remain in a local scope create a virtual environment before continuing
- Install packages using the command in your terminal ```pip install -r "requirements.txt"```
## Usage
- To start run ```python3 main.py```
- Play by either using the keyboard or a mouse to click the corresponding letter guess
- Choose 5 letters to create a valid word
- The game loop will inform the player:
  -  if the word is a word in the wordle dictionary
  -  if it is the correct word
  -  if it is incorrect it will show the user:
    - if a letter is correct and in the correct postion
    - if a letter is correct and in the wrong position
    - or if a letter is not in the correct word
- Once the game is won or all chances are exhausted the user can play again or quit
- The player may also exit at any time by clicking the exit button

## Future
- Update User Interface to a more modern design
