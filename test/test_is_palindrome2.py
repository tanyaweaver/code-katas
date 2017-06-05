import pytest

from src.is_anagram import is_palindrome1, is_palindrome2


TEST = [
    ('abscder', False),
    ('noon', True),
    ('noodoon', True),
    ('', True),
    (None, False)
]


@pytest.mark.parametri
ze('s, result', TEST)
def test_is_palindrome1(
s, result):
    assert is_palindrome1(s) == result


@pytest.mark.parametri
ze('s, result', TEST)
def test_is_palindrome2(
s, result):
    assert is_palindrome2(s) == result
