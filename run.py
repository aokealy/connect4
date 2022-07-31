import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
rows = 6
cols = 7

def printGameBoard():
  print("\n     A    B    C    D    E    F    G  ", end="")
  for x in range(rows):
    print("\n   +----+----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(cols):
      if(gameBoard[x][y] == "🔴"):
        print("",gameBoard[x][y], end=" |")
      elif(gameBoard[x][y] == "🟡"):
        print("", gameBoard[x][y], end=" |")
      else:
        print(" ", gameBoard[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn
#check for row and columns to have 4 chips in a row of same colour
def checkForWinner(chip):
    ### check horizontal spaces
    for y in range(rows):
      for x in range(cols - 3):
        if(gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip):
            print("\nGame Over!S", chip, " wins! Thank you for playing :D")
            return True   

    ### check vertical spaces
    for y in range(rows):
      for x in range(cols - 3):
        if(gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip):
            print("\nGame Over!S", chip, " wins! Thank you for playing :D")
            return True
    ### check diagonal spaces (top right to bottom left)
    for y in range(rows - 3):
      for x in range(3, cols):
        if(gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip):
            print("\nGame Over!S", chip, " wins! Thank you for playing :D")
            return True

    ### check diagonal spaces (top left to bottom right)
    for y in range(rows - 3):
      for x in range(cols - 3):
        if(gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip):
            print("\nGame Over!S", chip, " wins! Thank you for playing :D")
            return True                                   

turnCounter = 0
while True:
    ### Do something in here          
