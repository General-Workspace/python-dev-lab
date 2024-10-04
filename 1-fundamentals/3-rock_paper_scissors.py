import random

CHOICES = ["rock", "paper", "scissors"]
COMPUTER_CHOICE = random.choice(CHOICES)
PLAYER_CHOICE = input("Rock, paper, or scissors?\n").lower()

if PLAYER_CHOICE == COMPUTER_CHOICE:
    print("Computer's choice: ", COMPUTER_CHOICE)
    print("It's a tie!")
elif PLAYER_CHOICE == "rock" and COMPUTER_CHOICE == "scissors" or PLAYER_CHOICE == "paper" and COMPUTER_CHOICE == "rock" or PLAYER_CHOICE == "scissors" and COMPUTER_CHOICE == "paper":
    print("Computer's choice: ", COMPUTER_CHOICE)
    print("You win!")
else:
    print("Computer's choice: ", COMPUTER_CHOICE)
    print("Computer wins!")