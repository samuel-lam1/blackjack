'''
Blackjack
This game is for 1 vs 1 (dealer vs player) only.
'''
from random import shuffle
from IPython.display import clear_output

suits = ('spades', 'hearts', 'clubs', 'diamonds')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
            '10':10, 'J':10, 'Q':10, 'K':10, 'A':(1,11)}

################################################################################

class Deck:
    '''Initialize the card deck and other actions'''
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for figure in values:
                self.all_cards.append((suit,figure))

    def shuffle(self):
        shuffle(self.all_cards)

    def draw_card(self):
        return self.all_cards.pop()

################################################################################

def display(cards,person,point):
    clear_output()
    if person == 'player':
        print("Player's card:\n")
    else:
        print("Dealer's card:\n")
    for item in cards:
        print(f'    {" ".join(item)}')
    print(f'\nTotal points: {point}\n')

def ask_for_draw(cards):
    choice = 'x'
    while choice not in ('Y','y','N','n'):
        choice = input('Do you need 1 more card? (y/n) ')
        if choice not in ('Y','y','N','n'):
            print('Sorry, invalid input, please try again.\n')
    if choice in ['Y','y']:
        cards.append(mydeck.all_cards.pop())
        return cards, True
    return cards, False

def total_point(cards):
    total = 0
    ace = 0
    for n in range(len(cards)):
        if cards[n][1] != 'A':
            total += values[cards[n][1]]
        else:
            ace += 1
    if ace >= 1: # Choose 11 as the value for Ace if the total value does not exceed 21
        for i in range(ace):
            if total + values['A'][1] <= 21:
                total += values['A'][1]
            else:
                total += values['A'][0]
    return total

def again():
    game ='x'
    while game not in ['Y','y','N','n']:
        game = input('Do you want to play again? (Y/N) ')
        if game not in ['Y','y','N','n']:
            print('Sorry, but your input is not valid.')
    return game

################################################################################

while True:
    mydeck = Deck()
    mydeck.shuffle()
    player = []
    player_point = 0
    dealer = []
    dealer_point = 0
    for num in range(0,2):
        player.append(mydeck.all_cards.pop())
        dealer.append(mydeck.all_cards.pop())
    win = 'x'

    draw = True
    while len(player) < 5 and total_point(player) <= 21 and draw:
        display(player, 'player', total_point(player))
        player, draw = ask_for_draw(player)
        display(player, 'player', total_point(player))
        if total_point(player) > 21:
            print("Player busted!\n")
            win = 'dealer'

    input("\n-------Press Enter to continue-------\n")

    draw = True
    while len(dealer) < 5 and total_point(player) <= 21 and total_point(dealer) <= 21 and draw:
        display(dealer, 'dealer', total_point(dealer))
        dealer, draw = ask_for_draw(dealer)
        display(dealer, 'dealer', total_point(dealer))
        if total_point(dealer) > 21:
            print("Dealer busted!\n")
            win = 'Player'

    if win == 'x':
        if total_point(player) > total_point(dealer):
            win = 'Player'
        elif total_point(player) < total_point(dealer):
            win = 'Dealer'
        else:
            win = 'Draw'

    print(f"Player's points: {total_point(player)}, dealer's points: {total_point(dealer)}\n")
    if win == 'Draw':
        print("It's a draw game!")
    else:
        print(f'Congratulations! {win} won the game!\n')
    if again() in ['N','n']:
        break
