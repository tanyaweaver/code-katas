import pytest
from src.dna_repeats import dna_repeats


STRING_RESULT = [
    ('aaaaabbbbbcaaaaabbbbbc', ['aaaaabbbbb', 'aaaabbbbbc']),
    ('aa', []),
    ('', []),
    ('aaaaaaaaaaa', ['aaaaaaaaaa'])
]


@pytest.mark.parametrize('string, result',  STRING_RESULT)
def test_dna_repeats1(string, result):
    assert dna_repeats(string) == result
