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
        self.bet = 0
        
    def win_bet(self):
    	self.total += self.bet*2
        
    
    def lose_bet(self):
    	self.total -= self.bet



def take_bet():
	betvalue = 0
	while betvalue not in range(1,10):	# TODO fix this range
		try:
			betvalue = int(input(f'Give me money: '))
			print(betvalue)
		except:
			print('VALUE ERROR')
		break

	pass

def hit(deck,hand):
	pass

def hit_or_stand(deck,hand):
	global playing  # to control an upcoming while loop
    
	pass

def show_some(player,dealer):
    
	pass
def show_all(player,dealer):
    
	pass

def player_busts():
    pass
def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass


def play_black_jack(self):
	pass
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
	mydeck = Deck()
	mydeck.shuffle()
	myhand = Hand()
	myhand.add_card(mydeck.deal())
	myhand.add_card(mydeck.deal())
	myhand.add_card(mydeck.deal())
	#print(mydeck)
	print(myhand)
	print(myhand.value)
	take_bet()
#myhand = Hand()


