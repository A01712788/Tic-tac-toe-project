import os

# function to clear the screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Board():
    def __init__(self): # defines the class
        self.cells = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.cells:
            print(" | ".join(row))
            print("-----------")

    def update_tile(self, row, col, player):
        self.cells[row][col] = player

    def winner(self, player):
        # Check rows
        for row in self.cells:
            if all(tile == player for tile in row):
                return True

        # Check columns
        for col in range(3):
            if all(row[col] == player for row in self.cells):
                return True

        # Check diagonals
        if all(self.cells[i][i] == player for i in range(3)) or \
           all(self.cells[i][2-i] == player for i in range(3)):
            return True

        return False

    def tie_game(self):
        return all(tile != " " for row in self.cells for tile in row)

    def reset_game(self):
        self.cells = [[" " for _ in range(3)] for _ in range(3)]

board = Board()

def print_header():
    print("Welcome to Tic-Tac-Toe! Project in progress by: Fernando Fon :)")
    print("\n---------------- How to play: (please read before playing!!) ---------------")
    print("1. Type the row and column number of the tile you want X or O to be in (0-2).")
    print("2. Player 1 is X, so it will go first.")
    print("3. Once a game is over, you can always play again by typing Y/N!")
    print("-------------------------------- Have fun! ---------------------------------\n")

def refresh_screen():
    clear_screen()
    print_header()
    board.display()

refresh_screen()

while True:
    refresh_screen()
    while True:
        try:
            x_row, x_col = map(int, input("X) Please choose a tile (row column) separated by a space: ").split())
            if 0 <= x_row <= 2 and 0 <= x_col <= 2:
                break
            else:
                print("Please enter row and column values between 0 and 2.")
        except ValueError:
            print("Please enter valid integers for row and column.")

    board.update_tile(x_row, x_col, "X")

    if board.winner("X"):
        refresh_screen()
        print("\nX wins!!\n")
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
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            print("Thanks for playing, bye!")
            break

    while True:
        try:
            o_row, o_col = map(int, input("O) Please choose a tile (row col): ").split())
            if 0 <= o_row <= 2 and 0 <= o_col <= 2: # check if row and column values are within the valid range
                break
            else:
                print("Please enter row and column values between 0 and 2.")
        except ValueError:
            print("Please enter valid integers for row and column.")

    board.update_tile(o_row, o_col, "O")

    if board.winner("O"):
        refresh_screen()
        print("\nO wins!!\n")
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
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            print("Thanks for playing, bye!")
            break
