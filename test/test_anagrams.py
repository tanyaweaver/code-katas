import pytest
from src.anagrams import anagrams1, anagrams2


TEST = [
    ('abcda', 'dbcaa', True),
    ('abcda', 'ddcba', False),
    ('', 'a', False),
    (None, None, False)
]


@pytest.mark.parametrize('s1, s2, result', TEST)
def test_abagrams1(s1, s2, result):
    assert anagrams1(s1, s2) == result


@pytest.mark.parametrize('s1, s2, result', TEST)
def test_abagrams(s1, s2, result):
    assert anagrams2(s1, s2) == result
