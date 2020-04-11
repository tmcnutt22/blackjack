import random

# function to determine a winner of each hand of blackjack
def black_jack_result(player_hand, dealer_hand):
    """
    This function takes in the arguments of the player's hand value and the 
    dealer's hand value and compares the result.

    Todo:
    have the the result of a win increment the player's stack of cash and
    decrement the player's cash stack when they lose. The CLI should still
    print the result (add in score of each hand) 
    """
    if player_hand > dealer_hand:
        print("Player wins!")
    elif dealer_hand > player_hand:
        print("Dealer wins")
    else:
        print("The result is a tie")


#black_jack_result(19,19)
# maybe these shouldn't take any arguments??
def player_hand():
    pass

def dealer_hand():
    pass


#deck of cards
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def show(self):
        print ("{} of {}".format(self.value, self.suit))
    
# card = Card("Diamonds", 6)
# card.show()

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
                #print ("{} of {}".format(v, s))

    def show(self):
        for c in self.cards:
            c.show() 

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()    



deck = Deck()
#deck.show()
deck.shuffle()
#deck.show()
card = deck.draw()
card.show()
