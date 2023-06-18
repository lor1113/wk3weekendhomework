import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame()
        self.card1 = Card("Hearts",1)
        self.card2 = Card("Spades",11)
        self.card3 = Card("Spades",2)
        self.card4 = Card("Diamonds",6)
    
    def test_check_for_ace_true(self):
        result = self.game.check_for_ace(self.card1)
        self.assertEqual(result,True)

    def test_check_for_ace_false(self):
        result = self.game.check_for_ace(self.card2)
        self.assertEqual(result,False)
    
    def test_highest_card_first(self):
        result = self.game.highest_card(self.card2,self.card3)
        self.assertEqual(result,self.card2)
    
    def test_highest_card_last(self):
        result = self.game.highest_card(self.card3,self.card4)
        self.assertEqual(result,self.card4)
    
    def test_card_total(self):
        cards = [self.card1,self.card2,self.card3,self.card4]
        result = self.game.cards_total(cards)
        self.assertEqual(result,"You have a total of 20")