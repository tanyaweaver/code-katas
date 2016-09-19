#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from forbes import (
    DATA, AGE_DICT, FORBES_BST,
    oldest_under_80, youngest)


def in_order_tr_list():
    in_order_tr = []
    for x in FORBES_BST.depth_in_order_tr():
        in_order_tr.append(x.value)
    return in_order_tr

IN_ORDER_TR = in_order_tr_list()


def test_data():
    """Prove that DATA is a list of 40 items."""
    assert len(DATA) == 40


def test_create_age_dict():
    """Prove that AGE_DICT has 40 billionairs combined."""
    counter = 0
    for key in AGE_DICT:
        for person in AGE_DICT[key]:
            counter += 1
    assert counter == 40


def test_create_binary_tree():
    """
    Prove that all ages are in the tree.
    """
    for key in AGE_DICT:
        if key > 0:
            assert key in IN_ORDER_TR


def test_oldest_under_eighty():
    """
    Prove that oldest_under_eighty() returns
    the expected value. Test that using bst depth in order
    traversal.
    """
    for x in range(len(IN_ORDER_TR) - 1):
        answer = IN_ORDER_TR[x]
        if IN_ORDER_TR[x + 1] >= 80:
            break
    assert answer == oldest_under_80(FORBES_BST, 80)


def test_youngest():
    """
    Prove that youngest() returns
    the expected value.
    """
    assert IN_ORDER_TR[0] == youngest(FORBES_BST)
