#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from autocomplete import Autocomplete
import pytest


def test_init_autocomlete():
    """Prove that an instance of autocomplete has the expected structure."""
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


AUTO = [
    ('c', ['cat', 'cats', 'catss']),
    ('ca', ['cat', 'cats', 'catss']),
    ('cat', ['cat', 'cats', 'catss']),
    ('cats', ['cats', 'catss', ]),
    ('catss', ['catss'])
]


@pytest.mark.parametrize('token, result_list', AUTO)
def test_autocomplete1(token, result_list):
    """Prove that autocomplete() returns an expected list."""
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
    """Prove that autocomplete() returns only <max_completions> suggestions."""
    a = Autocomplete(VOCABULARY, 2)
    result = []
    for x in a.autocomplete(token):
        result.append(x)
    assert len(result) == 2


INPUT = [
    (123), (), ({'a': 1}), ([1, 2]), ('a')
]


@pytest.mark.parametrize('token', INPUT)
def test_empty_list_returned_for_bad_input(token):
    """Prove that autocomplete returns an empty list for bad input."""
    a = Autocomplete(VOCABULARY, 2)
    result = []
    for x in a.autocomplete(token):
        result.append(x)
    assert result == []
