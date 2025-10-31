import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

my_hand = 0
dealer_hand = 0

game_in_play = True
print("Let's play Blackjack!\n")


card1 = random.choice(cards)
card2 = random.choice(cards)
if card1 == 11 and card2 == 11:
    my_hand += card1 - 10
    my_hand += card2
else:
    my_hand += card1
    my_hand += card2
print(f"You have been dealt {card1} and {card2} which total {my_hand}\n")
dealer_card1 = random.choice(cards)
dealer_hand += dealer_card1
print(f"Dealer has been dealt {dealer_card1}")
dealer_card2 = random.choice(cards)
if dealer_card1 == 11 and dealer_card2 == 11:
    dealer_hand += dealer_card2 - 10
else:
    dealer_hand += dealer_card2
print(f"Dealer also has one card face down which he flips and it is a {dealer_card2}")
print(f"Dealer's total is {dealer_hand}\n")

while game_in_play:
    if my_hand > 21 and dealer_hand > 21:
        print("You both bust! Game over.\n")
        game_in_play = False
    elif my_hand == 21 and dealer_hand == 21:
        print("It is a draw! Game over.\n")
        game_in_play = False
    elif my_hand == 21 and dealer_hand < 21:
        print("You win! Game over.\n")
    elif my_hand < 21 and dealer_hand == 21:
        print("You lose! Game over.\n")
        game_in_play = False
    elif my_hand < 21 and dealer_hand > 21:
        print("Dealer busts! You win! Game over.\n")
        game_in_play = False
    elif my_hand < 21 and dealer_hand < 21 and dealer_hand < 17:
        decision = input("Enter 'hit' or 'stay' to continue...\n")
        if decision == "hit":
            card3 = random.choice(cards)
            my_hand += card3
            print(f"You were dealt {card3}, with the total of {my_hand}\n")
            dealer_card3 = random.choice(cards)
            dealer_hand += dealer_card3
            print(f"Dealer was dealt {dealer_card3}, now with a total of {dealer_hand}\n")
            if my_hand == 21 and (dealer_hand > 21 or dealer_hand < 21):
                print("You win! Game over.\n")
                game_in_play = False
            elif my_hand > 21 and dealer_hand < 21:
                print("Dealer wins! You lose! Game over.\n")
                game_in_play = False
        elif decision == "stay":
            print(f"You still have a total of {my_hand}\n")
            dealer_card3 = random.choice(cards)
            dealer_hand += dealer_card3
            print(f"Dealer was dealt {dealer_card3}, now with a total of {dealer_hand}\n")
    elif my_hand < 21 and dealer_hand < 21 and dealer_hand > 17:
        decision = input("Enter 'hit' or 'stay' to continue...\n")
        if decision == "hit":
            card4 = random.choice(cards)
            my_hand += card4
            print(f"You were dealt {card4}, with the total of {my_hand}\n")
            print(f"The dealer has a total of {dealer_hand} so he will stay\n")
            if my_hand > 21 and dealer_hand > 21:
                print("Dealer busts! You bust! Game over.\n")
                game_in_play = False
            elif my_hand > 21 and dealer_hand < 21:
                print("Dealer wins, you bust! Game over.\n")
                game_in_play = False
        elif decision == "stay":
            print(f"You still have a total of {my_hand}\n")
            print(f"The dealer has a total of {dealer_hand}\n")
            continue
