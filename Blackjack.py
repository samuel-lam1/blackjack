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

class Participant:
    '''hold the information of a player and other function to manipulate the data'''
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.bet_amount = 0
        self.all_cards = []
        self.all_cards.append(mydeck.draw_card())
        self.all_cards.append(mydeck.draw_card())

    def pool_set(self):
        amount = 'x'
        while amount.isdigit() is False or int(amount) not in range(1,1000001):
            amount = input("please input the initial amount of player's money (maximum $1,000,000):\n  $")
            if amount.isdigit() is False or int(amount) <= 0:
                print('Sorry, input is not valid.\n')
            elif int(amount) > 1000000:
                print('Sorry, amount out of range.\n')
        self.money = int(amount)

    def bet(self):
        bet = 'x'
        clear_output()
        while bet.isdigit() is False or int(bet) not in range(1,self.money+1):
            bet = input(f"Total money: ${self.money}\nPlease input the betting amount (minimum $1):\n  $")
            if bet.isdigit() is False or int(bet) <= 0:
                print('Sorry, input is not valid.\n')
            elif int(bet) > self.money:
                print('Sorry, you bet more than you have!\n')
        self.bet_amount = int(bet)

    def ask_for_take(self):
        choice = 'x'
        while choice not in ('Y','y','N','n'):
            choice = input('Do you need 1 more card? (y/n) ')
            if choice not in ('Y','y','N','n'):
                print('Sorry, invalid input, please try again.\n')
        if choice in ['Y','y']:
            self.all_cards.append(mydeck.draw_card())
            return True
        return False

    def total_point(self):
        point = 0
        ace = 0
        for item in self.all_cards:
            if item[1] != 'A':
                point += values[item[1]]
            else:
                ace += 1
        if ace >= 1: # Choose 11 as the value for Ace if the total value does not exceed 21
            for i in range(ace):
                if point + values['A'][1] <= 21:
                    point += values['A'][1]
                else:
                    point += values['A'][0]
        return point

    def update_pool(self, check):
        if check == self.name:
            self.money += self.bet_amount
        elif check != 'Draw':
            self.money -= self.bet_amount

################################################################################

def display(person):
    clear_output()
    if person.name != 'Dealer':
        print(f'Total money: ${person.money}, betting amount: ${person.bet_amount}\n')
        print(f"{dealer.name}'s card:\n    {' '.join(dealer.all_cards[0])}\n    hidden\n")
    print(f"{person.name}'s card:\n")
    for item in person.all_cards:
        print(f'    {" ".join(item)}')
    print(f'\nTotal points: {person.total_point()}\n')

def check_win(check, deal, play):
    if check == 'Draw':
        if play.total_point() > deal.total_point():
            check = play.name
        elif play.total_point() < deal.total_point():
            check = deal.name

    print(f"{play.name}'s points: {play.total_point()}, {deal.name}'s points: {deal.total_point()}\n")
    if check == 'Draw':
        print("It's a draw game!")
    else:
        print(f'Congratulations! {check} won the game!\n')
    return check

def again(play):
    game ='x'
    if play.money <= 0:
        print("You don't have any money left!")
    while game not in ['Y','y','N','n']:
        game = input('Do you want to play again? (Y/N) ')
        if game not in ['Y','y','N','n']:
            print('Sorry, but your input is not valid.')
    return game

################################################################################

money_last_round = 0
while True:
    # Initial setup
    mydeck = Deck()
    mydeck.shuffle()
    player = Participant('Player')
    dealer = Participant('Dealer')
    player.money = money_last_round
    if player.money <= 0:
        player.pool_set()
    player.bet()
    # Player's turn
    win = 'Draw'
    take = True
    while len(player.all_cards) < 5 and player.total_point() <= 21 and take:
        display(player)
        take = player.ask_for_take()
        display(player)
        if player.total_point() > 21:
            print("Player busted!\n")
            win = 'Dealer'
    input("\n-------Press Enter to continue.-------\n")
    # Dealer's turn
    take = True
    while len(dealer.all_cards) < 5 and player.total_point() <= 21 and dealer.total_point() <= 21 and take:
        display(dealer)
        take = dealer.ask_for_take()
        display(dealer)
        if dealer.total_point() > 21:
            print("Dealer busted!\n")
            win = 'Player'
    # Check for winner and ask for continue
    player.update_pool(check_win(win, dealer, player))
    print(f'Betting amount: ${player.bet_amount}, total money of {player.name} after this round: ${player.money}\n')
    money_last_round = player.money
    if again(player) in ['N','n']:
        break
