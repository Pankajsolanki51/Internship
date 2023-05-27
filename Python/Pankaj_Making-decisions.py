print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
import random
secret_number = random.randint(1, 100)

# Game loop
game_over = False
while not game_over:
    # Prompt the player for a guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Compare the guess with the secret number
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        game_over = True
    elif guess < secret_number:
        print("Too low! Try guessing a higher number.")
    else:
        print("Too high! Try guessing a lower number.")

print("Thank you for playing!")
