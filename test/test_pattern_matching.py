import pytest
from src.pattern_matching import regex_matching, compare_strings


RESULT1 = [
    ('abcdef', 'abcdefr', True),
    ('^abc', 'abcdfer', True),
    ('d$', 'abcd', True),
    ('asd', 'dfrty', False),
    ('aaaac', 'aaaaac', True)
]

RESULT2 = [
    ('abcdef', 'abcdef', True),
    ('abc', 'abcdfer', False),
    ('d', '', False),
    (None, 'df', False),
    (None, None, False)
]


@pytest.mark.parametrize('s1, s2, result', RESULT2)
def test_compare_strings1(s1, s2, result):
    assert compare_strings(s1, s2) == result


@pytest.mark.parametrize('pattern, test, result', RESULT1)
def test_matching1(pattern, test, result):
    assert regex_matching(pattern, test) == result
