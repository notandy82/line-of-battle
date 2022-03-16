# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import random
# Player and computer boards
PLAYER_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
PLAYER_GUESS_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
COMPUTER_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]
COMPUTER_GUESS_BOARD = [["\u001b[34m~\u001b[0m"] * 6 for i in range(6)]


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


def place_ships(board):
    """
    For loop to place each ship on the computer's board
    """
    for ship in range(10):               
        ship_column, ship_row = random.randint(0, 5), random.randint(0, 5)
        while board[ship_column][ship_row] == "@":
            ship_column, ship_row = random.randint(0, 5), random.randint(0, 5)
        board[ship_column][ship_row] = "@"
        

def player_coordinates():
    """
    Function takes player input to determine player target
    """
    column = input("What column (A - F) shall we fire at? ")
    while column not in "ABCDEF":
        print("Enter a valid column")
        column = input("What column (A - F) shall we fire at? ")
    row = input("What row (1 - 6) shall we fire at? ")
    while row not in "123456":
        print("Enter a valid row")
        row = input("What row (1 - 6) shall we fire at? ")
    return convert_letters[column], int(row) - 1


def computer_coordinates():
    """
    function uses random numbers to determine the computer target
    """
    column, row = random.randint(0, 5), random.randint(0, 5)
    



# welcome_message()
# username_input()

place_ships(COMPUTER_BOARD)
print_board(COMPUTER_BOARD)
place_ships(PLAYER_BOARD)
print_board(PLAYER_BOARD)

