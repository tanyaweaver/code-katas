#!/usr/bin/env python
# -*- coding: utf -8 -*-
import pytest
from sort_cards_no_pq import sort_cards

TEST = [
    ((list('39A5T824Q7J6K')), list('A23456789TJQK')),
    ((list('Q286JK395A47T')), list('A23456789TJQK')),
    ((list('54TQKJ69327A8')), list('A23456789TJQK')),
]


@pytest.mark.parametrize('shuffled, sorted', TEST)
def test_sort_cards(shuffled, sorted):
    """
    Tests whether shuffled cards are sorted properly by sort_cards().
    """
    assert sort_cards(shuffled) == sorted


def test_sort_error():
    """
    Test whether a KeyError is raised when there is not a card
    in the list.
    """
    with pytest.raises(KeyError):
        sort_cards(list('ABCD12345'))
