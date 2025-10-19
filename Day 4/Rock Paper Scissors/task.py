import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def rock_paper_scissors():
    choice = input("Choose among 'rock', 'paper', or 'scissors' to play: ").lower()
    computer_choice = random.choice([rock, paper, scissors])

    if choice == "rock":
        if computer_choice == scissors:
            print("Computer: \n" + computer_choice)
            print("You: \n" + rock + "\nYou win!")
        elif computer_choice == paper:
            print("Computer: \n" + computer_choice)
            print("You: \n" + rock + "\nYou lose!")
        elif computer_choice == rock:
            print("Computer: \n" + computer_choice)
            print("You: \n" + rock + "\nDraw!")
    elif choice == "paper":
        if computer_choice == rock:
            print("Computer: \n" + computer_choice)
            print("You: \n" + paper + "\nYou win!")
        elif computer_choice == paper:
            print("Computer: \n" + computer_choice)
            print("You: \n" + paper + "\nDraw!")
        elif computer_choice == scissors:
            print("Computer: \n" + computer_choice)
            print("You: \n" + paper + "\nYou lose!")
    elif choice == "scissors":
        if computer_choice == paper:
            print("Computer: \n" + computer_choice)
            print("You: \n" + scissors + "\nYou win!")
        elif computer_choice == rock:
            print("Computer: \n" + computer_choice)
            print("You: \n" + scissors + "\nYou lose!")
        elif computer_choice == scissors:
            print("Computer: \n" + computer_choice)
            print("You: \n" + scissors + "\nDraw!")

    play_again = input("Play again? Y/N: ").lower()
    if play_again == "y":
        rock_paper_scissors()

rock_paper_scissors()
