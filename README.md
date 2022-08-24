# SlutProjecktProgramering1LOLLMAOMasterMind

## Description
The program is writen in Python. The program is made so you kan play the board game Master Mind without the physical board game.

<<<<<<< HEAD
## Technology/Languages/Built
=======
## Technology
>>>>>>> 06986d62db6380d2c21dfee3699d4e9fd3c29b5b

- Python
- TKinter

<<<<<<< HEAD
## Requirements/Prerequisites
=======
## Requirements
>>>>>>> 06986d62db6380d2c21dfee3699d4e9fd3c29b5b
- Python 3.9.6
- TKinter library

## Installation

This project is tested with Python version Python 3.9.6. To install Python visit (https://www.python.org/downloads/)
[Follow the link for the latest version.]

Clone repository
```cmd
git clone 

https://github.com/Dripmaster69/SlutProjecktProgramering1LOLLMAOMasterMind
```
## Code conventions

pep-8

## How it works

Playing Master Mind means that the computer generates a list of colors that are not displayed to the user and then the user must guess which colors are in the list and also guess which place in the list the color is on. You guess in rounds so first you guess all the colors in the list and the results you can get back are red which means that the color is not in the list, yellow if the color is in the list but in the wrong place and green if the color is in the list and is on right place. When all results show green, it means that all colors have been placed in the correct order and the player who guessed his list first and within 9 rounds or if you play alone, guess the right order within 9 rounds you win the game.

<<<<<<< HEAD
Komplicated code in the program:
=======
Complicated code in the program:
>>>>>>> 06986d62db6380d2c21dfee3699d4e9fd3c29b5b

The code make sure that the checking of the guesses sends out the right hint for the spot in the list it is currently checking (This code was added because in the event that the same color repeted it self the checking metod would change a already correctly given hint into the wrong one because the code checked each answer from the begining before).

```python
for x in range(lenght):
    if attempt == sequence[x].value:
        if x < counter:
            if attempts[x] != sequence[x].color:
                return "🟡"
        if x > counter:
            return "🟡"
```

The code creats a window with a grid of a bunch of small windows. The grid is 5 by 3 and this is used because windows can take alot more commands then a the .grid command. This healps with spaceing and structure of the window.

```python
window = tk.Tk()

for y in range(5):
    window.columnconfigure(y, weight=1, minsize=75)
    window.rowconfigure(y, weight=1, minsize=50)
    for x in range(3):
        frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
        frame1.grid(row=y, column=x, padx=5, pady=5)
```

## Example

<<<<<<< HEAD
Code with TKinter:

Code with TKinter:

## To do/Roadmap
=======
Code without TKinter:

![Skärmklipp2](https://user-images.githubusercontent.com/95741620/168275614-cdc9581e-f014-4a19-8d14-7a8c14216f79.PNG)

Code with TKinter:

![Skärmklipp](https://user-images.githubusercontent.com/95741620/168275569-24abcd9c-5dac-4c9d-9cfd-f186069d01df.PNG)

## To do
>>>>>>> 06986d62db6380d2c21dfee3699d4e9fd3c29b5b

- [ ] Code the functions of the buttons
- [ ] Connect the TKinter code with the game code
- [ ] Give the TKinter window a background
- [ ] Add language
<<<<<<< HEAD
    - [x] Swedish
    - [ ] English
=======
    - [ ] Swedish
    - [x] English
>>>>>>> 06986d62db6380d2c21dfee3699d4e9fd3c29b5b
- [ ] Code a AI
- [ ] Code gamemode 3 (You vs computer/AI)
- [ ] Set up a wedsite/platform for the game

## Changelog

### Version 1.0.1

#### Added or changed

- Added the class Contains and Game
- Added Alpha version of the Main funktion

### Version 1.0.2

#### Added or changed

 - Added Beta version of the Main funktion
 - Added more methods for the Game class

### Version 1.0.3

#### Added or changed

 - Added a new class called Player
 - Added a general gamemode 1 method for the class Game
 - Added a gamemode 2 method for the class Game

#### Removed

- Removed old/nongeneral version of gamemode 1 method in the class Game

### Version 1.0.4

#### Added or changed

 - Added bug fixing code

#### Removed

 - Removed nonfunktioning and nonoptimised code.

### Version 1.0.5

#### Added or changed

 - Added Alpha version of Tkinter code

### Version 1.0.6

#### Added or changed

 - Changed the TKinter code strukture to fit/fit better with TKinters syntax

<<<<<<< HEAD
### Version 1.0.6
=======
### Version 1.0.7
>>>>>>> 06986d62db6380d2c21dfee3699d4e9fd3c29b5b

#### Added or changed

 - Added Doc Strings

## Contribution

As an assessment has not yet been made of the task, no pull requests are allowed. As soon as an assessment has been made, this will be allowed.

In the event of major changes, I want an issue to be opened up for discussion about what should be changed.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

<<<<<<< HEAD
***Skriv här hur du blir kontaktad ifall det finns frågor om projektet***

=======
>>>>>>> 06986d62db6380d2c21dfee3699d4e9fd3c29b5b
Maximilian Waldenfeldt Uggla - Twitter: @Mutheruggla - Discord: Puggla#0380 - maxi.uggla@gmail.com

Project link: https://github.com/Dripmaster69/SlutProjecktProgramering1LOLLMAOMasterMind

## Acknowledgments

<<<<<<< HEAD
- "Niclas Lund"
- [TKinter tutorial](https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter)
=======
- Niclas Lund
- [TKinter tutorial](https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter)
>>>>>>> 06986d62db6380d2c21dfee3699d4e9fd3c29b5b
