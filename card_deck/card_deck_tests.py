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
            self.card_one.__repr__(),
            "2 of Hearts"
        )


if __name__ == "__main__":
    unittest.main()