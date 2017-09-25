import random 
from game import *
class ai:
	game = game()

	def copy(self, board): #Makes a copy of main board.
		copyBoard = board
		return copyBoard
#Checks if can win with next move.
	def checkIfCanWin(self, user, x, board, realBoard): 
		for i in range(1, len(board)):
			if board[i] == " ":
				board[i] = user
				if checkIfWond(board):
					realBoard[i] = x
					return True
					board[i] = " "
					break
				else:
					board[i] = " "
#Takes a random place in board and placeses it.
	def _randomMove(self, user, board):
		taken = False
		while taken == False:
			rnd = random.randrange(1, len(board))
			if board[rnd] == " ":
				board[rnd] = user
				taken = True 

#Not in use.
	def _aiMove(self, move, board, user):
		board[move] = user


#Algorithm for checking if the current board has a winner. 
def checkIfWond(board):
		x = 1 
		while x < 10: #Checks from bottom left to right, and upwards.
			if (board[x] == board[x+1] 
			and board[x] == board[x+2] 
			and board[x] != " "): 
				return True
			else: 
				x += 3
		x = 7
		while x < 10: #Checks from top left to bot, and going right.
			if (board[x] == board[x-3] 
			and board[x] == board[x-6] 
			and board[x] != " "): 
				return True
			else: 
				x += 1
		x = 7 
		y = 2
		y2 = 4
		while x < 10: #Checks diagonal from top left to bottom right, and top right to bottom left.
			if (board[x] == board[x-y] 
			and board[x] == board[x-y2] 
			and board[x] != " "):
				return True
			else:
				x += 2
				y *= 2
				y2 *= 2