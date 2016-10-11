# -*- coding: utf-8 -*-
from models import Card, Deck
from views import deck
import unittest


class Tests(unittest.TestCase):
    def test_create_deck(self):
        self.assertEqual(len(deck), 52)
        self.assertTrue(isinstance(deck.cards[0], Card))
        self.assertEqual(deck.cards[0].suit, 'Hearts')
        self.assertEqual(deck.cards[0].value, '2')

    def test_get_card_by_index(self):
        card = deck.get_card_by_index(5)
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(card.value, '6')

    def test_get_card_position(self):
        card = deck[25]
        self.assertEqual(card.suit, 'Diamonds')
        self.assertEqual(card.value, 'King')
        self.assertEqual(deck.get_card_position(card), 25)

    def test_get_random_card(self):
        random_card1 = deck.get_random_card()
        random_card2 = deck.get_random_card()
        random_card3 = deck.get_random_card()
        self.assertNotEqual(random_card1, random_card2, random_card3)

    def test_comparison(self):
        card1 = deck[6]
        card2 = deck[26]
        self.assertEqual(card1.value, '7')
        self.assertEqual(card2.value, 'Ace')
        self.assertEqual(deck.comparison(card1, card2), 'Ace|Diamonds - most value card')
        card3 = deck[11]
        card4 = deck[11]
        self.assertEqual(card3.value, 'Queen')
        self.assertEqual(card4.value, 'Queen')
        self.assertEqual(deck.comparison(card3, card4), 'Cards is equal')

    def test_card_sort_for_suit(self):
        hearts_cards = deck.card_sort_for_suit('Clubs')
        self.assertEqual([card.suit for card in hearts_cards], ['Clubs'] * 13)

    def test_card_sort_for_values(self):
        jack_cards = deck.card_sort_for_value('Jack')
        self.assertEqual([card.value for card in jack_cards], ['Jack'] * 4)


if __name__ == '__main__':
    unittest.main()
