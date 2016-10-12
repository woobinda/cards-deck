# -*- coding: utf-8 -*-
import random


class Card:
    """
    Object class to create a playing card.
    """
    def __init__(self, value, cost, suit):
        self.value = value
        self.suit = suit
        self.cost = cost

    def __repr__(self):
        return '%s|%s' % (self.value, self.suit)


class Deck:
    """
    Object class to create a deck of playing card.
    All the cards are placed in an array of 'self.cards'.
    """
    def __init__(self, cards=[]):
        self.cards = cards

    def __getitem__(self, index):
        return self.cards[index - 1]

    def get_card_position(self, card):
        return self.cards.index(card) + 1

    def get_random_card(self):
        return random.choice(self.cards)

    def cards_shuffle(self):
        return random.shuffle(self.cards)

    def comparison(self, card1, card2):
        if card1.cost > card2.cost:
            return 1
        if card1.cost < card2.cost:
            return -1
        return 0

    def card_sort_for_suit(self, suit):
        return [card for card in self.cards if card.suit == suit]

    def card_sort_for_value(self, value):
        return [card for card in self.cards if card.value == value]

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        for card in enumerate(self.cards):
            print(card[0] + 1, card[1])
        return ''
