#When we run the programm, in generates a random number between 1 and 100 and the user has to guess.
#If unvalid number guessed (letter, not in the range), error message.
#If number input too high or too low, "too high" or "too low" message.

# Make the computer choose a random number
import random
computer_number = random.randint(1, 100)

# Input a random number between 1 and 100 AND KEEP INPUTTING AS LONG AS A VALID NUMBER ISNT INPUTED
while True:
    try:
        user_number = int(input("Guess a number between 1 and 100: ").strip())

        # If number is not valid : "Please ener a valid number"
        if user_number < 1 or user_number > 100:
            print("Please enter a valid number.")

        # If number is too high : "Too high!"
        elif user_number > computer_number:
            print("Too high!")

        # If number is too low : "Too low!"
        elif user_number < computer_number:
            print("Too low!")

        # If number found : "Congratulations! You guessed the number!"
        else:
            print("Congratulations! You guessed the number!")
            break

    except ValueError:
        print("Please enter a valid number.")
