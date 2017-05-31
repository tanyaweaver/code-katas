from fib import fib_rec, fib_var

fibonacci = ((-10, None), (0, None), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8))


def test_fib_rec1():
    for member, result in fibonacci:
        assert fib_rec(member) == result


def test_fib_var1():
    for member, result in fibonacci:
        assert fib_var(member) == result
