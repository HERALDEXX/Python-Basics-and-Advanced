'''Write a program that generates a random number between 1 and 100 and asks the user to guess it. The program should provide feedback on whether the guess is too high or too low until the user guesses correctly.'''

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the user's guess to None
    user_guess = None
    
    # Loop until the user guesses the correct number
    while user_guess != number_to_guess:
        # Ask the user for their guess
        user_guess = int(input("Guess the number (between 1 and 100): "))
        
        # Provide feedback
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")

# Call the function
guess_the_number()