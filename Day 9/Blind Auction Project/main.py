# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)

names_and_bids = {}

def blind_auction():

    name = input("What is your name? ")
    bid_amount = float(input("What is your bid? "))

    names_and_bids[name] = bid_amount

    more_bidders = input("\nAre there any other bids out there? Type 'yes' or 'no'\n").lower()

    highest_bidder = ""
    highest_bid = 0

    if more_bidders == 'yes':
        blind_auction()
    if more_bidders == 'no':
        for name, bid_amount in names_and_bids.items():
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                highest_bidder = name
        print(f"\nHighest bidder is {highest_bidder} with a bid amount of {highest_bid}")

blind_auction()