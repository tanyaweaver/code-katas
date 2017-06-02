import pytest
from src.phone_buttons import phone_buttons

TEST = [
    ('', []),
    ('2', ['a', 'b', 'c']),
    ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
]


@pytest.mark.parametrize('numbers, letters', TEST)
def test_buttons(numbers, letters):
    assert phone_buttons(numbers) == letters
