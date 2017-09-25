class game:
	def playGround(self, board): #Prints out the board.
	    print('   |   |')
	    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	    print('   |   |')
	    print('-----------')
	    print('   |   |')
	    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	    print('   |   |')
	    print('-----------')
	    print('   |   |')
	    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	    print('   |   |')

	def draw(self, board): #Checks if the game is draw.
		count = 1
		for i in range(1, len(board)):
			if board[i] != " ":
				count += 1
		if count == 10:
			return True


	def checkIfWon(self, board):#Algoritm for checking if someone won.
		x = 1 
		while x < 10: #More detail on the same algorithm in "aiMove.py"
			if (board[x] == board[x+1] 
			and board[x] == board[x+2] 
			and board[x] != " "): 
				return True
			else: 
				x += 3
		x = 7
		while x < 10:
			if (board[x] == board[x-3] 
			and board[x] == board[x-6] 
			and board[x] != " "): 
				return True
			else: 
				x += 1
		x = 7 
		y = 2
		y2 = 4
		while x < 10:
			if (board[x] == board[x-y] 
			and board[x] == board[x-y2] 
			and board[x] != " "):
				return True
			else:
				x += 2
				y *= 2
				y2 *= 2

	def makeMove(self, board, player): #Gives the player a chance to take a unused place on the board.
		move = int(input("Use your notepad: "))
		if move > 0 and move < 10 and board[move] == " ":
			board[move] = player
		else:									
			print "Invalid input..."
			makeMove(board, player)

	#My own making of "new line"
	def nl(self, gamemode): 
		if gamemode:
			print "\n"*11
		else: 
			print "\n"*10