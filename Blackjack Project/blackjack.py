import random
from blackjackart import logo
def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def add_cards(cards):
    total = 0
    for i in cards:
        total += i
    if total == 21 and len(cards) == 2:
        return 0
    if total > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        total = 0
        for i in cards:
            total += i
    return total

def compare(user_x, dealer_y):
    if user_x == dealer_y:
        return 'Draw'
    elif dealer_y == 0:
        return 'Lose, dealer has Blackjack'
    elif user_x == 0:
        return 'Win with a Blackjack'
    elif user_x > 21:
        return 'You went over. You lose'
    elif dealer_y > 21:
        return 'Dealer went over. You win'
    elif user_x > dealer_y:
        return 'You win'
    else:
        return 'You lose'

def play_game():
    print(logo)

    is_game_over = False

    user_total_cards = 0
    dealer_total_cards = 0
    user_cards = []
    dealer_cards = []

    for _ in range(2):
        user_cards.append(deal())
        dealer_cards.append(deal())


    while not is_game_over:
        
        user_total_cards = add_cards(user_cards)
        dealer_total_cards += add_cards(dealer_cards)
        print(f'Your cards -> {user_cards}, current score -> {user_total_cards}')
        print(f'Dealers first card -> {dealer_cards[0]}')

        if user_total_cards == 0 or dealer_total_cards == 0 or user_total_cards > 21:
            is_game_over = True

        else:
            get_another_card = input('Type y to get another card, type n to pass -> ')

            if get_another_card == 'y':
                user_cards.append(deal())
                user_total_cards = add_cards(user_cards)

            else:
                is_game_over = True

    while dealer_total_cards != 0 and dealer_total_cards < 17:
        dealer_cards.append(deal())
        dealer_total_cards += add_cards(dealer_cards)

    print(f'Your final hand -> {user_cards}, final score -> {user_total_cards}')
    print(f'Dealers final hand -> {dealer_cards}, final score -> {dealer_total_cards}')

    print(compare(user_total_cards, dealer_total_cards))

while input('Do you want to play a game of Blackjack? Type y or n -> ') == 'y':
    print('\n' * 20)
    play_game()
    