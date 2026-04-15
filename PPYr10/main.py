import os
from colorama import Fore, Style
import time
import numpy as np


rows = [[0, 0, 6, 6], [0, 2, 8, 1], [0, 0, 5, 0], [0, 3, 0, 0]]

Board_size = 4

Yellow_start = Fore.YELLOW + Style.BRIGHT

Cyan_start = Fore.CYAN + Style.BRIGHT

green_start = Fore.GREEN + Style.BRIGHT

Purple_start = Fore.MAGENTA + Style.BRIGHT

Colour_end = Style.RESET_ALL


def tutorial():
    print("How to play: \nUse ",Yellow_start, "WASD", Colour_end ," to merge identical blocks\nIdentical blocks will add together to form a larger block (eg 2→2 = 4)\nEvery movement will spawn either a 2 or a 4 on a random empty space\nKeep playing until you create", Yellow_start, "2048", Colour_end," or run out of space!")

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

def MergeOneRowLeft(row):
    for x in range(Board_size - 1):
        for i in range(Board_size - 1, 0, -1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    
    for i in range(Board_size-1):
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0

    for i in range(Board_size - 1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0

    return row
    
def MergeLeft(New_Board):
    for i in range(Board_size):
        New_Board[i] = MergeOneRowLeft(New_Board[i])
    return New_Board

def reverseOrders(row):
    ReversedBoard = []
    for i in range (Board_size -1, -1, -1):
        ReversedBoard.append(row[i])
    return ReversedBoard

def MergeRight(New_Board):
    for i in range(Board_size):
        New_Board[i] = reverseOrders(New_Board[i])
        New_Board[i] = MergeOneRowLeft(New_Board[i])
        New_Board[i] = reverseOrders(New_Board[i])
    return New_Board


def TransposeBoard(New_Board):
    New_Board = np.array(rows).T
    return New_Board

def MergeDown(New_Board):
    New_Board = TransposeBoard(New_Board)
    New_Board = MergeLeft(New_Board)
    New_Board = TransposeBoard(New_Board)
    New_Board = TransposeBoard(New_Board)
    print(New_Board)
    return New_Board

    


def scoreboard():
    Scoreboard = open("Leaderboard.txt", "w")
    Scoreboard.close()
    return Scoreboard

def updateScore():
    username = input("Enter name:")


def IsFileEmpty(Scoreboard):
    if not os.path.exists(Scoreboard):
        print("Sorry! No one has played yet!")
        return False
    
    else:
        with open(Scoreboard, 'r') as file:
            leaderboard = file.read()
            print(leaderboard)
    
    return os.path.getsize(Scoreboard) == 0

def Game():
    print("Work in progress")



def main_menu():
    print(Yellow_start,"Welcome to...")
    time.sleep(0.6)
    print("""
╔═══╦═══╦╗─╔╦═══╗
║╔═╗║╔═╗║║─║║╔═╗║
╚╝╔╝║║║║║╚═╝║╚═╝║
╔═╝╔╣║║║╠══╗║╔═╗║
║║╚═╣╚═╝║──║║╚═╝║
╚═══╩═══╝──╚╩═══╝""",Colour_end)
    time.sleep(0.6)
    print(green_start,"[Play]",Colour_end)
    time.sleep(0.5)
    print(Cyan_start,"[Tutorial]", Colour_end)
    time.sleep(0.5)
    print(Purple_start,"[Score]",Colour_end)
    time.sleep(0.5)
    choice = input("What would you like to do?\n")

    if choice == "Tutorial":
        tutorial()
    elif choice == "Score":
        pass

    elif choice == "Play":
        Game()

MergeDown(rows)

# when milestone reached:
# git stage*
# git commit -m "blahblahlal"
# git push