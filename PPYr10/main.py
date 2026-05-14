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

Red_start = Fore.RED + Style.BRIGHT

Colour_end = Style.RESET_ALL


def tutorial():
    print("How to play: \nUse ",Yellow_start, "WASD", Colour_end ," to merge identical blocks")
    time.sleep(0.7)
    print("Identical blocks will add together to form a larger block (eg 2→2 = 4)")
    time.sleep(0.7)
    print("Every movement will spawn either a 2 or a 4 on a random empty space")
    time.sleep(0.7)
    print("Keep playing until you create", Yellow_start, "2048", Colour_end," or run out of space!")

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
    for i in range(Board_size):
        for j in range (i, Board_size):
            if j != i:
                temporary = New_Board[i][j]
                New_Board[i][j] = New_Board[j][i]
                New_Board[j][i] = temporary

                
    return New_Board

def MergeDown(New_Board):
    
    New_Board = TransposeBoard(New_Board)
    
    New_Board = MergeRight(New_Board)
    
    New_Board = TransposeBoard(New_Board) 
    return New_Board

def MergeUp(New_Board):
    New_Board = TransposeBoard(New_Board)
    
    New_Board = MergeLeft(New_Board)
    
    New_Board = TransposeBoard(New_Board) 
    return New_Board

def CalculateScore():
    score = [[sum(row) for row in zip(*rows)]]
    print(score)
    for num in score:
        num = int(num)
    score = sum(score)
    return score

def scoreboard():
    Scoreboard = open("Leaderboard.txt", "w")
    Scoreboard.close()
    return Scoreboard

def updateScore(Scoreboard):
    username = input("Enter name:")
    names = []
    scores = []
    names.append(username)
    #scores.append()
    Scoreboard.write(username)



def IsFileEmpty(Scoreboard):
    if not os.path.exists(Scoreboard):
        print("Sorry! No one has played yet!")
        return False
    
    else:
        with open(Scoreboard, 'r') as file:
            leaderboard = file.read()
            print(leaderboard)
    
    return os.path.getsize(Scoreboard) == 0

def movement():
    directions = ["a", "s", "w", "d"]
    display_board()
    move = input("Make your move: ")
    move = move.lower()
    while move not in directions:
        print(Red_start, "That isn't a move!", Colour_end)
        move = input("Try again: ")
        move = move.lower()
    
    if move == "a":
        MergeLeft(rows)
        display_board
    elif move == "s":
        MergeDown(rows)
        display_board
    elif move == "w":
        MergeUp(rows)
        display_board()
    elif move == "d":
        MergeRight(rows)
        display_board()


    
def Game():
    pass
    



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
    choice = choice.lower()
    while choice != "play":
        if choice == "tutorial":
            tutorial()
            choice = input("what would you like to do? ")
        elif choice == "score":
            pass

    if choice == "play":
        Game()

movement()
# when milestone reached:
# git stage*
# git commit -m "blahblahlal"
# git push