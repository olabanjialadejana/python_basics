import os
import art


def add_to_bid(bidder_name, bid_price):
    bid[bidder_name] = bid_price

# This is a function to get the highest bidder from {bid}


def find_highest_bidder(bidding_record):
    # bid i.e bidding_record = {'olabanji': 345, 'kemio': 456, 'tunji': 457}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bid = {}
keep_on = True
while keep_on:
    print(art.logo)
    user_name = input("What is your name? \n")
    amount = int(input("How much are you bidding? \n$"))
    add_to_bid(user_name, amount)
    question = input("Are there any other bidders? Type 'yes' or 'no'\n")
    os.system("cls")
    if question == 'no':
        keep_on = False

find_highest_bidder(bid)
# all_bids = []
# for num in bid.values():
#     all_bids.append(num)

# highest_bid = max(all_bids)


# # Get the key corresponding to value highest_bid (** I copied the code. But it somehow worked!! I have to learn how it was done!!!)
# highest_key = list(filter(lambda x: bid[x] == highest_bid, bid))[0]

# # This code is contributed by Edula Vinay Kumar Reddy (i.e. the copied lambda)

# print(f'The winner is {highest_key} with a bid of ${highest_bid}')
