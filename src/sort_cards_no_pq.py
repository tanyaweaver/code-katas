#!/usr/bin/env python
# -*- coding: utf -8 -*-


def rank(card):
    ranks = {"A": 1, "T": 10, "J": 11, "Q": 12, "K": 13}
    if card in ranks:
        return ranks[card]
    elif card in list('23456789'):
        return int(card)
    else:
        raise KeyError("Make sure every item in the list is a card!")


def sort_cards(cards):
    for i in range(len(cards) - 1):
        if rank(cards[i]) > rank(cards[i + 1]):
            cards[i], cards[i + 1] = cards[i + 1], cards[i]
            sort_cards(cards)
    return cards
