# -*- coding: utf-8 -*-
from models import Card, Deck

values_table = [['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], \
                    ['10', 10], ['Jack', 11], ['Queen', 12], ['King', 13], ['Ace', 14]]
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
warning = '\nИндекс карты (число), должен находиться в диапозоне (1 ~ 52)\n'
menu = ("""\n
Доступные опции:\n
1.Выбор карты по положению в колоде
2.Определение текущего места  выбранной карты в колоде
3.Случайный выбор карты
4.Перемешивание колоды
5.Сравнивание двух карт по “весу”
6.Сортировка карт по масти
7.Сортировка карт по значению
8.Доступные опции
9.Выход из приложения
\n""")


def create_deck():
    deck = Deck()
    for suit in card_suits:
        for value in values_table:
            deck.cards.append(Card(value[0], suit, value[1]))
    return deck


deck = create_deck()


def choice_1():
    try:
        card_index = input('Введите индекс карты (1 ~ 52): ')
        if card_index == 0:
            print(warning)
            return choice_1()
        card = deck[card_index]
        print('\nВыбраная карта: %s\n' % card)
        return card, run(card)
    except SyntaxError:
        print(warning)
        return choice_1()
    except IndexError:
        print(warning)
        return choice_1()
    except NameError:
        print(warning)
        return choice_1()


def choice_2(card):
    try:
        print ('\nПозиция выбранной карты: %s\n' % deck.get_card_position(card))
        return deck.get_card_position(card)
    except ValueError:
        print('\nКарта не выбрана, выберите карту используя пункт (1 или 3)\n')


def choice_3():
    card = deck.get_random_card()
    print('\nСлучайно выбраная карта: %s\n' % card)
    return card, run(card)


def choice_4():
    deck.cards_shuffle()
    print('\nПеремешанная колода: \n')
    print(deck)
    return deck


def choice_5():
    print('Выберите две карты для сравнения, по индексу\n')
    try:
        card1_index = input('Первая карта: ')
        card1 = deck[card1_index]
        print('\n%s\n' % card1)
        card2_index = input('Вторая карта: ')
        card2 = deck[card2_index]
        print('\n%s\n' % card2)
        most_value_card = deck.comparison(card1, card2)
        print('%s\n') % most_value_card
        return most_value_card
    except SyntaxError:
        print(warning)
        return choice_5()
    except IndexError:
        print(warning)
        return choice_5()
    except NameError:
        print(warning)
        return choice_5()


def choice_6():
    print('\nДоступные масти:\n')
    for suit in enumerate(card_suits):
        print(suit[0] + 1, suit[1])
    try:
        suit_index = input('\nВыберите масть по индексу: ')
        suit = card_suits[suit_index - 1]
        print('\n')
        print('%s') % deck.card_sort_for_suit(suit)
        print('\n')
        return deck.card_sort_for_suit(suit)
    except SyntaxError:
        print(warning)
        return choice_6()
    except IndexError:
        print(warning)
        return choice_6()
    except NameError:
        print(warning)
        return choice_6()


def choice_7():
    print('\nДоступные значения:\n')
    card_values = [value[0] for value in values_table]
    for value in enumerate(card_values):
        print(value[0] + 1, value[1])
    try:
        value_index = input('\nВыберите значение карты по индексу: ')
        value = card_values[value_index - 1]
        print('\n')
        print('%s') % deck.card_sort_for_value(value)
        print('\n')
        return deck.card_sort_for_value(value)
    except SyntaxError:
        print(warning)
        return choice_7()
    except IndexError:
        print(warning)
        return choice_7()
    except NameError:
        print(warning)
        return choice_7()


def choice_8():
    print(menu)


def choice_9():
    print('Bye!\n')
    exit()


def run(card=None):
    try:
        choice = input('Введите номер опции: ')
        if choice not in range(1, 10):
            print('\nДоступные опции (1-9), для вывода списка доступных опций введите (8)\n')
            return run(card)
    except NameError:
        return run(card)
    except SyntaxError:
        return run(card)

    else:
        if choice == 1:
            choice_1()

        if choice == 2:
            choice_2(card)

        if choice == 3:
            choice_3()

        if choice == 4:
            choice_4()

        if choice == 5:
            print('%s' % deck)
            choice_5()

        if choice == 6:
            choice_6()

        if choice == 7:
            choice_7()

        if choice == 8:
            choice_8()

        if choice == 9:
            choice_9()
        return run(card)
