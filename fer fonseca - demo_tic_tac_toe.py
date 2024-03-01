import os
os.system("cls")

class Board():
	def __init__(self):
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

board = Board()

def print_header():
	print("Welcome to Tic-Tac-Toe ! Project in progress by: Fernando Fon :)")

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

	o_choice = int(input("O) Please choose a tile (1 - 9): "))
	board.update_tile(o_choice, "O")