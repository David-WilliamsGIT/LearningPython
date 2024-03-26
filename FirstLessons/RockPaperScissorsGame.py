# A rock, paper and scissors game

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:  
        player = input("rock, paper or scissors?: ").lower()  
        if player not in choices:
            print("Invalid choice")
        else:
            break
    if player == computer:
        print("Player plays: " + player)
        print("Computer plays: " + computer)
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("Player plays: " + player)
            print("Computer plays: " + computer)
            print("You lose!")
        if computer == "scissors":
            print("Player plays: " + player)
            print("Computer plays: " + computer)
            print("You win!")
    elif player == "paper":
        if computer == "rock":
            print("Player plays: " + player)
            print("Computer plays: " + computer)
            print("You win!")
        if computer == "scissors":
            print("Player plays: " + player)
            print("Computer plays: " + computer)
            print("You lose!")
    elif player == "scissors":
        if computer == "rock":
            print("Player plays: " + player)
            print("Computer plays: " + computer)
            print("You lose!")
        if computer == "paper":
            print("Player plays: " + player)
            print("Computer plays: " + computer)
            print("You win!")

    player_again = input("Play again? (yes/no): ").lower()

    if player_again != "yes":
        break
print("Bye! Have a nice day!")
