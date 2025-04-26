auction_status = True
dic_auction = {}

while auction_status:
    name = input("What is your name?  ")
    bid = input("What is your bid?: $ ")
    dic_auction[name] = bid
    status = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if status == 'no':
        winner = [key for key, value in dic_auction.items() if value == max(dic_auction.values())]
        print(f"The Winner is {winner[0].capitalize()} with a bid of {max(dic_auction.values())}$ ")
        auction_status = False
    else:
        print("\n" * 100)
