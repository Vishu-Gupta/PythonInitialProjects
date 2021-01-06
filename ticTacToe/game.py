import random
# spots of board considered same as numpad
def drawBoard(board):
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("---------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("---------")
    print(f"{board[1]} | {board[2]} | {board[3]}")

def compMove(filledSpots):
    compMove = 0
    while compMove in filledSpots:
        compMove=random.randint(1,9)
    print(f"Comp Moves on position {compMove}")
    return compMove

def playerMove(filledSpots):
    playerMove = int(input("Your Move Man  "))
    while playerMove in filledSpots:#this logic needs to be imporved
        print("Come on Man.Check before hitting enter") 
        playerMove = int(input())
    return playerMove

def recordFilledSpots(filledSpots,move):
    filledSpots.append(move)
    return filledSpots

def updateBoardStatus(move,char,currentBoard):
    currentBoard[move]=char
    return currentBoard

def characterChoice():
    compChar = random.choice(["X","O"])
    if(compChar=="X"):
        print("Computer will play X, Player O")
        return compChar , "O"
    else :
        print("Player will play X, Computer O ")
        return compChar, "X"

def decision(currentBoard):
    return ((currentBoard[7]==currentBoard[8] and currentBoard[9]==currentBoard[8] and currentBoard[8]!=" ")or
    (currentBoard[4]==currentBoard[5] and currentBoard[6]==currentBoard[5] and currentBoard[5]!=" ")or
    (currentBoard[1]==currentBoard[2] and currentBoard[3]==currentBoard[1] and currentBoard[1]!=" ")or
    (currentBoard[7]==currentBoard[4] and currentBoard[7]==currentBoard[1] and currentBoard[1]!=" ")or
    (currentBoard[8]==currentBoard[5] and currentBoard[8]==currentBoard[2] and currentBoard[2]!=" ")or
    (currentBoard[9]==currentBoard[6] and currentBoard[9]==currentBoard[3] and currentBoard[9]!=" ")or
    (currentBoard[7]==currentBoard[5] and currentBoard[7]==currentBoard[3] and currentBoard[5]!=" ")or
    (currentBoard[1]==currentBoard[5] and currentBoard[9]==currentBoard[1] and currentBoard[5]!=" "))

#drawBoard([0,"X","O","X","O","X","O","X","X","X"]) # to check functioning of drawBoard
comp_Char,player_Char = characterChoice() # initial selection of characters
if comp_Char=="X":
    move = True #move as true will indicate its computers move 
else :
    move = False #move as false will indicate its Players move
currentBoard=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
filledSpots=[0]
while(len(filledSpots) <= 10 and  not decision(currentBoard)):
    if(move):
        comp_Move=compMove(filledSpots)
        currentBoard = updateBoardStatus(comp_Move,comp_Char,currentBoard)
        filledSpots = recordFilledSpots(filledSpots,comp_Move)
        move = False #switch to Playermove
    else :
        player_Move=playerMove(filledSpots)
        currentBoard = updateBoardStatus(player_Move,player_Char,currentBoard)
        filledSpots = recordFilledSpots(filledSpots,player_Move)
        move = True #switch to compMove
    drawBoard(currentBoard)
if len(filledSpots)==9:
    print("Match ended in Tie")
elif (not move):
    print("Match ended with Computers win")
else :
    print("Congrats Man. You won")

