import os

SCOREBOARD_FILE = "tictactoe_score.txt"

# function to clear the screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Board():
    def __init__(self): # defines the class and initializes the game board
        self.cells = [[" " for _ in range(3)] for _ in range(3)]

    def display(self): # function to display the game board
        for row in self.cells: # iterates through each row
            print(" | ".join(row))
            print("-----------")

    def update_tile(self, row, col, player): # function to update a tile on the game board
        if self.cells[row][col] == " ":  # check if tile is empty
            self.cells[row][col] = player # sets the chosen tile to the player's symbol (X or O)
            return True
        else:
            print("Tile already occupied. Please choose another tile.")
            return False

    def winner(self, player): # function to check if a player has won
        # Check rows
        for row in self.cells:
            if all(tile == player for tile in row):
                return True

        # check columns in case of winning
        for col in range(3): # iterates through each column
            if all(row[col] == player for row in self.cells): # checks if all tiles in a column belong to the same player
                return True # returns True if a player has won

        # check diagonals in case of winning
        if all(self.cells[i][i] == player for i in range(3)) or \
           all(self.cells[i][2-i] == player for i in range(3)):
            return True

        return False

    def tie_game(self): # function to check if the game is a tie
        return all(tile != " " for row in self.cells for tile in row)

    def reset_game(self): # function to reset the game board
        self.cells = [[" " for _ in range(3)] for _ in range(3)]

board = Board() # creates an instance of the Board class

def load_scoreboard(): # function to load the scoreboard from a file
    if not os.path.exists(SCOREBOARD_FILE):
        return {"X_wins": 0, "O_wins": 0, "X_losses": 0, "O_losses": 0}
    else:
        with open(SCOREBOARD_FILE, "r") as file:
            data = file.read().splitlines()
            scoreboard = {
                "X_wins": int(data[1].split(": ")[1]),
                "O_wins": int(data[2].split(": ")[1]),
                "X_losses": int(data[3].split(": ")[1]),
                "O_losses": int(data[4].split(": ")[1])
            }
        return scoreboard

def save_scoreboard(scoreboard): # function to save the scoreboard to a file
    with open(SCOREBOARD_FILE, "w") as file: # opens the scoreboard file in write mode
        file.write("SCOREBOARD\n")
        file.write("Wins of X: {}\n".format(scoreboard["X_wins"]))
        file.write("Wins of O: {}\n".format(scoreboard["O_wins"]))
        file.write("Losses of X: {}\n".format(scoreboard["X_losses"]))
        file.write("Losses of O: {}\n".format(scoreboard["O_losses"]))

def print_scoreboard(scoreboard): # function to print the scoreboard
    print("SCOREBOARD")
    print("Wins of X:", scoreboard["X_wins"])
    print("Wins of O:", scoreboard["O_wins"])
    print("Losses of X:", scoreboard["X_losses"])
    print("Losses of O:", scoreboard["O_losses"])

def print_header(): # function to print the game header
    print("Welcome to Tic-Tac-Toe! Project by: Fernando Fonseca A01712788")
    print("\n---------------- How to play: (please read before playing!!) ---------------")
    print("1. Type the row and column number of the tile you want X or O to be in (0-2).")
    print("2. Player 1 is X, so it will go first.")
    print("3. Once a game is over, you can always play again by typing Y/N!")
    print("-------------------------------- Have fun! ---------------------------------\n")

def refresh_screen():  # function to refresh the screen
    clear_screen() # clears the screen
    print_header() # prints the game header
    board.display() # displays the game board

scoreboard = load_scoreboard() # loads the scoreboard

refresh_screen() # refreshes the screen to display the game board

while True: # main game loop for 'X' player
    refresh_screen() # refreshes the screen at the start of each turn
    while True:
        try:
            x_row, x_col = map(int, input("X) Please choose a tile (row column) separated by a space: (e.g. 0 1): ").split())
            if 0 <= x_row <= 2 and 0 <= x_col <= 2:
                if board.update_tile(x_row, x_col, "X"):
                    refresh_screen()
                    break
            else:
                print("Please enter row and column values between 0 and 2.")
        except ValueError:
            print("Please enter valid integers for row and column.")

    if board.winner("X"):
        scoreboard["X_wins"] += 1
        scoreboard["O_losses"] += 1
        save_scoreboard(scoreboard)
        refresh_screen()
        print("\nX wins!!\n")
        print_scoreboard(scoreboard)
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            print("Thanks for playing, bye!")
            break

    if board.tie_game():
        refresh_screen()
        print("\nTie game!!\n")
        print_scoreboard(scoreboard)
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            print("Thanks for playing, bye!")
            break

    while True: # main game loop for 'O' player
        try:
            o_row, o_col = map(int, input("O) Please choose a tile (row column) separated by a space: (e.g. 0 1): ").split())
            if 0 <= o_row <= 2 and 0 <= o_col <= 2: # check if row and column values are within the valid range
                if board.update_tile(o_row, o_col, "O"):
                    refresh_screen()
                    break
            else:
                print("Please enter row and column values between 0 and 2.")
        except ValueError:
            print("Please enter valid integers for row and column.")

    if board.winner("O"):
        scoreboard["O_wins"] += 1
        scoreboard["X_losses"] += 1
        save_scoreboard(scoreboard)
        refresh_screen()
        print("\nO wins!!\n")
        print_scoreboard(scoreboard)
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            print("Thanks for playing, bye!")
            break

    if board.tie_game():
        refresh_screen()
        print("\nTie game!!\n")
        print_scoreboard(scoreboard)
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            print("Thanks for playing, bye!")
            break
