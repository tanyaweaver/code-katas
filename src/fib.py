def fib_rec(n):
    if n in (1, 2):
        return 1
    elif n <= 0:
        return None
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_var(n):
    if n <= 0:
        return None
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def fib_memoization(fib_var, n):
    memo = {}
    if n not in memo:
        memo[n] = fib_var(n)
    return memo[n]
