# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import random

PLAYER_BOARD = [["~"] * 10 for i in range(10)]
COMPUTER_BOARD = [["~"] * 10 for i in range(10)]
PLAYER_TARGET_BOARD = [["~"] * 10 for i in range(10)]
COMPUTER_TARGET_BOARD = [["~"] * 10 for i in range(10)]

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
    print("Welcome to The Line of Battle")
    time.sleep(5)
    print("""
    Your fleet has been ordered to sea to track and defeat the enemy.
    After three weeks of sailing, the enemy fleet is in sight.
    The drums sound to beat to quarters!
    """)
    time.sleep(5)
    print("The battle is waged on a 10 x 10 grid")
    print("You must sink the computer's vessels before yours are sunk")
    print("Your fleet consists of 5 ships")
    print("You have 1 first rate that covers 5 spaces")
    print("You have 1 second rate that covers 4 spaces")
    print("You have 2 frigates that each cover 3 spaces")
    print("You have 1 gunboat that covers 2 spaces")
    print("")
    
def username_input():
    """
    Input takes the name of the user for game personalisation
    """
    print("What is your name Admiral?")
    while True:
        username = input("Enter the name you wish to go by:")
        if name_check(username):
            break
    print("Prepare for battle, Admiral " + username + "!")
    return username

def name_check(username):
    """
    This ensures the player has entered at least one character for
    a name and tells the player to enter a name.
    """
    if len(username) ==  0:
        print("Please enter at least 1 character")
        return False
    else:
        return True


#welcome_message()
username_input()
