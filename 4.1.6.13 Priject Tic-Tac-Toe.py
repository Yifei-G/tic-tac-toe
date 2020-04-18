def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
# The output of the board should be the following:
# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   5   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+

	horizonLine= "+-------+-------+-------+"
	verticalLine ="|"+"       |"+"       |"+"       |"
	for rows in board:
		print(horizonLine)
		print(verticalLine)
		print("|   "+rows[0]+"   |   "+rows[1]+"   |   "+rows[2]+"   |")
		print(verticalLine)
	else:
		print(horizonLine)


def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
	#Check if the number entered is valid
	try:
		userMove = int(input("Enter a number between 1-9 for your move:" ))
		if userMove < 1 or userMove > 9:
			print("Please don't trick me, I am a sophisicate program! please enter a valid number!")
			return EnterMove(board)
		
		#Updating the board	
		else:
			setMove = False
			for rows in board:
				for index in range (len(rows)):
					if str(userMove) == rows[index]:
						rows[index] = "O"
						setMove = True
					else:
						continue

			#If user choose a already taken number, force user to choose a new number			
			if (setMove is not True):
				print("The field you choose is already taken, please enter a new number")
				EnterMove(board)

	#user enters a string, thrown ValueError message
	except ValueError:
		print("Please don't trick me, I am a sophisicate program! You didn't enter a number at all!")
		return EnterMove(board)

	DisplayBoard(board)
	freeList = MakeListOfFreeFields(board)
	return freeList

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#Output example: [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    freeList = []
    freeSpace = ()
    for row in range(len(board)):
        for column in range (len(board)):
        	#Check is the position is a number (not O and not X)
            if (board[row][column] is not "O") and (board[row][column] is not "X") :
                freeSpace=(row,column)
                freeList.append(freeSpace)
    return freeList

def VictoryFor(board, freeList):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
	xWin = ["X","X","X"]
	oWin = ["O","O","O"]
	newBoard = []
	newBoard1=[]
	i = 0
	j = 0

	def parseBoard (gameBoard):
		checkCounter = 0
		for rows in gameBoard:
			checkCounter +=1
			result = winnerCheck(rows,len(gameBoard),checkCounter)
			if result:
				return result

	#This is a inner function to check the winner of the game
	#return True or None to determine if the game is over or should be continued
	def winnerCheck (checkList,totalRows,checkCounter):
		if checkList == xWin:
			print("Opss... I guess my program is just too clever for you, but don't worry you can always try again!")
			return True

		elif checkList == oWin:
			print("Congrats! You win the game!!!")
			return True

		else:
			#This is the tie situation, if no more available moves and checked all the rows with no winning situation
			if (freeList == []) and (checkCounter == totalRows):
				print("This is a Tie!!")
				return True
			return None


	#This is the first winning situation, any row has three-"O" or three-"X" in a roll
	#Output: [["1","2","3"],["4","5","6"],["7","8","9"]]
	gameOver = parseBoard(board)
	if gameOver:
		return gameOver


	#This is the second winning situation, any colum has three-"O" or three-"X" in a roll
	#Output: [["1","4","7"],["2","5","8"],["3","6","9"]]
	while i < len(board):
		newRow = []
		for rows in board:
			newRow.append(rows[i])
		newBoard.append(newRow)	
		i+=1

	gameOver = parseBoard(newBoard)
	if gameOver:
		return gameOver

	#This is the third winning situation, the 2 diagonal has three-"O" or three-"X" in a roll
	#the diagonal is row0[0] row1[1] row2[2] and row0[2] row1[1] row2[0]
	#The output is [["1","5","9"],["3","5","7"]]
	i = 0
	while i<2:
		newRow=[]
		for rows in board:
			newRow.append(rows[j])
			if i < 1:
				j+=1
			else:
				j-=1

		newBoard1.append(newRow)
		i+=1
		j-=1

	gameOver = parseBoard(newBoard1)
	if gameOver:
		return gameOver

def DrawMove(board,freePositionList):
#
# the function draws the computer's move and updates the board
#
    computerMove = ()
    i=0
    FoundvalidMove = False

    while (FoundvalidMove is False):
    	#generate a random position, the output example (1,2)
        while i < 2:
            computerMove += (randrange(3),)
            i+=1

        if computerMove in freePositionList:
            board[computerMove[0]][computerMove[1]] = "X"
            FoundvalidMove = True
        #If the random posisiton is not free anymore, force the program to generate new position
        else:
        	computerMove = ()
        	i=0

    freeList = MakeListOfFreeFields(board)
    DisplayBoard(board)
    return freeList

from random import randrange
# Use the init function to include all the functions need to be initialized when launching the program
def Init():
	freeList = []
	board = [["1","2","3"],["4","X","6"],["7","8","9"]]
	print("Welcome to Yoki's Tic-Tac-Toe challenge! Let's have some fun during the COVID-19 quarentine period!!!")
	DisplayBoard(board)

	while True:	
		#User's turn
		freeList = EnterMove(board)
		endOfGame = VictoryFor(board,freeList)
		if endOfGame:
			break

		#Computer's turn
		freeList = DrawMove(board,freeList)
		endOfGame = VictoryFor(board,freeList)
		if endOfGame:
			break
	print("Game is over!!! Thanks for playing!!")

Init()