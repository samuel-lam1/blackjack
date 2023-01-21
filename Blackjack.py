'''
Blackjack
This game is for 1 vs 1 (Player vs Banker) only.
'''
from random import shuffle
from IPython.display import clear_output

suits = ('spades', 'hearts', 'clubs', 'diamonds')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':(1,11)}

class card:
    '''For storing card information'''
    def __init__(self, flower, figure):
        self.flower = flower
        self.figure = figure

    def __str__(self):
        return f'{self.flower}, {self.figure}'

class deck:
    '''Initialize the card deck and other actions'''
    def __init__(self):
        self.all_cards = []
        for flower in suits:
            for figure in values:
                self.all_cards.append(card(flower,figure))

    def shuffle(self):
        shuffle(self.all_cards)

    def draw_card(self):
        return self.all_cards.pop()

def display(card,person,point):
    clear_output()
    if person == 'player':
        print("Player's card:\n")
    else:
        print("Banker's card:\n")
    for n in range(len(card)):
        print(f'    {card[n]}')
    print(f'\nTotal points: {point}\n')

def ask_for_draw(card):
    choice = 'x'
    while choice not in ('Y','y','N','n'):
        choice = input('Do you need 1 more card? (y/n) ')
        if choice not in ('Y','y','N','n'):
            print('Sorry, invalid input, please try again.\n')
    if choice in ['Y','y']:
        card.append(mydeck.all_cards.pop())
        return card, True
    else:
        return card, False

def total_point(card):
    total = 0
    ace = 0
    for n in range(len(card)):
        if card[n].figure != 'A':
            total += values[card[n].figure]
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

while True:
    mydeck = deck()
    mydeck.shuffle()
    player = []
    player_point = 0
    banker = []
    banker_point = 0     
    for n in range(0,2):
        player.append(mydeck.all_cards.pop())
        banker.append(mydeck.all_cards.pop())
    win = 'x'

    draw = True    
    while len(player) < 5 and total_point(player) <= 21 and draw:
        display(player, 'player', total_point(player))
        player, draw = ask_for_draw(player)
        display(player, 'player', total_point(player))
        if total_point(player) > 21:
            print("Player's cards exploded!\n")
            win = 'Banker'

    input("\n-------Press Enter to continue.-------\n")

    draw = True
    while len(banker) < 5 and total_point(player) <= 21 and total_point(banker) <= 21 and draw:
        display(banker, 'banker', total_point(banker))
        banker, draw = ask_for_draw(banker)
        display(banker, 'banker', total_point(banker))
        if total_point(banker) > 21:
            print("Banker's cards exploded!\n")
            win = 'Player'

    if win == 'x':
        if total_point(player) > total_point(banker):
            win = 'Player'
        elif total_point(player) < total_point(banker):
            win = 'Banker'
        else:
            win = 'Draw'

    print(f"Player's points: {total_point(player)}, Banker's points: {total_point(banker)}\n")
    if win == 'Draw':
        print("It's a draw game!")
    else:
        print(f'Congratulations! {win} won the game!\n')
    if again() in ['N','n']:
        break
