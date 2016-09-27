#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from autocomplete import Autocomplete
import pytest


def test_init_autocomlete():
    a = Autocomplete(['cat', 'cats'])
    assert a._trie.head == {
        'c': {
            'a': {
                't': {
                    '$': {},
                    's': {'$': {}}
                     }
                }
            }
        }


def test_autocomplete_trie_traversal():
    a = Autocomplete(['cat', 'cats'])
    result = []
    for x in a._trie.traversal('c'):
        result.append(x)
    for token in ['cat', 'cats']:
        assert token in result


AUTO = [
    ('c', ['cat', 'cats', 'catss']),
    ('ca', ['cat', 'cats', 'catss']),
    ('cat', ['cat', 'cats', 'catss']),
    ('cats', ['cats', 'catss', ]),
    ('catss', ['catss'])
]


@pytest.mark.parametrize('token, result_list', AUTO)
def test_autocomplete1(token, result_list):
    a = Autocomplete(['cat', 'cats', 'catss'])
    result = []
    for x in a.autocomplete(token):
        result.append(x)
    for token in result_list:
        assert token in result

VOCABULARY = ['hi', 'hir', 'hirt', 'hirtd', 'hirtds']
RESULT_LEN = [
    ('h'), ('hi'), ('hir'), ('hirt'), ('hirtd')
]


@pytest.mark.parametrize('token', RESULT_LEN)
def test_autocomplete2(token):
    a = Autocomplete(VOCABULARY, 2)
    result = []
    for x in a.autocomplete(token):
        result.append(x)
    assert len(result) == 2
