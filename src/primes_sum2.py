def primes_sum2(n):
    if n < 2:
        return 0
    sum = 2
    for i in range(3, n + 1):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            sum += i
    return sum % (10 ** 9 + 7)
