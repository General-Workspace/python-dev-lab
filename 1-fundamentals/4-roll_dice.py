import random

roll = random.randint(1, 6)
guess = int(input("Guess the number on the die:\n "))

if guess == roll:
    print("Great job! You guessed correctly.")
else:
    print("Sorry, the number was", roll)