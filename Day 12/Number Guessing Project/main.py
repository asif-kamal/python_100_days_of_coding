import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    selection = random.randint(1, 101)

    attempts = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5

    has_ended = False

    while not has_ended:
        if attempts > 0:
            print(f"You have {attempts} attempts to guess the number.")
            guess = input("Make a guess: ")
            if guess.isnumeric():
                if int(guess) == selection:
                    print(f"You guessed the number!")
                    has_ended = True
                elif int(guess) > selection:
                    print("Too high!")
                elif int(guess) < selection:
                    print("Too low!")
                elif int(guess) > 100 or int(guess) < 1:
                    print("Number should be between 1 and 100 inclusive!")
                attempts -= 1
            else:
                print("Invalid entry!")
        else:
            print(f"You lose! The number was {selection}")
            has_ended = True

number_guessing_game()