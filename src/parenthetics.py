# -*- encoding: utf-8 *-*
# This is an http-server#
from __future__ import unicode_literals
from stack import Stack


def parenthetics(string):
    """
    <string> must be a unicode string.
    Return '0' if the string is 'balanced',
    return '1' if the string is open,
    return '-1' if the string is 'broken'.
    Return None for an empty string.
    """
    if not isinstance(string, str):
        raise TypeError('<string> must be a unicode string.')
    stack = Stack()
    while len(string) != 0:
        for char in string:
            if char == '(':
                stack.push(1)
                string = string[1:]
            elif char == ')':
                try:
                    stack.pop()
                except AttributeError:
                    return -1
            else:
                string = string[1:]
        if len(stack) != 0:
            return 1
        return 0
