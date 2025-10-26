import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
place_holder = len(chosen_word)

display_at_the_start = ""


for number in range(place_holder):
    display_at_the_start += "_"

#print(chosen_word)
print(display_at_the_start)
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: \n").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display_after_guess = ""

for letter in chosen_word:
    if letter == guess:
        display_after_guess += letter
    else:
        display_after_guess += "_"

print(display_after_guess)

