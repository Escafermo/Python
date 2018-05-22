'''
This script handles a simple game of Blackjack.
The rules are the same of the classic game:
Get as close to 21 as you can without going over! Dealer hits until reaches 17.
Aces count as 1 or 11.
'''
import random
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
PLAYING = True
# # # # # # # ### # # # # # # #
class Card:
    '''
    Class that defines what is a Card using the pre-defined SUITS and RANKS.
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'{self.rank} of {self.suit}'
class Deck:
    '''
    Class that defines what is the Deck using pre-defined Cards.
        Shuffle: randomly reorder the Decks' content
        Deal: returns the next card of the Deck and moves up a index (repeat)
    '''
    def __init__(self):
        '''
        Init_function
        '''
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
    def __str__(self):
        '''
        Print_function
        '''
        thisdeck = ''
        for card in self.deck:
            thisdeck += '\n '+card.__str__()
        return 'The deck has:' + thisdeck
    def shuffle(self):
        '''
        Shuffles the Deck's Cards in random order
        '''
        random.shuffle(self.deck)
    def deal(self):
        '''
        Deals a card to Player or Dealer and removes it from the Deck
        '''
        thiscard = self.deck.pop()
        return thiscard
class Hand:
    '''
    Class that keeps track of the Player's and Dealer's Cards.
        Add Card: appends a card to the Hand
        Adjust for Ace: adjusts value for Ace Card according to the game's rules.
    '''
    def __init__(self):
        '''
        Init_function
        '''
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        '''
        Receives the dealt Card and appends it to the Hand
        '''
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        '''
        If a Hand has a value of over 21 and an Ace,
        the Ace can have a value of 1 to prevent BUST.
        '''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips:
    '''
    Class that keeps the Player's Chips for betting purposes.
    '''
    def __init__(self, chips):
        '''
        Init_function
        '''
        self.total = chips
        self.bet = 0
    def win_bet(self):
        '''
        Adds the amount of the Bet to the Player's Chip's total
        '''
        self.total += (self.bet)
    def lose_bet(self):
        '''
        Removes the amount of the Bet to the Player's Chip's total
        '''
        self.total -= self.bet
# # # # # # # ### # # # # # # #
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(deck, player_hand):
    global PLAYING
    while True:
        thisentry = input('Give me Hit or Stand: ')
        if thisentry == 'Hit':
            hit(deck, player_hand)
        elif thisentry == 'Stand':
            print('Player stands. Dealer is Playing')
            PLAYING = False
        else:
            print('Value Error! Try again.')
            continue
        break
def show_some(player_hand, dealer_hand):
    print(f'\nDealer hand has one card hidden. ')
    print(f'Dealer shown card is: {dealer_hand.cards[1]}')
    print('\nYour hand: ', *player_hand.cards, sep='\n ')
    print(f'Your value: {player_hand.value}')
def show_all(player_hand, dealer_hand):
    print('\nDealer hand: ', *dealer_hand.cards, sep='\n ')
    print(f'Dealer value: {dealer_hand.value}')
    print('\nYour hand: ', *player_hand.cards, sep='\n ')
    print(f'Your value: {player_hand.value}')
def player_busts(player_chips):
    print(f'PLAYER BUSTED!\nYour chips were: {player_chips.total}')
    player_chips.lose_bet()
    print(f'Lost {player_chips.bet} chips\nNew chips: {player_chips.total}')
def player_wins(player_chips):
    print(f'PLAYER WINS!\nYour chips were: {player_chips.total}')
    player_chips.win_bet()
    print(f'Won {player_chips.bet} chips\nNew chips: {player_chips.total}')
def dealer_busts(player_chips):
    print(f'DEALER BUSTED!\nYour chips were: {player_chips.total}')
    player_chips.win_bet()
    print(f'Won {player_chips.bet} chips\nNew chips: {player_chips.total}')
def dealer_wins(player_chips):
    print(f'DEALER WINS!\nYour chips were: {player_chips.total}')
    player_chips.lose_bet()
    print(f'Lost {player_chips.bet} chips\nNew chips: {player_chips.total}')
def push():
    print('DEALER AND PLAYER TIED!')
# # # # # # # ### # # # # # # #
if __name__ == "__main__":
    FIRST_PLAY = True
    while True:
        print("Welcome to Blackjack\n")
        mydeck = Deck()
        mydeck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(mydeck.deal())
        dealer_hand.add_card(mydeck.deal())
        player_hand.add_card(mydeck.deal())
        dealer_hand.add_card(mydeck.deal())
        if FIRST_PLAY:
            player_chips = Chips(100)
        elif not FIRST_PLAY:
            player_chips = Chips(player_chips.total)
        take_bet(player_chips)
        show_some(player_hand, dealer_hand)
        while PLAYING:
            hit_or_stand(mydeck, player_hand)
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_busts(player_chips)
                break
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                print('\nDealer hand < 17 in value! Dealer hit!')
                hit(mydeck, dealer_hand)
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
            else:
                push()
        print(f'\nPlayer chips are: {player_chips.total}')
        NEW_GAME = input('Do you want to play another hand (y/n)? ')
        if NEW_GAME[0].lower() == 'y' and player_chips.total > 0:
            PLAYING = True
            FIRST_PLAY = False
            continue
        elif player_chips.total == 0:
            print("Get out of here, you don't have any money left!")
            break
        else:
            print('Thank you for Playing Blackjack')
            break
