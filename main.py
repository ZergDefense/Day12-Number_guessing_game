import random

import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

number_of_attempts = 0
number_to_guess = random.randint(1, 100)
guess = 0


def show_number_of_attempts():
    print(f"You have {number_of_attempts} attempts to guess the number.")


def evaluate_guess(attempts):
    if attempts == 0:
        print("No more attempts, you lose. :(\n")
        return
    if guess == number_to_guess:
        print("Very well done, you win!\n")
    elif guess < number_to_guess:
        print("Too low. \nGuess again.\n")
        attempts -= 1
    elif guess > number_to_guess:
        print("Too high. \nGuess again.\n")
        attempts -= 1

    return attempts


print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if chosen_difficulty == "hard":
    number_of_attempts = HARD_LEVEL_TURNS
elif chosen_difficulty == "easy":
    number_of_attempts = EASY_LEVEL_TURNS
else:
    print("Invalid input.")

show_number_of_attempts()

while guess != number_to_guess and number_of_attempts != 0:
    guess = int(input("Make a guess: "))
    number_of_attempts = evaluate_guess(number_of_attempts)
    if guess != number_to_guess:
        show_number_of_attempts()

