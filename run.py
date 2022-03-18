# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import random

# Player and computer boards
PLAYER_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
PLAYER_TARGET_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
COMPUTER_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
COMPUTER_TARGET_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]


# Letter to number conversion for coordinate system
convert_letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}


def print_board(board):
    """
    Creates the boards for the player and computer
    """
    print("  A B C D E F")
    print("  -----------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def welcome_message():
    """
    Introduction screen
    """
    print("""
            ____|___ ___|__
           |       | |     |
    _      |       | |     |\\
   / |     |       | |     | \\
  /__|     |_______| |_____|  \\
 ____|____     |        |      \\
 \\  o o o \\____|________|_______\\__
  \\   o o o o  o o o o o o o o  /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    print("Welcome to The Line of Battle \n")
    time.sleep(5)
    print("Your fleet has been ordered to sea to track and defeat the enemy.")
    print("After three weeks of sailing, the enemy fleet is in sight.")
    print("The drums sound to beat to quarters!")
    time.sleep(5)
    print("The battle is waged on a 6 x 6 grid")
    print("Your fleet consists of 10 ships")
    print("Each ship covers 1 grid space")
    print("Your ships are indicated by @")
    print("Alternate turns with the computer firing shots")
    print("A hit is shown with \u001b[31mX\u001b[0m")
    print("A miss is shown with O")
    print("You must sink the computer's vessels before yours are sunk")
    time.sleep(5)


def username_input():
    """
    Input takes the name of the user for game personalisation
    """
    print("What is your name Admiral? ")
    while True:
        username = input("Enter the name you wish to go by: ")
        if name_check(username):
            break
    print("Prepare for battle, Admiral " + username + "!")
    return username


def name_check(username):
    """
    This ensures the player has entered at least one character for
    a name and tells the player to enter a name.
    """
    if len(username) == 0:
        print("Please enter at least 1 character")
        return False
    else:
        return True


def place_ships(board):
    """
    For loop to place each ship on the computer's board
    """
    for ship in range(10):
        row, column = random.randint(0, 5), random.randint(0, 5)
        while board[row][column] == "@":
            row, column = random.randint(0, 5), random.randint(0, 5)
        board[row][column] = "@"


def player_coordinates():
    """
    Function takes player input to determine player target
    """
    row = input("What row (1 - 6) shall we fire at? ")
    while row not in ["1", "2", "3", "4", "5", "6"]:
        print("Enter a valid row")
        row = input("What row (1 - 6) shall we fire at? ")
    column = input("What column (A - F) shall we fire at? ").upper()
    while column not in ["A", "B", "C", "D", "E", "F"]:
        print("Enter a valid column")
        column = input("What column (A - F) shall we fire at? ").upper()
    return int(row) - 1, convert_letters[column]


def computer_coordinates():
    """
    function uses random numbers to determine the computer target
    """
    row, column = random.randint(0, 5), random.randint(0, 5)
    return row, column


def count_hits(board):
    """
    Checks how many hits there have been
    """
    hits = 0
    for column in board:
        for row in column:
            if row == "\u001b[31mX\u001b[0m":
                hits += 1
    return hits


def turn(board):
    """
    Function runs the player's and the computer's turn
    """
    if board == PLAYER_TARGET_BOARD:
        row, column = player_coordinates()
        if board[row][column] == "O":
            print("We already fired there, Admiral")
            turn(board)
        elif board[row][column] == "\u001b[31mX\u001b[0m":
            print("We already fired there, Admiral")
            turn(board)
        elif COMPUTER_BOARD[row][column] == "@":
            board[row][column] = "\u001b[31mX\u001b[0m"
            print("It's a hit, Admiral!")
        else:
            board[row][column] = "O"
            print("It's a miss, Admiral")
        print_board(PLAYER_TARGET_BOARD)
    else:
        row, column = computer_coordinates()
        if board[row][column] == "O":
            turn(board)
        elif board[row][column] == "\u001b[31mX\u001b[0m":
            turn(board)
        elif PLAYER_BOARD[row][column] == "@":
            board[row][column] = "\u001b[31mX\u001b[0m"
            print("We're hit, Admiral!")
        else:
            board[row][column] = "O"
            print("They missed us, Admiral")


def start_game():
    """
    Starts the game, contains all game functions
    """
    start = input("Press S to start the game ").upper()
    while start != "S":
        start = input("Press S to start the game ").upper()
    welcome_message()
    username_input()
    place_ships(COMPUTER_BOARD)
    place_ships(PLAYER_BOARD)
    while True:
        while True:
            print_board(PLAYER_TARGET_BOARD)
            turn(PLAYER_TARGET_BOARD)
            break
        if count_hits(PLAYER_TARGET_BOARD) == 10:
            print("I wish you joy of your victory, Admiral!")
            break
        while True:
            turn(COMPUTER_TARGET_BOARD)
            print_board(COMPUTER_TARGET_BOARD)
            break
        if count_hits(COMPUTER_TARGET_BOARD) == 10:
            print("Oh dear, this isn't good Admiral")
            break


def end_game():
    """
    Adds a message indicating how to play again
    """
    print("If you'd like to play again, please refresh your browser")
    print("or hit run program")
    time.sleep(2)
    print("See you soon!")


start_game()
end_game()
