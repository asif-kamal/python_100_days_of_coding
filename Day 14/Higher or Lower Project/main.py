import art
import game_data
import random



dictionary_A = {}
dictionary_B = {}
game_play = True
score= 0

while game_play:
    print(art.logo, end='\r')

    if dictionary_A == {}:
        dictionary_A = random.choice(game_data.data)
    print(f"Compare A: {dictionary_A.get('name')}, a {dictionary_A.get('description')} from {dictionary_A.get('country')}", end='\r')
    print(f"{art.vs}", end='\r')

    dictionary_B = random.choice(game_data.data)
    print(f"Against B: {dictionary_B.get('name')}, a {dictionary_B.get('description')} from {dictionary_B.get('country')}")
    choice = input("Who has more followers? Type 'A' or 'B': \n").upper()

    if choice == 'A' and int(dictionary_A.get('follower_count')) > int(dictionary_B.get('follower_count')):
        score += 1
        print(f"\nYou're right! Current score: {score}", end='\r')

    elif choice == 'B' and int(dictionary_A.get('follower_count')) < int(dictionary_B.get('follower_count')):
        score += 1
        dictionary_A = dictionary_B
        print(f"\nYou're right! Current score: {score}", end='\r')

    elif choice == 'A' and int(dictionary_A.get('follower_count')) < int(dictionary_B.get('follower_count')):
        print(f"\nYou got it wrong. Current score: {score}. Game over.")
        game_play = False

    elif choice == 'B' and int(dictionary_A.get('follower_count')) > int(dictionary_B.get('follower_count')):
        print(f"\nYou got it wrong. Current score: {score}. Game over.")
        game_play = False