# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def welcome_message():
    """
    Introduction screen
    Input field for player to place their name
    """
    username = input("What is your name? ")
    print("Welcome to the Line of Battle, Admiral " + username)

welcome_message()