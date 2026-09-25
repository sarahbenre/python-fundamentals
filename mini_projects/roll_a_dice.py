# Project - Roll a Dice
# Rules & Logic:
#   Roll the dice? (y/n)
#   If Y -> 2 random numbers between 1 and 6
#   If N -> "Thanks for playing!" and terminate loop
#   If invalid input -> Error message and ask again

import random

# Game loop
while True:
    choice = input("Roll the dice? (y/n): ").lower()
    # .lower() converts user input to lowercase so capital 'Y' or 'N' also work
    
    if choice == "y":
        nb1 = random.randint(1, 6)
        nb2 = random.randint(1, 6)
        print(f"{nb1}, {nb2}")
        # f-strings allow variable evaluation directly inside print placeholders ({})

    elif choice == "n":
        print("Thanks for playing!")
        break  # Exit the loop

    else:
        print("Error: Invalid input. Please enter 'y' or 'n'.")
