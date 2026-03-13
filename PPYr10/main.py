rows = [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



def tutorial():
    print("How to play: \nUse WASD to merge identical blocks\nIdentical blocks will add together to form a larger block (eg 2→2 = 4)\nEvery movement will spawn either a 2 or a 4 on a random empty space\nKeep playing until you creat 2048 or run out of space!")

def display_board():
    largestValue = rows[0][0]
    for row in rows:
        for block in row:
            if block > largestValue:
                largestValue = block
    
    Spaces = len(str(largestValue))

    for row in rows:
        currentRow = "|"
        for block in row:
            if block == 0:
                currentRow += " " * Spaces + "|"
            else: 
                currentRow += (" " * (Spaces - len(str(block)))) + str(block) + "|"
        print(currentRow)

def MergeLeft():
    pass

def MergeRight():
    pass

def MergeUp():
    pass

def MergeDown():
    pass


def scoreboard():
    Scoreboard = open("scores.txt", "w")
    Scoreboard.close()
    return Scoreboard

def IsFileEmpty():
    pass



def main_menu():
    print("Welcome to 2048.\n[Play]\n[Tutorial]\n[Score]")
    choice = input("What would you like to do?\n")
    if choice == "Tutorial":
        tutorial()
    elif choice == "Score":
        pass
    elif choice == "Play":
        display_board()



def scoreboard():
    Scoreboard = open("scores.txt", "w")
    Scoreboard.close()
    return Scoreboard

def updateScore():
    pass

main_menu()
