# -*- coding: utf-8 -*-
import random


class Card:
    def __init__(self, value, suit, cost):
        self.value = value
        self.suit = suit
        self.cost = cost

    def __repr__(self):
        return '%s|%s' % (self.value, self.suit)


class Deck:

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
        cards = (card1, card2)
        if card1.cost != card2.cost:
            biggest_card_cost = max([card1.cost, card2.cost])
            most_value_card = [card for card in cards if card.cost == biggest_card_cost][0]
            return '%s - most value card' % most_value_card
        return 'Cards is equal'

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
