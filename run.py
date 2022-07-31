import random 

print("Welcome to connect 4")
print("--------------------")

possibleLetters = ["A","B","C","D","E","F","G",]
gameBoard [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], 
["","","","","","",""],  ["","","","","","",""], ["","","","","","",""]]
rows = 6
cols = 7

def printGameBoard():
    print("\n    A    B    C    D    E    F    G  ", end="")
    for x  in range(rows):
     print("\n   +----+----+----+----+----+----+")
