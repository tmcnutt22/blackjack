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

#need to figure out best way to implement the deck of cards, that also deletes
#a card and can be rerun to replenish the deck
CARD_SUITS = ["hearts", "diamonds", "spades", "clubs"]
CARD_NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_VALUES = [2,3,4,5,6,7,8,9,10,10,10,10,11]
shuffled_deck = {}
deck_of_cards = []

#function to "shuffle" a fresh, full deck. 
def shuffle_deck():
    for card_suit in CARD_SUITS:
        for card_number in CARD_NUMBERS:
            return deck_of_cards.append(card_number + " of " + card_suit) 

print(shuffle_deck)
print(deck_of_cards)

