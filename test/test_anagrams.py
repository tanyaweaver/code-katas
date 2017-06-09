import pytest
from src.anagrams import anagrams1, anagrams2, anagrams3


TEST = [
    ('abcda', 'dbcaa', True),
    ('abcda', 'ddcba', False),
    ('', 'a', False),
    (None, None, False)
]


@pytest.mark.parametrize('s1, s2, result', TEST)
def test_anagrams1(s1, s2, result):
    assert anagrams1(s1, s2) == result


@pytest.mark.parametrize('s1, s2, result', TEST)
def test_anagrams2(s1, s2, result):
    assert anagrams2(s1, s2) == result


@pytest.mark.parametrize('s1, s2, result', TEST)
def test_anagrams3(s1, s2, result):
    assert anagrams3(s1, s2) == result
