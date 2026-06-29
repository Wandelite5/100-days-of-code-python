# TODO-1: Ask the user for input use def for highest bider 

bid_dict ={}

def highest_bider(bids):
    current_bid = 0
    for bid in bids:
        if bid_dict[bid] > current_bid:
            current_bid = bid_dict[bid]
    print(bid,current_bid)


while True:
    user = str(input("Enter your name: "))
    biding = int(input("Enter your bid: $"))
    bid_dict[user] = biding
    print(100 * "\n")
    continue_bid = input("Are there any other bidders? Type 'yes or 'no'. ")
    if continue_bid == 'no':
        highest_bider(bids=bid_dict)
        break
        winner = max(bid_dict, key=bid_dict.get)
        print(winner)
        break
    else:
        continue



