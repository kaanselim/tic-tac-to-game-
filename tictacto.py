theBoard = {
	'1': ' ' , '2': ' ' , '3': ' ',
	'4': ' ' , '5': ' ' , '6': ' ',
	'7': ' ' , '8': ' ' , '9': ' '
}

board_keys = []

def printBoard(board):
	print("|"+board['1']+"|"+board['2']+"|"+board['3']+"|")
	print("|"+board['4']+"|"+board['5']+"|"+board['6']+"|")
	print("|"+board['7']+"|"+board['8']+"|"+board['9']+"|")

for key in theBoard:
	board_keys.append(key)

def game():
	
	
	count = 0
	turn = 'X'


	for i in range(10):
		printBoard(theBoard)
		print("player X turn")
		move = input("pick one of the squares from 1-9\n ")


		
		if theBoard[move] == ' ':
			theBoard[move] = turn
			count +=1
		else:
			print("plesae pick an empty square")
			continue

		if count >= 5:
			# winning conditions 
			if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
				printBoard(theBoard)
				print("\nGame Over.\n")                
				print(" **** " +turn + " won. ****")                
				break
			elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
				printBoard(theBoard)
				print("\nGame Over.\n")                
				print(" **** " +turn + " won. ****")
				break
			elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
				print("\nGame Over.\n")                
				print(" **** " +turn + " won. ****")
				break
			elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
				printBoard(theBoard)
				print("\nGame Over.\n")                
				print(" **** " +turn + " won. ****")
				break
			elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
				printBoard(theBoard)
				print("\nGame Over.\n")                
				print(" **** " +turn + " won. ****")
				break
			elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
				print("\nGame Over.\n")                
				print(" **** " +turn + " won. ****")
				break 
			elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
				printBoard(theBoard)
				print("\nGame Over.\n")                
				print(" **** " +turn + " won. ****")
				break
			elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
				printBoard(theBoard)
				print("\nGame Over.\n")                
				print(" **** " +turn + " won. ****")
				break 

		if count == 9:
			print("\n game over\n")
			print("its a tie")



		if turn == "X":
			turn ="O"
		else:
			turn = "X"

	restart = input("want to replay")
	if restart == "y":
		for key in board_keys:
			theBoard[key] = " "
	game()


game()





