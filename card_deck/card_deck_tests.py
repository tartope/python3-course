import unittest
from deck_of_cards_exercise import Card, Deck

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card_one = Card("2", "Hearts")

    def test_init(self):
        """cards should have a suit and value"""
        self.assertEqual(self.card_one.value, "2")
        self.assertEqual(self.card_one.suit, "Hearts")

    def test_repr(self):
        self.assertEqual(
            # repr(self.card_one),  #<-- this is the better way but below works too
            self.card_one.__repr__(),
            "2 of Hearts"
        )

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """deck should have cards attribute which is a list, and have a length of 52"""
        # is instance of self.deck.cards a list, True or False
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """repr should return a string 'Deck of 52 cards' """
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        """count should return a count of the number of cards"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards, specified"""
        # deal 10 cards
        cards = self.deck._deal(10)
        # determine that the length of cards is 10
        self.assertEqual(len(cards), 10)
        # determine that the remaining deck count is 42
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        """_deal should deal the number of cards left"""
        # try to deal 100 cards (there's only 52 in the deck)
        cards = self.deck._deal(100)
        # check that the length of cards is 52
        self.assertEqual(len(cards), 52)
        # check that the count is now empty because all 52 cards have been dealth
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """_deal should throw a ValueError if deck is empty"""
        # this deals the entire deck
        self.deck._deal(self.deck.count())
        # raise a ValueError if you try to deal 1 more card
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        # check what the last card is and save it to a variable
        card = self.deck.cards[-1]
        # make another variable that deals the last card
        dealt_card = self.deck.deal_card()
        # card and dealt_card should equal
        self.assertEqual(card, dealt_card)
        # the deck count should now be 51
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """deal_hand should deal the number of cards passed"""
        # deal 20 cards
        cards = self.deck.deal_hand(20)
        # check the length of cards is 20
        self.assertEqual(len(cards), 20)
        # check the length of the deck is now 32
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        # slice with a single colon makes a copy to keep the original state; make a copy and save to a variable
        cards = self.deck.cards[:]
        # then shuffle the deck
        self.deck.shuffle()
        # check that they are different (that the inital state (cards), is different from the current state (self.deck.cards))
        self.assertNotEqual(cards, self.deck.cards)
        # checks that length is the same as before
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        """shuffle should throw a ValueError if the deck is not full (empty or partially full)"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()

if __name__ == "__main__":
    unittest.main()