
import random

def number_guessing_game():
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 10  # User has 10 attempts

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}: Enter your guess: ")
        
        # Input validation
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check the guess
        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
        
        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()