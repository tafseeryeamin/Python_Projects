bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ").strip()
    try:
        bid_amount = float(input("What is your bid?: $"))
    except ValueError:
        print("Invalid bid amount. Please enter a valid number.")
        continue
    bids[name] = bid_amount
    should_continue = input("Is there any other bidder? (y/n): ").lower().strip()
    if should_continue == "n":
        continue_bidding = False

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Call the function to find the highest bidder after the bidding process is complete
find_highest_bidder(bids)
