# Description
# Auction Program -> the winner is the highest bidder but no one know's anyone else's bids during the auction
# After the bidders have done bidding, the player with the highest bid will then be revealed to the players

from secretauctionprogramart import logo
print(logo)

# dictionary -> for key we have the user's name
# dictionary -> for value we have the user's bid
auction_program = {

}


def find_highest_bidder(dictionary): # find the highest bidder in the auction program dictionary
    highest_bid = 0 # 1000
    winner = ''
    for bidder in auction_program:
        bid_amount = dictionary[bidder] #1000, 500, 3000
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}.')
game_over = False
while not game_over:
    
    user_name = input('What is your name? -> ')
    user_bid = int(input('What is your bid? -> $'))
    auction_program[user_name] = user_bid
    user_input = input('Are there any other bidders? Type yes or no -> ').lower()
    if user_input == 'no':
        game_over = True
        find_highest_bidder(auction_program)
    elif user_input == 'yes':
        print('\n' * 20)
        