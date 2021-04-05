#This is a TicTacToe game that is played in the console
#@author Marius Haueis
#@version 05.04.2021

#Global variables
# Gameboard
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
gameStillGoing = True
winner = None
currentPlayer = "X"

#visualize Gameboard
def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Handles the players moves
def handleTurn():
    position = input("Choose a position from 1-9: ")
    position = int(position) -1
    if board[position] != "-":
        print("The coosen Tile has been filled, choose another Tile.")
        handleTurn()
    else:
        board[position] = currentPlayer
        displayBoard()

#Checks if the game is over
def checkIfGameOver():
    if checkIfWin():
        print("")
        print(currentPlayer + " wins.")  
        print("Congratulations!!!")     
    elif checkIfTie():
        print("The result is a tie.")
        

# returns wheter the game has been won
def checkIfWin():
    global winner
    global gameStillGoing
    #check rows
    if checkRows() or checkColumns() or checkDiagnols():
        gameStillGoing = False
        return True
    
#returns the winning player
def checkRows():    
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        return True
        
#returns the winning player
def checkColumns():
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        return True
 
def checkDiagnols():
    diagnol1 = board[0] == board[4] == board[8] != "-"
    diagnol2 = board[2] == board[4] == board[6] != "-"   
    if diagnol1 or diagnol2:
        return True
    


#checks if the board is full
def checkIfTie():
    for n in board:
        if n == "-":
            return False
    gameStillGoing = False
    return True   

#returns the player that is not the current player
def flipPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#Gameplay Mainfunction
def playGame():
    global gameStillGoing
    displayBoard()
    while gameStillGoing:
        print("It's " + currentPlayer+ " turn, please make your move.")
        handleTurn()       
        checkIfGameOver()
        flipPlayer()
playGame()