# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
from random import randint

# Player and computer boards
PLAYER_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
PLAYER_GUESS_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
COMPUTER_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
COMPUTER_GUESS_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]


# Letter to number conversion for coordinate system
convert_letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,}


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
            ____|____ ___|__
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
    print("What is your name Admiral?")
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


def place_ship(board):
    """
    For loop to place each ship on the computer's board
    """
    for ship_length in range(10):
        while True:
            if board == COMPUTER_BOARD:
                ship_column, ship_row = randint(0, 7), randint(0, 7)
                if board[ship_column][ship_row] == "@":
                    ship_column, ship_row = randint(0, 7), randint(0, 7)
                else:
                    board[ship_column][ship_row] = "@"

def player_input(place_ship):
    """
    FILL ME OUT!
    """
    if place_ship is True:
        while True:
            try:
                column = input("Choose a column A - F for your ship: ")
                if column in "ABCDEF":
                    column = convert_letters[column]
                    break
            except KeyError:
                print("Enter a letter A-F")
        while True:
            try:
                row = input("Choose a row 1 - 6 for your ship: ")
                if row in "123456789":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Enter a number 1 - 6")
        return column, row
    else:
        while True:
            try:
                column = input("Choose the column to fire at A - F: ")
                if column in "ABCDEF":
                    column = convert_letters[column]
                    break
            except KeyError:
                print("Enter a valid letter A - F")
        while True:
            try:
                row = input("Enter the row to fire at 1 - 6: ")
                if row in "123456":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Enter a valid number 1 - 6")
        return column, row


# welcome_message()
# username_input()


place_ship(PLAYER_BOARD)

