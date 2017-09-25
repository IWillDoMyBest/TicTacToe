import random
from game import *
from aiMove import *


def turnGen(): #letting someone random start.
	randoms = random.getrandbits(1)
	if randoms == 1:
		return True
	else: 
		return False

def gamePlay(): #The "game" start point.
	tictactoe = [" "]*10

	hero = turnGen()
	if hero:
		player = "x"
		aiHero = "o"
	else:
		player = "o"
		aiHero = "x"

	on = True

	if turnGen():
		turn = True
	else:
		turn = False

	while on: #The game loop.
		game.playGround(tictactoe)
		game.nl(on)

		if turn: #Players turn.
			try: 
				game.makeMove(tictactoe, player)
			except:
				print "Invalid move!"
				game.makeMove(tictactoe, player)
		else: #Ai's turn.
			boardC = tictactoe
			if ai.checkIfCanWin(aiHero, aiHero, tictactoe, boardC):
				pass
			elif ai.checkIfCanWin(player, aiHero, tictactoe, boardC): 
				pass
			else: 
				if on:
					ai._randomMove(aiHero, tictactoe)

		if game.checkIfWon(tictactoe):#Cheking if someone won.
			game.playGround(tictactoe)
			game.nl(on)

			if turn:
				print player+" won"
			else: 
				print aiHero+" won"

			on = False
			break

		if game.draw(tictactoe): #Cheking if it's draw. 
			game.playGround(tictactoe)
			game.nl(on)

			print "Draw!"

			on = False
			break

		if turn:
			turn = False
		else: 
			turn = True

if __name__ == "__main__": #__init__
	game = game()
	ai = ai()
	gamePlay()
	again = raw_input("Press enter to play again: ")
	while again == "":
		gamePlay()
		again = raw_input("Press enter to play again: ")


	



