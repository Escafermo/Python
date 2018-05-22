import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (f'{self.rank} of {self.suit}')

class Deck:
    '''
    Function that defines what is the Deck using pre-defined Suits and Ranks.
        Shuffle: randomly reorder the Decks' content
        Deal: returns the next card of the Deck and moves up a index (repeat)
    '''
    def __init__(self):
        self.deck = []  # start with an empty list
        self.currentindex = -1
        for suit in suits:
            for rank in ranks:
                thiscard = rank +' of '+ suit
                self.deck += [thiscard]
    def __str__(self):
        return str(self.deck)
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        while self.currentindex <= len(self.deck):
            self.currentindex+=1
            #print(self.deck[self.currentindex])
            return self.deck[self.currentindex]




class Hand:
	def __init__(self):
		self.cards = []  # start with an empty list as we did in the Deck class
		self.value = 0   # start with zero value
		self.aces = 0    # add an attribute to keep track of aces
    
	def add_card(self,card):
		self.cards.append(card)
		cardkey = card.split()[0]
		for (key, value) in (values.items()):
			if cardkey in key:
				if cardkey == 'Ace' and self.value+value > 21:
					self.value += 1
				else:
					self.value += value
		return self.value
       
	def adjust_for_ace(self):
		#if cardkey == 'Ace' and self.value+value > 21:
    		#self.value+=1
    		# TODO adjust IF player human (?)
		pass

	def hide_card(self):
		dealer_value = 0
		dealer_card = self.cards[1].split()[0]
		for (key, value) in (values.items()):
			if dealer_card in key:
				dealer_value += value
		print(f'Dealer shown card is: {self.cards[1::]}')
		return print((f'Dealer sown card value is: {dealer_value}'))

	def __str__(self):
		return str((self.cards))
    
#myDict = {'age': ['12'], 'address': ['34 Main Street, 212 First Avenue'],
  #        'firstName': ['Alan', 'Mary-Ann'], 'lastName': ['Stone', 'Lee']}

#def search(myDict, lookup):
#    for key, value in myDict.items():
 #       for v in value:
  #          if lookup in v:
   #             return key

#search(myDict, 'Mary')

class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0  # TODO FIX THIS NUMBER

    def win_bet(self):
    	self.total += (self.bet*2)
    	return self.total
    def lose_bet(self):
    	self.total -= self.bet
    	return self.total

    def __str__(self):
        return str((self.total))


def take_bet():
	betvalue = 0
	while betvalue not in range(1,10):	# TODO fix this range
		try:
			betvalue = int(input(f'Input bet amount: '))
			return(betvalue)
		except:
			print('Value Error: input a number from 1 to your total chips')
			continue
		#break

	pass

def hit(deck,hand):
	newcard = deck.deal()
	hand.add_card(newcard)
	pass

def hit_or_stand(deck,player_hand):
	global playing  #to control an upcoming while loop
	thisentry = ''
	while thisentry != 'Hit' or thisentry != 'Stand':
		if player_hand.value == 21:
				player_wins()
		thisentry = str(input('Give me Hit or Stand: '))
		if thisentry == 'Hit':
			hit(deck, player_hand)
			break
		elif thisentry == 'Stand':
			playing = False
			break

def show_some(player_hand,dealer_hand):
	#dealer_hide_hand = Hand()
	#dealer_hide_hand.add_card(dealer_hide_card)
	print(f'\nDealer hand has one card hidden. ')#nIt has a value of {dealer_hide_hand.value}')
	dealer_hand.hide_card()
	print(f'\nYour hand: {player_hand}\nYour value: {player_hand.value}')
	pass
def show_all(player_hand,dealer_hand):
	print(f'\nDealer hand: {dealer_hand}\nDealer value: {dealer_hand.value}')
	print(f'\nYour hand: {player_hand}\nYour value: {player_hand.value}')

	pass

def player_busts():
	print(f'PLAYER BUSTED!\nYour chips were: {player_chips}')
	player_chips.lose_bet()
	print(f'Lost {player_chips.bet} chips\nNew chips: {player_chips}')
	push()
def player_wins():
	print(f'PLAYER WINS!\nYour chips were: {player_chips}')
	player_chips.win_bet()
	print(f'Won {player_chips.bet*2} chips\nNew chips: {player_chips}')
	push()
def dealer_busts():
	print(f'DEALER BUSTED!\nYour chips were: {player_chips}')
	player_chips.win_bet()
	print(f'Won {player_chips.bet*2} chips\nNew chips: {player_chips}')
	push()
    
def dealer_wins():
	print(f'DEALER WINS!\nYour chips were: {player_chips}')
	player_chips.lose_bet()
	print(f'Lost {player_chips.bet} chips\nNew chips: {player_chips}')
	push()
    
def push():
	play_again = ''
	while play_again != 'Y' or play_again != 'N':
		play_again = str(input('Would you like to play more (Y/N): '))
		if play_again == 'Y':
			playing = True
			play_black_jack()
		elif play_again == 'N':
			exit()

def play_black_jack():
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

		player_chips.bet = take_bet()

		show_some(player_hand,dealer_hand)

		while playing == True:
			hit_or_stand(mydeck,player_hand)
			show_some(player_hand,dealer_hand)
			#if player_hand.value == 21:
			#	player_wins()
			if player_hand.value > 21:
				player_busts()
		#print(playing)
		print('\n>>> Player Stand: Showing all cards<<<\n')
		show_all(player_hand,dealer_hand)
		while dealer_hand.value < 17:
			print('\nDealer hand < 17 in value! Dealer hit!')
			hit(mydeck,dealer_hand)
			show_all(player_hand,dealer_hand)
			if dealer_hand.value > 21:
				dealer_busts()
		if player_hand.value > dealer_hand.value:
			player_wins()
		else:
			dealer_wins()

	#while True:
    # Print an opening statement
    # Create & shuffle the deck, deal two cards to each player
    # Set up the Player's chips
    # Prompt the Player for their bet
    # Show cards (but keep one dealer card hidden)
    #while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        # Show cards (but keep one dealer card hidden)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        #    break
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        # Show all cards
        # Run different winning scenarios
    # Inform Player of their chips total 
    # Ask to play again
    #    break


if __name__ == "__main__":
	player_chips = Chips()
	play_black_jack()

	#show_some(player_hand,dealer_hand)
	#show_all(player_hand,dealer_hand)

	#player_busts()
	#player_wins()


	#print(player_hand)
	#print(player_hand.value)
	#hit_or_stand(mydeck,player_hand)
	#hit(mydeck, player_hand)
	#print(player_hand)
	#print(player_hand.value)
	#take_bet()




#player_hand = Hand()


