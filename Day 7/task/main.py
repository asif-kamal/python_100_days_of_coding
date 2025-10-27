import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

display = ""
all_guesses = []
# TODO-1: - Use a while loop to let the user guess again.
while display != chosen_word:
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            all_guesses.append(guess)
# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter in all_guesses:
            display += letter
        else:
            display += "_"


    print(display)

