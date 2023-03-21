from random import shuffle

# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)
        # or
        # return f"{self.value}" of {self.suit}"  <-- f string


# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck.

class Deck:
    def __init__(self):
        # create two lists of suits and card values
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # grab every possible pair and put in a list
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
        # print(self.cards)

        # or list comprehension version:
        # self.cards = [Card(value, suit) for suit in suits for value in values]
        # print(self.cards)

    def __repr__(self):
        # return f"Deck of {self.count()} cards"
        return "Deck of {} cards".format(self.count())

    # this turns the list of cards into an iterator, which is  iterable  :P
    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    # the underscore makes it clear that this is a private/internal method (deal_card and deal_hand both call this method)
    def _deal(self, num):
        # grab the number of cards in the deck
        count = self.count()
        # compare the number that's passed in to the number of cards in the deck, and use whichever one is lower
        # the actual number of cards to be removed should be the minimum of the count (number of cards in deck), or the number passed in
        actual = min([count, num])
        # print(f"Going to remove {actual} cards")
        # edge case: if the deck has 0 cards in it, return the error message
        if count == 0:
            raise ValueError("All cards have been dealt")
        # take the last number of cards and return them as a list, and also remove them from self.cards because to deal a card you have to take them out of the deck
        # use slice, start from negative actual all the way to the end to remove cards (ie. cardsList = [a,b,c,d,e,f,g,h,i,j]; to remove 3 cards: start from -3 back (h) and slice until the end (j); this removes [h,i,j])
        cards = self.cards[-actual:]
        # update self.cards so it goes from the beginning of the list, up until what was just removed (ie. cardsList = [a,b,c,d,e,f,g,h,i,j]; to update: start from beginning (a) up until what was removed (g); this gives us [a,b,c,d,e,f,g])
        self.cards = self.cards[:-actual]
        # return what was removed
        return cards

    def deal_card(self):
        # deals only 1 card, and the 0th element
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        # deals the number of cards by calling _deal method
        return self._deal(hand_size)

    # use import statement at the top (from random import shuffle)
    def shuffle(self):
        # if it's not a full deck, error message
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        # use import shuffle to shuffle cards
        shuffle(self.cards)
        # return shuffled instance
        return self

    



card = Card("A", "Hearts")
# card2 = Card("10", "Diamonds")
# card3 = Card("K", "Spades")
# print(card.value)  #//=> A
# print(card.suit)  #//=> Hearts
# print(card)  #//=> A of Hearts
# print(card2)  #//=> 10 of Diamonds
# print(card3)  #//=> K of Spades


# returns the whole deck:
deck = Deck()  #//=> [A of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, J of Hearts, Q of Hearts, K of Hearts, A of Diamonds, 2 of Diamonds, 3 of Diamonds, 4 of Diamonds, 5 of Diamonds, 6 of Diamonds, 7 of Diamonds, 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, J of Diamonds, Q of Diamonds, K of Diamonds, A of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, J of Clubs, Q of Clubs, K of Clubs, A of Spades, 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 9 of Spades, 10 of Spades, J of Spades, Q of Spades, K of Spades]

# returns the print statement inside this method:
# deck._deal(54) #//=> Going to remove 52 cards
# deck._deal(5) #//=> Going to remove 5 cards

# returns the number of cards in list self.cards:
# print(deck.count())  #//=> 52
# returns the number of cards represented by the repr method:
# print(deck)  #//=> Deck of 52 cards

# returns the private _deal method:
# print(deck._deal(3))  #//=>  [J of Spades, Q of Spades, K of Spades]
# returns the number of cards in self.dards after the _deal method:
# print(deck.count())  #//=> 49

# print(deck._deal(52))  #//=> deals all 52 cards
# print(deck.count())  #//=> 0
# print(deck._deal(3))  #//=> ValueError: All cards have been dealt

# shuffles the entire deck using shuffle method:
# deck.shuffle()
# after the shuffle method, returns deck instance with card attribute to see all cards
# print(deck.cards)  #//=> returns a list with all the cards shuffled

# deals one card using deal_card method:
# card = deck.deal_card()
# print(card) #//=>  8 of Spades

# deals a hand of 5 cards using deal_hand method:
# # hand = deck.deal_hand(5)
# # print(hand) #//=>  [2 of Hearts, 6 of Hearts, 6 of Spades, 8 of Clubs, Q of Spades]

# try error message:
# card = deck.deal_card()  #//=> deals 1 card
# hand2 = deck.deal_hand(50)  #//=> deals 50 cards
# card2 = deck.deal_card()  #//=> deals 1 more card (all 52 have been dealt at this point)
# print(deck.cards) #//=> []  #//=> shows that cards list is now empty
# card2 = deck.deal_card() #//=>  All cards have been dealt (shows error message)

# uses iter method and iterates over every card:
# for card in deck:
#     print(card)

# the for loop above returns:
# A of Hearts
# 2 of Hearts
# 3 of Hearts
# 4 of Hearts
# 5 of Hearts
# 6 of Hearts
# 7 of Hearts
# 8 of Hearts
# 9 of Hearts
# 10 of Hearts
# J of Hearts
# Q of Hearts
# K of Hearts
# A of Diamonds
# 2 of Diamonds
# 3 of Diamonds
# 4 of Diamonds
# 5 of Diamonds
# 6 of Diamonds
# 7 of Diamonds
# 8 of Diamonds
# 9 of Diamonds
# 10 of Diamonds
# J of Diamonds
# Q of Diamonds
# K of Diamonds
# A of Clubs
# 2 of Clubs
# 3 of Clubs
# 4 of Clubs
# 5 of Clubs
# 6 of Clubs
# 7 of Clubs
# 8 of Clubs
# 9 of Clubs
# 10 of Clubs
# J of Clubs
# Q of Clubs
# K of Clubs
# A of Spades
# 2 of Spades
# 3 of Spades
# 4 of Spades
# 5 of Spades
# 6 of Spades
# 7 of Spades
# 8 of Spades
# 9 of Spades
# 10 of Spades
# J of Spades
# Q of Spades
# K of Spades