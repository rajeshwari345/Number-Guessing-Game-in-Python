import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    # Initialize the maximum number of attempts
    max_attempts = 6
    
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 6 attempts to guess it.")
    
    while attempts < max_attempts:
        # Ask the player for their guess
        user_guess = input("Enter your guess: ")
        
        # Check if the input is a valid number
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    # If the player runs out of attempts, reveal the number
    print(f"Sorry, you didn't guess the number. The correct answer was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
