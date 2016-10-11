# -*- coding: utf-8 -*-
import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '%s|%s' % (self.value, self.suit)


class Deck:
    values_table = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, \
                    '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, cards=[]):
        self.cards = cards

    def get_card_by_index(self, index):
        return self.cards[index - 1]

    def get_card_position(self, card):
        return self.cards.index(card) + 1

    def get_random_card(self):
        return random.choice(self.cards)

    def cards_shuffle(self):
        return random.shuffle(self.cards)

    def comparison(self, card1, card2):
        cards = (card1, card2)
        if self.values_table[card1.value] != self.values_table[card2.value]:
            biggest_card_value = max([self.values_table[card.value] for card in cards])
            most_value_card = [card for card in cards if self.values_table[card.value] == biggest_card_value][0]
            return '%s - most value card' % most_value_card
        return 'Cards is equal'

    def card_sort_for_suit(self, suit):
        return [card for card in self.cards if card.suit == suit]

    def card_sort_for_value(self, value):
        return [card for card in self.cards if card.value == value]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index - 1]

    def __repr__(self):
        for card in enumerate(self.cards):
            print(card[0] + 1, card[1])
        return ''
