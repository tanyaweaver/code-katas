#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from trie import Trie


class Autocomplete(object):
    """Define class Autocomplete"""
    def __init__(self, vocabulary, max_completions=5):
        """Create an instance of the class."""
        self._trie = Trie(iterable=vocabulary)
        self.max_completions = max_completions

    def autocomplete(self, token=None):
        """Return list of autocomplete suggestions, based on vocabulary."""
        result = []
        counter = 0
        if token and isinstance(token, type('abc')):
            for x in self._trie.traversal(token[0]):
                if counter < self.max_completions:
                    if x.startswith(token):
                        result.append(x)
                        counter += 1
        return result
    __call__ = autocomplete
