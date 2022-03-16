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
    Combines functions to place player ships and computer ships
    """
    for ship_length in SHIP_LENGTHS:
        while True:
            if board == COMPUTER_BOARD:
                direction, column, row = random.choice(["H", "V"]), \
                    random.randint(0, 8), random.randint(0, 8)
                if ship_fit(ship_length, column, row, direction):
                    if not ship_overlap(board, column, row, direction,
                                        ship_length):
                        if direction == "H":
                            for i in range(column, column + ship_length):
                                board[i][row] = "@"
                        else:
                            for i in range(row, row + ship_length):
                                board[column][i] = "@"
                        break
            else:
                place_ship = True
                print("Place ship with a length of " + str(ship_length))
                column, row, direction = player_input(place_ship)
                if ship_fit(ship_length, column, row, direction):
                    if ship_overlap(board, column, row, direction,
                                    ship_length):
                        print("We can't go there, Admiral!")
                    else:
                        print("That'll do nicely, Admiral")
                        if direction == "H":
                            for i in range(column, column + ship_length):
                                board[i][row] = "@"
                        else:
                            for i in range(row, row + ship_length):
                                board[column][i] = "@"
                        print_board(PLAYER_BOARD)
                        break


def ship_fit(SHIP_LENGTH, column, row, direction):
    """
    Determines if ship fits on board
    """
    if direction == "H":
        if column + SHIP_LENGTH > 9:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 9:
            return False
        else:
            return True


def ship_overlap(board, column, row, direction, ship_length):
    """
    Determines if ship is placed where another ship already is
    """
    if direction == "H":
        for i in range(column, column + ship_length):
            if board[i][row] == "@":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[column][i] == "@":
                return True
    return False


def player_input(place_ship):
    """
    FILL ME OUT!
    """
    if place_ship is True:
        while True:
            try:
                direction = input("Choose a direction (H or V): ")
                if direction == "H" or direction == "V":
                    break
            except TypeError:
                print("Enter H or V")
        while True:
            try:
                column = input("Choose a column A - I for your ship: ")
                if column in "ABCDEFGHI":
                    column = convert_letters[column]
                    break
            except KeyError:
                print("Enter a letter A-I")
        while True:
            try:
                row = input("Choose a row 1 - 9 for your ship: ")
                if row in "123456789":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Enter a number 1 - 9")
        return column, row, direction
    else:
        while True:
            try:
                column = input("Choose the column to fire at A - I: ")
                if column in "ABCDEFGHI":
                    column = convert_letters[column]
                    break
            except KeyError:
                print("Enter a valid letter A - I")
        while True:
            try:
                row = input("Enter the row to fire at 1 - 9: ")
                if row in "123456789":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Enter a valid number 1 - 9")
        return column, row


# welcome_message()
# username_input()


print_board(COMPUTER_BOARD)

