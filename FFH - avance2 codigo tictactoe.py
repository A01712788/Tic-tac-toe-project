import os
os.system("cls")

class Board():
	def __init__(self): #defines the class
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

	def display(self):
		print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
		print("-----------")
		print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
		print("-----------")
		print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

	def update_tile(self, tile_no, player):
		if self.cells[tile_no] == " ":
			self.cells[tile_no] = player
	
	def winner(self, player):
		if self.cells[1]==player and self.cells[2]== player and self.cells[3]== player: #checks if theres X or O in rows number 1,2,3
			return True 
		if self.cells[4]==player and self.cells[5]== player and self.cells[6]== player: #checks if theres X or O in rows number 4,5,6
			return True 
		if self.cells[7]==player and self.cells[8]== player and self.cells[9]== player: #checks if theres X or O in rows number 7,8,9
			return True 
		if self.cells[1]==player and self.cells[5]== player and self.cells[9]== player: #check if theres X or O in rows number 1,2,3
			return True 
		if self.cells[3]==player and self.cells[5]== player and self.cells[7]== player: #check if theres X or O in rows number 1,2,3
			return True 
		if self.cells[7]==player and self.cells[4]== player and self.cells[1]== player: #check if theres X or O in rows number 1,2,3
			return True 
		if self.cells[2]==player and self.cells[5]== player and self.cells[8]== player: #check if theres X or O in rows number 1,2,3
			return True 
		if self.cells[3]==player and self.cells[6]== player and self.cells[9]== player: #check if theres X or O in rows number 1,2,3
			return True 

		return False

	def tie_game(self): #declare function for a tie game
		used_cells = 0
		for cell in self.cells:
			if cell != " ":
				used_cells +=1
		if used_cells == 9:
			return True
		else:
			return False

	def reset_game(self):
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


board = Board()

def print_header():
	print("Welcome to Tic-Tac-Toe ! Project in progress by: Fernando Fon :)")
	print("\nHow to play: (please read before playing!!) ")
	print("1. Type the number of the tile you want X or O to be in (1-9).")
	print("2. Player 1 is X, so it will go first.")
	print("3. Once a game is over, you can always play again by typing Y/N!")
	print("Have fun!")
	print()
def refresh_screen(): #func to clear the screan
	os.system("cls")

	print_header() #show the header

	board.display() #show the board

refresh_screen()

while True:
	refresh_screen()

	x_choice = int(input("X) Please choose a tile (1 - 9): "))

	board.update_tile(x_choice, "X")

	refresh_screen()
	
	if board.winner("X"): #checks for an X win
		print("\nX wins!!\n")
		play_again = str(input("Would you like to play again? (Y/N) > ")).upper()
		if play_again == "Y":
			board.reset_game()
			continue
		else:
			print("Thanks for playing, bye!")
			break

	if board.tie_game(): #checks for a tie game after X's turn
		print("\nTie game!!\n")
		play_again = str(input("Would you like to play again? (Y/N) > ")).upper()
		if play_again == "Y":
			board.reset_game()
			continue
		else:
			print("Thanks for playing, bye!")
			break

	o_choice = int(input("O) Please choose a tile (1 - 9): "))

	board.update_tile(o_choice, "O")

	if board.winner("O"): #checks for an O win
		print("\nO wins!!\n")
		play_again = str(input("Would you like to play again? (Y/N) > ")).upper()
		if play_again == "Y":
			board.reset_game()
			continue
		else:
			print("Thanks for playing, bye!")
			break

	if board.tie_game(): #checks for a tie game after O's turn
		print("\nTie game!!\n")
		play_again = str(input("Would you like to play again? (Y/N) > ")).upper()
		if play_again == "Y":
			board.reset_game()
			continue
		else:
			break



