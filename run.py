# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
from random import randint

# Player and computer boards
PLAYER_BOARD = [["\u001b[34m~\u001b[0m"] * 9 for i in range(9)]
COMPUTER_BOARD = [["\u001b[34m~\u001b[0m"] * 9 for i in range(9)]

# List of ship lengths for the game
SHIPS = [2, 3, 3, 4, 5]

# Letter to number conversion for coordinate system
convert_letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}

def print_board(board):
    """
    Creates the boards for the player and computer
    """
    print("  A B C D E F J H I")
    print("  ~~~~~~~~~~~~~~~~~")
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
    print("The battle is waged on a 9 x 9 grid")
    print("Your fleet consists of 5 ships")
    print("You have 1 first rate that covers 5 spaces")
    print("You have 1 second rate that covers 4 spaces")
    print("You have 2 frigates that each cover 3 spaces")
    print("You have 1 gunboat that covers 2 spaces")
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


def place_computer_ships(COMPUTER_BOARD):
    """
    Random placement for the computer's ships
    """
    for ship in range(5):
        ship_column, ship_row = randint(0,9), randint(0,9)
        while board[ship_column][ship_row] == "X":
            ship_column, ship_row = randint(0,9), randint(0,9)
        board[ship_column][ship_row] = "X"


def place_ships(PLAYER_BOARD):
    """
    Function for player to place ships
    """
    column = input("Choose a column A - I to place your ship")
    while column not in "ABCDEFGHI":
        print("Please enter a valid column")
        column = input("Choose a column A - I to place your ship")
    row = input("Choose a row 1 - 9 to place your ship")
    while row not in "123456789":
        print("Please enter a valid row")
        row = input("Choose a row 1 - 9 to place your ship")

# welcome_message()
# username_input()
# place_ships()
# place_computer_ships()
print_board(COMPUTER_BOARD)
print_board(PLAYER_BOARD)
