def get_top_bid(bidding_dictionary):
    highest_bid = 0
    highest_bidder = ""

    for bidder in auction_dictionary:

        if auction_dictionary[bidder] > highest_bid:
            highest_bid = auction_dictionary[bidder]
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")


print("Welcome to the secret auction.")

auction_dictionary = {}
auction_running = True
while auction_running:

    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid? $"))

    auction_dictionary[user_name] = user_bid

    keep_going = input("Are there any other bidders? ('Yes' or 'No')\n").lower()
    if keep_going == "no":
        auction_running = False
    print("\n" * 20)

get_top_bid(auction_dictionary)
