#!/usr/bin/env python
# -*- coding: utf -8 -*-


from __future__ import unicode_literals, division

from priority_q import PriorityQ

RANKS = {"A": 1, "T": 10, "J": 11, "Q": 12, "K": 13}


def sort_cards(cards):
    card_rank_list = []
    for card in cards:
        if card in list('23456789'):
            card_rank_list.append((int(card), card))
        else:
            if card in RANKS:
                card_rank_list.append((RANKS[card], card))
            else:
                raise KeyError("Make sure every item in the list is a card!")
    return PriorityQ(card_rank_list).display_values()
