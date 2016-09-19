#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
import json
from bst import Bst
import requests


with open('assets/forbes_billionaires_2016.json') as data_file:
    DATA = json.load(data_file)


def create_age_dictionary(data):
    """
    Create dictionary where key=age and
    value=list of billionaires of that age.
    Don't include negative values for age (bad data in json).
    """
    age_dict = {}
    for person in data:
        if person['age'] > 0:
            age_dict.setdefault(person['age'], []).append(person)
    return age_dict

AGE_DICT = create_age_dictionary(DATA)


def create_binary_tree(age_dict):
    """
    Create a binary tree with billionairs' ages.
    """
    bst = Bst()
    for key in age_dict:
        bst.insert(key)
    return bst

FORBES_BST = create_binary_tree(AGE_DICT)


def oldest_under_80(bst, age):
    """
    Return value of the node that is closest smaller to 80.
    """
    current = bst.head
    while current:
        if current.value >= age:
            pending = current
            current = current.left
        else:
            pending = current
            current = current.right
    if pending.value >= age:
        pending = pending.parent
    return pending.value


def youngest(bst):
    """Return the samllest node.value in the tree."""
    current = bst.head
    while current:
        pending = current
        current = current.left
    return pending.value


def internet_scraper(sym):
    response = requests.get('http://dev.markitondemand.com/'
                            'Api/v2/Quote/json?symbol=' + sym)
    if response.status_code == 200:
        entries = {key: value for key, value in response.json().items()}
    print(entries['Name'], entries['LastPrice'])


def ages_of_two(age):
    old = oldest_under_80(FORBES_BST, age)
    young = youngest(FORBES_BST)
    list_old, list_young = [], []
    for x in AGE_DICT[old]:
        list_old.append((x['name'], x['net_worth (USD)'], x['source']))
    for x in AGE_DICT[young]:
        list_young.append((x['name'], x['net_worth (USD)'], x['source']))
    print('Forbes 40 billionaires info.')
    print('Oldest under {} (age {}):'.format(age, old))
    for x in list_old:
        print(str(x[0]) + ',', 'net worth: ', x[1], 'USD,', x[2])
    print('Youngest (age {}):'.format(young))
    for x in list_young:
        print(str(x[0]) + ',', 'net worth: ', x[1], 'USD,', x[2])
    return list_old, list_young


if __name__ == '__main__':
    ages_of_two(70)
    internet_scraper('NKE')
    internet_scraper('FB')
