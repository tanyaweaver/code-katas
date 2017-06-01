import pytest
from src.primes_sum2 import primes_sum2

SUM = [
    (3, 5),
    (5, 10),
    (1, 0),
    (7, 17),
    (6, 10),
    (11, 28),
    (520060, 693177248)
]


@pytest.mark.parametrize('n, sum', SUM)
def test_primes1(n, sum):
    assert primes_sum2(n) == sum
