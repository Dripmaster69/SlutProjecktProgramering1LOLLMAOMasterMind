# TODO:
# Kommentera ditt program (engelska)
# tkinter

#imports
import sys
import random
import tkinter

#Classes
class Contains:
    def __init__(self, color: str, value: str) -> None:
        self.color = color
        self.value = value

    def get_color(self): 
        """_Gets the a string with the colors name_

        Returns:
            _String_: _Returns the specified color for example Red or Blue_
        """
        return self.color

    def get_value(self): 
        """_Gets the value given to a color_

        Returns:
            _Str_: _A Tag for each individual color to easier identify them_
        """
        return self.value

class Game:
    def __init__(self, name, sequence) -> None:
        self.name = name
        self.sequence = sequence

    def __str__(self, lenght) -> str: 
        slot = ""
        for x in range(lenght):
            slot += ("___ ")
        return f"""
        Welcome to {self.name}, the secret sequense is {len(self.sequence)} slots long, start guessing!
        The sequence can only contain Red, Yellow, Blue, Orange, Green and Purple.
        The sequence follows the formula: {slot}
        """
    
    def get_game_opperations(self, secret_sequence, sequence_lenght, game_mode, win_indicator, players): # Preforms the gam opperations for game mode 1 v 0 and game operations for player 1 in game mode 2
        """_Preforms the game opperations for game mode 1 and game operations for player 1 in game mode 2_

        Args: Vilka argument och dess typer kommer in?
            secret_sequence (_List_): _A randomly generated list from the possible color opptions_
            sequence_lenght (_Int_): _The lengt of the list secret_sequence specified by the user_
            game_mode (_Int_): _The game mode the user choose to play_
            win_indicator (_Int_): _A tag for the players to indicate who won_
            players (_List_): _List with the names of the players, in game mode 1 the list is filled with one empty string_
        """
        markers = []
        attempts = []
        counter = 0
        for x in secret_sequence:
            attempt = input(f"{players[0].player_name} guess the slot in the sequence starting from the left: ")
            attempt = attempt.split(" ")[0]
            attempts.append(attempt)
            markers.append(self.check_attempt(attempt, x.value, counter, attempts, sequence_lenght, secret_sequence))
            counter += 1
        string = "" 
        for x in markers:
            string += f"  {x}"
        for x in attempts:
            string += f"  {x}"
        print(string)
        if self.check_win(secret_sequence, attempts) == True:
            self.get_winner(game_mode, win_indicator, players)
        markers.clear()
        attempts.clear()
    
    def get_game_opperations2(self, secret_sequence_two, sequence_lenght, game_mode, win_indicator, players):
        """_Preform the game opperations for player 2 in game mode 2_

        Args:
            secret_sequence_two (_List_): _A randomly generated list from the possible color opptions_
            sequence_lenght (_Int_): _The lengt of the list secret_sequence_two specified by the user_
            game_mode (_Int_): _The game mode the user choose to play_
            win_indicator (_Int_): _A tag for the players to indicate who won_
            players (_List_): _List with the names of the players_
        """
        markers = []
        attempts = []
        counter = 0
        for x in secret_sequence_two:
            attempt = input(f"{players[1].player_name} guess the slot in the sequence starting from the left: ")
            attempt = attempt.split(" ")[0]
            attempts.append(attempt)
            markers.append(self.check_attempt(attempt, x.value, counter, attempts, sequence_lenght, secret_sequence_two))
            counter += 1
        string = "" 
        for x in markers:
            string += f"  {x}"
        for x in attempts:
            string += f"  {x}"
        print(string)
        if self.check_win(secret_sequence_two, attempts) == True:
            self.get_winner(game_mode, win_indicator, players)
        markers.clear()
        attempts.clear()
    
    def get_game_opperations3():
        pass

    def check_attempt(self, attempt, value, counter, attempts, lenght, sequence):
        """_Converts the users attepts to the colors assigned value and then checks if the guess is correct, checks if the color is in the sequence and if the guess is incorrect_

        Args:
            attempt (_Str_): _The users guess of a sertain slot in the sequence_
            value (_Str_): _The value associated with a sertain color_
            counter (_Int_): _Function uses the varible to check answers so we dont reassign previus correct answers with almost right answers_
            attempts (_List_): _List of all previus gusses made by a player so we dont reassign previus correct answers with almost right answers_
            lenght (_Int_): _The lengt of the sequence the user is trying to guess_
            sequence (_list_): _The sequence the user is trying to guess_

        Returns:
            _Str_: _With an emoji with apropriate color for the correctness of the guess_
        """
        if attempt == "Red":
            attempt = "1"
            if attempt == value:
                return "🟢"
        if attempt == "Yellow":
            attempt = "2"
            if attempt == value:
                return "🟢"
        if attempt == "Blue":
            attempt = "3"
            if attempt == value:
                return "🟢"
        if attempt == "Orange":
            attempt = "4"
            if attempt == value:
                return "🟢"
        if attempt == "Green":
            attempt = "5"
            if attempt == value:
                return "🟢"
        if attempt == "Purple":
            attempt = "6"
            if attempt == value:
                return "🟢"
        for x in range(lenght):
            if attempt == sequence[x].value:
                if x < counter:
                    if attempts[x] != sequence[x].color:
                        return "🟡"
                if x > counter:
                    return "🟡"
        return "🔴"
    
    def check_win(self, sequence, attempts):
        """_Checks if a player has guess all the right colors in the sequence_

        Args:
            sequence (_List_): _The sequence the user is trying to guess_
            attempts (_List_): _List of all previus gusses made by a player so we can check if they are the same as sequence_

        Returns:
            _Bool_: _Bool tells us if a turn of guesses ha sresulted in guessing the right sequence_
        """
        index = 0
        for x in sequence:
            if x.color != attempts[index]:
                return False
            index += 1
        return True

    def get_winner(self, game_mode, win_indicator, players):
        """_Gets the winner for game modes 1, 2 and 3_

        Args:
            game_mode (_Int_): _The game mode the user chose to play_
            win_indicator (_Int_): _A tag for the players to indicate who won_
            players (_List_): _List with the names of the players_
        """
        if game_mode == 1 or game_mode == 3:
            print("You won!")
            sys.exit()
        if win_indicator == 1:
            print(f"{players[0].player_name} wins!")
            sys.exit()
        if win_indicator == 2:
            print(f"{players[1].player_name} wins!")
            sys.exit()
        
class Player:
    def __init__(self, player_name: str) -> None:
        self.player_name = player_name

    def get_player_name(self):
        """_Gets the players name that has been put in by the user_

        Returns:
            _Str_: _Returns a string with the name of the player_
        """
        return self.player_name

class Computer:
    pass

def initialize_game(sequence_options : list):
    """_Creats a list of all colors and values assigned to those colors as well as creats class instances_

    Args:
        sequence_options (List): _List of all the possible colors a slot in the sequence can be filld with_
    """
    sequence_options.append(Contains("Red", "1"))
    sequence_options.append(Contains("Yellow", "2"))
    sequence_options.append(Contains("Blue", "3"))
    sequence_options.append(Contains("Orange", "4"))
    sequence_options.append(Contains("Green", "5"))
    sequence_options.append(Contains("Purple", "6"))

# Main function
def main():
    print("""
            Menu
        1. for 1 vs 0
        2. for 1 vs 1
        3. for 1 vs Computor
    """)
    a = True
    while a:
        game_mode = int(input("Your Choice: "))
        if game_mode == 1 or game_mode == 2 or game_mode == 3:
            a = False
    sequence_lenght = int(input("How long do you want the secret sequence to be: "))
    sequence_options = []
    secret_sequence = []
    secret_sequence_two = []
    initialize_game(sequence_options)
    for x in range(sequence_lenght):
        secret_sequence.append(sequence_options[random.randint(0, 5)])
    if game_mode == 2:
        for x in range(sequence_lenght):
            secret_sequence_two.append(sequence_options[random.randint(0, 5)])

    the_game = Game("Master Mind", secret_sequence)
    if game_mode == 1:
        players = []
        players.append(Player(""))
        print(the_game.__str__(sequence_lenght))
        for x in range(8):
            print(f"Round {x+1} of 9")
            the_game.get_game_opperations(secret_sequence, sequence_lenght, 1, 1, players)
        print("You lost!")
        sys.exit()
    if game_mode == 2:
        players = []
        player_one = input("Write player1's name: ")
        player_two = input("Write player2's name: ")
        players.append(Player(f"{player_one}"))
        players.append(Player(f"{player_two}"))
        print(the_game.__str__(sequence_lenght))
        for x in range(8):
            print(f"Round {x+1} of 9")
            the_game.get_game_opperations(secret_sequence, sequence_lenght, 2, 1, players)
            the_game.get_game_opperations2(secret_sequence_two, sequence_lenght, 2, 2, players)

if __name__ == "__main__":
    main()