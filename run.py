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
    Input field for player to place their name
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
    username = input("What is your name? ")
    print("Prepare for battle, Admiral " + username + "!")

welcome_message()
